# Changelog

Consuming apps pin `ftl-themes` as a git submodule, so breaking contract
changes are called out explicitly here.

## v3.7.0 — segmented control, sortable/sticky tables, remaining chrome gaps

Closes out the backlog flagged alongside v3.6.0: a component pattern
common enough to add speculatively (segmented control), two `.ftl-table`
hooks a data-heavy consumer will need, and the three browser-chrome
surfaces v3.6.0 didn't reach (native `<select>`'s closed-box arrow,
autofill, native `<dialog>`'s `::backdrop`). All additive, all
token-driven with base-token fallbacks.

### Added

- **`.ftl-segmented`** (+ `.ftl-segmented-item`, `.is-active`) — a
  segmented control / toggle group for mutually-exclusive view switches,
  distinct from `.ftl-tabs` (navigates) and `.ftl-badge-button`
  (multi-select filter chips).
- **`.ftl-table` sticky header** — `.ftl-table.is-sticky thead th` pins
  the header within the table's own scroll container.
- **`.ftl-table` sort indicator** — a clickable cursor, hover tint, and
  themed arrow on any `<th aria-sort="ascending"/"descending">`, reusing
  the attribute a screen reader already wants rather than adding a
  parallel `.is-sorted` class.
- **`.ftl-select` closed-box arrow** now themed via a CSS-triangle
  (`--ftl-select-arrow-fg`, default `--ftl-muted`) instead of the
  browser's own. The open dropdown list stays native OS chrome — no CSS
  can reach it.
- **Autofill** on `.ftl-input` now respects `--ftl-input-bg`/`-fg`
  instead of the browser's forced yellow/blue fill.
- **`dialog.ftl-modal::backdrop`** themed via `--ftl-overlay-bg`/`-blur`,
  for apps using the native `<dialog>` element instead of the
  `.ftl-modal-overlay` div pattern.

## v3.6.0 — browser-chrome theming

Closes the gap between "every `.ftl-*` component is themed" and "the whole
page looks themed": platform-painted surfaces (text selection, scrollbars,
form placeholder text, the input caret, `<kbd>`/`<code>`/`<pre>`) previously
fell back to the browser's own default appearance regardless of theme,
which was the most visible remaining "generic browser" tell in an
otherwise fully-themed retro/console page. All additive, all token-driven
with base-token fallbacks — no theme file needs to change to pick these up.

### Added

- **`::selection`** now themed (`--ftl-selection-bg`/`-fg`, default accent /
  on-accent).
- **Scrollbars** themed via `scrollbar-color`/`scrollbar-width` (Firefox)
  and the `::-webkit-scrollbar*` pseudo-elements (Chromium/Safari):
  `--ftl-scrollbar-thumb` (default `--ftl-border`), `-thumb-hover` (default
  `--ftl-accent`), `-track` (default transparent), `-size`, `-radius`,
  `-width`.
- **`::placeholder`** on `.ftl-input`/`.ftl-textarea` (`--ftl-input-placeholder`,
  default `--ftl-muted`) — previously always the browser's own gray.
- **Input caret color** (`--ftl-input-caret`, default `--ftl-focus`).
- **`<kbd>`** — a themed inline keyboard-shortcut glyph
  (`--ftl-kbd-bg`/`-fg`/`-border`/`-radius`/`-shadow`).
- **`<code>`/`<pre>`** — themed inline and block code
  (`--ftl-code-bg`/`-fg`, `--ftl-code-block-bg`/`-border`), distinct from
  `.ftl-readout` (a live machine value) and `.ftl-mono` (a bare
  font-family utility).

## v3.5.2 — consumer-reported fixes: color-scheme, density-scaled targets, offline lint

Addresses issues filed from real integration work in CuTePi, PI9696, and
Playlist Lab.

### Added

- **`color-scheme` per theme** (#21). Every theme's root block now
  declares `color-scheme: light;`/`dark;` matching its palette, judged
  from `--ftl-surface` (the substrate that actually carries content, not
  `--ftl-bg`, which can be purely decorative — windows95's teal desktop
  is the case that mattered here). UA-owned chrome (scrollbars, native
  date/time pickers, autofill) now matches instead of defaulting to light
  under every dark theme. `scripts/check.py` fails a theme with zero or
  more than one declaration. Themes still don't respond to
  `prefers-color-scheme` — this only declares what they already are.
- **`--ftl-density` now scales interactive targets** (#26): `.ftl-checkbox`,
  `.ftl-switch`, and `.ftl-slider`'s thumb size with density, not just
  padding. A touch-first theme at density 1.15+ gets bigger grab targets
  to match its roomier spacing. Default density renders byte-identical to
  before; per-part tokens (`--ftl-switch-*`, `--ftl-slider-thumb-size`)
  still override.
- **`.ftl-badge-warning`** (#19) — the fourth severity variant, matching
  `-accent`/`-danger`/`-success`.
- **Lint: no remote URLs** (#25). `scripts/check.py` now fails any theme
  or core file containing a remote `url(...)` or `@import` — a
  field-offline consumer embeds the bundles specifically so the UI works
  with zero network access; one remote reference upstream would silently
  break that guarantee.
- **"Requires: L0/L1" badge rolled out to all 26 READMEs** (#18), all
  `Requires: L1` (every current theme sets `--ftl-app-*`). The lint is
  promoted from warn to fail now that the rollout is complete.

### Verified already fixed (stale issue reports)

Issues #8 (LCARS headings), #9 (TRON focus-outline clipping), #10
(windows95 body-text contrast), and #11 (cue-lab GO min-target) were
already resolved in an earlier pass — confirmed against current source,
no further change needed.

## v3.5.1 — compare mode, signature-detail pass, source-accuracy fixes

### Added

- **`example.html` compare mode.** Pick two themes and see both rendered
  full-width side by side (each an embedded copy of the page itself), with
  each theme's "Signature details" pulled from its README into the
  sidebar for a read-without-scrolling comparison. Deep-linkable via
  `?compare=1&a=<slug>&b=<slug>`.
- **`docs/engine-improvements.md`** — a written set of recommendations
  from this review pass: what was implemented, what's deferred and why
  (visual regression testing, a token-diff tool, a per-theme token-usage
  report), and what was deliberately rejected (an authenticity "score",
  auto-generating READMEs from CSS).
- Every theme's README now has a "Signature details" section (11 of 26
  didn't); `scripts/check.py`'s docs rule now warns if a new theme ships
  without one, since that's the section compare mode surfaces.

### Changed

- Every theme's one-line `Description:` (feeds `dist/themes.json` and
  theme pickers) now names a concrete signature detail instead of a
  generic palette summary. `CONTRACT.md`'s theme index rewritten
  accordingly, with a new "Signature detail" column.
- **`lcars`**: `--ftl-lcars-sky` corrected from an unsourced pastel
  periwinkle (`#9999ff`) to `#6699ff`, closer to the Okuda reference
  palette's documented blue family ("mariner"/"bahama-blue") while
  staying inside the button-text contrast floor (the literal reference
  blue fails at 3.9:1). `--ftl-accent` and `--ftl-lcars-lavender` were
  verified exact matches to the reference and needed no change.
- **`winxp-luna`**: softened an overclaiming comment about the Start-button
  green being "the actual" color to "the commonly cited" one — no single
  hex was ever an officially published constant.

## v3.5.0 — five more themes: Windows 7 Aero, Alienware, Vaporwave, Material, Bloomberg Terminal

### Added

- **`win7-aero`** — frosted glass via real `backdrop-filter` blur over the
  Aero blue desktop gradient, distinct from `winxp-luna`'s opaque gloss.
- **`alienware`** — matte black, angular `clip-path`-cut corners (reusing
  tron's clipped-focus workaround), a single AlienFX cyan glow.
- **`vaporwave`** — outrun synthwave: magenta/cyan gradient chrome text,
  deep-purple void, perspective grid-floor status strip.
- **`material`** — Google Material Design: flat color, layered elevation
  `box-shadow` stacks instead of gloss/blur, underlined text fields.
- **`bloomberg`** — black-and-amber monospace data density; `--ftl-density:
  0.7` as a deliberate extreme-density stress test for `.ftl-table`.

All five contrast-checked (≥4.5:1 on required pairs) before landing;
`vaporwave`'s danger red was darkened one step past the literal reference
(`#ff3864` fails 4.5:1 against white) for the same reason `winxp-luna`'s
success green and `barbie`'s accent pink were.

### Fixed

- **`winxp-luna`**: `.ftl-btn-primary` and `.ftl-btn-go` used the chrome
  blue, contradicting this theme's own README ("green means go, blue means
  select"). Both now use the Start-button green; the title bar, focus
  ring, and "this is selected" states stay blue.
- **`material`**, **`vaporwave`**: the app bar's `.ftl-nav-brand` and
  active `.ftl-nav-item` used the shared `--ftl-nav-*` token defaults
  (accent-colored text), which are invisible or near-invisible against
  these two themes' accent-colored bars. Re-pointed the tokens on
  `.ftl-app-bar` specifically so the standalone `.ftl-nav` component
  (different background) is unaffected.

## v3.4.2 — remove `winxp-zune`

**Breaking for any app pinning `data-theme="winxp-zune"` or serving
`dist/winxp-zune.css`.** The theme is removed: `themes/winxp-zune/` and
`dist/winxp-zune.css` are deleted, and its row is gone from `dist/themes.json`
and the CONTRACT.md theme index. `winxp-luna` (the default Luna Blue XP
desktop, added in v3.3.0) remains and is unaffected — the two were always
visually distinct, not a swap of one for the other. An app still on
`winxp-zune` should switch its `data-theme`/link to `winxp-luna` or another
theme; there is no automatic redirect.

## v3.4.1 — flagship-theme fidelity pass on the v3.4.0 components

Fixes the gap where all 22 themes rendered the 19 new v3.4.0 components
(toast, alert, card, context menu, dropzone, avatar, tooltip, popover,
pagination, breadcrumbs, skeleton) with plain unstyled fallback tokens.
Seven themes with the strongest visual identity now give them real
theme-specific chrome, matching their existing idiom: `lcars` (candy-bar
borders, elbow radii), `matrix` (green glow, phosphor shadows), `tron`
(cyan glow, cut corners kept square on these), `windows95` (beveled
chrome, marching-ants tooltip), `winxp-luna` (Luna gloss), `barbie`
(pink/gold gloss), `hot-wheels` (flame glow). All new fg/bg pairs
contrast-checked (≥5:1) before landing. The remaining 15 themes are
unaffected — token-only theming is still a legitimate baseline.

## v3.4.0 — component library expansion

Non-breaking: every token and class from prior versions is unchanged. All
additions read existing base tokens with fallbacks, so every theme picks
them up with zero theme-file changes.

### Added

Sourced from real duplication found in the three consuming apps (CuTePi's
context menu and dropzone, PI9696's icon button and settings rows,
Playlist-Lab's toast/card/badge-button/empty-state) plus a curated set of
generic primitives the component landscape was conspicuously missing:

- `.ftl-toast` / `.ftl-toast-region` — transient dismissable notifications.
- `.ftl-spinner` — a bare loading indicator for non-htmx async work.
- `.ftl-context-menu` (+ `-item`, `-divider`) — cursor/anchor-positioned menu.
- `.ftl-dropzone` — drag-and-drop file target, with `.is-dragover` state.
- `.ftl-field-group` (+ `-title`) — a titled group of `.ftl-field` rows.
- `.ftl-btn-icon` — a circular icon-only button modifier on `.ftl-btn`.
- `.ftl-card` — a lighter-weight `.ftl-panel` sibling.
- `.ftl-badge-button` — a clickable badge (filter chip).
- `.ftl-empty-state` (+ `-icon`, `-title`, `-hint`).
- `.ftl-tooltip` via `[data-tooltip]` — CSS-only, no JS required.
- `.ftl-popover` — a `.ftl-dropdown`-style surface, app-toggled.
- `.ftl-accordion-item`/`-trigger`/`-panel` — built on native `<details>`.
- `.ftl-breadcrumbs` (+ `-item`, `.is-current`).
- `.ftl-pagination` (+ `-item`, `.is-active`, `.is-disabled`).
- `.ftl-alert` (+ `-info/-success/-warning/-danger`) — persistent inline banner.
- `.ftl-skeleton` (+ `-text`, `-block`) — shimmer loading placeholder.
- `.ftl-avatar` (+ `-sm`, `-lg`).
- `.ftl-stat` (+ `-value`, `-label`, `-trend`) — KPI tile.
- `.ftl-divider` / `.ftl-divider-v`.

See CONTRACT.md "Component vocabulary — v3.4.0 additions" for markup
examples of each. `demo.html` has a new "v3.4.0 additions" section.

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
