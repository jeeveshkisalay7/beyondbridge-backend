import re
content = open('contact.html', encoding='utf-8').read()

# Replace the form entirely in the new book.html
form_html = '''
            <form id="booking-form" class="auth-form fade-enter visible" style="padding: 56px; border: 1px solid var(--border); background: var(--dark);">
                <div class="form-row" style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 24px;">
                    <div class="field" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">Full Name</label>
                        <input type="text" id="b-name" required placeholder="John Doe" style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none;">
                    </div>
                    <div class="field" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">Email</label>
                        <input type="email" id="b-email" required placeholder="you@example.com" style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none;">
                    </div>
                </div>
                <div class="form-row" style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 24px;">
                    <div class="field" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">WhatsApp Number</label>
                        <input type="text" id="b-phone" required placeholder="+91..." style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none;">
                    </div>
                    <div class="field" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">Current Profession</label>
                        <select id="b-profession" style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none;">
                            <option value="Merchant Navy">Merchant Navy</option>
                            <option value="Defence / Ex-Defence">Defence / Ex-Defence</option>
                            <option value="Other Service Background">Other Service Background</option>
                        </select>
                    </div>
                </div>
                <div class="form-row" style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 24px;">
                    <div class="field" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">Rank / Designation</label>
                        <input type="text" id="b-rank" required placeholder="e.g. Chief Officer" style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none;">
                    </div>
                    <div class="field" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">Years of Experience</label>
                        <input type="number" id="b-exp" required placeholder="e.g. 5" style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none;">
                    </div>
                </div>
                
                <div class="form-row" style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 24px;">
                    <div class="field" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">Target MBA Year</label>
                        <input type="text" id="b-year" required placeholder="2026/2027" style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none;">
                    </div>
                    <div class="field" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">GMAT Status</label>
                        <input type="text" id="b-gmat" required placeholder="Taken/Planning/Exempt" style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none;">
                    </div>
                </div>

                <div class="form-row" style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 24px;">
                    <div class="field" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">Current Location</label>
                        <input type="text" id="b-loc" required placeholder="City, Country" style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none;">
                    </div>
                    <div class="field" style="display: flex; flex-direction: column; gap: 8px;">
                        <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">Preferred Geography</label>
                        <input type="text" id="b-geo" required placeholder="India/US/Europe/UK" style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none;">
                    </div>
                </div>

                <div class="field" style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 24px;">
                    <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">Target Schools (if any)</label>
                    <input type="text" id="b-schools" placeholder="ISB, INSEAD, LBS, etc." style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none;">
                </div>

                <div class="field" style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 24px;">
                    <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">Main Concern or Goal</label>
                    <textarea id="b-concern" required placeholder="What do you need help with?" style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none; min-height: 120px; font-family: var(--font-sans);"></textarea>
                </div>
                
                <div class="field" style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 24px;">
                    <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">Upload Resume (PDF)</label>
                    <input type="file" id="b-resume" accept=".pdf" style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none;">
                </div>

                <div class="field" style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 24px;">
                    <label style="color: var(--cream); font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.1em;">Select Package</label>
                    <select id="b-package" style="background: var(--charcoal); border: 1px solid var(--border); color: var(--cream); padding: 16px; outline: none;">
                        <option value="free_discovery">Free Discovery Call (Free)</option>
                        <option value="bridge_diagnostic">BridgeStart Profile Diagnostic (₹1,999)</option>
                        <option value="resume_linkedin">Resume & LinkedIn Transformation (₹4,999)</option>
                        <option value="single_india">Single School India MBA Advisory (₹19,999)</option>
                        <option value="three_india">Three-School India MBA Pack (₹59,999)</option>
                        <option value="single_global">Single School Global MBA Advisory (₹39,999)</option>
                        <option value="global_three">Global MBA 3-School Pack (₹99,999)</option>
                        <option value="mba360">MBA360 Premium Advisory (₹1,99,999)</option>
                        <option value="interview_mastery">Interview Mastery Pack (₹11,999)</option>
                        <option value="ding_analysis">Reapplicant / Ding Analysis (₹9,999)</option>
                        <option value="hourly_advisory">Hourly Advisory (₹3,999/hr)</option>
                    </select>
                </div>

                <div id="booking-error" class="error-msg"></div>
                <button type="submit" class="btn-primary" style="width: 100%; padding: 16px; margin-top: 16px;">Proceed to Booking</button>
            </form>
'''

book_content = re.sub(r'<form class="auth-form.*?</form>', form_html, content, flags=re.DOTALL)
book_content = book_content.replace('</head>', '    <script src="https://sdk.cashfree.com/js/v3/cashfree.js"></script>\n</head>')

# Add JS script
script = '''
    <script>
        const cashfree = Cashfree({ mode: "sandbox" });

        document.getElementById('booking-form').addEventListener('submit', async function(e) {
            e.preventDefault();
            const btn = e.target.querySelector('button[type=submit]');
            btn.classList.add('loading');
            const errEl = document.getElementById('booking-error');
            errEl.classList.remove('show');

            const formData = new FormData();
            formData.append('fullName', document.getElementById('b-name').value);
            formData.append('email', document.getElementById('b-email').value);
            formData.append('phone', document.getElementById('b-phone').value);
            formData.append('profession', document.getElementById('b-profession').value);
            formData.append('rankDesignation', document.getElementById('b-rank').value);
            formData.append('yearsExperience', document.getElementById('b-exp').value);
            formData.append('targetMbaYear', document.getElementById('b-year').value);
            formData.append('gmatStatus', document.getElementById('b-gmat').value);
            formData.append('currentLocation', document.getElementById('b-loc').value);
            formData.append('preferredGeography', document.getElementById('b-geo').value);
            formData.append('targetSchools', document.getElementById('b-schools').value);
            formData.append('mainConcern', document.getElementById('b-concern').value);
            
            const resumeFile = document.getElementById('b-resume').files[0];
            if(resumeFile) formData.append('resume', resumeFile);

            const packageId = document.getElementById('b-package').value;
            
            const token = localStorage.getItem('token');
            const headers = {};
            if(token) headers['Authorization'] = `Bearer ${token}`;

            try {
                // 1. Submit form
                let res = await fetch('http://localhost:3001/api/booking/submit', {
                    method: 'POST',
                    headers: headers,
                    body: formData
                });
                let data = await res.json();
                
                if (!res.ok) {
                    throw new Error(data.error || 'Failed to submit form');
                }

                const bookingId = data.bookingId;

                // 2. Create Payment
                res = await fetch('http://localhost:3001/api/booking/create-payment', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        ...headers
                    },
                    body: JSON.stringify({
                        bookingId,
                        packageId,
                        customerName: document.getElementById('b-name').value,
                        customerEmail: document.getElementById('b-email').value,
                        customerPhone: document.getElementById('b-phone').value
                    })
                });
                data = await res.json();
                btn.classList.remove('loading');

                if (!res.ok) {
                    throw new Error(data.error || 'Failed to initialize payment');
                }

                if (data.isFree) {
                    showNotif(data.message);
                    document.getElementById('booking-form').reset();
                } else {
                    // Redirect to Cashfree checkout
                    cashfree.checkout({ paymentSessionId: data.paymentSessionId });
                }

            } catch (err) {
                btn.classList.remove('loading');
                errEl.textContent = err.message || 'An error occurred during booking.';
                errEl.classList.add('show');
            }
        });
    </script>
'''

book_content = book_content.replace('</body>', script + '\n</body>')

open('book.html', 'w', encoding='utf-8').write(book_content)
print('Created book.html')
