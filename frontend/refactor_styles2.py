import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    if filepath == 'index.html':
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Footer bg to #E5FCF5
    content = re.sub(
        r'<footer style="([^"]*?)background:\s*#000080;([^"]*?)"',
        r'<footer style="\g<1>background: #E5FCF5;\g<2>"',
        content
    )
    
    # Footer color to #000000
    content = re.sub(
        r'<footer style="([^"]*?)color:\s*var\(--text-dim\);([^"]*?)"',
        r'<footer style="\g<1>color: #000000;\g<2>"',
        content
    )

    # Replace var(--text-muted) with #000000 specifically inside the footer.
    def adjust_footer(match):
        footer_content = match.group(0)
        footer_content = footer_content.replace('color: var(--text-muted)', 'color: #000000')
        return footer_content
        
    content = re.sub(r'<footer.*?</footer>', adjust_footer, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done')
