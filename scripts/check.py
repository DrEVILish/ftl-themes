#!/usr/bin/env python3
"""Contract lint for ftl-themes.

Every rule corresponds to a bug that actually shipped once:

  tokens     a theme omitting a token silently inherited core's fallback,
             which looked plausible on dark themes and invisible on light.
  variants   a theme declaring background/color on a BASE component selector
             outranks core's unscoped variant rules (html[data-theme] .ftl-btn
             is 0,2,1 vs .ftl-btn-danger at 0,1,0), so danger/success buttons
             silently lost their fill. Themes must set --ftl-<comp>-* at root
             scope instead: a declaration on the element always beats an
             inherited one, so variants keep winning.
  focus      a theme setting `outline: none` left controls with no visible
             keyboard focus indicator.
  important  `* { box-shadow: none !important }` also erased the table's
             is-active row marker.
  contrast   filled controls painted with --ftl-bg as the foreground fail on
             light palettes; --ftl-on-* exist to prevent it. Soft checks
             (page-backdrop text, AAA target, accent legibility) are skipped
             for themes whose README documents a `contrast-exempt:` rationale;
             the hard 4.5:1 floor never is.
  dist       committed bundles must match a fresh build, since submodule
             consumers cannot run the build themselves. themes.json is
             deterministic (content-hash version, no wall-clock fields), so
             it is checked like every other dist file.
  docs       a theme without a stated intent gets "improved" into a different
             theme by the next contributor. Requires "Signature details" too,
             not just "Core values" — that's the section example.html's
             compare mode surfaces, and 11 themes shipped without it before
             a v3.5.1 pass caught the gap.
  layout     a theme is a layout as much as a palette; one that sets no
             --ftl-app-* property renders in the default arrangement.
  motion     unprompted infinite animation plays for users who asked the OS
             to stop it; gate it behind prefers-reduced-motion: no-preference
             (the matrix pattern), never behind nothing.
  requires   a theme without a Requires: L0/L1 badge leaves apps guessing
             whether it needs the app shell (the LCARS-on-a-token-only-app
             failure). All 26 themes were badged in one pass (#18); new
             themes must ship one too — promoted from warn to fail once
             the rollout reached 100%.
  color-scheme  without it, UA-owned chrome (scrollbars, native date/time
             pickers, autofill) renders for the wrong palette under every
             dark theme, even though every .ftl-* control is themed
             correctly. Declaring it changes no behavior — themes still
             don't respond to prefers-color-scheme, by design.
  remote-url a theme or core file referencing a remote url()/@import makes
             every consumer depend on connectivity; a field-offline
             consumer (a recorder with no network) needs every bundle to
             work fully embedded.
  scheme     the manifest's scheme/luminance must match a re-derivation from
             the theme source, so hand-edited manifests can't drift. Distinct
             from the color-scheme rule above: this checks the *manifest's*
             stamped value against the CSS; that one checks the CSS declares
             a value at all.
"""
import glob
import json
import os
import re
import subprocess
import sys

import build_manifest  # noqa: E402  (sys.path[0] is scripts/ when run as a script)

REQUIRED_TOKENS = [
    "bg", "surface", "surface-2", "border", "hairline", "text", "muted",
    "accent", "accent-2", "danger", "success", "warning",
    "on-accent", "on-danger", "on-success",
    "radius", "font", "font-mono", "flare",
]

# Base component selectors: a theme must not set these properties on them.
BASE_COMPONENTS = [
    "ftl-btn", "ftl-panel", "ftl-modal", "ftl-dropdown", "ftl-input",
    "ftl-select", "ftl-textarea", "ftl-badge", "ftl-nav-item", "ftl-tab",
    # v3.4.0 additions: same base-rule-plus-custom-property-variant
    # architecture as .ftl-btn, so the same cascade bug applies to them.
    "ftl-toast", "ftl-context-menu", "ftl-dropzone", "ftl-card",
    "ftl-alert", "ftl-avatar", "ftl-popover", "ftl-pagination-item",
    "ftl-breadcrumb-item",
]
FORBIDDEN_ON_BASE = ["background", "background-color", "color"]

failures = []
warnings = []


def fail(theme, rule, msg):
    failures.append(f"{theme}: [{rule}] {msg}")


def warn(theme, rule, msg):
    warnings.append(f"{theme}: [{rule}] {msg}")


def strip_comments(css):
    return re.sub(r"/\*.*?\*/", "", css, flags=re.S)


def strip_gated_motion(css):
    """Remove @media (prefers-reduced-motion: no-preference) blocks."""
    out, i, n = [], 0, len(css)
    gate = re.compile(r"@media\s*\(\s*prefers-reduced-motion\s*:\s*no-preference\s*\)\s*\{")
    while i < n:
        m = gate.search(css, i)
        if not m:
            out.append(css[i:])
            break
        out.append(css[i:m.start()])
        depth, j = 1, m.end()
        while j < n and depth:
            if css[j] == "{":
                depth += 1
            elif css[j] == "}":
                depth -= 1
            j += 1
        i = j
    return "".join(out)


def rules_of(css):
    """[(selector, body)] for every comma-split selector, comments removed."""
    out = []
    for m in re.finditer(r"([^{}@]+)\{([^{}]*)\}", strip_comments(css)):
        for sel in m.group(1).split(","):
            out.append((sel.strip(), m.group(2)))
    return out


def luminance(rgb):
    def chan(c):
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (chan(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = luminance(a[:3]), luminance(b[:3])
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def resolve(tokens, value, depth=0):
    """Resolve a token value down to (r, g, b, a), if it is a literal color
    or a var() chain ending in one. A translucent result keeps its alpha:
    whether it is legible depends on what it is measured against, so the
    pair site composites it over its partner."""
    value = value.strip()
    if depth > 6:
        return None
    if value.startswith("#"):
        h = value.lstrip("#")
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        if len(h) != 6:
            return None
        n = int(h, 16)
        return ((n >> 16) & 255, (n >> 8) & 255, n & 255, 1.0)
    m = re.match(r"^rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:[,\s]+([\d.]+))?\s*\)$", value)
    if m:
        return (float(m.group(1)), float(m.group(2)), float(m.group(3)),
                float(m.group(4)) if m.group(4) else 1.0)
    m = re.match(r"^var\(\s*--ftl-([a-z0-9-]+)", value)
    if m and m.group(1) in tokens:
        return resolve(tokens, tokens[m.group(1)], depth + 1)
    return None


for path in sorted(glob.glob("themes/*/theme.css")):
    theme = os.path.basename(os.path.dirname(path))
    css = open(path).read()
    body = strip_comments(css)

    tokens = {}
    for m in re.finditer(r"--ftl-([a-z0-9-]+)\s*:\s*([^;]+);", body):
        tokens.setdefault(m.group(1), m.group(2).strip())

    missing = [t for t in REQUIRED_TOKENS if t not in tokens]
    if missing:
        fail(theme, "tokens", f"missing required token(s): {', '.join('--ftl-' + t for t in missing)}")

    # UA-owned chrome (scrollbars, native pickers, autofill) stays light
    # under a dark theme unless told otherwise — declaring color-scheme
    # doesn't change theme behavior (themes still don't respond to
    # prefers-color-scheme, by design), it only tells the browser what the
    # theme already is.
    scheme_matches = re.findall(r"color-scheme\s*:\s*(light|dark)\s*;", body)
    if not scheme_matches:
        fail(theme, "color-scheme", "no `color-scheme` declaration — UA-owned controls "
                                     "(scrollbars, native pickers, autofill) render for the "
                                     "wrong palette. Declare `color-scheme: light;` or `dark;` "
                                     "in the theme's root block.")
    elif len(scheme_matches) > 1:
        fail(theme, "color-scheme", f"multiple `color-scheme` declarations "
                                     f"({', '.join(scheme_matches)}) — exactly one expected.")

    # Field-offline consumers (e.g. a recorder with no network) embed the
    # bundles specifically so the UI never depends on connectivity. A
    # remote url()/@import would silently break that guarantee.
    for m in re.finditer(r"url\(\s*['\"]?(https?:)?//", body):
        fail(theme, "remote-url", f"contains a remote `url(...)` reference "
                                   f"(`{m.group(0)}`) — themes must be usable fully offline; "
                                   f"vendor the asset into assets/ instead.")
    for m in re.finditer(r"@import\s+(?:url\()?['\"]?(https?:)?//", body):
        fail(theme, "remote-url", f"contains a remote `@import` (`{m.group(0)}`) — "
                                   f"themes must be usable fully offline.")

    for sel, decls in rules_of(css):
        last = sel.split()[-1] if sel.split() else sel
        classes = set(re.findall(r"\.([\w-]+)", last))
        has_pseudo = bool(re.search(r":[\w-]+", last))
        # A base component selector carries exactly the component class and
        # no variant/state class alongside it.
        for comp in BASE_COMPONENTS:
            if classes == {comp} and not has_pseudo:
                for prop in FORBIDDEN_ON_BASE:
                    if re.search(r"(?:^|;)\s*" + prop + r"\s*:", decls):
                        fail(theme, "variants",
                             f"`{sel}` sets `{prop}` on a base component — this outranks "
                             f"core's .{comp}-* variant rules and erases them. Set "
                             f"--{comp}-bg / --{comp}-fg at root scope instead.")
        if re.search(r"outline\s*:\s*none", decls) and "focus" in sel:
            fail(theme, "focus",
                 f"`{sel}` removes the focus outline. Recolor via --ftl-focus or add a "
                 f"glow via --ftl-focus-ring instead; never remove the indicator.")
        if last in ("*", "*::before", "*::after") and "!important" in decls:
            fail(theme, "important",
                 f"`{sel}` uses !important on a universal selector — it also erases "
                 f"state indicators like .ftl-table tr.is-active's marker.")

    # Every theme states its intent in prose beside its CSS: what look it is
    # reproducing, its core values, and how to tell an inauthentic result.
    # A palette without that context gets "improved" into something else.
    readme = os.path.join(os.path.dirname(path), "README.md")
    readme_text = open(readme).read() if os.path.exists(readme) else ""
    if not readme_text:
        fail(theme, "docs", "no README.md beside theme.css — every theme documents "
                            "what it is trying to achieve (see any existing theme)")
    else:
        # "Signature details" specifically (not just Core values) is what
        # example.html's compare mode surfaces — a theme missing it isn't
        # broken, but it's invisible to that tool, so the same soft warning
        # applies here as to the other structural sections.
        for heading in ("What this theme is trying to achieve", "Core values", "Signature details"):
            if heading.lower() not in readme_text.lower():
                warn(theme, "docs", f"README.md has no '{heading}' section")

    # Contrast floor for filled controls, using the theme's own token values.
    # Text is checked against --ftl-surface, the substrate it actually sits
    # on (panels, cards, modals). --ftl-bg can legitimately be a decorative
    # backdrop that never carries body text — Windows 95's teal desktop is
    # the canonical case — so failing text against it would be wrong; it's
    # reported as a warning instead. The soft rows (warn-level floors: the
    # decorative-backdrop check, the AAA target, accent legibility) are
    # skipped for a theme whose README carries a documented
    # `contrast-exempt:` marker — authenticity sometimes demands a
    # deliberately low-contrast decorative pair, and the README line is
    # where the rationale lives. The hard 4.5:1 floors are never exempted.
    exempt = "contrast-exempt:" in readme_text.lower()
    for label, fg_tok, bg_tok, floor, hard in (
        ("primary button", "on-accent", "accent", 4.5, True),
        ("danger button", "on-danger", "danger", 4.5, True),
        ("success button", "on-success", "success", 4.5, True),
        ("body text", "text", "surface", 4.5, True),
        ("muted text", "muted", "surface", 3.0, True),
        ("body text on page backdrop", "text", "bg", 4.5, False),
        ("body text (AAA)", "text", "surface", 7.0, False),
        ("body text on backdrop (AAA)", "text", "bg", 7.0, False),
        ("accent legibility", "accent", "surface", 3.0, False),
        ("accent on page backdrop", "accent", "bg", 3.0, False),
    ):
        if not hard and exempt:
            continue
        fg = resolve(tokens, tokens.get(fg_tok, ""))
        bg = resolve(tokens, tokens.get(bg_tok, ""))
        if not (fg and bg):
            continue
        if bg[3] < 1:
            continue  # translucent backdrop: what is behind it is unknown
        if fg[3] < 1:
            fg = tuple(fg[i] * fg[3] + bg[i] * (1 - fg[3]) for i in range(3)) + (1.0,)
        ratio = contrast(fg, bg)
        if ratio < floor:
            msg = (f"{label}: --ftl-{fg_tok} {fg} on --ftl-{bg_tok} {bg} = "
                   f"{ratio:.1f}:1 (floor {floor}:1)")
            (fail if hard else warn)(theme, "contrast", msg)

    # Coverage: report components the theme never touches, so an author can
    # see what they skipped. Informational, not a failure — token-only
    # theming is a legitimate and encouraged starting point.
    styled = {c for sel, _ in rules_of(css) for c in re.findall(r"\.(ftl-[\w-]+)", sel)}
    proped = {m.group(1) for m in re.finditer(r"--ftl-(btn|panel|modal|input|nav|table|tab|badge|progress|slider|switch|dropdown)\b", body)}
    if not styled and not proped:
        warn(theme, "coverage", "styles no components at all beyond tokens")

    # A theme is a layout as much as a palette — switching to one should move
    # the furniture, not only recolor it. Themes that set no --ftl-app-*
    # property render in the shell's default arrangement, which is legitimate
    # but usually means the layout pass was forgotten.
    if not re.search(r"--ftl-app-[\w-]+\s*:", body):
        warn(theme, "layout", "defines no --ftl-app-* layout personality — the app "
                              "shell will look identical to every other such theme")

    ungated = strip_gated_motion(body)
    if re.search(r"animation\s*:[^;}]*\binfinite\b", ungated):
        fail(theme, "motion", "infinite animation outside a "
             "prefers-reduced-motion: no-preference gate plays for users who "
             "asked the OS to stop it — wrap it like matrix does")

    if "requires:" not in readme_text.lower():
        fail(theme, "requires", "README.md has no 'Requires: L0/L1' badge — "
             "apps cannot tell whether this theme needs the app shell "
             "(see CONTRACT.md \"Adoption levels\")")

# Remote URLs are also checked in core/ (themes/ is covered per-theme above)
# — a field-offline consumer embeds dist/, so a remote reference anywhere in
# the source it's built from breaks the same offline guarantee.
for path in sorted(glob.glob("core/*.css")):
    body = strip_comments(open(path).read())
    for m in re.finditer(r"url\(\s*['\"]?(https?:)?//", body):
        failures.append(f"core: [remote-url] {path} contains a remote `url(...)` "
                         f"reference (`{m.group(0)}`) — vendor the asset instead.")
    for m in re.finditer(r"@import\s+(?:url\()?['\"]?(https?:)?//", body):
        failures.append(f"core: [remote-url] {path} contains a remote `@import` "
                         f"(`{m.group(0)}`).")

# dist/ must match a fresh build — including themes.json, which is
# deterministic now (its version is a content hash of the bundles; no
# wall-clock field survives a rebuild).
subprocess.run(["scripts/build.sh"], check=True, stdout=subprocess.DEVNULL)
diff = subprocess.run(["git", "diff", "--name-only", "--", "dist"],
                      capture_output=True, text=True).stdout.split()
if diff:
    failures.append("dist: committed bundles are stale — run scripts/build.sh and commit "
                    f"({', '.join(diff)})")

# The manifest must list every theme, and each entry must carry the fields
# integrators actually rely on: dataTheme (guaranteed equal to slug — spelled
# out per-entry anyway, per CONTRACT.md "dataTheme"), the build-identity
# version, and the scheme/luminance stamp — which is cross-checked here
# against a fresh derivation, so a hand-edited manifest cannot drift from
# what the theme source actually says.
manifest = json.load(open("dist/themes.json"))
slugs = {e["slug"] for e in manifest}
on_disk = {os.path.basename(os.path.dirname(p)) for p in glob.glob("themes/*/theme.css")}
if slugs != on_disk:
    failures.append(f"manifest: dist/themes.json lists {sorted(slugs)} but themes/ has {sorted(on_disk)}")
for entry in manifest:
    if not entry["description"]:
        warn(entry["slug"], "manifest", "no `Description:` line in the theme header comment")
    if entry.get("dataTheme") != entry.get("slug"):
        fail(entry.get("slug", "?"), "manifest",
             f"dataTheme {entry.get('dataTheme')!r} != slug {entry.get('slug')!r} — "
             f"CONTRACT.md guarantees these are always equal")
    missing = [k for k in ("version", "scheme", "luminance", "hasChrome", "shellAware")
               if k not in entry]
    if missing:
        fail(entry.get("slug", "?"), "manifest", f"missing field(s): {', '.join(missing)}")
        continue
    scheme, lum = build_manifest.scheme_of(open(f"themes/{entry['slug']}/theme.css").read())
    if (entry["scheme"], entry["luminance"]) != (scheme, lum):
        fail(entry["slug"], "scheme",
             f"manifest says {entry['scheme']}/{entry['luminance']} but the theme "
             f"source re-derives to {scheme}/{lum} — rebuild the manifest, don't edit it")

# Staged copy must equal the fresh build (version is deterministic, so no
# carve-out is needed any more). A staged manifest predating the scheme
# fields is the one-time migration and is exempt.
staged_raw = subprocess.run(["git", "show", ":dist/themes.json"],
                            capture_output=True, text=True)
if staged_raw.returncode == 0:
    try:
        staged_manifest = json.loads(staged_raw.stdout)
        if any("scheme" not in e for e in staged_manifest):
            raise json.JSONDecodeError("pre-scheme format", "", 0)  # migration exempt
        if staged_manifest != manifest:
            failures.append("dist/themes.json: staged copy differs from a fresh build — "
                            "run scripts/build.sh and commit")
    except json.JSONDecodeError:
        pass  # staged copy predates this format; first migration is exempt

for w in warnings:
    print(f"warn  {w}")
for f in failures:
    print(f"FAIL  {f}")
print(f"\n{len(on_disk)} themes checked — {len(failures)} failure(s), {len(warnings)} warning(s)")
sys.exit(1 if failures else 0)
