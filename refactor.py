import os
import re

dir_path = r'C:\Users\PC\Documents\Dan\agy-research'

# Mapping of replacements (order matters)
replacements = [
    (r'Antigravity CLI', 'Antigravity CLI'),
    (r'Antigravity', 'Antigravity'),
    (r'agy-research', 'agy-research'),
    (r'antigravity-cli', 'antigravity-cli'),
    (r'\.agy', '.agy'),
    (r'AGY\.md', 'AGY.md'),
    (r'AGY', 'AGY'),
    (r'\bclaude\b', 'agy')
]

skip_dirs = {'.git', 'node_modules', '.mcp-server-biblio', 'packages'}
skip_extensions = {'.png', '.jpg', '.pdf', '.zip'}

for root, dirs, files in os.walk(dir_path):
    dirs[:] = [d for d in dirs if d not in skip_dirs]
    for file in files:
        if any(file.endswith(ext) for ext in skip_extensions):
            continue
        
        filepath = os.path.join(root, file)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            new_content = content
            for old, new in replacements:
                new_content = re.sub(old, new, new_content)
                
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated: {filepath}")
        except Exception as e:
            print(f"Could not process {filepath}: {e}")
