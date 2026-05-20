import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements

    # Landing Page Logo
    content = re.sub(
        r'<img src="assets/logo-cropped\.png" alt="Beyond Bridge Logo" class="logo-main" style="height: 80px; transform: scale\(1\.2\);">',
        r'<div class="logo-main-text" style="font-size: 4rem;"><span class="logo-beyond">Beyond</span><span class="logo-bridge">Bridge<span class="logo-dot">.</span></span></div>',
        content
    )

    # Auth Panel Logo
    content = re.sub(
        r'<img src="assets/logo-cropped\.png" alt="Beyond Bridge Logo" class="logo-main" style="height: 48px; margin-bottom: 12px;">',
        r'<div class="logo-main-text" style="font-size: 2.2rem; margin-bottom: 12px;"><span class="logo-beyond">Beyond</span><span class="logo-bridge">Bridge<span class="logo-dot">.</span></span></div>',
        content
    )

    # Navbar Logo
    content = re.sub(
        r'<img src="assets/logo-cropped\.png" alt="Beyond Bridge" class="logo-main" style="height: 32px;?[^>]*>',
        r'<div class="logo-main-text" style="font-size: 1.4rem;"><span class="logo-beyond">Beyond</span><span class="logo-bridge">Bridge<span class="logo-dot">.</span></span></div>',
        content
    )

    # Footer Logo
    content = re.sub(
        r'<img src="assets/logo-cropped\.png" alt="Beyond Bridge" class="logo-main" style="height: 40px;?[^>]*>',
        r'<div class="logo-main-text" style="font-size: 1.8rem; opacity: 0.6;"><span class="logo-beyond">Beyond</span><span class="logo-bridge">Bridge<span class="logo-dot">.</span></span></div>',
        content
    )
    
    # Catch any remaining ones (like in dashboard maybe)
    content = re.sub(
        r'<img src="assets/logo-cropped\.png" alt="Beyond Bridge" class="logo-main">',
        r'<div class="logo-main-text" style="font-size: 1.4rem;"><span class="logo-beyond">Beyond</span><span class="logo-bridge">Bridge<span class="logo-dot">.</span></span></div>',
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated logos in all HTML files.")
