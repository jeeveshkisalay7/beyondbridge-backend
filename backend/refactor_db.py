import os
import re

def refactor_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace db.prepare(...).get(...) -> await db.get(..., ...)
    content = re.sub(r"db\.prepare\((['`].*?['`])\)\.get\((.*?)\)", r"await db.get(\1, \2)", content)
    # Case with no args
    content = re.sub(r"db\.prepare\((['`].*?['`])\)\.get\(\)", r"await db.get(\1)", content)
    
    # Replace db.prepare(...).run(...) -> await db.run(..., ...)
    content = re.sub(r"db\.prepare\((['`].*?['`])\)\.run\((.*?)\)", r"await db.run(\1, \2)", content)
    # Case with no args
    content = re.sub(r"db\.prepare\((['`].*?['`])\)\.run\(\)", r"await db.run(\1)", content)
    
    # Fix multiline prepare:
    # const stmt = db.prepare(`...`); stmt.run(...) -> const result = await db.run(`...`, ...)
    # In authController.js:
    # const stmt = db.prepare(`...`); stmt.run(firstName, ...);
    
    # We will just manually fix the known multiline ones if they exist, or do a general replace:
    # Actually, in authController:
    # const stmt = db.prepare(`...`);
    # stmt.run(...);
    # Let's replace manually for the complex ones:
    content = re.sub(r"const stmt = db\.prepare\((`[^`]+`)\);\s*stmt\.run\((.*?)\);", r"await db.run(\1, \2);", content)
    
    # In bookingController.js:
    # const stmt = db.prepare(`...`);
    # const result = stmt.run(...);
    content = re.sub(r"const stmt = db\.prepare\((`[^`]+`)\);\s*const result = stmt\.run\((.*?)\);", r"const result = await db.run(\1, \2);", content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Refactored {filepath}")

if __name__ == '__main__':
    base_dir = 'c:/Users/jeeve/Desktop/Beyondbridge/backend/controllers'
    refactor_file(os.path.join(base_dir, 'authController.js'))
    refactor_file(os.path.join(base_dir, 'bookingController.js'))
