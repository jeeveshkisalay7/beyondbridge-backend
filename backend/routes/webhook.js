const express = require('express');
const router  = express.Router();
const crypto  = require('crypto');
require('dotenv').config();

router.post('/cashfree', express.raw({ type: 'application/json' }), (req, res) => {
  // Verify Cashfree webhook signature
  const signature  = req.headers['x-webhook-signature'];
  const timestamp  = req.headers['x-webhook-timestamp'];
  const rawBody    = req.body.toString();
  const payload    = timestamp + rawBody;
  const expected   = crypto.createHmac('sha256', process.env.CASHFREE_SECRET_KEY)
                           .update(payload).digest('base64');

  if (signature !== expected) {
    console.warn('Webhook signature mismatch');
    return res.status(400).send('Invalid signature');
  }

  const event = JSON.parse(rawBody);
  console.log('Cashfree webhook event:', event.type);

  // Handle payment events here if needed (backup to verify-payment endpoint)
  res.status(200).send('OK');
});

module.exports = router;
