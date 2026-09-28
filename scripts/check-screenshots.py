#!/usr/bin/env python3
import json, sys
from pathlib import Path

path = Path(sys.argv[1] if len(sys.argv) > 1 else "assets/screenshots/manifest.json")
data = json.loads(path.read_text(encoding="utf-8"))
required = {"id","file","step","os","os_version","thonny_version","language","captured_at","source","alt","status"}
allowed = {"candidate","verified","stale"}
seen=set()
errors=[]
for i,item in enumerate(data.get("screenshots", []),1):
    missing=required-set(item)
    if missing: errors.append(f"entry {i}: missing {', '.join(sorted(missing))}")
    sid=item.get("id")
    if sid in seen: errors.append(f"entry {i}: duplicate id {sid}")
    seen.add(sid)
    if item.get("status") not in allowed: errors.append(f"entry {i}: invalid status")
    if item.get("language") not in {"no","en","neutral"}: errors.append(f"entry {i}: invalid language")
    file=item.get("file","")
    if file and (file.startswith("/") or ".." in Path(file).parts): errors.append(f"entry {i}: unsafe file path")
    if item.get("status")=="verified":
        p=Path("assets/screenshots")/file
        if not p.is_file(): errors.append(f"entry {i}: verified file missing: {p}")
        if not str(item.get("alt","")).strip(): errors.append(f"entry {i}: verified screenshot needs alt text")
if errors:
    print("\n".join("ERROR: "+e for e in errors)); raise SystemExit(1)
print(f"OK: screenshot manifest passed ({len(seen)} entries)")
