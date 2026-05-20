const db = require('../config/db');

class UserModel {
  // Find a user account by email address
  async findByEmail(email) {
    const query = 'SELECT * FROM users WHERE email = ? LIMIT 1';
    const [rows] = await db.query(query, [email.trim().toLowerCase()]);
    return rows[0] || null;
  }

  // Find a user account by ID
  async findById(id) {
    const query = 'SELECT id, full_name, email, is_verified, created_at FROM users WHERE id = ? LIMIT 1';
    const [rows] = await db.query(query, [id]);
    return rows[0] || null;
  }

  // Create a new unverified user account
  async create(fullName, email, hashedPassword) {
    const query = 'INSERT INTO users (full_name, email, hashed_password, is_verified) VALUES (?, ?, ?, false)';
    const [result] = await db.query(query, [
      fullName.trim(),
      email.trim().toLowerCase(),
      hashedPassword
    ]);
    return result.insertId;
  }

  // Set is_verified = true for a user
  async verify(email) {
    const query = 'UPDATE users SET is_verified = true WHERE email = ?';
    const [result] = await db.query(query, [email.trim().toLowerCase()]);
    return result.affectedRows > 0;
  }

  // Delete user account (helpful for cleaning up unverified user entries)
  async delete(email) {
    const query = 'DELETE FROM users WHERE email = ?';
    const [result] = await db.query(query, [email.trim().toLowerCase()]);
    return result.affectedRows > 0;
  }
}

module.exports = new UserModel();
