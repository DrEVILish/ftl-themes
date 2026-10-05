#!/usr/bin/env python3
"""Emit JSON coverage and actionable source gaps for one or all themes."""
import argparse
import glob
import json
import os
import re
import sys

import build_manifest
import cssparse
import theme_inheritance

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("--theme", action="append", default=[])
args = ap.parse_args()
core_files = sorted(glob.glob("core/components/*.css"))
core_classes = set()
for path in core_files:
    core_classes.update(re.findall(r"(?<![\w-])\.([a-z][a-z0-9-]*)", open(path, encoding="utf-8").read()))
themes = sorted(glob.glob("themes/*/theme.css"))
known = {os.path.basename(os.path.dirname(p)) for p in themes}
unknown = set(args.theme) - known
if unknown:
    sys.exit("unknown theme(s): " + ", ".join(sorted(unknown)))
reports = []
for path in themes:
    slug = os.path.basename(os.path.dirname(path))
    if args.theme and slug not in args.theme:
        continue
    source = open(path, encoding="utf-8").read()
    full_source = theme_inheritance.rules(slug)
    own = set(re.findall(r"(?<![\w-])\.([a-z][a-z0-9-]*)", cssparse.strip_comments(full_source)))
    tokens = build_manifest.root_tokens(full_source, slug)
    icons = build_manifest.icon_ids("themes/%s/icons.svg" % slug)
    core_icons = {"icon-" + x.strip() for x in open("assets/icons/core-set.txt", encoding="utf-8") if x.strip()}
    declared_assets = set(re.findall(r"url\(['\"]?assets/([^)'\"]+)", full_source))
    undeclared = sorted(x for x in declared_assets if not os.path.isfile("themes/%s/assets/%s" % (slug, x)) and not os.path.isfile("assets/%s" % x))
    references = os.path.isdir("references/%s" % slug)
    findings = []
    if not references:
        findings.append({"rule": "THM-REFERENCE", "file": "references/%s/" % slug, "line": None, "message": "No reference set found; human review required."})
    for asset in undeclared:
        match = re.search(r"url\(['\"]?assets/" + re.escape(asset), full_source)
        findings.append({"rule": "THM-ASSET", "file": path, "line": full_source.count("\n", 0, match.start()) + 1 if match else None, "message": "Referenced asset is missing: assets/%s" % asset})
    reports.append({
        "slug": slug,
        "family": [name for name, _ in theme_inheritance.chain(slug)],
        "manifest": "dist/themes.json#%s" % slug,
        "preview": "gallery.html?theme=%s" % slug,
        "tokens": sorted(tokens),
        "componentCoverage": {"styledSelectors": len(own & core_classes), "coreDefaults": len(core_classes - own), "total": len(core_classes)},
        "fonts": sorted(set(re.findall(r"url\(['\"]?assets/fonts/([^)'\"]+)", full_source))),
        "iconCoverage": {"overrides": len(icons & core_icons), "total": len(core_icons), "allOverrides": len(icons)},
        "referenceFiles": len(glob.glob("references/%s/**/*" % slug, recursive=True)) if references else 0,
        "findings": findings,
        "visualReview": "human",
    })
print(json.dumps({"contract": 4, "themes": reports}, indent=2))
