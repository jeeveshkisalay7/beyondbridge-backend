import glob, re, os
for f in glob.glob('*.html'):
    content = open(f, encoding='utf-8').read()
    
    # Remove the mobile-nav block completely
    # It might look like: <nav class="mobile-nav"> ... </nav>
    # or with HTML comments: <!-- Mobile nav overlay --> ... </nav>
    
    # Let's match from <!-- Hamburger to </button>
    content = re.sub(r'<!-- Hamburger button.*?</button>', '', content, flags=re.DOTALL)
    # Match from <!-- Mobile nav overlay to </nav> that has class="mobile-nav"
    content = re.sub(r'<!-- Mobile nav overlay.*?<nav class="mobile-nav">.*?</nav>', '', content, flags=re.DOTALL)
    
    # Also just in case they don't have the comments:
    content = re.sub(r'<button class="hamburger".*?</button>', '', content, flags=re.DOTALL)
    content = re.sub(r'<nav class="mobile-nav">.*?</nav>', '', content, flags=re.DOTALL)
    
    # Wait, the first <nav tag might match if we aren't careful? No, we used `<nav class="mobile-nav">`
    open(f, 'w', encoding='utf-8').write(content)

print('Removed mobile nav from all HTML files!')
