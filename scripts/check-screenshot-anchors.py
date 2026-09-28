#!/usr/bin/env python3
import json, re, sys
from pathlib import Path

manifest=json.loads(Path("assets/screenshots/manifest.json").read_text(encoding="utf-8"))
items={x.get("step"):x for x in manifest.get("screenshots",[])}
errors=[]

for source in ("index.html","en/index.html"):
    text=Path(source).read_text(encoding="utf-8")
    anchors=set(re.findall(r'<!-- SCREENSHOT:([A-Za-z0-9_-]+) -->', text))
    for step in sorted(anchors):
        if step not in items:
            errors.append(f"{source}: screenshot anchor has no manifest entry: {step}")

    for sid,item in items.items():
        if item.get("language") not in {"neutral","no","en"}: continue
        if f"<!-- SCREENSHOT:{sid} -->" in text and item.get("status")=="stale":
            errors.append(f"{source}: stale screenshot is still anchored: {sid}")

expected={"windows-download","windows-install","windows-start","macos-download",
          "macos-install","macos-start","linux-install","linux-launch",
          "first-program","run-program"}
missing=expected-set(items)
if missing:
    errors.extend(f"manifest: missing required candidate {x}" for x in sorted(missing))

if errors:
    print("\n".join("ERROR: "+e for e in errors)); raise SystemExit(1)
print(f"OK: screenshot anchors are synchronized ({len(items)} manifest entries)")
