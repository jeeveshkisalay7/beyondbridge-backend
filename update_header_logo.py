import os
import glob
import re

files = glob.glob('frontend/*.html')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # The header logos typically use height 32px or 64px, the footer logo uses 40px
    # Or we can specifically replace only the first occurrence if we split by <footer>
    parts = content.split('<!-- FOOTER -->')
    if len(parts) == 2:
        new_header = parts[0].replace('assets/logo.png', 'assets/custom-logo.png')
        new_content = new_header + '<!-- FOOTER -->' + parts[1]
    else:
        # Fallback if no FOOTER tag: replace the 32px / 64px logos.
        new_content = content.replace('src="assets/logo.png" alt="Beyond Bridge" class="logo-main" style="height: 32px;"', 'src="assets/custom-logo.png" alt="Beyond Bridge" class="logo-main" style="height: 32px;"')
        new_content = new_content.replace('src="assets/logo.png" alt="Beyond Bridge" class="logo-main" style="height: 64px;"', 'src="assets/custom-logo.png" alt="Beyond Bridge" class="logo-main" style="height: 64px;"')
        
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")
