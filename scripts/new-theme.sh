#!/usr/bin/env bash
# Scaffolds themes/<name>/theme.css from a template listing every --ftl-*
# token and the components most themes end up touching, so authoring a
# theme is "fill in the blanks" rather than starting from a blank file.
# Usage: scripts/new-theme.sh <theme-slug>
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
slug="${1:-}"

if [ -z "$slug" ]; then
  echo "usage: $0 <theme-slug>  (e.g. hot-wheels)" >&2
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
 * One line describing the visual reference this theme is styled after.
 * See CONTRACT.md for what each token/component controls before filling
 * these in — copy an existing theme under themes/ for a worked example
 * close to what you're building.
 */

html[data-theme="$slug"] {
  --ftl-bg: #000000;
  --ftl-surface: #111111;
  --ftl-surface-2: #1a1a1a;
  --ftl-border: #333333;
  --ftl-hairline: #222222;
  --ftl-text: #ffffff;
  --ftl-muted: #999999;
  --ftl-accent: #ffffff;
  --ftl-accent-2: #cccccc;
  --ftl-danger: #ff4d4d;
  --ftl-success: #4dff88;
  --ftl-warning: #ffcc4d;
  --ftl-radius: 0.25rem;
  --ftl-font: sans-serif;
  --ftl-font-mono: monospace;
  --ftl-flare: #ffffff;
}

/* Optional: page-level background treatment (gradient, grid, texture). */
html[data-theme="$slug"] {
}

/* Optional: heading voice (case, tracking, weight, glow). */
html[data-theme="$slug"] h1,
html[data-theme="$slug"] h2,
html[data-theme="$slug"] h3 {
}

/* .ftl-btn / .ftl-btn-primary / .ftl-btn-secondary / .ftl-btn-danger --
   override shape/look beyond the token defaults if this theme's buttons
   need more than a recolor (bevels, gloss, clip-path corners, ...). */
html[data-theme="$slug"] .ftl-btn {
}

/* .ftl-panel / .ftl-modal / .ftl-dropdown -- surfaces. */
html[data-theme="$slug"] .ftl-panel,
html[data-theme="$slug"] .ftl-modal,
html[data-theme="$slug"] .ftl-dropdown {
}

/* .ftl-input / .ftl-select -- form controls. */
html[data-theme="$slug"] .ftl-input,
html[data-theme="$slug"] .ftl-select {
}

/* .ftl-table -- header/row treatment. */
html[data-theme="$slug"] .ftl-table th {
}

/* .ftl-nav -- top bar. */
html[data-theme="$slug"] .ftl-nav {
}
EOF

echo "scaffolded themes/$slug/theme.css"
echo "next: fill in the tokens/overrides, then run scripts/build.sh"
echo "add a row for it to CONTRACT.md's theme index and to demo.html's theme list"
