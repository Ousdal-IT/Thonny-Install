#!/usr/bin/env python3
import json
from pathlib import Path
import html

MANIFEST=Path("assets/screenshots/manifest.json")
OUT=Path("site")
data=json.loads(MANIFEST.read_text(encoding="utf-8"))
verified=[x for x in data.get("screenshots",[]) if x.get("status")=="verified"]

for lang, source in (("no","index.html"),("en","en/index.html")):
    dest=OUT/source
    text=dest.read_text(encoding="utf-8")
    for item in verified:
        if item.get("language") not in {lang,"neutral"}: continue
        step=item.get("step","")
        src=item["file"].replace("\\","/")
        if not (Path("assets/screenshots")/src).is_file(): continue
        href=("assets/screenshots/"+src) if lang=="no" else ("../assets/screenshots/"+src)
        marker=f'<!-- SCREENSHOT:{step} -->'
        block=(f'<figure class="screenshot-inline" data-screenshot-step="{html.escape(step)}">'
               f'<img loading="lazy" src="{html.escape(href)}" alt="{html.escape(item["alt"])}">'
               f'<figcaption>{html.escape(item["alt"])}</figcaption></figure>')
        text=text.replace(marker,block)
    dest.write_text(text,encoding="utf-8")
print(f"OK: inserted verified screenshots by step ({len(verified)} verified entries)")
