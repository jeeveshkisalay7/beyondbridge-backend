import os
import glob
import re

html_files = glob.glob('*.html')

new_nav = """    <!-- NAVBAR -->
    <nav style="display: flex; justify-content: space-between; align-items: center; padding: 24px 60px; border-bottom: 1px solid var(--border); position: sticky; top: 0; background: rgba(11, 11, 11, 0.9); backdrop-filter: blur(10px); z-index: 100;">
        <a href="home.html" style="text-decoration: none;">
            <div class="logo-main-text" style="font-size: 1.4rem;"><span class="logo-beyond">Beyond</span><span class="logo-bridge">Bridge<span class="logo-dot">.</span></span></div>
        </a>
        <div style="display: flex; gap: 24px; align-items: center; font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase;">
            <a href="home.html" style="color: var(--cream); text-decoration: none;">Home</a>
            <a href="about.html" style="color: var(--cream); text-decoration: none;">About</a>
            <a href="services.html" style="color: var(--cream); text-decoration: none;">Services</a>
            <a href="pricing.html" style="color: var(--cream); text-decoration: none;">Pricing</a>
            <a href="contact.html" style="color: var(--cream); text-decoration: none;">Contact</a>
            
            <!-- Dropdown -->
            <div class="nav-dropdown">
                <button class="nav-dropbtn" style="background: none; border: none; color: var(--text-dim); font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase; cursor: pointer; display: flex; align-items: center; gap: 4px; font-family: var(--font-sans);">
                    More <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
                </button>
                <div class="nav-dropdown-content">
                    <a href="mariners.html">For Mariners</a>
                    <a href="defence.html">For Defence</a>
                    <a href="pathways.html">MBA Pathways</a>
                    <a href="process.html">Our Process</a>
                    <a href="resources.html">Resources</a>
                    <a href="faq.html">FAQ</a>
                </div>
            </div>
            
            <a href="dashboard.html" style="color: var(--cream); text-decoration: none; border-left: 1px solid var(--border); padding-left: 24px;">Dashboard</a>
            <a href="#" onclick="handleLogout()" style="color: var(--text-dim); text-decoration: none;">Logout</a>
        </div>
    </nav>"""

for filepath in html_files:
    if filepath == 'index.html':
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match the old navigation + overlay menu and replace it with just the new navbar
    # We look for <!-- NAVBAR --> followed by anything up to <!-- FULLSCREEN MENU OVERLAY --> 
    # and then up to the closing two </div> of the menu overlay.
    
    # We can match from <!-- NAVBAR --> to the second </div> after <!-- FULLSCREEN MENU OVERLAY -->
    # A robust way is:
    pattern = r'<!-- NAVBAR -->.*?<!-- FULLSCREEN MENU OVERLAY -->.*?</div>\s*</div>'
    content = re.sub(pattern, new_nav, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Navigation updated to dropdown in all subpages.")
