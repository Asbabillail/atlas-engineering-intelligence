#!/usr/bin/env python3
"""Bundle plugin runtime files for a supported importer (stdlib only)."""
from pathlib import Path
import json, subprocess, sys, zipfile
root=Path(__file__).resolve().parents[1]
code=subprocess.call([sys.executable,str(root/'scripts/validate_plugin.py')])
if code: sys.exit(code)
manifest=json.loads((root/'plugin.json').read_text(encoding='utf-8'))
name=manifest['name']; version=manifest['version']
out=root/'dist'/f'{name}-v{version}.zip'
out.parent.mkdir(exist_ok=True)
files=[root/'plugin.json', *sorted((root/'skills').rglob('*'))]
files=[f for f in files if f.is_file() and '__pycache__' not in f.parts]
with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED) as z:
    for f in files:
        z.write(f, f'{name}/{f.relative_to(root).as_posix()}')
print('WROTE:',out)
