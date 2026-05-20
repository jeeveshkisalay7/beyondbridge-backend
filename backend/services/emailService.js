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
  tls: {
    rejectUnauthorized: false
  },
  connectionTimeout: 5000, // Fail fast (5 seconds) instead of hanging!
  greetingTimeout: 5000
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
  try {
    await transporter.sendMail({
      from:    process.env.EMAIL_FROM || process.env.EMAIL_USER,
      to:      toEmail,
      subject: 'Your BeyondBridge verification code',
      html,
    });
  } catch (err) {
    console.error('Failed to send email. The OTP for', toEmail, 'is:', otp);
    console.error('Email error details:', err.message);
    
    // TEMPORARY FIX: Don't crash the signup if email fails.
    // Instead, log the OTP directly to the terminal so we can test the app!
    console.log(`\n======================================================`);
    console.log(`⚠️ EMAIL FAILED TO SEND!`);
    console.log(`BUT DON'T WORRY, USE THIS OTP TO CONTINUE: ${otp}`);
    console.log(`======================================================\n`);
  }
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
