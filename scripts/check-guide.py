#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
import sys

class GuideParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids=set(); self.hrefs=[]; self.lang=None; self.title=False
        self.h1=0; self.main=0; self.skip=False
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=="html": self.lang=a.get("lang")
        if tag=="title": self.title=True
        if tag=="h1": self.h1+=1
        if tag=="main": self.main+=1
        if "id" in a: self.ids.add(a["id"])
        if tag=="a":
            href=a.get("href","")
            self.hrefs.append(href)
            if "skip-link" in a.get("class","").split() and href=="#innhold":
                self.skip=True

def fail(msg):
    print("ERROR:", msg)
    raise SystemExit(1)

path=Path(sys.argv[1])
text=path.read_text(encoding="utf-8")
p=GuideParser(); p.feed(text)

if p.lang != "no": fail("html lang must be no")
if p.h1 != 1: fail("guide must contain exactly one h1")
if p.main != 1: fail("guide must contain exactly one main element")
if not p.skip: fail("missing skip link to #innhold")
for required in ("windows","mac","linux","test","hjelp","innhold"):
    if required not in p.ids: fail(f"missing required id: {required}")
for href in p.hrefs:
    if href.startswith("#") and href[1:] not in p.ids:
        fail(f"broken internal link: {href}")
for phrase in ("Ousdal IT","thonny.org","print(\"Hei!\")","Jeg sitter fast"):
    if phrase not in text: fail(f"missing required content: {phrase}")
print(f"OK: {path} passed guide checks")
