#!/usr/bin/env python3
"""Validate a local theme pack and optionally write a standalone preview."""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_manifest
import cssparse

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("pack", help="directory containing manifest.json")
ap.add_argument("--preview", action="store_true", help="write preview.html into the pack")
args = ap.parse_args()
root = Path(args.pack).resolve()
issues = []

def issue(rule, message):
    issues.append("[%s] %s" % (rule, message))

try:
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
except (OSError, ValueError) as exc:
    sys.exit("[PACK-MANIFEST] Cannot read manifest.json: %s" % exc)

def safe_file(value, rule):
    if not isinstance(value, str) or not value or "\\" in value:
        issue(rule, "Expected a relative file path.")
        return None
    path = (root / value).resolve()
    if root not in path.parents or not path.is_file():
        issue(rule, "File is missing or escapes the pack: %s" % value)
        return None
    return path

if not isinstance(manifest, dict):
    sys.exit("[PACK-MANIFEST] manifest.json must contain an object")
allowed = {"formatVersion", "name", "slug", "contract", "minimumLibraryVersion", "css", "assets", "icons", "variants", "license"}
for key in sorted(set(manifest) - allowed):
    issue("PACK-FIELD", "Unknown field: " + key)
required = ("formatVersion", "name", "slug", "contract", "minimumLibraryVersion", "css", "license")
for key in required:
    if key not in manifest:
        issue("PACK-FIELD", "Missing required field: " + key)
if manifest.get("formatVersion") != 1:
    issue("PACK-VERSION", "formatVersion must be 1")
for key in ("name", "minimumLibraryVersion"):
    if not isinstance(manifest.get(key), str) or not manifest[key].strip():
        issue("PACK-FIELD", key + " must be a non-empty string")
slug = manifest.get("slug", "")
if not isinstance(slug, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
    issue("PACK-SLUG", "slug must be lowercase kebab-case")
if manifest.get("contract") != 4:
    issue("PACK-CONTRACT", "contract must match the supported contract version 4")
lic = manifest.get("license")
if (not isinstance(lic, dict) or not isinstance(lic.get("name"), str) or not lic["name"].strip()
        or not isinstance(lic.get("notice"), str) or not lic["notice"].strip()):
    issue("PACK-LICENSE", "license needs a name and notice file")
css_path = safe_file(manifest.get("css"), "PACK-CSS")
if isinstance(lic, dict):
    safe_file(lic.get("notice"), "PACK-LICENSE")
assets = manifest.get("assets", [])
if not isinstance(assets, list):
    issue("PACK-ASSET", "assets must be an array")
    assets = []
for value in assets:
    safe_file(value, "PACK-ASSET")
if manifest.get("icons"):
    safe_file(manifest["icons"], "PACK-ICONS")
variants = manifest.get("variants", [])
if not isinstance(variants, list) or any(not isinstance(v, dict) or not isinstance(v.get("id"), str) or not v["id"].strip() or not isinstance(v.get("label"), str) or not v["label"].strip() for v in variants):
    issue("PACK-VARIANTS", "variants must be objects with string id and label fields")
css = css_path.read_text(encoding="utf-8") if css_path else ""
css = cssparse.strip_comments(css)
# Mask strings so examples in content: or font names are not CSS requests.
strings = re.compile(r"\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*'", re.S)
syntax = strings.sub(lambda m: " " * len(m.group()), css)
# This small validator does not decode CSS escapes in identifiers or paths.
if "\\" in syntax:
    issue("PACK-CSS-ESCAPE", "CSS escapes in identifiers are not supported; use literal names")
if re.search(r"@import\b", syntax, re.I):
    issue("PACK-REMOTE-CSS", "Remote imports and external/data URLs are not allowed")
if re.search(r"(?<![\w-])(?:-webkit-)?image-set\(", syntax, re.I):
    issue("PACK-ASSET", "image-set() is not supported; use url() for pack assets")
declared = {value for value in assets if isinstance(value, str)}
url_pattern = re.compile(r'''url\(\s*(?:"((?:\\.|[^"\\])*)"|'((?:\\.|[^'\\])*)'|([^)]*))\s*\)''', re.I | re.S)
for start in re.finditer(r"(?<![\w-])url\(", syntax, re.I):
    match = url_pattern.match(css, start.start())
    if not match:
        issue("PACK-ASSET", "Malformed CSS asset URL")
        continue
    url = next(value for value in match.groups() if value is not None).strip()
    if re.search(r"[\x00-\x1f\x7f]", url):
        issue("PACK-ASSET", "Control characters are not allowed in CSS asset URLs")
        continue
    if "\\" in url:
        issue("PACK-CSS-ESCAPE", "CSS escapes in asset URLs are not supported; use literal paths")
        continue
    if re.match(r"(?:[a-z][a-z0-9+.-]*:|//)", url, re.I):
        issue("PACK-REMOTE-CSS", "Remote imports and external/data URLs are not allowed")
        continue
    if not url or url.startswith("#") or url.startswith("var("):
        continue
    referenced = (css_path.parent / url).resolve() if css_path else root
    if root not in referenced.parents or not referenced.is_file():
        issue("PACK-ASSET", "CSS asset is missing or escapes the pack: " + url)
    else:
        relative = referenced.relative_to(root).as_posix()
        if relative not in declared:
            issue("PACK-ASSET", "CSS asset is not declared in manifest.assets: " + relative)


def check_scope(source):
    scoped = re.compile(r"^html\[data-theme=([\"'])" + re.escape(str(slug)) + r"\1\](?=$|[\s.#[:>+~])")
    for prelude, body in cssparse.statements(source):
        if body is None:
            continue
        at_rule = re.match(r"@[-a-z]+", prelude, re.I)
        name = at_rule.group().lower() if at_rule else ""
        if name in cssparse.GROUPING or name == "@starting-style":
            check_scope(body)
        elif name:
            if name not in ("@font-face", "@keyframes", "@-webkit-keyframes"):
                issue("PACK-SCOPE", "Unsupported unscoped CSS block: " + prelude)
        else:
            for selector in cssparse.split_top(prelude):
                if not scoped.match(selector):
                    issue("PACK-SCOPE", "Selector must start with the theme root: " + selector)


check_scope(css)
tokens = build_manifest.root_tokens(css, slug) if slug else {}
if slug and not tokens:
    issue("PACK-SCOPE", "CSS must scope theme rules to html[data-theme=\"%s\"]" % slug)
required_tokens = {"--bg", "--surface", "--surface-2", "--border", "--hairline", "--text", "--muted", "--accent", "--accent-2", "--danger", "--success", "--warning", "--on-accent", "--on-danger", "--on-success", "--radius", "--font", "--font-mono", "--flare"}
for token in sorted(required_tokens - set(tokens)):
    issue("PACK-TOKEN", "Theme root is missing " + token)
if issues:
    print("\n".join(issues), file=sys.stderr)
    sys.exit(1)
if args.preview:
    title = str(manifest.get("name", slug)).replace("&", "&amp;").replace("<", "&lt;").replace('"', "&quot;")
    preview_css = css_path.parent / ".ftl-preview-theme.css"
    preview_css.write_text("@layer ui {\n" + css_path.read_text(encoding="utf-8") + "\n}\n", encoding="utf-8")
    css_href = preview_css.relative_to(root).as_posix().replace("&", "&amp;").replace('"', "&quot;")
    layout = (Path(__file__).resolve().parents[1] / "core" / "layout.css").read_text(encoding="utf-8")
    core_href = (Path(__file__).resolve().parents[1] / "dist" / "core.css").as_uri()
    html = ('<!doctype html><html lang="en" data-theme="%s"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width"><title>%s preview</title>'
            '<link rel="stylesheet" href="%s"><link rel="stylesheet" href="%s">'
            '<style>@layer ui { %s }</style></head><body class="app">'
            '<header class="app-bar">%s theme pack</header><main class="app-main"><h1>%s</h1>'
            '<p class="text-muted">Local theme pack preview</p><section class="panel">'
            '<h2>Components</h2><button class="btn btn-primary">Primary action</button> '
            '<button class="btn btn-secondary">Secondary</button><p><span class="badge badge-success">Ready</span> '
            '<span class="badge badge-warning">Review</span></p></section></main>'
            '<footer class="app-status">Validated local preview</footer></body></html>') % (
                slug, title, core_href, css_href, layout, title, title)
    (root / "preview.html").write_text(html, encoding="utf-8")
    print("wrote %s/preview.html" % root)
else:
    print("valid theme pack: %s" % manifest.get("name", slug))
