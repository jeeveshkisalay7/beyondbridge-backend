const PDFDocument = require('pdfkit');
const fs = require('fs');
const path = require('path');

async function generateInvoice(bookingDetails) {
  const {
    bookingId, firstName, lastName, email, phone,
    packageName, packagePrice, paymentRef, paidAt
  } = bookingDetails;

  const invoiceDir  = path.join(__dirname, '..', 'invoices');
  if (!fs.existsSync(invoiceDir)) fs.mkdirSync(invoiceDir, { recursive: true });

  const invoicePath = path.join(invoiceDir, `BB-${bookingId}-invoice.pdf`);
  const doc         = new PDFDocument({ margin: 50, size: 'A4' });
  const stream      = fs.createWriteStream(invoicePath);

  doc.pipe(stream);

  // Header
  doc.rect(0, 0, doc.page.width, 80).fill('#0a1628');
  doc.fillColor('#ffffff').fontSize(24).font('Helvetica-Bold')
     .text('BeyondBridge', 50, 25);
  doc.fillColor('#c8a96e').fontSize(9).font('Helvetica')
     .text('MBA & MARITIME ADVISORY', 50, 55, { characterSpacing: 2 });

  doc.fillColor('#333333');

  // Invoice title
  doc.moveDown(2);
  doc.fillColor('#C0392B').fontSize(18).font('Helvetica-Bold').text('PAYMENT INVOICE', { align: 'right' });
  doc.fillColor('#555').fontSize(10).font('Helvetica')
     .text(`Invoice #: BB-${bookingId}`, { align: 'right' })
     .text(`Date: ${new Date(paidAt || Date.now()).toLocaleDateString('en-IN', { year:'numeric', month:'long', day:'numeric' })}`, { align: 'right' });

  // Divider
  doc.moveDown(1);
  doc.moveTo(50, doc.y).lineTo(545, doc.y).strokeColor('#e0e0e0').lineWidth(1).stroke();
  doc.moveDown(1);

  // Bill to
  doc.fillColor('#888').fontSize(9).font('Helvetica').text('BILLED TO');
  doc.fillColor('#111').fontSize(12).font('Helvetica-Bold').text(`${firstName} ${lastName}`);
  doc.fillColor('#555').fontSize(10).font('Helvetica').text(email).text(phone);

  doc.moveDown(2);

  // Package table
  doc.fillColor('#0a1628').rect(50, doc.y, 495, 36).fill();
  doc.fillColor('#ffffff').fontSize(10).font('Helvetica-Bold')
     .text('Description', 60, doc.y - 25)
     .text('Amount', 450, doc.y - 25, { width: 80, align: 'right' });

  doc.moveDown(0.5);
  doc.fillColor('#111').fontSize(11).font('Helvetica').text(packageName, 60, doc.y);
  const amount = `₹${(packagePrice / 100).toLocaleString('en-IN')}`;
  doc.text(amount, 450, doc.y - 15, { width: 80, align: 'right' });

  doc.moveDown(2);
  doc.moveTo(50, doc.y).lineTo(545, doc.y).strokeColor('#e0e0e0').lineWidth(0.5).stroke();
  doc.moveDown(1);

  // Total
  doc.fillColor('#111').fontSize(13).font('Helvetica-Bold')
     .text('Total Paid:', 380)
     .fillColor('#C0392B').text(amount, 460, doc.y - 19, { width: 80, align: 'right' });

  doc.moveDown(1);
  doc.fillColor('#888').fontSize(9).font('Helvetica').text(`Payment Reference: ${paymentRef}`);

  // Footer
  const footerY = doc.page.height - 80;
  doc.moveTo(50, footerY).lineTo(545, footerY).strokeColor('#e0e0e0').lineWidth(0.5).stroke();
  doc.fillColor('#888').fontSize(8).font('Helvetica')
     .text('BeyondBridge Advisory | contact@beyond-bridge.com | beyond-bridge.com', 50, footerY + 10, { align: 'center' })
     .text('This is a computer-generated invoice and does not require a physical signature.', { align: 'center' });

  doc.end();

  return new Promise((resolve, reject) => {
    stream.on('finish', () => resolve(invoicePath));
    stream.on('error', reject);
  });
}

module.exports = { generateInvoice };
