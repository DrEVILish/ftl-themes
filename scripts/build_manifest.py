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
HEX_RE = re.compile(r"^#([0-9a-fA-F]{6})$")
RGBA_RE = re.compile(r"^rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:[,\s]+([\d.]+))?\s*\)$")


def parse_color(value):
    """(r, g, b, a) floats or None, for the syntaxes theme sources use."""
    value = value.strip()
    m = HEX_RE.match(value)
    if m:
        n = int(m.group(1), 16)
        return ((n >> 16) & 255, (n >> 8) & 255, n & 255, 1.0)
    m = RGBA_RE.match(value)
    if m:
        alpha = float(m.group(4)) if m.group(4) else 1.0
        return (float(m.group(1)), float(m.group(2)), float(m.group(3)), alpha)
    return None


def tokens_of(body):
    """--ftl-name: value; last declaration wins, as in CSS."""
    out = {}
    for m in VAR_RE.finditer(body):
        out["--" + m.group(1)] = m.group(2).strip()
    return out


def scheme_of(body):
    """("light"|"dark", luminance) the way integrators used to derive it.

    The app's panels sit on --ftl-surface; if that is translucent or missing
    it is composited over the theme's shell/page background (--ftl-app-bg /
    --ftl-app-main-bg / --ftl-bg, first that exists) and plain-weighted
    luminance above 0.55 reads as light. Unparseable themes read as dark —
    the historical default — and stamp luminance null.
    """
    tokens = tokens_of(body)
    surface = parse_color(tokens.get("--ftl-surface", ""))
    if surface is None:
        return "dark", None
    if surface[3] < 1:
        for name in ("--ftl-app-bg", "--ftl-app-main-bg", "--ftl-bg"):
            base = parse_color(tokens.get(name, ""))
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
        scheme, luminance = scheme_of(src)
        entries.append({
            "slug": slug,
            "dataTheme": slug,
            "label": label,
            "description": header_field(src, "Description"),
            "hasChrome": os.path.exists(os.path.join(os.path.dirname(path), "chrome.css")),
            "shellAware": bool(re.search(r"--ftl-app-[A-Za-z0-9-]+\s*:", src)),
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
