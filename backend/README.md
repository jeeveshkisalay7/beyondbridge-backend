# Beyond Bridge Backend Server

A Node.js Express server that manages real user authentication, secure PBKDF2 password hashing, and email verification with OTPs (One-Time Passwords) for the Beyond Bridge Advisory website.

---

## Technical Specifications
* **Runtime**: Node.js (>=18.0.0)
* **Framework**: Express.js
* **Email Dispatch**: Nodemailer (with auto-generated Ethereal Dev Account fallback)
* **Security**: Safe PBKDF2 Password Hashing (100,000 iterations, 64-byte salt, SHA-512)
* **Database**: Lightweight atomic JSON storage (`data/users.json`, `data/pending.json`)

---

## Installation & Setup

1. **Navigate to the Backend Directory**:
   ```bash
   cd backend
   ```

2. **Install Dependencies**:
   ```bash
   npm install
   ```

3. **Configure Environment Variables**:
   Open `.env` in the `backend/` directory. By default, it runs on port `5000` with no SMTP keys (which triggers the zero-config Ethereal mail integration).
   
   To use your own SMTP server (e.g. Gmail), fill in:
   ```env
   PORT=5000
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=your-email@gmail.com
   SMTP_PASS=your-app-password
   SMTP_FROM="Beyond Bridge Advisory <noreply@beyondbridge.com>"
   ```

4. **Launch the Server**:
   ```bash
   npm start
   ```

---

## Zero-Config Developer Testing (Email Fallback)
If you don't supply real SMTP credentials inside `.env`:
1. The server will auto-create a temporary **Ethereal Mail** testing account.
2. A real email will be dispatched.
3. The console will print a clickable preview link:
   ```
   ======================================================
   📧 EMAIL DISPATCH SUCCESSFUL
   Recipient: you@example.com
   OTP Code:  739281
   
   🔗 TEST EMAIL PREVIEW URL:
   👉 https://ethereal.email/message/YxJvW4Zp...
   (Click the link above to view the actual email layout in your browser!)
   ======================================================
   ```
4. Clicking that link opens the real Ethereal inbox in your browser, where you can see the premium formatted HTML email exactly as your user would see it!
5. In addition, the OTP will be appended to `otp_debug.log` in the root of the workspace for ultra-fast copies.
