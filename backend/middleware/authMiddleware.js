const jwt = require('jsonwebtoken');
const UserModel = require('../models/userModel');
require('dotenv').config();

const JWT_SECRET = process.env.JWT_SECRET || 'super_secret_beyondbridge_key_1928374655';

const protectRoute = async (req, res, next) => {
  let token = null;

  // 1. Read token from HTTP-only Cookie
  if (req.cookies && req.cookies.token) {
    token = req.cookies.token;
  }
  // 2. Fallback to Authorization Header (Bearer Token)
  else if (req.headers.authorization && req.headers.authorization.startsWith('Bearer')) {
    token = req.headers.authorization.split(' ')[1];
  }

  // 3. Reject if no token
  if (!token) {
    return res.status(401).json({
      success: false,
      message: 'Access denied. Please log in to proceed.'
    });
  }

  try {
    // 4. Verify token
    const decoded = jwt.verify(token, JWT_SECRET);

    // 5. Look up user and confirm they are verified
    const user = await UserModel.findById(decoded.id);
    if (!user) {
      return res.status(401).json({
        success: false,
        message: 'Invalid session. User account not found.'
      });
    }

    if (!user.is_verified) {
      return res.status(401).json({
        success: false,
        message: 'Account not verified. Please verify your email first.'
      });
    }

    // 6. Inject user model into request
    req.user = user;
    next();
  } catch (err) {
    console.error('JWT Verification Error:', err.message);
    return res.status(401).json({
      success: false,
      message: 'Session has expired or token is invalid. Please log in again.'
    });
  }
};

module.exports = {
  protectRoute
};
