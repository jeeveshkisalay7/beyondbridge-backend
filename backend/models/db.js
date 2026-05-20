const mysql = require('mysql2/promise');
require('dotenv').config();

const pool = mysql.createPool({
  host: process.env.DB_HOST,
  port: process.env.DB_PORT || 3306,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD || process.env.DB_PASS,
  database: process.env.DB_NAME,
  ssl: process.env.DB_SSL === 'true' ? { 
    // ca: require('fs').readFileSync(require('path').join(__dirname, '..', 'ca.pem')), // Uncomment if using Aiven CA cert
    rejectUnauthorized: false 
  } : undefined,
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0
});

async function initDB() {
  try {
    const connection = await pool.getConnection();
    console.log('✅ MySQL connected');
    
    await connection.execute(`
      CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        phone VARCHAR(255),
        profession VARCHAR(255),
        company VARCHAR(255),
        rank_designation VARCHAR(255),
        years_experience INT,
        password_hash VARCHAR(255) NOT NULL,
        is_verified TINYINT DEFAULT 0,
        subscribe_blog TINYINT DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
      )
    `);

    await connection.execute(`
      CREATE TABLE IF NOT EXISTS otps (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) NOT NULL,
        otp VARCHAR(255) NOT NULL,
        expires_at DATETIME NOT NULL,
        used TINYINT DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
      )
    `);

    await connection.execute(`
      CREATE TABLE IF NOT EXISTS bookings (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        full_name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone VARCHAR(255) NOT NULL,
        profession VARCHAR(255),
        rank_designation VARCHAR(255),
        years_experience INT,
        current_location VARCHAR(255),
        target_mba_year VARCHAR(255),
        preferred_geography VARCHAR(255),
        target_schools TEXT,
        gmat_status VARCHAR(255),
        main_concern TEXT,
        resume_path VARCHAR(255),
        preferred_slot VARCHAR(255),
        package_id VARCHAR(255),
        package_name VARCHAR(255),
        package_price INT,
        payment_status VARCHAR(255) DEFAULT 'pending',
        payment_order_id VARCHAR(255),
        payment_ref VARCHAR(255),
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id)
      )
    `);

    await connection.execute(`
      CREATE TABLE IF NOT EXISTS payments (
        id INT AUTO_INCREMENT PRIMARY KEY,
        booking_id INT NOT NULL,
        cashfree_order_id VARCHAR(255),
        cashfree_payment_id VARCHAR(255),
        amount INT NOT NULL,
        currency VARCHAR(10) DEFAULT 'INR',
        status VARCHAR(50) DEFAULT 'created',
        invoice_path VARCHAR(255),
        paid_at DATETIME,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (booking_id) REFERENCES bookings(id)
      )
    `);

    connection.release();
  } catch (err) {
    console.error('❌ MySQL connection failed:', err);
  }
}

initDB();

const dbWrapper = {
  async get(sql, ...params) {
    const [rows] = await pool.execute(sql, params);
    return rows[0];
  },
  async run(sql, ...params) {
    const [result] = await pool.execute(sql, params);
    return { lastInsertRowid: result.insertId, changes: result.affectedRows };
  },
  async all(sql, ...params) {
    const [rows] = await pool.execute(sql, params);
    return rows;
  }
};

module.exports = dbWrapper;
