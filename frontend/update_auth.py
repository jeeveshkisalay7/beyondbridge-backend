import re

content = open('index.html', encoding='utf-8').read()

new_js = '''        /* ── Login handler ──────────────────────────────────────────── */
        async function handleLogin(e) {
            e.preventDefault();
            const btn = e.submitter || e.target.querySelector('button[type=submit]');
            btn.classList.add('loading');

            const email = document.getElementById('li-email').value;
            const password = document.getElementById('li-pw').value;
            const subscribed = document.getElementById('subscribe-blog').checked;

            try {
                const res = await fetch('http://localhost:3001/api/auth/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password, subscribeBlog: subscribed })
                });
                const data = await res.json();
                btn.classList.remove('loading');

                if (res.ok) {
                    localStorage.setItem('loggedIn', 'true');
                    localStorage.setItem('token', data.token);
                    localStorage.setItem('subscribed', subscribed ? 'true' : 'false');
                    showNotif('✓ Signed in successfully.');
                    setTimeout(() => {
                        window.location.href = 'home.html';
                    }, 1200);
                } else {
                    if(data.needsVerification) {
                        showNotif('⚠️ Please verify your email first.');
                        showOTPScreen(email);
                    } else {
                        showNotif('❌ ' + data.error);
                    }
                }
            } catch (err) {
                btn.classList.remove('loading');
                showNotif('❌ Failed to connect to backend server');
            }
        }

        /* ── Signup handler ──────────────────────────────────────────── */
        async function handleSignup(e) {
            e.preventDefault();

            const pw = document.getElementById('su-pw').value;
            const pw2 = document.getElementById('su-pw2').value;
            const errEl = document.getElementById('signup-error');

            if (pw !== pw2) {
                errEl.textContent = 'Passwords do not match.';
                errEl.classList.add('show');
                return;
            }
            if (pw.length < 8) {
                errEl.textContent = 'Password must be at least 8 characters.';
                errEl.classList.add('show');
                return;
            }
            errEl.classList.remove('show');

            const btn = e.target.querySelector('button[type=submit]');
            btn.classList.add('loading');

            const payload = {
                firstName: document.getElementById('su-first').value,
                lastName: document.getElementById('su-last').value,
                email: document.getElementById('su-email').value,
                phone: document.getElementById('su-country-code').value + document.getElementById('su-phone').value,
                profession: document.getElementById('su-profession').value,
                designation: document.getElementById('su-designation').value,
                experience: document.getElementById('su-experience').value,
                geography: document.getElementById('su-geography').value,
                password: pw
            };

            try {
                const res = await fetch('http://localhost:3001/api/auth/signup', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                const data = await res.json();
                btn.classList.remove('loading');
                
                if (res.ok) {
                    showOTPScreen(payload.email);
                } else {
                    errEl.textContent = data.error;
                    errEl.classList.add('show');
                }
            } catch (err) {
                btn.classList.remove('loading');
                errEl.textContent = 'Failed to connect to backend server';
                errEl.classList.add('show');
            }
        }

        let currentSignupEmail = '';
        function showOTPScreen(email) {
            currentSignupEmail = email;
            document.getElementById('form-signup').style.display = 'none';
            document.getElementById('form-login').style.display = 'none';
            document.getElementById('signup-success').classList.add('show');
            document.getElementById('signup-success').innerHTML = `
                <h3 style="font-family: var(--font-display); font-size: 1.5rem; margin-bottom: 12px; color: var(--cream);">Verify Your Email</h3>
                <p style="color: var(--text-dim); margin-bottom: 24px; font-size: 0.9rem;">We sent a 6-digit code to <strong>${email}</strong>. Please enter it below.</p>
                <div class="form-group" style="margin-bottom: 16px;">
                    <input type="text" id="su-otp" placeholder="Enter 6-digit OTP" maxlength="6" style="letter-spacing: 4px; text-align: center; font-size: 1.2rem; font-weight: bold;">
                </div>
                <div id="otp-error" class="error-msg"></div>
                <button type="button" onclick="verifyOTP()" class="btn-primary" style="width: 100%; margin-bottom: 16px;">Verify Code</button>
                <button type="button" onclick="resendOTP()" class="btn-ghost" style="width: 100%; font-size: 0.8rem;">Resend Code</button>
            `;
        }

        async function verifyOTP() {
            const otp = document.getElementById('su-otp').value;
            const errEl = document.getElementById('otp-error');
            if(!otp || otp.length !== 6) {
                errEl.textContent = 'Please enter a valid 6-digit code.';
                errEl.classList.add('show');
                return;
            }
            errEl.classList.remove('show');

            try {
                const res = await fetch('http://localhost:3001/api/auth/verify-otp', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email: currentSignupEmail, otp })
                });
                const data = await res.json();
                
                if (res.ok) {
                    localStorage.setItem('loggedIn', 'true');
                    localStorage.setItem('token', data.token);
                    showNotif('✓ Email verified! Welcome to BeyondBridge.');
                    setTimeout(() => {
                        window.location.href = 'home.html';
                    }, 1200);
                } else {
                    errEl.textContent = data.error;
                    errEl.classList.add('show');
                }
            } catch (err) {
                errEl.textContent = 'Failed to connect to backend server';
                errEl.classList.add('show');
            }
        }

        async function resendOTP() {
            try {
                const res = await fetch('http://localhost:3001/api/auth/resend-otp', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email: currentSignupEmail })
                });
                const data = await res.json();
                if(res.ok) {
                    showNotif('✓ New OTP sent to your email.');
                } else {
                    showNotif('❌ ' + data.error);
                }
            } catch (err) {
                showNotif('❌ Failed to resend OTP.');
            }
        }
'''

# Find the start of the login handler comment and replace everything from there to the end of the script block
content = re.sub(r'/\* ── Login handler ──────────────────────────────────────────── \*/.*}\n\s*</script>', new_js + '\n    </script>', content, flags=re.DOTALL)

open('index.html', 'w', encoding='utf-8').write(content)
print('Updated index.html with API auth logic')
