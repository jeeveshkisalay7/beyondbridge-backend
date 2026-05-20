const nodemailer = require('nodemailer');
const fs = require('fs');
const path = require('path');
require('dotenv').config();

// Append OTP to a debug file in case of no mail client or internet
const DEBUG_LOG_FILE = path.join(__dirname, '..', '..', 'otp_debug.log');

function writeDebugOtp(email, otp) {
  try {
    const logMsg = `[${new Date().toISOString()}] Email: ${email} | OTP: ${otp}\n`;
    fs.appendFileSync(DEBUG_LOG_FILE, logMsg, 'utf8');
  } catch (err) {
    console.error('Error writing debug OTP log:', err);
  }
}

// Function to generate Nodemailer transporter
async function getMailTransporter() {
  if (process.env.SMTP_HOST && process.env.SMTP_USER && process.env.SMTP_PASS) {
    console.log('Using configured SMTP provider...');
    return nodemailer.createTransport({
      host: process.env.SMTP_HOST,
      port: parseInt(process.env.SMTP_PORT || '587', 10),
      secure: parseInt(process.env.SMTP_PORT, 10) === 465,
      auth: {
        user: process.env.SMTP_USER,
        pass: process.env.SMTP_PASS
      }
    });
  }

  // Fallback Ethereal setup
  console.log('No SMTP configurations in .env. Initializing Ethereal Test Mail...');
  const testAccount = await nodemailer.createTestAccount();
  return nodemailer.createTransport({
    host: 'smtp.ethereal.email',
    port: 587,
    secure: false,
    auth: {
      user: testAccount.user,
      pass: testAccount.pass
    }
  });
}

// Modern HTML Template for OTP Email
function getOtpEmailTemplate(name, otp) {
  return `
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verify your Beyond Bridge Account</title>
    <style>
      body {
        margin: 0;
        padding: 0;
        background-color: #f7f9fa;
        font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        color: #2b303a;
      }
      .email-wrapper {
        width: 100%;
        padding: 40px 0;
        background-color: #f7f9fa;
      }
      .email-container {
        max-width: 580px;
        margin: 0 auto;
        background-color: #ffffff;
        border: 1px solid #e1e8ed;
        border-radius: 6px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03);
        overflow: hidden;
      }
      .email-header {
        background-color: #0b0b0b;
        padding: 32px 40px;
        text-align: center;
        border-bottom: 1px solid #222222;
      }
      .logo-text {
        font-size: 24px;
        font-weight: bold;
        letter-spacing: -0.02em;
        color: #ffffff;
        text-decoration: none;
      }
      .logo-dot {
        color: #d4b880;
      }
      .email-body {
        padding: 48px 40px;
      }
      .greeting {
        font-size: 20px;
        font-weight: 500;
        color: #0b0b0b;
        margin-top: 0;
        margin-bottom: 16px;
      }
      .description {
        font-size: 15px;
        line-height: 1.6;
        color: #555555;
        margin-bottom: 32px;
      }
      .otp-box {
        background-color: #f9f6f0;
        border: 1px dashed #d4b880;
        border-radius: 4px;
        padding: 24px 0;
        text-align: center;
        margin-bottom: 32px;
      }
      .otp-code {
        font-size: 38px;
        font-weight: bold;
        letter-spacing: 0.3em;
        color: #d4b880;
        font-family: monospace;
        margin-left: 0.3em;
      }
      .warning-note {
        font-size: 13px;
        line-height: 1.5;
        color: #888888;
        border-left: 2px solid #d4b880;
        padding-left: 12px;
        margin-bottom: 32px;
      }
      .email-footer {
        background-color: #fafbfc;
        padding: 32px 40px;
        border-top: 1px solid #e1e8ed;
        text-align: center;
      }
      .footer-tagline {
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #888888;
        margin-bottom: 8px;
      }
      .footer-copy {
        font-size: 11px;
        color: #aaaaaa;
        margin: 0;
      }
    </style>
  </head>
  <body>
    <div class="email-wrapper">
      <div class="email-container">
        
        <!-- Header -->
        <div class="email-header">
          <span class="logo-text">Beyond<span style="color:#d4b880">Bridge<span class="logo-dot">.</span></span></span>
        </div>
        
        <!-- Body -->
        <div class="email-body">
          <h2 class="greeting">Hello ${name},</h2>
          <p class="description">Thank you for joining Beyond Bridge. To complete your account registration and secure your profile, please verify your email address using the one-time code below.</p>
          
          <div class="otp-box">
            <span class="otp-code">${otp}</span>
          </div>
          
          <div class="warning-note">
            This verification code is strictly private and valid for **5 minutes**. If you did not initiate this registration request, please secure your email or contact support.
          </div>
          
          <p class="description" style="margin-bottom: 0;">Best regards,<br><strong>Beyond Bridge Team</strong></p>
        </div>
        
        <!-- Footer -->
        <div class="email-footer">
          <div class="footer-tagline">MBA &amp; Career Transition Advisory</div>
          <p class="footer-copy">&copy; 2026 Beyond Bridge Advisory. All rights reserved.</p>
        </div>
        
      </div>
    </div>
  </body>
  </html>
  `;
}

// Primary Send Mail Interface
async function sendOtpEmail(email, name, otp) {
  // Always write debug file for developer convenience
  writeDebugOtp(email, otp);

  try {
    const transporter = await getMailTransporter();
    const fromAddress = process.env.SMTP_FROM || '"Beyond Bridge" <noreply@beyondbridge.com>';
    
    const mailOptions = {
      from: fromAddress,
      to: email,
      subject: `Verify your email — Beyond Bridge [Code: ${otp}]`,
      text: `Hello ${name}, your verification OTP is: ${otp}. It expires in 5 minutes.`,
      html: getOtpEmailTemplate(name, otp)
    };

    const info = await transporter.sendMail(mailOptions);
    console.log(`\n======================================================`);
    console.log(`📧 EMAIL DISPATCH SUCCESSFUL`);
    console.log(`Recipient: ${email}`);
    console.log(`OTP Code:  ${otp}`);
    
    const previewUrl = nodemailer.getTestMessageUrl(info);
    if (previewUrl) {
      console.log(`\n🔗 ETHEREAL PREVIEW URL:`);
      console.log(`👉 ${previewUrl}`);
      console.log(`(Click the link above to view your message in Ethereal's web viewer!)`);
    }
    console.log(`======================================================\n`);

    return { success: true, previewUrl };
  } catch (err) {
    console.error('❌ Nodemailer Error: Failed to send OTP email:', err.message);
    return { success: false, error: err.message };
  }
}

module.exports = {
  sendOtpEmail
};
