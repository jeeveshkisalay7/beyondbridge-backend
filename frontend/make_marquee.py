import re

def create_marquee(match):
    inner_html = match.group(1)
    
    # We replace the grid container with a marquee wrapper
    header = '''<div class="marquee-wrapper">
                <div class="marquee-track">'''
    # we duplicate inner_html to make the loop seamless
    footer = '''</div></div>'''
    return header + inner_html + inner_html + footer

with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<div class="grid-3">(.*?)</div>\s*</div>\s*</section>', lambda m: create_marquee(m) + '\n        </div>\n    </section>', content, flags=re.DOTALL)

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('pricing.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(400px, 1fr\)\); gap: 40px;">(.*?)</div>\s*</div>\s*</section>', lambda m: create_marquee(m) + '\n        </div>\n    </section>', content, flags=re.DOTALL)

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(content)
