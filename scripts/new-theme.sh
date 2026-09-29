#!/usr/bin/env bash
# Scaffolds themes/<slug>/theme.css from a template listing every required
# --* token and the component override points most themes reach for, so
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
 * version: set component look through the --<component>-* properties in
 * the root block below. Declaring background/color on a base component
 * selector (html[data-theme="$slug"] .btn) outranks core's variant rules
 * and erases them — scripts/check.sh will fail the build if you do.
 */

html[data-theme="$slug"] {
  /* --- Required tokens (all of them; the lint fails on omissions) ------ */
  --bg: #000000;          /* page backdrop */
  --surface: #111111;     /* panels/cards — where body text sits */
  --surface-2: #1a1a1a;   /* inputs, menus, recessed areas */
  --border: #333333;
  --hairline: #222222;    /* quieter than border: row rules */
  --text: #ffffff;
  --muted: #999999;
  --accent: #ffffff;      /* primary interactive color */
  --accent-2: #cccccc;
  --danger: #ff4d4d;
  --success: #4dff88;
  --warning: #ffcc4d;
  /* Foregrounds for the fills above. Must hit 4.5:1 against them. */
  --on-accent: #000000;
  --on-danger: #000000;
  --on-success: #000000;
  --radius: 0.25rem;      /* 0 for a sharp-cornered theme */
  --font: sans-serif;
  --font-mono: monospace;
  --flare: #ffffff;       /* the one "extra" decorative color */
  /* Required by the lint: tells the browser which palette UA-owned chrome
     (scrollbars, native pickers, autofill) should match. */
  color-scheme: dark;         /* light for a light palette */

  /* --- Optional: component look. Delete what you don't need. ---------- *
   * Full set of override points: every var(--…, fallback) in
   * core/core.css. Common ones: */
  /* --btn-bg: transparent; */
  /* --btn-fg: var(--accent); */
  /* --btn-radius: 0; */
  /* --btn-transform: uppercase; */
  /* --btn-shadow-hover: 0 0 10px var(--accent); */
  /* --input-bg: #000; */
  /* --focus-ring: 0 0 8px var(--accent); */
  /* --panel-bg: linear-gradient(180deg, #1a1a1a, #111); */
  /* --panel-shadow: 0 4px 14px rgba(0,0,0,0.4); */
  /* --table-head-bg: var(--surface-2); */
  /* --row-selected-bg: rgba(255,255,255,0.12); */
  /* --nav-bg: #000; */
  /* --overlay-bg: rgba(0,0,0,0.7); */
  /* --indicator-fg: var(--accent); */
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
/* html[data-theme="$slug"] .btn { clip-path: …; } */

/* Optional: per-variant tweaks belong on the variant selector. */
/* html[data-theme="$slug"] .btn-danger { --btn-border: …; } */
EOF

# check.sh fails a theme without a README carrying a Requires: badge, and
# warns on each missing section — scaffold them so the author fills in
# prose instead of discovering the rules one lint run at a time.
cat > "$dir/README.md" <<'EOF'
# <Display Name>

> <one line: the look this theme reproduces>

**Requires: L0** — tokens only; change to L1 once the theme sets `--app-*`
layout properties. See CONTRACT.md "Adoption levels".

## What this theme is trying to achieve

<the reference look, and what makes it recognisable>

## Core values

1. <a principle the next contributor must not "improve" away>

## Signature details

- <a concrete, checkable detail>

## Tell-tales of an inauthentic result

- <what a wrong rendering of this theme looks like>
EOF

cat > "$dir/icons.svg" <<EOF
<!-- $slug icon overrides.
     Optional: every theme falls back to the generic icon set (1,000+ icons) at
     assets/icons/icons.svg for any id it doesn't redraw here. Only add a
     <symbol> below when this theme's signature look genuinely calls for a
     different silhouette (e.g. block-graphics, brand-specific glyphs) —
     most themes don't need to override anything.
     Pattern and full id list: docs/icon-library-roadmap.md. Ids must match
     the generic set's icon-<name> convention exactly, or the build fails
     (an override must replace an id that exists in the generic set). See
     themes/aqua/icons.svg or themes/lego-classic/icons.svg for worked
     examples of the convention: viewBox="0 0 24 24", stroke-based paths
     using currentColor, fill/stroke-width driven by the icon-* tokens
     unless a specific stroke-width is being set deliberately. -->
<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
  <defs>
    <!-- <symbol id="icon-home" viewBox="0 0 24 24">
      <path d="M3 11.5 12 4l9 7.5"/>
    </symbol> -->
    <!-- <symbol id="icon-settings" viewBox="0 0 24 24">
      <circle cx="12" cy="12" r="8"/>
    </symbol> -->
    <!-- <symbol id="icon-close" viewBox="0 0 24 24">
      <path d="M17 7 7 17"/>
      <path d="M7 7l10 10"/>
    </symbol> -->
  </defs>
</svg>
EOF

echo "scaffolded themes/$slug/theme.css, themes/$slug/README.md and themes/$slug/icons.svg"
echo
echo "next:"
echo "  1. fill in the tokens (and a Theme-Name/Description in the header) and README.md"
echo "  2. (optional) uncomment/add <symbol> overrides in icons.svg for this theme's signature icons"
echo "  3. scripts/build.sh    # regenerates dist/$slug.css and dist/themes.json"
echo "  4. scripts/check.sh    # token completeness, contrast, focus, variants"
echo "  5. open components.html and pick your theme from the switcher"
echo "  6. add a row to CONTRACT.md's theme index"
