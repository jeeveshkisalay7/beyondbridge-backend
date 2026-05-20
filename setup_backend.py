import os

BACKEND_DIR = 'c:/Users/jeeve/Desktop/Beyondbridge/backend'

def create_file(path, content):
    full_path = os.path.join(BACKEND_DIR, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f"Created {path}")

def setup_backend():
    files = {
        'package.json': """
{
  "name": "beyondbridge-backend",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js"
  },
  "dependencies": {
    "express": "^4.18.2",
    "cors": "^2.8.5",
    "dotenv": "^16.3.1",
    "bcryptjs": "^2.4.3",
    "jsonwebtoken": "^9.0.2",
    "nodemailer": "^6.9.7",
    "pdfkit": "^0.14.0",
    "multer": "^1.4.5-lts.1",
    "express-rate-limit": "^7.1.5",
    "better-sqlite3": "^9.2.2",
    "axios": "^1.6.2",
    "uuid": "^9.0.0",
    "crypto": "^1.0.1"
  },
  "devDependencies": {
    "nodemon": "^3.0.2"
  }
}
        """,
        '.env.example': """
# Server
PORT=3001
NODE_ENV=development
FRONTEND_URL=http://localhost:5500

# JWT
JWT_SECRET=your_super_secret_jwt_key_change_this_in_production

# Database
DB_TYPE=sqlite
# For production MySQL on cPanel:
# DB_TYPE=mysql
# DB_HOST=localhost
# DB_USER=your_cpanel_db_user
# DB_PASS=your_cpanel_db_password
# DB_NAME=beyondbridge_db

# Email (Gmail SMTP or cPanel email)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_SECURE=false
EMAIL_USER=your_gmail@gmail.com
EMAIL_PASS=your_gmail_app_password
EMAIL_FROM="BeyondBridge <your_gmail@gmail.com>"
ADMIN_EMAIL=contact@beyond-bridge.com

# Cashfree Payment Gateway
CASHFREE_APP_ID=your_cashfree_app_id
CASHFREE_SECRET_KEY=your_cashfree_secret_key
CASHFREE_ENV=sandbox
# Change to: production  when going live
CASHFREE_BASE_URL=https://sandbox.cashfree.com/pg

# WhatsApp (Twilio — fill when client provides)
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886

# Company info for invoices
COMPANY_NAME=BeyondBridge Advisory Pvt Ltd
COMPANY_EMAIL=contact@beyond-bridge.com
COMPANY_ADDRESS=India
        """,
        'models/db.js': """
const path = require('path');
require('dotenv').config();

let db;

if (process.env.DB_TYPE === 'mysql') {
  // cPanel production
  const mysql = require('mysql2/promise');
  const pool = mysql.createPool({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASS,
    database: process.env.DB_NAME,
    waitForConnections: true,
    connectionLimit: 10,
  });
  db = pool;
  console.log('✅ MySQL connected');
} else {
  // Local development — SQLite
  const Database = require('better-sqlite3');
  const dbPath = path.join(__dirname, '..', 'beyondbridge.db');
  db = new Database(dbPath);
  console.log('✅ SQLite connected at', dbPath);

  // Create tables
  db.exec(`
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      first_name TEXT NOT NULL,
      last_name TEXT NOT NULL,
      email TEXT UNIQUE NOT NULL,
      phone TEXT,
      profession TEXT,
      company TEXT,
      rank_designation TEXT,
      years_experience INTEGER,
      password_hash TEXT NOT NULL,
      is_verified INTEGER DEFAULT 0,
      subscribe_blog INTEGER DEFAULT 0,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS otps (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      email TEXT NOT NULL,
      otp TEXT NOT NULL,
      expires_at DATETIME NOT NULL,
      used INTEGER DEFAULT 0,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS bookings (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      user_id INTEGER,
      full_name TEXT NOT NULL,
      email TEXT NOT NULL,
      phone TEXT NOT NULL,
      profession TEXT,
      rank_designation TEXT,
      years_experience INTEGER,
      current_location TEXT,
      target_mba_year TEXT,
      preferred_geography TEXT,
      target_schools TEXT,
      gmat_status TEXT,
      main_concern TEXT,
      resume_path TEXT,
      preferred_slot TEXT,
      package_id TEXT,
      package_name TEXT,
      package_price INTEGER,
      payment_status TEXT DEFAULT 'pending',
      payment_order_id TEXT,
      payment_ref TEXT,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (user_id) REFERENCES users(id)
    );

    CREATE TABLE IF NOT EXISTS payments (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      booking_id INTEGER NOT NULL,
      cashfree_order_id TEXT,
      cashfree_payment_id TEXT,
      amount INTEGER NOT NULL,
      currency TEXT DEFAULT 'INR',
      status TEXT DEFAULT 'created',
      invoice_path TEXT,
      paid_at DATETIME,
      created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (booking_id) REFERENCES bookings(id)
    );
  `);
}

module.exports = db;
        """,
        'server.js': """
require('dotenv').config();
const express    = require('express');
const cors       = require('cors');
const path       = require('path');

const authRoutes    = require('./routes/auth');
const bookingRoutes = require('./routes/booking');
const webhookRoutes = require('./routes/webhook');

const app  = express();
const PORT = process.env.PORT || 3001;

// ─── MIDDLEWARE ───────────────────────────────────────────
app.use(cors({
  origin: process.env.FRONTEND_URL || '*',
  credentials: true
}));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));

// Serve frontend build if needed
// app.use(express.static(path.join(__dirname, '../frontend')));

// ─── ROUTES ───────────────────────────────────────────────
app.use('/api/auth',    authRoutes);
app.use('/api/booking', bookingRoutes);
app.use('/api/webhook', webhookRoutes);

// Health check
app.get('/api/health', (req, res) => res.json({ status: 'ok', env: process.env.NODE_ENV }));

// ─── START ────────────────────────────────────────────────
app.listen(PORT, () => {
  console.log(`🚀 BeyondBridge backend running on http://localhost:${PORT}`);
});
        """,
        'services/emailService.js': """
const nodemailer = require('nodemailer');
require('dotenv').config();

const transporter = nodemailer.createTransport({
  host:   process.env.EMAIL_HOST,
  port:   parseInt(process.env.EMAIL_PORT),
  secure: process.env.EMAIL_SECURE === 'true',
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASS,
  },
});

// ─── OTP Email ────────────────────────────────────────────
async function sendOTPEmail(toEmail, firstName, otp) {
  const html = `
    <div style="font-family:'DM Sans',Arial,sans-serif;background:#0d0d0d;color:#f5f0e8;padding:48px;max-width:560px;margin:auto;border-radius:8px;">
      <h1 style="font-family:Georgia,serif;color:#f5f0e8;font-size:2rem;margin:0 0 8px;">BeyondBridge</h1>
      <p style="color:#c8a96e;letter-spacing:0.2em;font-size:0.75rem;text-transform:uppercase;">MBA & Maritime Advisory</p>
      <hr style="border:none;border-top:1px solid #2a2a2a;margin:28px 0;">
      <h2 style="color:#f5f0e8;font-size:1.3rem;">Hi ${firstName}, verify your email</h2>
      <p style="color:#888;line-height:1.7;">Your one-time verification code is:</p>
      <div style="background:#1c1c1c;border:1px solid #2a2a2a;border-radius:6px;padding:28px;text-align:center;margin:24px 0;">
        <span style="font-size:2.8rem;font-weight:700;letter-spacing:0.4em;color:#C0392B;">${otp}</span>
      </div>
      <p style="color:#888;font-size:0.85rem;">This code expires in <strong style="color:#f5f0e8;">10 minutes</strong>. Do not share it with anyone.</p>
      <p style="color:#555;font-size:0.8rem;margin-top:32px;">If you did not create a BeyondBridge account, ignore this email.</p>
    </div>
  `;
  await transporter.sendMail({
    from:    process.env.EMAIL_FROM,
    to:      toEmail,
    subject: 'Your BeyondBridge verification code',
    html,
  });
}

// ─── Payment Invoice Email ─────────────────────────────────
async function sendInvoiceEmail(toEmail, firstName, bookingDetails, invoicePath) {
  const { packageName, packagePrice, bookingId, paymentRef } = bookingDetails;
  const html = `
    <div style="font-family:'DM Sans',Arial,sans-serif;background:#0d0d0d;color:#f5f0e8;padding:48px;max-width:560px;margin:auto;border-radius:8px;">
      <h1 style="font-family:Georgia,serif;color:#f5f0e8;font-size:2rem;margin:0 0 8px;">BeyondBridge</h1>
      <p style="color:#c8a96e;letter-spacing:0.2em;font-size:0.75rem;text-transform:uppercase;">MBA & Maritime Advisory</p>
      <hr style="border:none;border-top:1px solid #2a2a2a;margin:28px 0;">
      <h2 style="color:#27ae60;">✓ Payment Confirmed</h2>
      <p style="color:#888;">Hi ${firstName}, your payment has been received successfully.</p>
      <div style="background:#1c1c1c;border:1px solid #2a2a2a;border-radius:6px;padding:24px;margin:24px 0;">
        <table style="width:100%;color:#f5f0e8;font-size:0.9rem;">
          <tr><td style="color:#888;padding:6px 0;">Package</td><td style="text-align:right;">${packageName}</td></tr>
          <tr><td style="color:#888;padding:6px 0;">Amount Paid</td><td style="text-align:right;color:#27ae60;">₹${(packagePrice/100).toLocaleString('en-IN')}</td></tr>
          <tr><td style="color:#888;padding:6px 0;">Booking ID</td><td style="text-align:right;">#BB-${bookingId}</td></tr>
          <tr><td style="color:#888;padding:6px 0;">Payment Ref</td><td style="text-align:right;">${paymentRef}</td></tr>
        </table>
      </div>
      <p style="color:#888;line-height:1.7;">Your invoice is attached to this email. Our team will contact you within 24 hours to schedule your first session.</p>
      <p style="color:#c8a96e;font-size:0.85rem;">BeyondBridge Team | contact@beyond-bridge.com</p>
    </div>
  `;
  const mailOptions = {
    from:    process.env.EMAIL_FROM,
    to:      toEmail,
    subject: `BeyondBridge — Payment Confirmed: ${packageName} | #BB-${bookingId}`,
    html,
  };
  if (invoicePath) {
    mailOptions.attachments = [{
      filename: `BeyondBridge_Invoice_BB-${bookingId}.pdf`,
      path:     invoicePath,
    }];
  }
  await transporter.sendMail(mailOptions);

  // Also notify admin
  await transporter.sendMail({
    from:    process.env.EMAIL_FROM,
    to:      process.env.ADMIN_EMAIL,
    subject: `[New Booking] ${firstName} — ${packageName} — ₹${(packagePrice/100).toLocaleString('en-IN')}`,
    html:    `<p>New booking received.<br>Name: ${firstName}<br>Email: ${toEmail}<br>Package: ${packageName}<br>Amount: ₹${(packagePrice/100).toLocaleString('en-IN')}<br>Booking ID: #BB-${bookingId}</p>`,
  });
}

module.exports = { sendOTPEmail, sendInvoiceEmail };
        """,
        'services/invoiceService.js': """
const PDFDocument = require('pdfkit');
const fs = require('fs');
const path = require('path');

async function generateInvoice(bookingDetails) {
  const {
    bookingId, firstName, lastName, email, phone,
    packageName, packagePrice, paymentRef, paidAt
  } = bookingDetails;

  const invoiceDir  = path.join(__dirname, '..', 'invoices');
  if (!fs.existsSync(invoiceDir)) fs.mkdirSync(invoiceDir, { recursive: true });

  const invoicePath = path.join(invoiceDir, `BB-${bookingId}-invoice.pdf`);
  const doc         = new PDFDocument({ margin: 50, size: 'A4' });
  const stream      = fs.createWriteStream(invoicePath);

  doc.pipe(stream);

  // Header
  doc.rect(0, 0, doc.page.width, 80).fill('#0a1628');
  doc.fillColor('#ffffff').fontSize(24).font('Helvetica-Bold')
     .text('BeyondBridge', 50, 25);
  doc.fillColor('#c8a96e').fontSize(9).font('Helvetica')
     .text('MBA & MARITIME ADVISORY', 50, 55, { characterSpacing: 2 });

  doc.fillColor('#333333');

  // Invoice title
  doc.moveDown(2);
  doc.fillColor('#C0392B').fontSize(18).font('Helvetica-Bold').text('PAYMENT INVOICE', { align: 'right' });
  doc.fillColor('#555').fontSize(10).font('Helvetica')
     .text(`Invoice #: BB-${bookingId}`, { align: 'right' })
     .text(`Date: ${new Date(paidAt || Date.now()).toLocaleDateString('en-IN', { year:'numeric', month:'long', day:'numeric' })}`, { align: 'right' });

  // Divider
  doc.moveDown(1);
  doc.moveTo(50, doc.y).lineTo(545, doc.y).strokeColor('#e0e0e0').lineWidth(1).stroke();
  doc.moveDown(1);

  // Bill to
  doc.fillColor('#888').fontSize(9).font('Helvetica').text('BILLED TO');
  doc.fillColor('#111').fontSize(12).font('Helvetica-Bold').text(`${firstName} ${lastName}`);
  doc.fillColor('#555').fontSize(10).font('Helvetica').text(email).text(phone);

  doc.moveDown(2);

  // Package table
  doc.fillColor('#0a1628').rect(50, doc.y, 495, 36).fill();
  doc.fillColor('#ffffff').fontSize(10).font('Helvetica-Bold')
     .text('Description', 60, doc.y - 25)
     .text('Amount', 450, doc.y - 25, { width: 80, align: 'right' });

  doc.moveDown(0.5);
  doc.fillColor('#111').fontSize(11).font('Helvetica').text(packageName, 60, doc.y);
  const amount = `₹${(packagePrice / 100).toLocaleString('en-IN')}`;
  doc.text(amount, 450, doc.y - 15, { width: 80, align: 'right' });

  doc.moveDown(2);
  doc.moveTo(50, doc.y).lineTo(545, doc.y).strokeColor('#e0e0e0').lineWidth(0.5).stroke();
  doc.moveDown(1);

  // Total
  doc.fillColor('#111').fontSize(13).font('Helvetica-Bold')
     .text('Total Paid:', 380)
     .fillColor('#C0392B').text(amount, 460, doc.y - 19, { width: 80, align: 'right' });

  doc.moveDown(1);
  doc.fillColor('#888').fontSize(9).font('Helvetica').text(`Payment Reference: ${paymentRef}`);

  // Footer
  const footerY = doc.page.height - 80;
  doc.moveTo(50, footerY).lineTo(545, footerY).strokeColor('#e0e0e0').lineWidth(0.5).stroke();
  doc.fillColor('#888').fontSize(8).font('Helvetica')
     .text('BeyondBridge Advisory | contact@beyond-bridge.com | beyond-bridge.com', 50, footerY + 10, { align: 'center' })
     .text('This is a computer-generated invoice and does not require a physical signature.', { align: 'center' });

  doc.end();

  return new Promise((resolve, reject) => {
    stream.on('finish', () => resolve(invoicePath));
    stream.on('error', reject);
  });
}

module.exports = { generateInvoice };
        """,
        'services/cashfreeService.js': """
const axios = require('axios');
require('dotenv').config();

const BASE_URL = process.env.CASHFREE_BASE_URL || 'https://sandbox.cashfree.com/pg';

const headers = {
  'x-client-id':     process.env.CASHFREE_APP_ID,
  'x-client-secret': process.env.CASHFREE_SECRET_KEY,
  'x-api-version':   '2023-08-01',
  'Content-Type':    'application/json',
};

async function createOrder({ orderId, amount, currency='INR', customerName, customerEmail, customerPhone, returnUrl }) {
  const payload = {
    order_id:       orderId,
    order_amount:   amount / 100,   // Cashfree takes rupees, not paise
    order_currency: currency,
    customer_details: {
      customer_id:    `cust_${Date.now()}`,
      customer_name:  customerName,
      customer_email: customerEmail,
      customer_phone: customerPhone,
    },
    order_meta: {
      return_url: returnUrl,
    },
  };

  const response = await axios.post(`${BASE_URL}/orders`, payload, { headers });
  return response.data;  // contains payment_session_id, order_id
}

async function verifyPayment(orderId) {
  const response = await axios.get(`${BASE_URL}/orders/${orderId}`, { headers });
  return response.data;  // order_status: PAID / ACTIVE / EXPIRED
}

module.exports = { createOrder, verifyPayment };
        """,
        'services/whatsappService.js': """
// WhatsApp notification service
// Currently stubbed — wire when client provides Twilio/WATI credentials

async function sendWhatsAppOTP(phone, firstName, otp) {
  console.log(`[WhatsApp STUB] OTP ${otp} to ${phone} for ${firstName}`);
  // TODO: Uncomment and fill credentials in .env
  /*
  const twilio = require('twilio')(process.env.TWILIO_ACCOUNT_SID, process.env.TWILIO_AUTH_TOKEN);
  await twilio.messages.create({
    from: process.env.TWILIO_WHATSAPP_FROM,
    to:   `whatsapp:${phone}`,
    body: `Hi ${firstName}, your BeyondBridge verification code is: *${otp}*\nValid for 10 minutes.`
  });
  */
}

async function sendWhatsAppInvoice(phone, firstName, bookingDetails) {
  console.log(`[WhatsApp STUB] Invoice to ${phone} for booking #BB-${bookingDetails.bookingId}`);
  // TODO: Wire Twilio/WATI here
  /*
  const { packageName, packagePrice, bookingId } = bookingDetails;
  const twilio = require('twilio')(process.env.TWILIO_ACCOUNT_SID, process.env.TWILIO_AUTH_TOKEN);
  await twilio.messages.create({
    from: process.env.TWILIO_WHATSAPP_FROM,
    to:   `whatsapp:${phone}`,
    body: `Hi ${firstName}! ✅ Your payment for *${packageName}* (₹${(packagePrice/100).toLocaleString('en-IN')}) is confirmed.\nBooking ID: #BB-${bookingId}\nOur team will reach out within 24 hours.\n— BeyondBridge Team`
  });
  */
}

module.exports = { sendWhatsAppOTP, sendWhatsAppInvoice };
        """,
        'routes/auth.js': """
const express      = require('express');
const router       = express.Router();
const rateLimit    = require('express-rate-limit');
const authCtrl     = require('../controllers/authController');

// Rate limit OTP endpoint — max 5 requests per 15 minutes per IP
const otpLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,
  message: { error: 'Too many OTP requests. Please wait 15 minutes.' }
});

router.post('/signup',        authCtrl.signup);
router.post('/verify-otp',    otpLimiter, authCtrl.verifyOTP);
router.post('/resend-otp',    otpLimiter, authCtrl.resendOTP);
router.post('/login',         authCtrl.login);
router.post('/logout',        authCtrl.logout);

module.exports = router;
        """,
        'controllers/authController.js': """
const bcrypt    = require('bcryptjs');
const jwt       = require('jsonwebtoken');
const { v4: uuidv4 } = require('uuid');
const db        = require('../models/db');
const { sendOTPEmail }      = require('../services/emailService');
const { sendWhatsAppOTP }   = require('../services/whatsappService');

function generateOTP() {
  return Math.floor(100000 + Math.random() * 900000).toString(); // 6 digits
}

// ─── SIGNUP ───────────────────────────────────────────────
exports.signup = async (req, res) => {
  try {
    const { firstName, lastName, email, phone, profession, company, rankDesignation, yearsExperience, password } = req.body;

    if (!firstName || !lastName || !email || !password) {
      return res.status(400).json({ error: 'Required fields missing.' });
    }

    // Check existing user
    const existing = db.prepare('SELECT id FROM users WHERE email = ?').get(email);
    if (existing) return res.status(409).json({ error: 'An account with this email already exists.' });

    const passwordHash = await bcrypt.hash(password, 12);

    // Insert user (unverified)
    const stmt = db.prepare(`
      INSERT INTO users (first_name, last_name, email, phone, profession, company, rank_designation, years_experience, password_hash, is_verified)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0)
    `);
    stmt.run(firstName, lastName, email, phone || '', profession || '', company || '', rankDesignation || '', yearsExperience || 0, passwordHash);

    // Generate & store OTP
    const otp       = generateOTP();
    const expiresAt = new Date(Date.now() + 10 * 60 * 1000).toISOString(); // 10 min
    db.prepare('INSERT INTO otps (email, otp, expires_at) VALUES (?, ?, ?)').run(email, otp, expiresAt);

    // Send OTP
    await sendOTPEmail(email, firstName, otp);
    await sendWhatsAppOTP(phone, firstName, otp);  // stub for now

    res.json({ success: true, message: 'OTP sent to your email. Please verify to complete signup.' });
  } catch (err) {
    console.error('Signup error:', err);
    res.status(500).json({ error: 'Signup failed. Please try again.' });
  }
};

// ─── VERIFY OTP ───────────────────────────────────────────
exports.verifyOTP = async (req, res) => {
  try {
    const { email, otp } = req.body;

    const record = db.prepare(`
      SELECT * FROM otps WHERE email = ? AND used = 0
      ORDER BY created_at DESC LIMIT 1
    `).get(email);

    if (!record) return res.status(400).json({ error: 'No OTP found. Please request a new one.' });
    if (new Date(record.expires_at) < new Date()) return res.status(400).json({ error: 'OTP has expired. Please request a new one.' });
    if (record.otp !== otp) return res.status(400).json({ error: 'Invalid OTP. Please try again.' });

    // Mark OTP used
    db.prepare('UPDATE otps SET used = 1 WHERE id = ?').run(record.id);

    // Verify user
    db.prepare('UPDATE users SET is_verified = 1 WHERE email = ?').run(email);

    // Issue JWT
    const user  = db.prepare('SELECT * FROM users WHERE email = ?').get(email);
    const token = jwt.sign({ userId: user.id, email: user.email }, process.env.JWT_SECRET, { expiresIn: '7d' });

    res.json({
      success: true,
      message: 'Email verified. Welcome to BeyondBridge!',
      token,
      user: { id: user.id, firstName: user.first_name, lastName: user.last_name, email: user.email }
    });
  } catch (err) {
    console.error('OTP verify error:', err);
    res.status(500).json({ error: 'Verification failed. Please try again.' });
  }
};

// ─── RESEND OTP ───────────────────────────────────────────
exports.resendOTP = async (req, res) => {
  try {
    const { email } = req.body;
    const user = db.prepare('SELECT * FROM users WHERE email = ?').get(email);
    if (!user) return res.status(404).json({ error: 'No account found with this email.' });
    if (user.is_verified) return res.status(400).json({ error: 'This account is already verified.' });

    const otp       = generateOTP();
    const expiresAt = new Date(Date.now() + 10 * 60 * 1000).toISOString();
    db.prepare('INSERT INTO otps (email, otp, expires_at) VALUES (?, ?, ?)').run(email, otp, expiresAt);
    await sendOTPEmail(email, user.first_name, otp);

    res.json({ success: true, message: 'New OTP sent to your email.' });
  } catch (err) {
    res.status(500).json({ error: 'Failed to resend OTP.' });
  }
};

// ─── LOGIN ────────────────────────────────────────────────
exports.login = async (req, res) => {
  try {
    const { email, password, subscribeBlog } = req.body;

    const user = db.prepare('SELECT * FROM users WHERE email = ?').get(email);
    if (!user) return res.status(401).json({ error: 'Invalid email or password.' });
    if (!user.is_verified) return res.status(403).json({ error: 'Please verify your email before logging in.', needsVerification: true });

    const valid = await bcrypt.compare(password, user.password_hash);
    if (!valid) return res.status(401).json({ error: 'Invalid email or password.' });

    // Update subscribe preference
    if (subscribeBlog !== undefined) {
      db.prepare('UPDATE users SET subscribe_blog = ? WHERE id = ?').run(subscribeBlog ? 1 : 0, user.id);
    }

    const token = jwt.sign({ userId: user.id, email: user.email }, process.env.JWT_SECRET, { expiresIn: '7d' });

    res.json({
      success: true,
      token,
      user: { id: user.id, firstName: user.first_name, lastName: user.last_name, email: user.email }
    });
  } catch (err) {
    console.error('Login error:', err);
    res.status(500).json({ error: 'Login failed. Please try again.' });
  }
};

exports.logout = (req, res) => {
  // JWT is stateless — frontend deletes the token
  res.json({ success: true, message: 'Logged out.' });
};
        """,
        'routes/booking.js': """
const express = require('express');
const router  = express.Router();
const multer  = require('multer');
const path    = require('path');
const bookCtrl = require('../controllers/bookingController');
const authMw   = require('../middleware/auth');

const storage = multer.diskStorage({
  destination: (req, file, cb) => cb(null, path.join(__dirname, '..', 'uploads')),
  filename:    (req, file, cb) => cb(null, `resume_${Date.now()}_${file.originalname}`)
});
const upload = multer({ storage, limits: { fileSize: 5 * 1024 * 1024 } }); // 5MB max

// Submit consultation form
router.post('/submit',         upload.single('resume'), bookCtrl.submitForm);

// Create Cashfree payment order
router.post('/create-payment', bookCtrl.createPayment);

// Verify payment after redirect
router.post('/verify-payment', bookCtrl.verifyPayment);

module.exports = router;
        """,
        'controllers/bookingController.js': """
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
    const booking = db.prepare('SELECT * FROM bookings WHERE id=?').get(bookingId);

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
        """,
        'middleware/auth.js': """
const jwt = require('jsonwebtoken');

module.exports = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token      = authHeader && authHeader.split(' ')[1]; // Bearer <token>

  if (!token) return res.status(401).json({ error: 'Authentication required.' });

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch {
    res.status(403).json({ error: 'Invalid or expired session. Please log in again.' });
  }
};
        """,
        'routes/webhook.js': """
const express = require('express');
const router  = express.Router();
const crypto  = require('crypto');
require('dotenv').config();

router.post('/cashfree', express.raw({ type: 'application/json' }), (req, res) => {
  // Verify Cashfree webhook signature
  const signature  = req.headers['x-webhook-signature'];
  const timestamp  = req.headers['x-webhook-timestamp'];
  const rawBody    = req.body.toString();
  const payload    = timestamp + rawBody;
  const expected   = crypto.createHmac('sha256', process.env.CASHFREE_SECRET_KEY)
                           .update(payload).digest('base64');

  if (signature !== expected) {
    console.warn('Webhook signature mismatch');
    return res.status(400).send('Invalid signature');
  }

  const event = JSON.parse(rawBody);
  console.log('Cashfree webhook event:', event.type);

  // Handle payment events here if needed (backup to verify-payment endpoint)
  res.status(200).send('OK');
});

module.exports = router;
        """
    }

    for path, content in files.items():
        create_file(path, content)

    # Create .env from .env.example
    create_file('.env', files['.env.example'])
    
    # Create uploads dir
    uploads_dir = os.path.join(BACKEND_DIR, 'uploads')
    os.makedirs(uploads_dir, exist_ok=True)
    
if __name__ == '__main__':
    setup_backend()
