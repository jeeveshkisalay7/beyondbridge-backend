const { v4: uuidv4 }            = require('uuid');
const db                         = require('../models/db');
const { createOrder, verifyPayment: cfVerify } = require('../services/cashfreeService');
const { generateInvoice }        = require('../services/invoiceService');
const { sendInvoiceEmail }       = require('../services/emailService');
const { sendWhatsAppInvoice }    = require('../services/whatsappService');

const PACKAGES = {
  free_discovery:     { name: 'Free Discovery Call',               price: 0 },
  bridge_diagnostic:  { name: 'BridgeStart Profile Diagnostic',    price: 199900 },   // paise
  resume_linkedin:    { name: 'Resume & LinkedIn Transformation',   price: 499900 },
  single_india:       { name: 'Single School India MBA Advisory',   price: 1999900 },
  three_india:        { name: 'Three-School India MBA Pack',        price: 5999900 },
  single_global:      { name: 'Single School Global MBA Advisory',  price: 3999900 },
  global_three:       { name: 'Global MBA 3-School Pack',           price: 9999900 },
  mba360:             { name: 'MBA360 Premium Advisory',            price: 19999900 },
  interview_mastery:  { name: 'Interview Mastery Pack',             price: 1199900 },
  ding_analysis:      { name: 'Reapplicant / Ding Analysis',        price: 999900 },
  hourly_advisory:    { name: 'Hourly Advisory',                    price: 399900 },
};

// ─── SUBMIT FORM ──────────────────────────────────────────
exports.submitForm = async (req, res) => {
  try {
    const { fullName, email, phone, profession, rankDesignation, yearsExperience,
            currentLocation, targetMbaYear, preferredGeography, targetSchools,
            gmatStatus, mainConcern, preferredSlot } = req.body;

    const resumePath = req.file ? req.file.filename : null;

    const stmt = db.prepare(`
      INSERT INTO bookings
        (full_name, email, phone, profession, rank_designation, years_experience,
         current_location, target_mba_year, preferred_geography, target_schools,
         gmat_status, main_concern, resume_path, preferred_slot, payment_status)
      VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,'pending')
    `);

    const result = stmt.run(fullName, email, phone, profession || '', rankDesignation || '',
                            yearsExperience || 0, currentLocation || '', targetMbaYear || '',
                            preferredGeography || '', targetSchools || '', gmatStatus || '',
                            mainConcern || '', resumePath, preferredSlot || '');

    res.json({ success: true, bookingId: result.lastInsertRowid });
  } catch (err) {
    console.error('Form submit error:', err);
    res.status(500).json({ error: 'Form submission failed. Please try again.' });
  }
};

// ─── CREATE PAYMENT ───────────────────────────────────────
exports.createPayment = async (req, res) => {
  try {
    const { bookingId, packageId, customerName, customerEmail, customerPhone } = req.body;

    const pkg = PACKAGES[packageId];
    if (!pkg) return res.status(400).json({ error: 'Invalid package.' });

    // Free package — no payment needed
    if (pkg.price === 0) {
      db.prepare('UPDATE bookings SET package_id=?, package_name=?, package_price=0, payment_status="free" WHERE id=?')
        .run(packageId, pkg.name, bookingId);
      return res.json({ success: true, isFree: true, message: 'Discovery call booked! Our team will contact you within 24 hours.' });
    }

    const orderId = `BB_${bookingId}_${Date.now()}`;
    const returnUrl = `${process.env.FRONTEND_URL}/payment-success.html?order_id=${orderId}&booking_id=${bookingId}`;

    const cfOrder = await createOrder({
      orderId,
      amount:        pkg.price,   // paise
      customerName,
      customerEmail,
      customerPhone,
      returnUrl
    });

    // Save order info
    db.prepare('UPDATE bookings SET package_id=?, package_name=?, package_price=?, payment_order_id=? WHERE id=?')
      .run(packageId, pkg.name, pkg.price, orderId, bookingId);

    db.prepare('INSERT INTO payments (booking_id, cashfree_order_id, amount, status) VALUES (?,?,?,?)')
      .run(bookingId, orderId, pkg.price, 'created');

    res.json({
      success:          true,
      paymentSessionId: cfOrder.payment_session_id,
      orderId:          cfOrder.order_id,
      amount:           pkg.price,
      packageName:      pkg.name,
    });
  } catch (err) {
    console.error('Create payment error:', err);
    res.status(500).json({ error: 'Payment initiation failed. Please try again.' });
  }
};

// ─── VERIFY PAYMENT ───────────────────────────────────────
exports.verifyPayment = async (req, res) => {
  try {
    const { orderId, bookingId } = req.body;

    const cfData = await cfVerify(orderId);

    if (cfData.order_status !== 'PAID') {
      return res.status(400).json({ error: 'Payment not completed.', status: cfData.order_status });
    }

    const paymentRef = cfData.cf_order_id || orderId;
    const paidAt     = new Date().toISOString();

    // Update booking
    db.prepare('UPDATE bookings SET payment_status="paid", payment_ref=? WHERE id=?')
      .run(paymentRef, bookingId);

    // Update payment record
    db.prepare('UPDATE payments SET cashfree_payment_id=?, status="paid", paid_at=? WHERE cashfree_order_id=?')
      .run(paymentRef, paidAt, orderId);

    // Get booking + user details for invoice
    const booking = await db.get('SELECT * FROM bookings WHERE id=?', bookingId);

    const invoiceData = {
      bookingId,
      firstName:    booking.full_name.split(' ')[0],
      lastName:     booking.full_name.split(' ').slice(1).join(' '),
      email:        booking.email,
      phone:        booking.phone,
      packageName:  booking.package_name,
      packagePrice: booking.package_price,
      paymentRef,
      paidAt,
    };

    // Generate invoice PDF
    const invoicePath = await generateInvoice(invoiceData);

    // Update payment with invoice path
    db.prepare('UPDATE payments SET invoice_path=? WHERE cashfree_order_id=?')
      .run(invoicePath, orderId);

    // Send email + WhatsApp
    await sendInvoiceEmail(booking.email, invoiceData.firstName, invoiceData, invoicePath);
    await sendWhatsAppInvoice(booking.phone, invoiceData.firstName, invoiceData);

    res.json({
      success:     true,
      message:     'Payment verified. Invoice sent to your email and WhatsApp.',
      bookingId,
      packageName: booking.package_name,
    });
  } catch (err) {
    console.error('Verify payment error:', err);
    res.status(500).json({ error: 'Payment verification failed. Contact support.' });
  }
};
