import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if match:
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(match.group(1).strip())
    
    new_content = re.sub(r'<style>.*?</style>', '<link rel="stylesheet" href="style.css" />', content, flags=re.DOTALL)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully refactored CSS out of index.html")
else:
    print("No style tag found.")
