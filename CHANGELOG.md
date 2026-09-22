# Changelog

Consuming apps pin `ftl-themes` as a git submodule, so breaking contract
changes are called out explicitly here.

## v3.3.0 — three more themes: Windows XP (Luna), Barbie, Hot Wheels

### Added

- **`winxp-luna`** — the default Luna Blue Windows XP desktop (glossy
  round-cornered blue title bar, tan/white content, Tahoma), distinct from
  the already-shipped `winxp-zune` reskin.
- **`barbie`** — hot-pink glamour: glossy pill chrome, gold sparkle
  headings, mint success state with dark-on-fill text.
- **`hot-wheels`** — blister-pack orange on track-black: a diagonal flame
  stripe across the app bar, a checkered-flag status strip, bold italic
  uppercase type.

All three ship a full `--ftl-app-*` layout personality (`shellAware:
true`), a `README.md`, and pass `scripts/check.py` at 0 failures / 0
warnings, including contrast: two of the three needed their accent one
shade darker than the "true" brand color to clear 4.5:1 against white fill
text (`winxp-luna`'s success green `#3d9f1e` → `#2e7a14`; `barbie`'s pink
`#e0218a` → `#c81b7a`) — noted inline in each theme's source so the
deviation from the brand reference is documented, not silent.

All additive, all inside individual themes or a single component's fixed
floor — no token or component contract changed shape.

### Fixed

- **`lcars` headings rendered in Trebuchet, not Antonio** (#8). Antonio is
  already shipped for the shell bar and readouts; `h1`-`h3` now lead with
  it too, so section titles stop reading as a second, unrelated theme next
  to the readouts.
- **`tron`'s cut-corner `clip-path` silently clipped the focus outline**
  (#9). `clip-path` clips everything the box paints, including core's
  `:focus-visible` outline — a keyboard user got no visible focus on
  buttons or panels, undetectable by `scripts/check.py`'s `outline: none`
  lint since nothing sets it to `none`. Added a `filter: drop-shadow(...)`
  focus treatment, which isn't clipped because it post-processes the
  already-cut shape. Also dropped `Eurostile, Orbitron` from the font
  stack: neither is vendored in `assets/`, so naming them just meant every
  real system silently rendered the generic-sans fallback while the stack
  claimed a face the theme doesn't ship.
- **`windows95`'s `--ftl-text` on `--ftl-bg` was 4.4:1, just under the
  4.5:1 floor** (#10). `--ftl-bg` moves from `#008080` to `#008282` — 2/255
  of extra green/blue, imperceptible on a decorative desktop backdrop that
  never carries body text, and the minimal change that crosses the floor.
  Real dialog contrast is unaffected: panels read `--ftl-surface`, not
  this token.
- **`.ftl-btn-go` had no minimum hit target** (#11): `--ftl-density`
  scaling (e.g. `cue-lab`'s `0.85` for a dense cue list) could shrink the
  one control every other element in a theme is allowed to compress
  around. Added a fixed `min-width`/`min-height: 44px` floor
  (`--ftl-go-min-target`) that density scaling cannot shrink — every other
  `.ftl-btn` in a theme keeps compressing freely.

## v3.2.0 — layout-tier themes degrade gracefully; adoption levels documented

Filed as ftl-themes#3 and #4 after real integrations (PI9696, CuTePi,
Playlist-Lab) all shipped as token-only: linking a layout-defining theme
like LCARS without adopting the `.ftl-app` shell produced "an orange-tinted
blue-future," not LCARS — technically correct, but not what "generic
project other apps can use easily" should mean without a documented path
to the real experience. All additive.

### Added

- **`.ftl-app-rail` degrades gracefully with no shell markup.**
  `core/ftl-layout.css`: `.ftl-app-rail:empty { display: none }` collapses
  a theme's decorative rail when the app added the element but left it
  empty (the documented, `aria-hidden`, no-content case); `.ftl-app:not(:has(>
  .ftl-app-rail))` collapses the column track itself when the app never
  added the element at all. Either way, a theme that opens a rail (LCARS,
  tron, wmp11, aqua, …) no longer paints an unexplained empty gutter in an
  app that hasn't adopted the shell — it just quietly doesn't reserve the
  space, per CONTRACT.md's new degrade rule: *a theme must not look broken
  one level down from what it was authored for*.
- **CONTRACT.md "Adoption levels"**: formalizes L0 (tokens only — today's
  actual state for every sibling app), L1 (the `.ftl-app` shell — layout-
  tier theming), L2 (theme-specific chrome or full `.ftl-*` component
  adoption), replacing the previous informal "adopting the shell is
  optional" note with an explicit, named ladder an integrator can point at.
- **`shellAware` field on every `dist/themes.json` entry** — `true` when a
  theme sets any `--ftl-app-*` property (the same detection
  `scripts/check.py`'s existing `layout` warning already used), so a
  picker can tell the user up front that a theme's full intent needs L1,
  instead of them discovering the gap after linking it.
- **A "Requires" note in every theme's `README.md`** naming what's lost at
  L0 and pointing at CONTRACT.md's "Adoption levels" for the fix.
- **`demo.html` L0/L1 toggle** — unchecking "App shell" strips the
  `.ftl-app*` classes from the same elements live, so the fidelity gap is
  visible in the one place a theme is meant to be evaluated, rather than
  only discoverable after a real app integration.

## v3.1.1 — contract gaps found by the first real integration

CuTePi's integration (DrEVILish/CuTePi#1) surfaced six gaps between what
the contract implied and what it actually guaranteed. All additive; no
existing field changed shape.

### Added

- **`dataTheme` field on every `dist/themes.json` entry**, explicitly equal
  to `slug` — CONTRACT.md already guaranteed this by construction, but an
  integrator had to infer or verify it themselves. Use `dataTheme`, not
  `slug`, when building a picker id.
- **`version`/`builtAt` on every manifest entry**, from `scripts/build.sh`
  (`git describe` + UTC timestamp). Since dist bundles inline the core
  component structure, every core change touches every theme's file — this
  is how an integrator confirms which build a deployment is actually
  serving. `scripts/check.py`'s dist-sync check now diffs `themes.json`'s
  content *excluding* these two fields (they legitimately change on every
  rebuild) while still failing on any other drift.
- **`dist/ftl-core.css`** — the reset + `.ftl-*` component structure alone,
  no theme, no app shell. For an app doing colour-only adoption (a token
  bridge onto its own existing classes, no `.ftl-*` markup) that doesn't
  want to load a full theme bundle just to get the component CSS it will
  never use. See CONTRACT.md "Color-only adoption".
- **CONTRACT.md**: a "Cache-busting" section recommending `?v=<manifest
  version>`, so family apps stop each inventing their own scheme (CuTePi's
  binary-mtime scheme predates this and still works — this just gives the
  next app a documented default); an "Avoiding name collisions with an
  app's own themes" section documenting the qualified-picker-id pattern
  (`app:lcars` / `ftl:lcars`) CuTePi had to invent from scratch; and the
  sibling-asset-serving requirement (previously a paragraph under "Serving
  the assets") promoted and spelled out as load-bearing, not incidental.

## v3.1.0 — palette variants, accent swatches, display options, 10 new themes

### Added

- **Palette variants** (`data-variant`) — a theme may ship more than one
  colorway under one identity, selected by an extra attribute on the
  theme's own selector (`html[data-theme="x"][data-variant="y"]`, which at
  specificity `(0,2,1)` outranks the theme's `(0,1,1)` root block, so no
  core mechanism is needed). `imac-g3` ships Bondi Blue (default) plus
  Blueberry/Grape/Tangerine.
- **Accent swatches** (`data-accent="1".."6"`) — a theme may offer curated,
  contrast-checked alternate accents as `--ftl-accent-swatch-<n>` /
  `--ftl-on-accent-swatch-<n>` pairs; core reads whichever the theme
  defines. This is the supported replacement for a "paste your own theme
  JSON" feature: every swatch is a colour the theme's author vouched for.
- **User display options**, independent of theme choice: a density
  override via inline style (`<html style="--ftl-density: 0.85">`, which
  wins over any stylesheet regardless of specificity); `data-motion`
  (`"reduced"`) to force animations/transitions off from an in-app toggle,
  not just the OS setting; `data-contrast` (`"high"`) to pull
  `--ftl-hairline`/`--ftl-muted` up to `--ftl-border`/`--ftl-text` and
  thicken the focus ring, without leaving the theme.
- **Ten new themes**: `imac-g3`, `winxp-zune`, `msdos`, `pipboy`, `nerv`,
  `aperture`, `death-star`, `lego-classic`, `steampunk`, `cyber-goth` —
  each with a `README.md`, contrast-checked, and given a distinct
  `--ftl-app-*` layout personality.

## v3.0.0 — themes control layout; instrument primitives; theme docs

### Added

- **The app shell (`core/ftl-layout.css`).** A theme is a layout as much as
  a palette. One markup contract — `.ftl-app` + `.ftl-app-bar` +
  `.ftl-app-rail` + `.ftl-app-main` + `.ftl-app-status` — which every theme
  re-arranges through `--ftl-app-*` properties, so switching theme moves the
  furniture instead of only recolouring it. LCARS opens a 6rem candy rail
  and elbows its sweep bar into it; blue-future runs edge-to-edge with no
  rail; Aqua and WMP11 become floating rounded windows; Windows 95 and
  WinAmp become beveled window chrome. The rail is decorative and painted
  in CSS, so no app ships theme-specific markup. Adopting the shell is
  optional.
- **Instrument primitives**: `.ftl-meter` (+ `.ftl-meter-v`, peak hold,
  tokenised band thresholds), `.ftl-readout` (+ `-lg`/`-sm`/`-unit`),
  `.ftl-transport` + `.ftl-btn-go`, and `.ftl-lamp`. These exist because the
  themes here are control surfaces — a recorder, a show console, a starship
  computer — and a palette alone cannot express that.
- **`--ftl-density`** — scales button, table-cell and panel padding.
  `cue-lab` sets `0.85` (fit the cue list), `lcars` sets `1.15` (wall panel).
- **A `README.md` beside every theme's CSS**, stating what that theme is
  trying to achieve: the reference, its core values, why the significant
  token values are what they are, what not to change, and the tell-tales of
  an inauthentic result. The lint now fails a theme that has none.
- Lint rules for the two above: `docs` (README present, with the expected
  sections) and `layout` (warns when a theme defines no `--ftl-app-*`
  personality).

### Changed

- **`blue-future`'s palette is reconciled against its reference device**
  rather than approximating it: `--ftl-accent` `#2fd6ff`→`#00d9ff`,
  `--ftl-border` `#176095`→`#0f3a5c`, `--ftl-surface` `#07172a`→`#0a1526`,
  `--ftl-text` `#dff4ff`→`#cfeeff`, `--ftl-muted` `#7ca6c3`→`#5b8aa8`,
  `--ftl-danger` `#ff5f87`→`#ff3355`, `--ftl-success` `#42ddb2`→`#2bffb0`,
  `--ftl-warning` → `#ff8c1a`, and the font stack leads with Consolas.
  Apps that used the old values will see a slight shift.
- `themes/lcars/chrome.css` is demoted to the optional richer frame; the
  shell is the default path. The Antonio `@font-face` moved into
  `theme.css`, since the shell's bar and the readouts both use it.
- `demo.html` is built on the shell, so the theme switcher demonstrates the
  layout change, and exercises the instrument primitives.

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
