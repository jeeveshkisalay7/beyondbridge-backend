/**
 * Input validation middlewares for robust authentication APIs
 */

// Helper: validate email address format
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// Helper: validate password complexity (production-ready)
function isStrongPassword(password) {
  // Min 8 characters, at least 1 uppercase letter, 1 lowercase letter, 1 number, and 1 special character
  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$/;
  return passwordRegex.test(password);
}

// Middleware: Validate Signup Fields
const validateSignup = (req, res, next) => {
  const { fullName, email, password, confirmPassword } = req.body;

  // 1. Check for empty fields
  if (!fullName || !email || !password || !confirmPassword) {
    return res.status(400).json({
      success: false,
      message: 'All fields (fullName, email, password, confirmPassword) are required.'
    });
  }

  // 2. Validate email format
  if (!isValidEmail(email)) {
    return res.status(400).json({
      success: false,
      message: 'Please enter a valid email address format.'
    });
  }

  // 3. Check password matching
  if (password !== confirmPassword) {
    return res.status(400).json({
      success: false,
      message: 'Passwords do not match.'
    });
  }

  // 4. Validate password complexity
  if (!isStrongPassword(password)) {
    return res.status(400).json({
      success: false,
      message: 'Password is too weak. It must contain at least 8 characters, including 1 uppercase, 1 lowercase, 1 digit, and 1 special symbol (e.g. @, $, !, %, *, ?, &, #).'
    });
  }

  next();
};

// Middleware: Validate OTP verification parameters
const validateVerifyOtp = (req, res, next) => {
  const { email, otp } = req.body;

  if (!email || !otp) {
    return res.status(400).json({
      success: false,
      message: 'Both email address and OTP verification code are required.'
    });
  }

  if (!isValidEmail(email)) {
    return res.status(400).json({
      success: false,
      message: 'Please enter a valid email address.'
    });
  }

  if (otp.trim().length !== 6 || !/^\d+$/.test(otp)) {
    return res.status(400).json({
      success: false,
      message: 'Verification code must be exactly 6 numeric digits.'
    });
  }

  next();
};

// Middleware: Validate Login Fields
const validateLogin = (req, res, next) => {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({
      success: false,
      message: 'Both email and password fields are required.'
    });
  }

  if (!isValidEmail(email)) {
    return res.status(400).json({
      success: false,
      message: 'Please enter a valid email address format.'
    });
  }

  next();
};

module.exports = {
  validateSignup,
  validateVerifyOtp,
  validateLogin
};
