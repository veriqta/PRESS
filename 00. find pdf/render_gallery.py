#!/usr/bin/env python3
"""Rebuild the GitHub cover grid and unavailable-title list from manifest.json."""
from pathlib import Path
from urllib.parse import quote
import html
import json

folder = Path(__file__).resolve().parent
manifest = json.loads((folder / "manifest.json").read_text())

def grid(items):
 out=['<table>']
 for i in range(0,len(items),3):
  out.append('<tr>')
  for x in items[i:i+3]:
   title=html.escape(x['title'],quote=True);img=f'<img src="{quote(x["cover"])}" alt="{title}" width="250" />'
   if x['pdf']:
    link=quote('../'+x['pdf']);content=f'<a href="{link}">{img}</a><br /><a href="{link}">{title}</a>'
   else:
    link=f'MISSING.md#item-{x["id"]}'
    label='PDF not available' if x['status']=='missing' else 'Reference image — no PDF confirmed'
    content=f'<a href="{link}">{img}</a><br />{title}<br /><strong>{label}</strong>'
   out.append(f'<td align="center" valign="top" width="33%">{content}</td>')
  if len(items[i:i+3])<3:out.extend('<td></td>' for _ in range(3-len(items[i:i+3])))
  out.append('</tr>')
 out.append('</table>');return '\n'.join(out)
body='''# Find a PDF

**[Visit VERIQTA — veriqta.com](https://veriqta.com/)**

[Library home](../README.md) · [Search titles](../CATALOG.md) · [Unavailable titles](MISSING.md)

Browse the covers and tap or click the publication you want to open its PDF on GitHub. Use the PDF page’s download control to save an individual publication for personal study under the [licence](../LICENSE).

Covers follow the supplied Instagram screenshots, with repeated posts removed. A few repository PDFs use a different cover design; the publication title and volume were checked. Covers marked **PDF not available** open the unavailable-title list rather than a different publication.

## Browse publications

'''
body+=grid([x for x in manifest if x['group']=='screenshots' and x['status']!='reference-image'])
body+='\n\n## More PDFs in the library\n\nThese publications are in the repository but were not shown in the supplied screenshots.\n\n'+grid([x for x in manifest if x['group']=='additional'])
body+='\n\n## Reference graphics\n\nThese posts are reference graphics. A standalone PDF has not been confirmed for them.\n\n'+grid([x for x in manifest if x['status']=='reference-image'])+'\n'
(folder/'README.md').write_text(body)
missing='''# Unavailable titles

[Cover gallery](README.md) · [Library home](../README.md)

These titles are visible in the supplied Instagram screenshots, but no matching PDF was found in the repository during the comparison. Related publications are not treated as substitutes. This list does not imply that a PDF previously existed here or was deleted.

## Publications without a matching PDF

'''
for x in manifest:
 if x['status']=='missing':missing+=f'<a id="item-{x["id"]}"></a>\n\n- **{x["title"]}** — [view cover]({x["cover"]}).\n\n'
missing+='## Reference graphics without a confirmed PDF\n\nThese are counted separately from publication covers.\n\n'
for x in manifest:
 if x['status']=='reference-image':missing+=f'<a id="item-{x["id"]}"></a>\n\n- **{x["title"]}** — [view image]({x["cover"]}).\n\n'
(folder/'MISSING.md').write_text(missing.rstrip()+'\n')
