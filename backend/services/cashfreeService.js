const axios = require('axios');
require('dotenv').config();

const BASE_URL = process.env.CASHFREE_BASE_URL || 'https://sandbox.cashfree.com/pg';

const headers = {
  'x-client-id':     process.env.CASHFREE_APP_ID,
  'x-client-secret': process.env.CASHFREE_SECRET_KEY,
  'x-api-version':   '2023-08-01',
  'Content-Type':    'application/json',
};

async function createOrder({ orderId, amount, currency='INR', customerName, customerEmail, customerPhone, returnUrl }) {
  const payload = {
    order_id:       orderId,
    order_amount:   amount / 100,   // Cashfree takes rupees, not paise
    order_currency: currency,
    customer_details: {
      customer_id:    `cust_${Date.now()}`,
      customer_name:  customerName,
      customer_email: customerEmail,
      customer_phone: customerPhone,
    },
    order_meta: {
      return_url: returnUrl,
    },
  };

  const response = await axios.post(`${BASE_URL}/orders`, payload, { headers });
  return response.data;  // contains payment_session_id, order_id
}

async function verifyPayment(orderId) {
  const response = await axios.get(`${BASE_URL}/orders/${orderId}`, { headers });
  return response.data;  // order_status: PAID / ACTIVE / EXPIRED
}

module.exports = { createOrder, verifyPayment };
