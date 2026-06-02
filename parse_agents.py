import os, json, re
import glob

agents_dir = r'C:\Users\PC\Documents\Dan\agy-research\.agy\agents'
agents = []
for filepath in glob.glob(os.path.join(agents_dir, '*.md')):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse frontmatter
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if match:
        frontmatter = match.group(1)
        body = match.group(2).strip()
        
        name = ''
        desc = ''
        for line in frontmatter.split('\n'):
            if line.startswith('name:'):
                name = line.split(':', 1)[1].strip()
            elif line.startswith('description:'):
                desc = line.split(':', 1)[1].strip().strip('\"\'')
                
        agents.append({
            'name': name or os.path.basename(filepath).replace('.md', ''),
            'description': desc[:150] + '...' if len(desc) > 150 else desc,
            'system_prompt': body
        })

with open(r'C:\Users\PC\Documents\Dan\agy-research\agents_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(agents, f)
