#!/usr/bin/env python3
from pathlib import Path
import re, sys

p=Path(sys.argv[1])
if not p.is_file(): raise SystemExit("ERROR: PDF missing")
data=p.read_bytes()
if len(data) < 20_000: raise SystemExit(f"ERROR: PDF suspiciously small ({len(data)} bytes)")
if not data.startswith(b"%PDF-"): raise SystemExit("ERROR: output is not a PDF")
pages=len(re.findall(rb"/Type\s*/Page\b", data))
if pages < 3: raise SystemExit(f"ERROR: expected multi-page guide, got {pages} pages")
if pages > 30: raise SystemExit(f"ERROR: suspicious page count: {pages}")
if b"%%EOF" not in data[-4096:]: raise SystemExit("ERROR: PDF EOF marker missing")
print(f"OK: {p} looks structurally valid ({len(data)} bytes, {pages} pages)")
