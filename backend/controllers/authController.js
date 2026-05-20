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
    const existing = await db.get('SELECT id, is_verified FROM users WHERE email = ?', email);
    if (existing) {
      if (existing.is_verified) {
        return res.status(409).json({ error: 'An account with this email already exists.' });
      } else {
        // Delete the unverified user so they can try signing up again cleanly
        await db.run('DELETE FROM users WHERE id = ?', existing.id);
      }
    }

    const passwordHash = await bcrypt.hash(password, 12);

    // Insert user (unverified)
    await db.run(`
      INSERT INTO users (first_name, last_name, email, phone, profession, company, rank_designation, years_experience, password_hash, is_verified)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0)
    `, firstName, lastName, email, phone || '', profession || '', company || '', rankDesignation || '', yearsExperience || 0, passwordHash);

    // Generate & store OTP
    const otp       = generateOTP();
    const expiresAt = new Date(Date.now() + 10 * 60 * 1000).toISOString().slice(0, 19).replace('T', ' '); // 10 min
    await db.run('INSERT INTO otps (email, otp, expires_at) VALUES (?, ?, ?)', email, otp, expiresAt);

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

    const record = await db.get(`
      SELECT * FROM otps WHERE email = ? AND used = 0
      ORDER BY created_at DESC LIMIT 1
    `, email);

    if (!record) return res.status(400).json({ error: 'No OTP found. Please request a new one.' });
    if (new Date(record.expires_at) < new Date()) return res.status(400).json({ error: 'OTP has expired. Please request a new one.' });
    if (record.otp !== otp) return res.status(400).json({ error: 'Invalid OTP. Please try again.' });

    // Mark OTP used
    await db.run('UPDATE otps SET used = 1 WHERE id = ?', record.id);

    // Verify user
    await db.run('UPDATE users SET is_verified = 1 WHERE email = ?', email);

    // Issue JWT
    const user  = await db.get('SELECT * FROM users WHERE email = ?', email);
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
    const user = await db.get('SELECT * FROM users WHERE email = ?', email);
    if (!user) return res.status(404).json({ error: 'No account found with this email.' });
    if (user.is_verified) return res.status(400).json({ error: 'This account is already verified.' });

    const otp       = generateOTP();
    const expiresAt = new Date(Date.now() + 10 * 60 * 1000).toISOString().slice(0, 19).replace('T', ' ');
    await db.run('INSERT INTO otps (email, otp, expires_at) VALUES (?, ?, ?)', email, otp, expiresAt);
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

    const user = await db.get('SELECT * FROM users WHERE email = ?', email);
    if (!user) return res.status(401).json({ error: 'Invalid email or password.' });
    if (!user.is_verified) return res.status(403).json({ error: 'Please verify your email before logging in.', needsVerification: true });

    const valid = await bcrypt.compare(password, user.password_hash);
    if (!valid) return res.status(401).json({ error: 'Invalid email or password.' });

    // Update subscribe preference
    if (subscribeBlog !== undefined) {
      await db.run('UPDATE users SET subscribe_blog = ? WHERE id = ?', subscribeBlog ? 1 : 0, user.id);
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
