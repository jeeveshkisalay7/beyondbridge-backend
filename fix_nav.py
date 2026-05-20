import os
import glob
import re

FRONTEND_DIR = 'c:/Users/jeeve/Desktop/Beyondbridge/frontend'

def replace_nav():
    html_files = glob.glob(os.path.join(FRONTEND_DIR, '*.html'))
    
    new_nav = """
        <div class="nav-desktop-links" style="display: flex; gap: 24px; align-items: center; font-size: 0.75rem; letter-spacing: 0.1em; text-transform: uppercase;">
            <a href="home.html" style="color: var(--cream); text-decoration: none;">Home</a>
            <a href="about.html" style="color: var(--cream); text-decoration: none;">About</a>
            <a href="mariners.html" style="color: var(--cream); text-decoration: none;">For Mariners</a>
            <a href="defence.html" style="color: var(--cream); text-decoration: none;">For Defence</a>
            <a href="pathways.html" style="color: var(--cream); text-decoration: none;">MBA Pathways</a>
            <a href="services.html" style="color: var(--cream); text-decoration: none;">Services</a>
            <a href="pricing.html" style="color: var(--cream); text-decoration: none;">Pricing</a>
            <a href="process.html" style="color: var(--cream); text-decoration: none;">Process</a>
            <a href="resources.html" style="color: var(--cream); text-decoration: none;">Resources</a>
            <a href="contact.html" style="color: var(--cream); text-decoration: none;">Book Consultation</a>
            <a href="dashboard.html" class="nav-logged-in" style="color: var(--cream); text-decoration: none; border-left: 1px solid var(--border); padding-left: 24px;">Dashboard</a>
            <a href="#" class="nav-logged-in" onclick="handleLogout()" style="color: var(--text-dim); text-decoration: none;">Logout</a>
        </div>
"""
    
    # We will search for `<div style="display: flex; gap: 24px; align-items: center; font-size: 0.75rem;`
    # up to `</div>` that matches its indentation. A regex might be complex, so let's do this line by line or with a robust regex.
    # The block ends after the `<a href="#" onclick="handleLogout()"...>Logout</a>` and its closing `</div>`

    nav_pattern = re.compile(r'<div style="display: flex; gap: 24px; align-items: center; font-size: 0.75rem;[^>]*>.*?<a href="#" onclick="handleLogout\(\)"[^>]*>Logout</a>\s*</div>', re.DOTALL)
    
    # In some files it has `<a href="index.html"...>Logout</a>` instead of `#`? Let's be broad.
    nav_pattern2 = re.compile(r'<div style="display: flex; gap: 24px; align-items: center; font-size: 0.75rem;[^>]*>.*?Logout</a>\s*</div>', re.DOTALL)
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        
        if re.search(nav_pattern2, content):
            content = re.sub(nav_pattern2, new_nav, content)
            modified = True
        
        # In index.html, there's no Logout maybe, let's check what's in index.html.
        # Oh, there's a Logout in index.html too? If not, we fall back to finding the dropdown.
        
        if modified:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated nav in {os.path.basename(file)}")
        else:
            print(f"Could not find nav block in {os.path.basename(file)}")

if __name__ == '__main__':
    replace_nav()
