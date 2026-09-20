# Changelog

Consuming apps pin `ftl-themes` as a git submodule, so breaking contract
changes are called out explicitly here.

## v2.0.0 — app-agnostic contract, hardened

### Breaking

- **`--ctp-*` tokens renamed to `--ftl-*`.** An app bridging its own tokens
  must update its alias block.
- **Bootstrap class names dropped.** Themes no longer style `.btn`,
  `.form-control`, `.table-dark`, `.navbar`, `.modal-content`; the
  vocabulary is now `.ftl-*` (see `CONTRACT.md`). An app can bridge by
  aliasing tokens and adopting the `.ftl-*` classes incrementally.
- **All app-specific selectors removed.** Nothing in this repo references
  any particular application's markup any more.
- **New required tokens**: `--ftl-on-accent`, `--ftl-on-danger`,
  `--ftl-on-success`. A theme omitting them now fails the lint.
- **Themes must set component look via `--ftl-<component>-*` at root
  scope**, not by declaring `background`/`color` on base component
  selectors. See the fix below for why.

### Fixed

- **Button variants were silently erased in 6 of 9 themes.** A theme's
  `html[data-theme="x"] .ftl-btn` rule (specificity 0,2,1) outranked core's
  unscoped `.ftl-btn-danger` (0,1,0), so semantic fills never applied — a
  delete button rendered identically to a normal one in `matrix`, `tron`,
  `winamp-classic` and `wmp11`. Components now read local custom properties
  with inline fallbacks, and variants set those properties on the element,
  where a declaration always beats an inherited one regardless of
  specificity. Verified: all 9 themes now resolve their semantic fills.
- **The LCARS display font never loaded** — the vendored Antonio files had
  no `@font-face` rule. Added, and `scripts/build.sh` now rewrites relative
  asset URLs for the `dist/` bundles so they resolve from there.
- **Invalid `border-radius` in the LCARS chrome** (a comma-separated list,
  which browsers drop whole) replaced with a valid shorthand.
- **`windows95` inputs had no focus indicator**: the theme set
  `outline: none` and replaced it with a `box-shadow` identical to its
  resting state. Core now always draws the outline; themes recolor it via
  `--ftl-focus` or add a glow via `--ftl-focus-ring`.
- **`cue-lab`'s `* { box-shadow: none !important }`** also erased
  `.ftl-table tr.is-active`'s row marker. "Flat" is now expressed by
  leaving shadow properties unset; row states additionally carry a
  background so no single language is load-bearing.
- **Contrast failures** in `aqua` (primary), `cue-lab` (danger) and `lcars`
  (danger) — palettes adjusted to clear 4.5:1.
- **Core's achromatic fallbacks**: were the blue-future palette, so a theme
  with a missing token inherited a plausible-looking dark navy that went
  invisible on light themes. Now obviously-wrong grays.

### Added

- `scripts/check.sh` — contract lint (token completeness, the variant rule,
  focus indicators, universal `!important`, contrast floors, stale `dist/`,
  manifest sync), run in CI by `.github/workflows/ci.yml`. Every rule maps
  to a bug in the "Fixed" list above.
- `dist/themes.json` — machine-readable theme index, so apps and `demo.html`
  stop hardcoding or scraping the theme list.
- **htmx state styling**: `.ftl-indicator`, plus `.htmx-request`,
  `.htmx-swapping`, `.htmx-added` and `.htmx-settling` treatments, themeable
  per theme. Previously every consuming app would have hand-rolled this.
- **New components**: `.ftl-modal-overlay` (was left to each app to
  reinvent), `.ftl-tabs`/`.ftl-tab`, `.ftl-label`/`.ftl-field`/
  `.ftl-field-hint`, `.ftl-textarea`, `.ftl-toolbar`, `.ftl-panel-header`,
  and the `.ftl-mono` tabular-numerals utility.
- Six new themes: `windows95`, `matrix`, `tron`, `aqua`, `winamp-classic`,
  `wmp11`.
- `demo.html` now builds its switcher from the manifest, exercises every
  component including htmx states, and has a `?chrome=1` mode that renders
  the LCARS chrome primitive.
- `docs/theme-backlog.md`, `docs/lcars-chrome.md`, `docs/authoring-a-theme.md`,
  `scripts/new-theme.sh`.
- `color-mix()` uses are now behind `@supports` with flat-color fallbacks.

### Known issues

- `windows95`'s body text on its teal *page backdrop* is 4.4:1 (the lint
  warns). Text in that theme sits on `#c0c0c0` panels at 11.5:1; the teal is
  a decorative desktop color that carries no body text, which is why this is
  a warning rather than a failure.
- `windows95` and `tron` name reference fonts (MS Sans Serif, Eurostile)
  that aren't web-available and fall back. Vendoring open substitutes is
  tracked in `docs/theme-backlog.md`.
