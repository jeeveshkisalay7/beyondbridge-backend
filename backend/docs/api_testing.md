# API Testing Reference Sheet

This document contains testing protocols and sample payloads for verifying the Beyond Bridge authentication endpoints using `curl` or Postman.

---

## Base API Configurations
* **Host URL**: `http://localhost:5000` (or your backend URL)
* **Headers**: `Content-Type: application/json`
* **Cookie Support**: Set-Cookie enabled for JWT session handling.

---

## 1. POST /signup
Initiates registration. Validates input, hashes password, saves unverified user, and dispatches a 6-digit OTP code to the email.

### cURL Request
```bash
curl -X POST http://localhost:5000/signup \
  -H "Content-Type: application/json" \
  -d '{
    "fullName": "Captain John Miller",
    "email": "miller@example.com",
    "password": "Password123!"
  }'
```
> [!TIP]
> Passwords must be at least 8 characters and contain 1 uppercase letter, 1 lowercase letter, 1 digit, and 1 special symbol.

### Success Response (`201 Created`)
```json
{
  "success": true,
  "message": "Account pre-registered successfully. Verification code sent to your email.",
  "data": {
    "email": "miller@example.com",
    "previewUrl": "https://ethereal.email/message/YxJvW4Zp5sT01928"
  }
}
```

### Validation Error Response (`400 Bad Request`)
```json
{
  "success": false,
  "message": "Password is too weak. It must contain at least 8 characters, including 1 uppercase, 1 lowercase, 1 digit, and 1 special symbol."
}
```

---

## 2. POST /verify-otp
Verifies the 6-digit code. On success, marks the account as verified and cleans up the OTP database record.

### cURL Request
```bash
curl -X POST http://localhost:5000/verify-otp \
  -H "Content-Type: application/json" \
  -d '{
    "email": "miller@example.com",
    "otp": "123456"
  }'
```

### Success Response (`200 OK`)
```json
{
  "success": true,
  "message": "Email verified successfully! Your account is now active. Please log in."
}
```

### Expired / Wrong OTP Response (`400 Bad Request`)
```json
{
  "success": false,
  "message": "Verification code has expired (5-minute limit). Please request a new one."
}
```

---

## 3. POST /resend-otp
Generates a fresh OTP code and resets the 5-minute countdown clock for an existing unverified user.

### cURL Request
```bash
curl -X POST http://localhost:5000/resend-otp \
  -H "Content-Type: application/json" \
  -d '{
    "email": "miller@example.com"
  }'
```

### Success Response (`200 OK`)
```json
{
  "success": true,
  "message": "A fresh verification code has been dispatched to your email address.",
  "data": {
    "email": "miller@example.com",
    "previewUrl": "https://ethereal.email/message/ZyUvW4Zp8sT09101"
  }
}
```

---

## 4. POST /login
Authenticates credentials. Sets a secure HTTP-Only cookie `token` and returns user parameters.

### cURL Request
```bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "miller@example.com",
    "password": "Password123!"
  }'
```

### Success Response (`200 OK`)
Sets header: `Set-Cookie: token=eyJhbGciOi...; Max-Age=86400; Path=/; HttpOnly; SameSite=Strict`
```json
{
  "success": true,
  "message": "Login successful.",
  "data": {
    "token": "eyJhbGciOi...",
    "user": {
      "id": 1,
      "fullName": "Captain John Miller",
      "email": "miller@example.com"
    }
  }
}
```

### Unverified Account Login Response (`403 Forbidden`)
If they try to login but never verified the OTP, the system rejects it and triggers a new OTP dispatch automatically!
```json
{
  "success": false,
  "message": "Your email address is unverified. A new verification code has been dispatched to your inbox. Please verify your account before logging in.",
  "data": {
    "unverified": true,
    "email": "miller@example.com"
  }
}
```

---

## 5. POST /logout
Clears the JWT session cookie instantly.

### cURL Request
```bash
curl -X POST http://localhost:5000/logout \
  -H "Content-Type: application/json"
```

### Success Response (`200 OK`)
Sets header: `Set-Cookie: token=; Max-Age=0; Path=/; HttpOnly; SameSite=Strict`
```json
{
  "success": true,
  "message": "Logged out successfully."
}
```
