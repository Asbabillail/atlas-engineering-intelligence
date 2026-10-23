#!/usr/bin/env python3
"""Export reviewable ATLAS per-skill ZIPs for Claude.ai-compatible Skills import."""
from pathlib import Path
import zipfile
root=Path(__file__).resolve().parents[1]
output=root/'dist'/'claude-skills'
output.mkdir(parents=True,exist_ok=True)
for file in sorted((root/'skills').glob('*/SKILL.md')):
    parent=file.parent
    destination=output/f'{parent.name}.zip'
    with zipfile.ZipFile(destination,'w',zipfile.ZIP_DEFLATED) as z:
        for f in sorted(parent.rglob('*')):
            if f.is_file() and '__pycache__' not in f.parts:
                z.write(f,(Path(parent.name)/f.relative_to(parent)).as_posix())
    print(destination.relative_to(root))
