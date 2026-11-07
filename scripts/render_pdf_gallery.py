#!/usr/bin/env python3
"""Build the root cover grid from pdf-gallery.json (Python standard library only)."""
from pathlib import Path
from urllib.parse import quote
import html
import json

root = Path(__file__).resolve().parent.parent
items = json.loads((root / 'scripts/pdf-gallery.json').read_text())
# Keep reference graphics after the publications.
items = [x for x in items if x['status'] != 'reference-image'] + [x for x in items if x['status'] == 'reference-image']
lines = ['**[Official VERIQTA website — veriqta.com](https://veriqta.com/)**', '', '<table width="100%">']
for start in range(0, len(items), 3):
    lines.append('<tr>')
    for item in items[start:start + 3]:
        title = html.escape(item['title'], quote=True)
        image = f'<img src="{quote(item["cover"])}" alt="{title}" title="{title}" width="100%" />'
        target = quote(item['pdf']) if item['pdf'] else f'docs/missing-pdfs.md#item-{item["id"]}'
        content = f'<a href="{target}">{image}</a>'
        if not item['pdf']:
            label = 'PDF not available' if item['status'] == 'missing' else 'Reference image — no PDF confirmed'
            content += f'<br /><strong>{label}</strong>'
        lines.append(f'<td align="center" valign="top" width="33%">{content}</td>')
    lines.extend('<td></td>' for _ in range(3 - len(items[start:start + 3])))
    lines.append('</tr>')
lines.extend(['</table>', '', '[Licence — all rights reserved](LICENSE)', ''])
(root / 'README.md').write_text('\n'.join(lines))
