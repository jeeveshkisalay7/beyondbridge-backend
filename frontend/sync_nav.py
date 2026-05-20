import glob, os, re
home_content = open('home.html', encoding='utf-8').read()
nav_match = re.search(r'(<nav[^>]*>.*?</nav>)', home_content, re.DOTALL)
if nav_match:
    nav_html = nav_match.group(1)
    # The user wants ALL pages to be consistent with home.html
    for f in glob.glob('*.html'):
        if f in ['index.html', 'home.html']: continue
        content = open(f, encoding='utf-8').read()
        content = re.sub(r'<nav[^>]*>.*?</nav>', nav_html, content, count=1, flags=re.DOTALL)
        open(f, 'w', encoding='utf-8').write(content)
        print('Updated', f)
else:
    print('Nav not found in home.html')
