const express = require('express');
const router  = express.Router();
const multer  = require('multer');
const path    = require('path');
const bookCtrl = require('../controllers/bookingController');
const authMw   = require('../middleware/auth');

const storage = multer.diskStorage({
  destination: (req, file, cb) => cb(null, path.join(__dirname, '..', 'uploads')),
  filename:    (req, file, cb) => cb(null, `resume_${Date.now()}_${file.originalname}`)
});
const upload = multer({ storage, limits: { fileSize: 5 * 1024 * 1024 } }); // 5MB max

// Submit consultation form
router.post('/submit',         upload.single('resume'), bookCtrl.submitForm);

// Create Cashfree payment order
router.post('/create-payment', bookCtrl.createPayment);

// Verify payment after redirect
router.post('/verify-payment', bookCtrl.verifyPayment);

module.exports = router;
