const mysql = require('mysql2/promise');
require('dotenv').config();

const dbConfig = {
  host: process.env.DB_HOST || 'localhost',
  port: parseInt(process.env.DB_PORT || '3306', 10),
  user: process.env.DB_USER || 'root',
  password: process.env.DB_PASS || '',
  database: process.env.DB_NAME || 'beyondbridge_db',
  ssl: process.env.DB_SSL === 'true' ? { 
    // ca: require('fs').readFileSync(require('path').join(__dirname, '..', 'ca.pem')), // Uncomment if using Aiven CA cert
    rejectUnauthorized: false 
  } : undefined,
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0
};

// Create a connection pool
const pool = mysql.createPool(dbConfig);

// Helper to test connection on startup
async function testConnection() {
  try {
    const connection = await pool.getConnection();
    console.log('✅ Connected to MySQL Database successfully.');
    connection.release();
  } catch (err) {
    console.error('❌ Failed to connect to MySQL database:', err.message);
    console.error('⚠️  Please ensure MySQL is running and database configuration in .env is correct.');
  }
}

testConnection();

module.exports = pool;
