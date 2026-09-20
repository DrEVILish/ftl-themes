#!/usr/bin/env bash
# Scaffolds themes/<slug>/theme.css from a template listing every required
# --ftl-* token and the component override points most themes reach for, so
# authoring a theme is "fill in the blanks".
# Usage: scripts/new-theme.sh <theme-slug>
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
slug="${1:-}"

if [ -z "$slug" ]; then
  echo "usage: $0 <theme-slug>  (e.g. hot-wheels)" >&2
  exit 1
fi
if ! printf '%s' "$slug" | grep -qE '^[a-z0-9]+(-[a-z0-9]+)*$'; then
  echo "slug must be lowercase kebab-case (letters, digits, hyphens)" >&2
  exit 1
fi

dir="$root/themes/$slug"
if [ -e "$dir" ]; then
  echo "themes/$slug already exists" >&2
  exit 1
fi

mkdir -p "$dir"

cat > "$dir/theme.css" <<EOF
/* ftl-themes: <Display Name>
 * Theme-Name: <Display Name>
 * Description: <one line — this becomes the theme's entry in dist/themes.json>
 *
 * Read CONTRACT.md § "How a theme overrides a component" first. The short
 * version: set component look through the --ftl-<component>-* properties in
 * the root block below. Declaring background/color on a base component
 * selector (html[data-theme="$slug"] .ftl-btn) outranks core's variant rules
 * and erases them — scripts/check.sh will fail the build if you do.
 */

html[data-theme="$slug"] {
  /* --- Required tokens (all of them; the lint fails on omissions) ------ */
  --ftl-bg: #000000;          /* page backdrop */
  --ftl-surface: #111111;     /* panels/cards — where body text sits */
  --ftl-surface-2: #1a1a1a;   /* inputs, menus, recessed areas */
  --ftl-border: #333333;
  --ftl-hairline: #222222;    /* quieter than border: row rules */
  --ftl-text: #ffffff;
  --ftl-muted: #999999;
  --ftl-accent: #ffffff;      /* primary interactive color */
  --ftl-accent-2: #cccccc;
  --ftl-danger: #ff4d4d;
  --ftl-success: #4dff88;
  --ftl-warning: #ffcc4d;
  /* Foregrounds for the fills above. Must hit 4.5:1 against them. */
  --ftl-on-accent: #000000;
  --ftl-on-danger: #000000;
  --ftl-on-success: #000000;
  --ftl-radius: 0.25rem;      /* 0 for a sharp-cornered theme */
  --ftl-font: sans-serif;
  --ftl-font-mono: monospace;
  --ftl-flare: #ffffff;       /* the one "extra" decorative color */

  /* --- Optional: component look. Delete what you don't need. ---------- *
   * Full set of override points: every var(--ftl-…, fallback) in
   * core/ftl-core.css. Common ones: */
  /* --ftl-btn-bg: transparent; */
  /* --ftl-btn-fg: var(--ftl-accent); */
  /* --ftl-btn-radius: 0; */
  /* --ftl-btn-transform: uppercase; */
  /* --ftl-btn-shadow-hover: 0 0 10px var(--ftl-accent); */
  /* --ftl-input-bg: #000; */
  /* --ftl-focus-ring: 0 0 8px var(--ftl-accent); */
  /* --ftl-panel-bg: linear-gradient(180deg, #1a1a1a, #111); */
  /* --ftl-panel-shadow: 0 4px 14px rgba(0,0,0,0.4); */
  /* --ftl-table-head-bg: var(--ftl-surface-2); */
  /* --ftl-row-selected-bg: rgba(255,255,255,0.12); */
  /* --ftl-nav-bg: #000; */
  /* --ftl-overlay-bg: rgba(0,0,0,0.7); */
  /* --ftl-indicator-fg: var(--ftl-accent); */
}

/* Optional: page background treatment (gradient, grid, texture). */
/* html[data-theme="$slug"] { background-image: …; } */

/* Optional: heading voice (case, tracking, weight, glow). */
/* html[data-theme="$slug"] h1,
   html[data-theme="$slug"] h2,
   html[data-theme="$slug"] h3 { text-transform: uppercase; } */

/* Optional: shape-only overrides are safe on base selectors — radius,
   clip-path, bevel border-color, letter-spacing. Only background/color are
   forbidden there (they'd erase the variants). */
/* html[data-theme="$slug"] .ftl-btn { clip-path: …; } */

/* Optional: per-variant tweaks belong on the variant selector. */
/* html[data-theme="$slug"] .ftl-btn-danger { --ftl-btn-border: …; } */
EOF

echo "scaffolded themes/$slug/theme.css"
echo
echo "next:"
echo "  1. fill in the tokens (and a Theme-Name/Description in the header)"
echo "  2. scripts/build.sh    # regenerates dist/$slug.css and dist/themes.json"
echo "  3. scripts/check.sh    # token completeness, contrast, focus, variants"
echo "  4. open demo.html and pick your theme from the switcher"
echo "  5. add a row to CONTRACT.md's theme index"
