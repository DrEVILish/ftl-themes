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
             light palettes; --ftl-on-* exist to prevent it.
  dist       committed bundles must match a fresh build, since submodule
             consumers cannot run the build themselves.
  docs       a theme without a stated intent gets "improved" into a different
             theme by the next contributor. Requires "Signature details" too,
             not just "Core values" — that's the section example.html's
             compare mode surfaces, and 11 themes shipped without it before
             a v3.5.1 pass caught the gap.
  layout     a theme is a layout as much as a palette; one that sets no
             --ftl-app-* property renders in the default arrangement.
"""
import glob
import json
import os
import re
import subprocess
import sys

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


def rules_of(css):
    """[(selector, body)] for every comma-split selector, comments removed."""
    out = []
    for m in re.finditer(r"([^{}@]+)\{([^{}]*)\}", strip_comments(css)):
        for sel in m.group(1).split(","):
            out.append((sel.strip(), m.group(2)))
    return out


def srgb(hexs):
    h = hexs.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def luminance(rgb):
    def chan(c):
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (chan(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = luminance(srgb(a)), luminance(srgb(b))
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def resolve(tokens, value, depth=0):
    """Resolve a token value down to a literal hex color, if it is one."""
    value = value.strip()
    if depth > 6:
        return None
    if value.startswith("#"):
        return value
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

    # Contrast floor for filled controls, using the theme's own token values.
    # Text is checked against --ftl-surface, the substrate it actually sits
    # on (panels, cards, modals). --ftl-bg can legitimately be a decorative
    # backdrop that never carries body text — Windows 95's teal desktop is
    # the canonical case — so failing text against it would be wrong; it's
    # reported as a warning instead.
    for label, fg_tok, bg_tok, floor, hard in (
        ("primary button", "on-accent", "accent", 4.5, True),
        ("danger button", "on-danger", "danger", 4.5, True),
        ("success button", "on-success", "success", 4.5, True),
        ("body text", "text", "surface", 4.5, True),
        ("muted text", "muted", "surface", 3.0, True),
        ("body text on page backdrop", "text", "bg", 4.5, False),
    ):
        fg = resolve(tokens, tokens.get(fg_tok, ""))
        bg = resolve(tokens, tokens.get(bg_tok, ""))
        if not (fg and bg):
            continue
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

    # Every theme states its intent in prose beside its CSS: what look it is
    # reproducing, its core values, and how to tell an inauthentic result.
    # A palette without that context gets "improved" into something else.
    readme = os.path.join(os.path.dirname(path), "README.md")
    if not os.path.exists(readme):
        fail(theme, "docs", "no README.md beside theme.css — every theme documents "
                            "what it is trying to achieve (see any existing theme)")
    else:
        text = open(readme).read()
        # "Signature details" specifically (not just Core values) is what
        # example.html's compare mode surfaces — a theme missing it isn't
        # broken, but it's invisible to that tool, so the same soft warning
        # applies here as to the other structural sections.
        for heading in ("What this theme is trying to achieve", "Core values", "Signature details"):
            if heading.lower() not in text.lower():
                warn(theme, "docs", f"README.md has no '{heading}' section")

    # A theme is a layout as much as a palette — switching to one should move
    # the furniture, not only recolor it. Themes that set no --ftl-app-*
    # property render in the shell's default arrangement, which is legitimate
    # but usually means the layout pass was forgotten.
    if not re.search(r"--ftl-app-[\w-]+\s*:", body):
        warn(theme, "layout", "defines no --ftl-app-* layout personality — the app "
                              "shell will look identical to every other such theme")

# dist/ must match a fresh build — except dist/themes.json, whose version/
# builtAt fields are expected to differ on every single build by design (see
# below) and would otherwise fail this check even when nothing meaningful
# changed.
subprocess.run(["scripts/build.sh"], check=True, stdout=subprocess.DEVNULL)
diff = subprocess.run(["git", "diff", "--name-only", "--", "dist", ":!dist/themes.json"],
                      capture_output=True, text=True).stdout.split()
if diff:
    failures.append("dist: committed bundles are stale — run scripts/build.sh and commit "
                    f"({', '.join(diff)})")

# The manifest must list every theme, and each entry must carry the fields
# integrators actually rely on: dataTheme (guaranteed equal to slug — spelled
# out per-entry anyway, per CONTRACT.md "dataTheme"), a hasChrome flag, and
# build identity. Content other than version/builtAt is compared against the
# staged copy, since those two fields legitimately differ on every rebuild.
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
    if "version" not in entry or "builtAt" not in entry:
        fail(entry.get("slug", "?"), "manifest", "missing version/builtAt")
    if "shellAware" not in entry:
        fail(entry.get("slug", "?"), "manifest", "missing shellAware")

def _without_build_identity(entries):
    return [{k: v for k, v in e.items() if k not in ("version", "builtAt")} for e in entries]

staged_raw = subprocess.run(["git", "show", ":dist/themes.json"],
                            capture_output=True, text=True)
if staged_raw.returncode == 0:
    try:
        staged_manifest = json.loads(staged_raw.stdout)
        if _without_build_identity(staged_manifest) != _without_build_identity(manifest):
            failures.append("dist/themes.json: staged content differs from a fresh build "
                            "(beyond version/builtAt) — run scripts/build.sh and commit")
    except json.JSONDecodeError:
        pass  # staged copy predates this format; first migration is exempt

for w in warnings:
    print(f"warn  {w}")
for f in failures:
    print(f"FAIL  {f}")
print(f"\n{len(on_disk)} themes checked — {len(failures)} failure(s), {len(warnings)} warning(s)")
sys.exit(1 if failures else 0)
