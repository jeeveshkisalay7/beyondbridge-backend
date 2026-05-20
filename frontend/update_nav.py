import os
import glob
import re

html_files = glob.glob('*.html')

new_nav = """    <!-- NAVBAR -->
    <nav style="display: flex; justify-content: space-between; align-items: center; padding: 24px 60px; border-bottom: 1px solid var(--border); position: sticky; top: 0; background: rgba(11, 11, 11, 0.9); backdrop-filter: blur(10px); z-index: 100;">
        <a href="home.html" style="text-decoration: none;">
            <div class="logo-main-text" style="font-size: 1.4rem;"><span class="logo-beyond">Beyond</span><span class="logo-bridge">Bridge<span class="logo-dot">.</span></span></div>
        </a>
        <div style="display: flex; gap: 32px; align-items: center; font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase;">
            <div class="nav-desktop-links" style="display: flex; gap: 24px;">
                <a href="services.html" style="color: var(--cream); text-decoration: none;">Services</a>
                <a href="pathways.html" style="color: var(--cream); text-decoration: none;">Pathways</a>
                <a href="pricing.html" style="color: var(--cream); text-decoration: none;">Pricing</a>
            </div>
            
            <div style="display: flex; gap: 24px; align-items: center; border-left: 1px solid var(--border); padding-left: 32px;">
                <a href="dashboard.html" style="color: var(--cream); text-decoration: none;">Dashboard</a>
                <button onclick="document.getElementById('mobile-menu').classList.add('active')" style="background: none; border: none; color: var(--cream); cursor: pointer; display: flex; align-items: center; gap: 8px; font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase; font-family: var(--font-sans);">
                    Menu 
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
                </button>
            </div>
        </div>
    </nav>

    <!-- FULLSCREEN MENU OVERLAY -->
    <div id="mobile-menu" class="mobile-menu-overlay">
        <div class="mobile-menu-content">
            <button onclick="document.getElementById('mobile-menu').classList.remove('active')" class="mobile-menu-close">&times;</button>
            <div class="mobile-menu-links">
                <a href="home.html">Home</a>
                <a href="about.html">About Us</a>
                <a href="mariners.html">For Mariners</a>
                <a href="defence.html">For Defence</a>
                <a href="pathways.html">MBA Pathways</a>
                <a href="services.html">All Services</a>
                <a href="pricing.html">Packages & Pricing</a>
                <a href="process.html">Our Process</a>
                <a href="resources.html">Resources</a>
                <a href="contact.html">Contact / Book Consult</a>
                <a href="faq.html">FAQ</a>
                <a href="#" onclick="handleLogout()" style="color: var(--accent); margin-top: 24px; font-size: 1rem; text-transform: uppercase; letter-spacing: 0.1em; font-family: var(--font-sans);">Logout</a>
            </div>
        </div>
    </div>"""

for filepath in html_files:
    if filepath == 'index.html':
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to match the entire nav block and replace it
    # We match from <nav to </nav>
    # Note: dashboard.html has <nav>...</nav> and home has <nav style="...">...</nav>
    content = re.sub(r'<nav.*?</nav>', new_nav, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Navigation updated in all subpages.")
