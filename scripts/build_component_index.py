#!/usr/bin/env python3
"""Build the small machine-readable map from component groups to their docs."""
import json
import os
import re
import argparse
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS_DIR = os.path.join(ROOT, "core", "components")
DOC_DIR = os.path.join(ROOT, "docs", "components")
OUT = os.path.join(DOC_DIR, "index.json")
ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("--check", action="store_true", help="fail if the checked-in index is stale")
args = ap.parse_args()
DEMOS = {
    "experience": "components-experience.html", "forms": "components-forms.html",
    "instruments": "components-instruments.html", "navigation": "components-navigation.html",
    "prose": "components-prose.html", "social": "components-social.html",
    "surfaces": "components-surfaces.html", "tables": "components-tables.html",
    "live": "mission-control.html", "desktop": "desktop.html",
    "audio": "audio-components.html", "console": "proseries.html", "signage": "signage.html", "sections": "components-sections.html", "shop": "components-shop.html",
}

records = []
for name in sorted(os.listdir(CSS_DIR)):
    if not name.endswith(".css"):
        continue
    group = name[:-4]
    source = os.path.join(CSS_DIR, name)
    text = open(source, encoding="utf-8").read()
    classes = sorted(set(re.findall(r"(?<![\w-])\.([a-z][a-z0-9-]*)", text)) -
                     {"is-active", "is-disabled", "is-error", "is-loading", "is-open", "is-selected", "is-stale", "is-updated"})
    tokens = sorted(set(re.findall(r"var\((--[a-z][a-z0-9-]*)", text)))
    docs = os.path.join("docs", "components", group + ".md")
    records.append({
        "id": group,
        "classes": classes,
        "tokens": tokens,
        "source": os.path.relpath(source, ROOT),
        "documentation": docs if os.path.isfile(os.path.join(ROOT, docs)) else "CONTRACT.md",
        "example": DEMOS.get(group, "components.html"),
    })

rendered = json.dumps({"contract": 4, "generated": "scripts/build_component_index.py", "groups": records}, indent=2) + "\n"
if args.check:
    if not os.path.isfile(OUT) or open(OUT, encoding="utf-8").read() != rendered:
        sys.exit("docs/components/index.json is stale; run python3 scripts/build_component_index.py")
    print("component index is current")
else:
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(rendered)
    print("built docs/components/index.json")
