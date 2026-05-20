# Frontend Integration Guide

This guide explains how to connect your static HTML frontend forms directly to the production modular Node.js/MySQL backend API routes.

---

## 1. Connecting the Signup Form (`POST /signup`)

If you are using a standard **Full Name, Email, Password, and Confirm Password** signup layout, map your form elements and submit handler like below:

### HTML Form Structure
```html
<!-- signup container -->
<div id="form-signup">
    <h2 class="auth-heading">Create your profile.</h2>
    <form class="auth-form" id="signup-form" onsubmit="handleSignup(event)">
        
        <div class="field">
            <label for="su-name">Full Name</label>
            <input type="text" id="su-name" placeholder="John Miller" required />
        </div>

        <div class="field">
            <label for="su-email">Email Address</label>
            <input type="email" id="su-email" placeholder="miller@example.com" required />
        </div>

        <div class="field">
            <label for="su-pw">Password</label>
            <input type="password" id="su-pw" placeholder="••••••••" required />
        </div>

        <div class="field">
            <label for="su-pw2">Confirm Password</label>
            <input type="password" id="su-pw2" placeholder="••••••••" required />
        </div>

        <div class="error-msg" id="signup-error"></div>

        <button class="btn-primary" type="submit" style="position:relative">
            Create Account
            <span class="spinner"></span>
        </button>
    </form>
</div>
```
> [!NOTE]
> If you are retaining your existing **Beyond Bridge** form (which has separate `su-first` and `su-last` inputs), you can dynamically concatenate them into a single string in Javascript:
> `const fullName = document.getElementById('su-first').value + ' ' + document.getElementById('su-last').value;`

### Javascript Submit Handler
```javascript
function handleSignup(e) {
    e.preventDefault();
    const errEl = document.getElementById('signup-error');
    errEl.classList.remove('show');

    const fullName = document.getElementById('su-name').value;
    const email = document.getElementById('su-email').value;
    const password = document.getElementById('su-pw').value;
    const confirmPassword = document.getElementById('su-pw2').value;

    // Front-end check
    if (password !== confirmPassword) {
        errEl.textContent = 'Passwords do not match.';
        errEl.classList.add('show');
        return;
    }

    const btn = e.target.querySelector('button[type=submit]');
    btn.classList.add('loading');

    fetch('/signup', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ fullName, email, password, confirmPassword })
    })
    .then(async res => {
        const data = await res.json();
        btn.classList.remove('loading');
        
        if (res.status === 201) {
            // Success! Lock email input, switch UI panel to OTP screen
            document.getElementById('otp-email-display').textContent = email;
            document.getElementById('form-signup').style.display = 'none';
            document.getElementById('form-otp').style.display = 'block';
            showNotif('✓ Verification OTP sent to your inbox.');
        } else {
            errEl.textContent = data.message || 'An error occurred during signup.';
            errEl.classList.add('show');
        }
    })
    .catch(err => {
        btn.classList.remove('loading');
        errEl.textContent = 'Failed to connect to the backend server.';
        errEl.classList.add('show');
    });
}
```

---

## 2. Connecting the OTP Verification Form (`POST /verify-otp`)

Once signup succeeds, toggle your UI to show the OTP verification panel.

### HTML Form Structure
```html
<!-- OTP Verification Panel -->
<div id="form-otp" style="display:none">
    <h2 class="auth-heading">Verify your email.</h2>
    <p class="auth-subheading">We have sent a 6-digit code to <strong id="otp-email-display">your email</strong>.</p>

    <form class="auth-form" id="otp-form" onsubmit="handleVerifyOtp(event)">
        <div class="field">
            <label for="otp-code">Verification Code</label>
            <input type="text" id="otp-code" placeholder="123456" required maxlength="6" pattern="\\d{6}" style="text-align: center; letter-spacing: 0.3em; font-size: 1.4rem;" />
        </div>

        <div class="error-msg" id="otp-error"></div>

        <button class="btn-primary" type="submit" style="position:relative">
            Verify & Activate
            <span class="spinner"></span>
        </button>
    </form>
</div>
```

### Javascript Verify Handler
```javascript
function handleVerifyOtp(e) {
    e.preventDefault();
    const errEl = document.getElementById('otp-error');
    errEl.classList.remove('show');

    const email = document.getElementById('su-email').value || document.getElementById('otp-email-display').textContent;
    const otp = document.getElementById('otp-code').value;

    const btn = e.target.querySelector('button[type=submit]');
    btn.classList.add('loading');

    fetch('/verify-otp', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, otp })
    })
    .then(async res => {
        const data = await res.json();
        btn.classList.remove('loading');
        
        if (res.status === 200) {
            showNotif('✓ Account activated! Please log in.');
            // Redirect to Login Tab
            switchTab('login');
            document.getElementById('form-otp').style.display = 'none';
            document.getElementById('form-login').style.display = 'block';
        } else {
            errEl.textContent = data.message || 'OTP verification failed.';
            errEl.classList.add('show');
        }
    })
    .catch(err => {
        btn.classList.remove('loading');
        errEl.textContent = 'Failed to connect to the backend server.';
        errEl.classList.add('show');
    });
}
```

---

## 3. Connecting the Login Form (`POST /login`)

Submits credentials and expects the backend to write the secure session JWT inside an **HTTP-only cookie** automatically.

### Javascript Login Handler
```javascript
function handleLogin(e) {
    e.preventDefault();
    const errEl = document.getElementById('login-error');
    errEl.classList.remove('show');

    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-pw').value;

    const btn = e.submitter || e.target.querySelector('button[type=submit]');
    btn.classList.add('loading');

    fetch('/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
    })
    .then(async res => {
        const data = await res.json();
        btn.classList.remove('loading');
        
        if (res.status === 200) {
            // Save state
            localStorage.setItem('loggedIn', 'true');
            localStorage.setItem('userEmail', email);
            
            showNotif('✓ Signed in successfully.');

            // Redirect to dashboard
            setTimeout(() => {
                window.location.href = 'home.html';
            }, 1000);
        } else if (res.status === 403 && data.data && data.data.unverified) {
            // Catch unverified account logins: automatically forward them to OTP verify tab!
            document.getElementById('otp-email-display').textContent = email;
            document.getElementById('form-login').style.display = 'none';
            document.getElementById('form-otp').style.display = 'block';
            showNotif('✓ Email unverified. A new OTP has been sent.');
        } else {
            errEl.textContent = data.message || 'Invalid email or password.';
            errEl.classList.add('show');
        }
    })
    .catch(err => {
        btn.classList.remove('loading');
        errEl.textContent = 'Failed to connect to the backend server.';
        errEl.classList.add('show');
    });
}
```

---

## 4. Connecting Logout (`POST /logout`)

Clears session tokens securely on both server-side cookies and client-side memory.

### Javascript Logout Handler
```javascript
function handleLogout() {
    fetch('/logout', {
        method: 'POST'
    })
    .then(() => {
        localStorage.clear(); // wipe local storage
        window.location.href = 'index.html'; // redirect
    })
    .catch(() => {
        // Fallback redirection even on connection errors
        localStorage.clear();
        window.location.href = 'index.html';
    });
}
```
