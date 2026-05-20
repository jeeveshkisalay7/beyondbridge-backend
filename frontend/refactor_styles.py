import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    if filepath == 'index.html':
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Nav bg to white
    content = content.replace('rgba(11, 11, 11, 0.9)', '#ffffff')

    # Footer bg to navy
    content = re.sub(
        r'<footer style="([^"]*?)background:\s*var\(--charcoal\);([^"]*?)"',
        r'<footer style="\g<1>background: #000080;\g<2>"',
        content
    )
    
    # Remove logo block from footer
    logo_pattern = r'<div style="margin-bottom: 32px;">\s*<div class="logo-main-text".*?</div>\s*</div>\s*'
    content = re.sub(logo_pattern, '', content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done')
