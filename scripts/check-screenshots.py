#!/usr/bin/env python3
import json, sys
from pathlib import Path

root = Path("assets/screenshots")
path = Path(sys.argv[1] if len(sys.argv) > 1 else root / "manifest.json")
data = json.loads(path.read_text(encoding="utf-8"))
required = {"id","file","step","os","os_version","thonny_version","language","captured_at","source","alt","status"}
allowed_status = {"candidate","verified","stale"}
allowed_language = {"no","en","neutral"}
allowed_suffix = {".png", ".jpg", ".jpeg", ".webp"}
seen_ids, registered, errors = set(), set(), []

for i,item in enumerate(data.get("screenshots", []),1):
    missing=required-set(item)
    if missing: errors.append(f"entry {i}: missing {', '.join(sorted(missing))}")
    sid=item.get("id")
    if not sid or sid in seen_ids: errors.append(f"entry {i}: missing or duplicate id {sid!r}")
    seen_ids.add(sid)
    if item.get("status") not in allowed_status: errors.append(f"entry {i}: invalid status")
    if item.get("language") not in allowed_language: errors.append(f"entry {i}: invalid language")

    file=str(item.get("file",""))
    p=Path(file)
    if not file or p.is_absolute() or ".." in p.parts:
        errors.append(f"entry {i}: unsafe or empty file path")
        continue
    if p.suffix.lower() not in allowed_suffix:
        errors.append(f"entry {i}: unsupported image type {p.suffix}")
    registered.add(p.as_posix())

    actual=root/p
    if item.get("status")=="verified":
        if not actual.is_file():
            errors.append(f"entry {i}: verified file missing: {actual}")
        elif actual.stat().st_size > 2_000_000:
            errors.append(f"entry {i}: image exceeds 2 MB: {actual}")
        if not str(item.get("alt","")).strip():
            errors.append(f"entry {i}: verified screenshot needs alt text")
        if not str(item.get("source","")).strip():
            errors.append(f"entry {i}: verified screenshot needs source")

disk_files={
    p.relative_to(root).as_posix()
    for p in root.rglob("*")
    if p.is_file() and p.suffix.lower() in allowed_suffix
}
for extra in sorted(disk_files-registered):
    errors.append(f"unregistered screenshot file: {extra}")

if errors:
    print("\n".join("ERROR: "+e for e in errors))
    raise SystemExit(1)
print(f"OK: screenshot manifest passed ({len(seen_ids)} entries, {len(disk_files)} image files)")
