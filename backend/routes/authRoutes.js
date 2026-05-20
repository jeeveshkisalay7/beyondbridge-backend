const express = require('express');
const router = express.Router();
const authController = require('../controllers/authController');
const { validateSignup, validateVerifyOtp, validateLogin } = require('../middleware/validationMiddleware');
const { authLimiter } = require('../utils/helpers');

// 1. Account Signup Endpoint
// Rate limited, checks input integrity, hashes password, saves record, and dispatches OTP code.
router.post('/signup', authLimiter, validateSignup, authController.signup);

// 2. OTP Verification Endpoint
// Rate limited, verifies correctness and expiry of OTP codes.
router.post('/verify-otp', authLimiter, validateVerifyOtp, authController.verifyOtp);

// 3. Resend OTP Verification Endpoint
router.post('/resend-otp', authLimiter, authController.resendOtp);

// 4. User Login Endpoint
// Rate limited, validates credentials, issues JWT inside HTTP-Only Secure cookie.
router.post('/login', authLimiter, validateLogin, authController.login);

// 5. User Logout Endpoint
router.post('/logout', authController.logout);

module.exports = router;
