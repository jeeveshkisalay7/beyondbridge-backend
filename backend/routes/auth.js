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
