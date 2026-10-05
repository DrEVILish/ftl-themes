#!/usr/bin/env python3
"""Writes dist/themes.json after build.sh has produced the CSS bundles.

Split out of build.sh (it was bash) because two of the fields it stamps are
derivations that scripts/check.py must be able to recompute from the built
bundles — importing this module instead of re-implementing the logic keeps
the stamp and the cross-check from drifting apart:

  version    deterministic: a git hash-object over every dist/*.css bundle's
             exact bytes, so it changes iff any served CSS changes.
             (Replaces git-describe + wall-clock builtAt, which churned on
             every rebuild and made submodule-pointer diffs meaningless.)
             It used to carry a -dirty suffix while core/ or themes/ had
             uncommitted edits, which made every source change a two-commit
             affair: the manifest built alongside the edit was stamped
             -dirty, and the clean rebuild after committing differed from
             it. The hash alone already names the exact CSS served.
  scheme     light/dark, derived exactly the way CuTePi's routes/themes.go
             derived it before this field existed (that app was the
             reference implementation): --surface, composited over the
             theme's first solid page/shell background when translucent,
             plain-weighted luminance, 0.55 threshold.

Consuming apps should treat every field here as build-produced, not source:
edit sources and re-run scripts/build.sh, never this file's output.
"""
import glob
import json
import os
import re
import subprocess
import xml.etree.ElementTree as ET

import cssparse

# Major version of the class/token contract the bundles implement. Bumped
# when a rename or removal would break a consumer's markup or CSS.
CONTRACT = 4

HEX_RE = re.compile(r"^#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")
RGBA_RE = re.compile(r"^rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:[,\s/]+([\d.]+)(%)?)?\s*\)$")


def parse_color(value):
    """(r, g, b, a) floats or None, for the syntaxes theme sources use:
    #rgb, #rgba, #rrggbb, #rrggbbaa, rgb()/rgba() in comma or space form."""
    value = value.strip()
    m = HEX_RE.match(value)
    if m:
        h = m.group(1)
        if len(h) <= 4:
            h = "".join(c * 2 for c in h)
        a = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
        n = int(h[:6], 16)
        return ((n >> 16) & 255, (n >> 8) & 255, n & 255, a)
    m = RGBA_RE.match(value)
    if m:
        alpha = float(m.group(4)) if m.group(4) else 1.0
        if m.group(5):
            alpha /= 100
        return (float(m.group(1)), float(m.group(2)), float(m.group(3)), alpha)
    return None


def root_tokens(src, slug):
    """--name: value from the theme's root block(s) only, merged in
    source order as the cascade would. Palette variants
    ([data-variant]) and element-scoped overrides (.app-status, …)
    are not the theme's default palette and must not stand in for it —
    reading every declaration in the file let a variant declared last
    (imac-g3's tangerine) stamp the default theme's luminance."""
    root = 'html[data-theme="%s"]' % slug
    out = {}
    for rule in cssparse.rules(src):
        # A root block inside @media/@supports only applies sometimes, so
        # it is not the default palette either.
        if rule.selector == root and cssparse.unconditional(rule.context):
            for name, value in cssparse.declarations(rule.body):
                if name.startswith("--"):
                    out[name] = value
    return out


def resolve_color(tokens, value, depth=0):
    """parse_color, following var(--…) chains through tokens."""
    if depth > 6:
        return None
    c = parse_color(value)
    if c is not None:
        return c
    m = re.match(r"^\s*var\(\s*(--[a-z0-9-]+)", value)
    if m and m.group(1) in tokens:
        return resolve_color(tokens, tokens[m.group(1)], depth + 1)
    return None


def scheme_of(src, slug):
    """("light"|"dark", luminance) the way integrators used to derive it.

    The app's panels sit on --surface; if that is translucent or missing
    it is composited over the theme's shell/page background (--app-bg /
    --app-main-bg / --bg, first that exists) and plain-weighted
    luminance above 0.55 reads as light. Unparseable themes read as dark —
    the historical default — and stamp luminance null.
    """
    tokens = root_tokens(src, slug)
    surface = resolve_color(tokens, tokens.get("--surface", ""))
    if surface is None:
        return "dark", None
    if surface[3] < 1:
        for name in ("--app-bg", "--app-main-bg", "--bg"):
            base = resolve_color(tokens, tokens.get(name, ""))
            if base is not None:
                a = surface[3]
                surface = (surface[0] * a + base[0] * (1 - a),
                           surface[1] * a + base[1] * (1 - a),
                           surface[2] * a + base[2] * (1 - a), 1.0)
                break
    lum = (0.2126 * surface[0] + 0.7152 * surface[1] + 0.0722 * surface[2]) / 255
    return ("light" if lum > 0.55 else "dark"), round(lum, 3)


def header_field(src, field):
    """Theme-Name/Description from the header comment, like build.sh did."""
    m = re.search(r"(?m)^[ \t]*\*?[ \t]*%s:[ \t]*(\S.*?)[ \t]*$" % field, src)
    return m.group(1) if m else ""


def component_classes(src):
    return set(re.findall(r"(?<![\w-])\.([a-z][a-z0-9-]*)", cssparse.strip_comments(src)))


def icon_ids(path):
    if not os.path.isfile(path):
        return set()
    try:
        return {el.get("id") for el in ET.parse(path).iter() if el.get("id")}
    except ET.ParseError:
        return set()


def version():
    """Build identity from the bundles themselves: changes iff they change."""
    blob = b"".join(open(f, "rb").read() for f in sorted(glob.glob("dist/*.css")))
    r = subprocess.run(["git", "hash-object", "--stdin"], input=blob,
                       capture_output=True)
    h = r.stdout.decode().strip()[:12]
    if r.returncode != 0 or not h:
        raise SystemExit("build_manifest: git hash-object failed: " + r.stderr.decode().strip())
    return h


def load_categories():
    """slug -> {category, era} from themes/categories.json. This is a
    curated classification (taxonomy documented in CONTRACT.md's Theme
    index section), not something derivable from the CSS itself, so it
    lives in its own small data file rather than 22 header-comment edits."""
    with open("themes/categories.json") as f:
        data = json.load(f)
    data.pop("_comment", None)
    return data


def write_manifest():
    version_ = version()
    categories = load_categories()
    entries = []
    core_classes = set()
    for component_path in glob.glob("core/components/*.css"):
        core_classes.update(component_classes(open(component_path, encoding="utf-8").read()))
    core_icons = {"icon-" + x.strip() for x in open("assets/icons/core-set.txt", encoding="utf-8") if x.strip()}
    for path in sorted(glob.glob("themes/*/theme.css")):
        slug = os.path.basename(os.path.dirname(path))
        src = open(path).read()
        label = header_field(src, "Theme-Name") or slug
        scheme, luminance = scheme_of(src, slug)
        meta = categories.get(slug, {})
        # Palette variants (CONTRACT.md "Palette variants") are listed in the
        # header as `Variants: id=Label, id=Label` so pickers can offer them.
        variants = [dict(zip(("id", "label"), (x.strip() for x in v.split("=", 1))))
                    for v in header_field(src, "Variants").split(",") if "=" in v]
        # Theme tint (CONTRACT.md "Theme tint"): `Tint: --token #default Label`.
        tm = re.match(r"(--[a-z0-9-]+)\s+(#[0-9a-fA-F]{6})\s*(.*)$", header_field(src, "Tint"))
        tint = {"token": tm.group(1), "default": tm.group(2).lower(), "label": tm.group(3) or "Tint"} if tm else None
        full_src = src
        chrome_path = os.path.join(os.path.dirname(path), "chrome.css")
        if os.path.isfile(chrome_path):
            full_src += "\n" + open(chrome_path, encoding="utf-8").read()
        own_classes = component_classes(full_src)
        overrides = icon_ids(os.path.join(os.path.dirname(path), "icons.svg"))
        references = [p for p in glob.glob("references/%s/**/*" % slug, recursive=True) if os.path.isfile(p)]
        fonts = sorted(set(re.findall(r"url\(['\"]?assets/fonts/([^)'\"]+)", full_src)))
        navigation = [x.strip() for x in header_field(src, "Navigation-Patterns").split(",") if x.strip()]
        entries.append({
            "slug": slug,
            "dataTheme": slug,
            "label": label,
            "description": header_field(src, "Description"),
            "hasChrome": os.path.exists(os.path.join(os.path.dirname(path), "chrome.css")),
            "shellAware": bool(re.search(r"--app-[A-Za-z0-9-]+\s*:",
                                         cssparse.strip_comments(src))),
            "version": version_,
            "contract": CONTRACT,
            "scheme": scheme,
            "luminance": luminance,
            "tokens": sorted(root_tokens(src, slug)),
            "fonts": fonts,
            "iconCoverage": {"overrides": len(overrides & core_icons), "total": len(core_icons), "allOverrides": len(overrides)},
            "references": {"files": len(references), "research": os.path.isfile("references/%s/RESEARCH.md" % slug)},
            "componentCoverage": {"styledSelectors": len(own_classes & core_classes), "coreDefaults": len(core_classes - own_classes), "total": len(core_classes)},
            "navigationPatterns": navigation,
            "category": meta.get("category"),
            "era": meta.get("era"),
            **({"variants": variants} if variants else {}),
            **({"tint": tint} if tint else {}),
        })
    lines = ",\n".join("  " + json.dumps(e, ensure_ascii=False) for e in entries)
    with open("dist/themes.json", "w") as f:
        f.write("[\n" + lines + "\n]\n")
    print("built dist/themes.json")


if __name__ == "__main__":
    write_manifest()
