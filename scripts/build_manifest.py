#!/usr/bin/env python3
"""Writes dist/themes.json after build.sh has produced the CSS bundles.

Split out of build.sh (it was bash) because two of the fields it stamps are
derivations that scripts/check.py must be able to recompute from the built
bundles — importing this module instead of re-implementing the logic keeps
the stamp and the cross-check from drifting apart:

  version    deterministic: a git hash-object over every dist/*.css bundle's
             exact bytes, so it changes iff any served CSS changes, and a
             -dirty suffix when the CSS sources have uncommitted edits.
             (Replaces git-describe + wall-clock builtAt, which churned on
             every rebuild and made submodule-pointer diffs meaningless.)
  scheme     light/dark, derived exactly the way CuTePi's routes/themes.go
             derived it before this field existed (that app was the
             reference implementation): --ftl-surface, composited over the
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

VAR_RE = re.compile(r"--(ftl-[a-z0-9-]+)\s*:\s*([^;]+)")
HEX_RE = re.compile(r"^#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")
RGBA_RE = re.compile(r"^rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:[,\s/]+([\d.]+)(%)?)?\s*\)$")
RULE_RE = re.compile(r"([^{}@]+)\{([^{}]*)\}")


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
    """--ftl-name: value from the theme's root block(s) only, merged in
    source order as the cascade would. Palette variants
    ([data-variant]) and element-scoped overrides (.ftl-app-status, …)
    are not the theme's default palette and must not stand in for it —
    reading every declaration in the file let a variant declared last
    (imac-g3's tangerine) stamp the default theme's luminance."""
    root = 'html[data-theme="%s"]' % slug
    out = {}
    for m in RULE_RE.finditer(re.sub(r"/\*.*?\*/", "", src, flags=re.S)):
        if root in (s.strip() for s in m.group(1).split(",")):
            for t in VAR_RE.finditer(m.group(2)):
                out["--" + t.group(1)] = t.group(2).strip()
    return out


def resolve_color(tokens, value, depth=0):
    """parse_color, following var(--ftl-…) chains through tokens."""
    if depth > 6:
        return None
    c = parse_color(value)
    if c is not None:
        return c
    m = re.match(r"^\s*var\(\s*(--ftl-[a-z0-9-]+)", value)
    if m and m.group(1) in tokens:
        return resolve_color(tokens, tokens[m.group(1)], depth + 1)
    return None


def scheme_of(src, slug):
    """("light"|"dark", luminance) the way integrators used to derive it.

    The app's panels sit on --ftl-surface; if that is translucent or missing
    it is composited over the theme's shell/page background (--ftl-app-bg /
    --ftl-app-main-bg / --ftl-bg, first that exists) and plain-weighted
    luminance above 0.55 reads as light. Unparseable themes read as dark —
    the historical default — and stamp luminance null.
    """
    tokens = root_tokens(src, slug)
    surface = resolve_color(tokens, tokens.get("--ftl-surface", ""))
    if surface is None:
        return "dark", None
    if surface[3] < 1:
        for name in ("--ftl-app-bg", "--ftl-app-main-bg", "--ftl-bg"):
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


def version():
    """Build identity from the bundles themselves: changes iff they change."""
    blob = b"".join(open(f, "rb").read() for f in sorted(glob.glob("dist/*.css")))
    h = subprocess.run(["git", "hash-object", "--stdin"], input=blob,
                       capture_output=True).stdout.decode().strip()[:12]
    dirty = subprocess.run(["git", "status", "--porcelain", "--", "core", "themes"],
                           capture_output=True, text=True).stdout.strip()
    return "ftl-" + h + ("-dirty" if dirty else "")


def write_manifest():
    version_ = version()
    entries = []
    for path in sorted(glob.glob("themes/*/theme.css")):
        slug = os.path.basename(os.path.dirname(path))
        src = open(path).read()
        label = header_field(src, "Theme-Name") or slug
        scheme, luminance = scheme_of(src, slug)
        entries.append({
            "slug": slug,
            "dataTheme": slug,
            "label": label,
            "description": header_field(src, "Description"),
            "hasChrome": os.path.exists(os.path.join(os.path.dirname(path), "chrome.css")),
            "shellAware": bool(re.search(r"--ftl-app-[A-Za-z0-9-]+\s*:",
                                         re.sub(r"/\*.*?\*/", "", src, flags=re.S))),
            "version": version_,
            "scheme": scheme,
            "luminance": luminance,
        })
    lines = ",\n".join("  " + json.dumps(e, ensure_ascii=False) for e in entries)
    with open("dist/themes.json", "w") as f:
        f.write("[\n" + lines + "\n]\n")
    print("built dist/themes.json")


if __name__ == "__main__":
    write_manifest()
