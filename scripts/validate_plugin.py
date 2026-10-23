#!/usr/bin/env python3
"""Offline structural checks for an ATLAS skills-only plugin (stdlib only)."""
from pathlib import Path
import json, re, sys
root = Path(__file__).resolve().parents[1]
errors=[]
try:
    manifest = json.loads((root/'plugin.json').read_text(encoding='utf-8'))
except Exception as ex:
    print(f'FAIL invalid plugin.json: {ex}')
    sys.exit(1)
if manifest.get('$schema')!='https://agent-plugins.org/schemas/1.0.0/plugin.schema.json':
    errors.append('missing/wrong Agent Plugins 1.0 schema')
name=manifest.get('name','')
if not isinstance(name,str) or not re.fullmatch(r'[a-z0-9](?:[a-z0-9.-]{0,62}[a-z0-9])?',name) or '--' in name or '..' in name:
    errors.append('invalid plugin name')
version=manifest.get('version','')
if not isinstance(version,str) or not re.fullmatch(r'\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?',version):
    errors.append('missing/invalid semver')
iface=manifest.get('extensions',{}).get('com.openai',{}).get('interface',{})
if not iface.get('displayName'):
    errors.append('missing displayName')
if len(iface.get('shortDescription',''))>30:
    errors.append('shortDescription exceeds 30 characters')
if iface.get('category')!='Developer Tools':
    errors.append('expected Developer Tools category')
skill_files=sorted((root/'skills').glob('*/SKILL.md'))
if len(skill_files)!=6:
    errors.append(f'expected six skills, found {len(skill_files)}')
seen=set()
for file in skill_files:
    s=file.read_text(encoding='utf-8')
    if not s.startswith('---\n'):
        errors.append(f'{file.relative_to(root)} missing frontmatter')
        continue
    match=re.match(r'^---\n(.*?)\n---\n',s,re.S)
    if not match:
        errors.append(f'{file.relative_to(root)} malformed frontmatter')
        continue
    f=match.group(1)
    nm=re.search(r'^name:\s*([a-z0-9-]+)\s*$', f, re.M)
    desc=re.search(r'^description:\s*(.+)$',f,re.M)
    if not nm or nm.group(1)!=file.parent.name:
        errors.append(f'{file.relative_to(root)} skill name must match folder')
    elif nm.group(1) in seen:
        errors.append(f'{file.relative_to(root)} duplicate skill name')
    else: seen.add(nm.group(1))
    if not desc or not desc.group(1).strip(' "\'' ):
        errors.append(f'{file.relative_to(root)} missing description')
    if file.stat().st_size>1024*1024:
        errors.append(f'{file.relative_to(root)} too large')
if errors:
    for e in errors: print('FAIL:',e)
    sys.exit(1)
print(f'PASS: {name} v{version}: manifest and {len(skill_files)} skills structurally checked')
print('NOTE: This does not test LLM behavior, package installation, or source security.')
