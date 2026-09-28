#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
import sys

class GuideParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids=set(); self.hrefs=[]; self.lang=None; self.h1=0; self.main=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=="html": self.lang=a.get("lang")
        if tag=="h1": self.h1+=1
        if tag=="main": self.main+=1
        if "id" in a: self.ids.add(a["id"])
        if tag=="a": self.hrefs.append(a.get("href",""))

def fail(msg):
    print("ERROR:", msg); raise SystemExit(1)

path=Path(sys.argv[1]); source=path.read_text(encoding="utf-8")
p=GuideParser(); p.feed(source)
if p.lang not in ("no","en"): fail("html lang must be no or en")
if p.h1 != 1: fail("guide must contain exactly one h1")
if p.main != 1: fail("guide must contain exactly one main")
required=("windows","mac","linux","test") + (("hjelp","innhold") if p.lang=="no" else ("help","content"))
for item in required:
    if item not in p.ids: fail(f"missing required id: {item}")
skip="#innhold" if p.lang=="no" else "#content"
if skip not in p.hrefs: fail(f"missing skip link: {skip}")
for href in p.hrefs:
    if href.startswith("#") and href[1:] not in p.ids: fail(f"broken internal link: {href}")
phrases=("Ousdal IT","thonny.org") + (('print("Hei!")',"Jeg sitter fast") if p.lang=="no" else ('print("Hello!")',"I'm stuck"))
for phrase in phrases:
    if phrase not in source: fail(f"missing required content: {phrase}")
print(f"OK: {path} passed {p.lang} guide checks")
