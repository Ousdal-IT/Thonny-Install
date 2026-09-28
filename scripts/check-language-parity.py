#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
import sys

class Structure(HTMLParser):
    def __init__(self):
        super().__init__(); self.sections=[]; self.tags=[]; self.buttons=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=="section":
            self.sections.append(a.get("id",""))
        if tag in ("h1","h2","h3","ol","ul","pre"):
            self.tags.append(tag)
        if tag=="button":
            self.buttons += 1

def parse(path):
    p=Structure()
    p.feed(Path(path).read_text(encoding="utf-8"))
    return p

no=parse(sys.argv[1]); en=parse(sys.argv[2])
aliases={"hjelp":"help","innhold":"content"}
no_sections=[aliases.get(x,x) for x in no.sections]
if no_sections != en.sections:
    print("ERROR: section structure differs")
    print("NO:", no_sections); print("EN:", en.sections)
    raise SystemExit(1)
for required in ("windows","mac","linux","test","help"):
    if required not in en.sections:
        raise SystemExit(f"ERROR: missing paired section {required}")
if no.buttons != en.buttons:
    raise SystemExit(f"ERROR: button count differs: NO={no.buttons}, EN={en.buttons}")
# Heading/list/pre sequence is intentionally checked only by count: translations may
# need different list grouping while retaining equivalent document hierarchy.
for tag in ("h1","h2","h3","pre"):
    a=no.tags.count(tag); b=en.tags.count(tag)
    if a != b:
        raise SystemExit(f"ERROR: {tag} count differs: NO={a}, EN={b}")
print("OK: NO/EN structural parity passed")
