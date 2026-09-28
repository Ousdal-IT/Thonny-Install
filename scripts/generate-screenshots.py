#!/usr/bin/env python3
import json
from pathlib import Path

MANIFEST=Path("assets/screenshots/manifest.json")
OUT=Path("site")
data=json.loads(MANIFEST.read_text(encoding="utf-8"))
verified=[x for x in data.get("screenshots",[]) if x.get("status")=="verified"]

labels={"no":"Skjermbilder","en":"Screenshots"}
for lang, source in (("no","index.html"),("en","en/index.html")):
    html=Path(source).read_text(encoding="utf-8")
    items=[]
    for item in verified:
        if item.get("language") not in {lang,"neutral"}: continue
        src=item["file"].replace("\\","/")
        if not (Path("assets/screenshots")/src).is_file(): continue
        href=("assets/screenshots/"+src) if lang=="no" else ("../assets/screenshots/"+src)
        items.append(f'<figure class="screenshot"><img loading="lazy" src="{href}" alt="{item["alt"]}"><figcaption>{item["step"]}</figcaption></figure>')
    block=""
    if items:
        block=f'<section class="card screenshot-gallery"><h2>{labels[lang]}</h2><div class="screenshot-grid">{"".join(items)}</div></section>'
    dest=OUT/source
    dest.parent.mkdir(parents=True,exist_ok=True)
    text=dest.read_text(encoding="utf-8")
    marker="<!-- SCREENSHOTS:GENERATED -->"
    if marker not in text: raise SystemExit(f"missing screenshot marker in {dest}")
    dest.write_text(text.replace(marker,block),encoding="utf-8")
print(f"OK: generated verified screenshot blocks ({len(verified)} verified entries)")
