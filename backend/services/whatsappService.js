// WhatsApp notification service
// Currently stubbed — wire when client provides Twilio/WATI credentials

async function sendWhatsAppOTP(phone, firstName, otp) {
  console.log(`[WhatsApp STUB] OTP ${otp} to ${phone} for ${firstName}`);
  // TODO: Uncomment and fill credentials in .env
  /*
  const twilio = require('twilio')(process.env.TWILIO_ACCOUNT_SID, process.env.TWILIO_AUTH_TOKEN);
  await twilio.messages.create({
    from: process.env.TWILIO_WHATSAPP_FROM,
    to:   `whatsapp:${phone}`,
    body: `Hi ${firstName}, your BeyondBridge verification code is: *${otp}*
Valid for 10 minutes.`
  });
  */
}

async function sendWhatsAppInvoice(phone, firstName, bookingDetails) {
  console.log(`[WhatsApp STUB] Invoice to ${phone} for booking #BB-${bookingDetails.bookingId}`);
  // TODO: Wire Twilio/WATI here
  /*
  const { packageName, packagePrice, bookingId } = bookingDetails;
  const twilio = require('twilio')(process.env.TWILIO_ACCOUNT_SID, process.env.TWILIO_AUTH_TOKEN);
  await twilio.messages.create({
    from: process.env.TWILIO_WHATSAPP_FROM,
    to:   `whatsapp:${phone}`,
    body: `Hi ${firstName}! ✅ Your payment for *${packageName}* (₹${(packagePrice/100).toLocaleString('en-IN')}) is confirmed.
Booking ID: #BB-${bookingId}
Our team will reach out within 24 hours.
— BeyondBridge Team`
  });
  */
}

module.exports = { sendWhatsAppOTP, sendWhatsAppInvoice };
