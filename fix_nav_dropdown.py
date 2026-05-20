import os
import glob
import re

FRONTEND_DIR = 'c:/Users/jeeve/Desktop/Beyondbridge/frontend'
html_files = glob.glob(os.path.join(FRONTEND_DIR, '*.html'))

new_nav = '''        <div class="nav-desktop-links" style="display: flex; gap: 24px; align-items: center; font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase;">
            <a href="home.html" style="color: var(--cream); text-decoration: none;">Home</a>
            <a href="about.html" style="color: var(--cream); text-decoration: none;">About</a>
            <a href="mariners.html" style="color: var(--cream); text-decoration: none;">For Mariners</a>
            <a href="defence.html" style="color: var(--cream); text-decoration: none;">For Defence</a>
            <a href="services.html" style="color: var(--cream); text-decoration: none;">Services</a>
            <a href="pricing.html" style="color: var(--cream); text-decoration: none;">Pricing</a>
            <a href="contact.html" style="color: var(--cream); text-decoration: none;">Contact</a>
            
            <!-- Dropdown -->
            <div class="nav-dropdown">
                <button class="nav-dropbtn" style="background: none; border: none; color: var(--text-dim); font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase; cursor: pointer; display: flex; align-items: center; gap: 4px; font-family: var(--font-sans);">
                    More <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
                </button>
                <div class="nav-dropdown-content">
                    <a href="pathways.html">MBA Pathways</a>
                    <a href="process.html">Our Process</a>
                    <a href="resources.html">Resources</a>
                    <a href="faq.html">FAQ</a>
                </div>
            </div>
            
            <a href="dashboard.html" class="nav-logged-in" style="color: var(--cream); text-decoration: none; border-left: 1px solid var(--border); padding-left: 24px;">Dashboard</a>
            <a href="#" class="nav-logged-in" onclick="handleLogout()" style="color: var(--text-dim); text-decoration: none;">Logout</a>
        </div>'''

# The current nav block starts with `<div class="nav-desktop-links"` and ends with `</div>`
nav_pattern = re.compile(r'<div class="nav-desktop-links"[^>]*>.*?Logout</a>\s*</div>', re.DOTALL)
# Also check for the case without class="nav-desktop-links"
nav_pattern2 = re.compile(r'<div style="display: flex; gap: 24px; align-items: center; font-size: 0.75rem;[^>]*>.*?Logout</a>\s*</div>', re.DOTALL)

for file in html_files:
    if os.path.basename(file) == 'index.html': continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    if re.search(nav_pattern, content):
        content = re.sub(nav_pattern, new_nav, content)
        modified = True
    elif re.search(nav_pattern2, content):
        content = re.sub(nav_pattern2, new_nav, content)
        modified = True
        
    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated nav in {os.path.basename(file)}')
    else:
        print(f'Could not find nav in {os.path.basename(file)}')
