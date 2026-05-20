import glob

old_a_tag = '<a href="home.html" style="text-decoration: none;">'
new_a_tag = '<a href="home.html" style="text-decoration: none; display: flex; align-items: center;">'

for f in glob.glob('frontend/*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Align the tab titles with the logo text perfectly
    content = content.replace(old_a_tag, new_a_tag)
    
    # Increase from 32px to 40px to match landing page proportion and push it slightly to align perfectly with baseline
    content = content.replace('src="assets/custom-logo.png" alt="Beyond Bridge" class="logo-main" style="height: 32px;"',
                              'src="assets/custom-logo.png" alt="Beyond Bridge" class="logo-main" style="height: 48px; object-fit: contain; margin-top: -6px;"')
    
    # If any the landing logo is 64px, maybe apply similar alignment tweaking if needed, but leaving as is for now.
    
    # Finally, for index.html auth panel, also update to custom-logo
    content = content.replace('src="assets/logo.png" alt="Beyond Bridge" class="logo-main" style="height: 40px; margin-bottom: 12px;"',
                              'src="assets/custom-logo.png" alt="Beyond Bridge" class="logo-main" style="height: 52px; object-fit: contain; margin-bottom: 12px;"')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated {f}')