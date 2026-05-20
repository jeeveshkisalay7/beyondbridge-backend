const db = require('../config/db');

class OtpModel {
  // Store a new OTP code in database (wiping out any previous OTPs for that email)
  async save(email, otp, expiresAt) {
    const emailNormalized = email.trim().toLowerCase();
    
    // 1. Clear any existing OTPs for this email to prevent collisions
    await this.deleteByEmail(emailNormalized);
    
    // 2. Insert new OTP
    const query = 'INSERT INTO otp_verifications (email, otp, expires_at) VALUES (?, ?, ?)';
    const [result] = await db.query(query, [emailNormalized, otp, expiresAt]);
    return result.insertId;
  }

  // Retrieve the latest OTP verification record for a specific email
  async findLatest(email) {
    const query = 'SELECT * FROM otp_verifications WHERE email = ? ORDER BY created_at DESC LIMIT 1';
    const [rows] = await db.query(query, [email.trim().toLowerCase()]);
    return rows[0] || null;
  }

  // Delete all OTPs associated with an email
  async deleteByEmail(email) {
    const query = 'DELETE FROM otp_verifications WHERE email = ?';
    const [result] = await db.query(query, [email.trim().toLowerCase()]);
    return result.affectedRows > 0;
  }

  // Delete expired OTP records (housekeeping helper)
  async clearExpired() {
    const query = 'DELETE FROM otp_verifications WHERE expires_at < NOW()';
    const [result] = await db.query(query);
    return result.affectedRows;
  }
}

module.exports = new OtpModel();
