# ftl-themes

An app-agnostic design system and theme library for Go + HTMX (or any
server-rendered, htmx-swapped) application. It is a small component class
vocabulary plus a `--*` design-token contract, and it ships a catalogue of
45 fully switchable themes, from LCARS to Windows 95 to a Matrix terminal,
Skyrim, Liquid Glass and black leather with gold. You write one set of
markup, link one stylesheet, and switch the whole look (layout included)
with one attribute. No JavaScript framework is needed.

**Live examples:** https://drevilish.github.io/ftl-themes/ (the gallery, the
component QA pages, demo apps and page templates, published from `main`).

> **Versions.** `main` follows the latest work. v5.3.0 adds metering (VU,
> LED and arc meters, VFD, an EQ with RTA and spectrogram), tape-deck
> components (seven-segment, transport keys, deck lamps, telemetry graphs)
> and a tertiary button level. v5.2.0 added cursor role
> tokens, build-time Windows and iOS theme families, box-selection feedback
> reports, and CSS-led foldable metadata. v5.1.0 added screen tiers, touch
> support, CSS-only state, component groups, templates, icons, favicons,
> emails, and the feature extensions documented in
> [`CHANGELOG.md`](CHANGELOG.md).
> v4.0.0 was **breaking**: the `ftl-` prefix was removed everywhere and
> every bundle sits in `@layer ui`. Migrate with the codemod described in
> [`docs/MIGRATING-v4.md`](docs/MIGRATING-v4.md). The last v3 release
> lives on the `v3` branch.

## Quick start

1. **Vendor the repo** (apps usually pin it as a git submodule) and serve
   `dist/` and `assets/` **as siblings**. Bundles load fonts from
   `../assets/…`, so any other arrangement silently drops the theme fonts.
2. **Link one bundle and set `data-theme` before first paint.** Only one
   `dist/*.css` may be loaded at a time.
3. **Adopt the app shell once.** Without it, layout themes only recolour.
4. **Write ordinary HTML with the component classes.** Every theme styles
   them.

```html
<!doctype html>
<html lang="en" data-theme="lcars">
<head>
  <link rel="stylesheet" href="/static/themes/lcars.css?v={{ .ThemesVersion }}">
  <link rel="icon" type="image/svg+xml" href="/static/themes/favicons/lcars.svg">
  <link rel="apple-touch-icon" href="/static/themes/favicons/lcars-180.png">
</head>
<body class="app">
  <header class="app-bar">
    <span class="nav-brand">Ops</span>
    <nav class="nav"><a class="nav-item is-active" href="/">Home</a><a class="nav-item" href="/logs">Logs</a></nav>
    <div class="cluster push"><button class="btn btn-primary">New</button></div>
  </header>
  <aside class="app-rail" aria-hidden="true"></aside>
  <main class="app-main">
    <section class="panel">
      <header class="panel-header"><h2>Status</h2></header>
      <button class="btn btn-secondary" hx-post="/sync">
        <svg class="icon"><use href="/static/themes/icons/lcars.svg#icon-refresh"/></svg>
        Sync <span class="indicator"></span>
      </button>
    </section>
  </main>
  <footer class="app-status">All systems nominal</footer>
</body>
</html>
```

Switching theme means changing the `href` of the stylesheet, favicon and
icon sprite, plus `data-theme`, all together. Server-side rendering is the
simplest way to do that.

[`CONTRACT.md`](CONTRACT.md) is the full reference. The headings named
below (in quotes) are its sections.

## Getting the most out of it

Work through these in order. Each one is optional, but each adds
something a user will notice.

### Theme selection

- **Build the theme picker from `dist/themes.json`**
  ("Enumerating themes"). Never hard-code the list. Each entry gives you:
  - `dataTheme`: the value to put in `data-theme`.
  - `label` and `description`: for the picker.
  - `scheme` (`light`/`dark`): use it to flip your own chrome (for example
    Bootstrap's `data-bs-theme`).
  - `shellAware`: whether the theme needs the app shell.
  - `variants`: palette sub-themes, applied with `data-variant`.
  - `tint`: a user-chosen colour. When a theme declares one, your
    appearance settings **must** offer it ("Theme tint"). It needs no JS:
    put the token inline on `<html>`.
- **Cache-bust with `version`** from `themes.json` (`?v=…`). It is a
  content hash of every bundle ("Cache-busting").

### Layout

- **Adopt the app shell**: `.app` with `.app-bar`, `.app-rail`, `.app-main`
  and `.app-status` ("The app shell", "Adoption levels"). Themes
  re-arrange it through tokens. LCARS opens its rail; HUD themes run edge
  to edge. You never write `if theme == …`.
  - L0 (no shell) still renders correctly, just recoloured.
  - L2 adds theme chrome such as `themes/lcars/chrome.css`.
- **Let the library handle screens and touch** ("Screen tiers",
  "Touch and pointer"). Four tiers (mobile, tablet, desktop, XL) and
  44px touch targets are built in, so don't write breakpoints for library
  components. What your markup should do:
  - Put the brand first in the bar, then `<nav class="nav">`, then the
    actions.
  - Wrap wide tables in `.table-wrap`, or use `.table.is-stacked` for
    cards on phones.
  - Wrap bare checkboxes in `label.check` with hidden text.

### Behaviour and state

- **Prefer HTML over scripts for state** ("CSS-only selection, tabs and
  panes", "Floating surfaces, menus and nesting"):
  - Tabs and selection: radios inside `.tab` and `.list-item`, with
    `.tabset` panels.
  - Drawers, menus and popovers: the `popover` attribute. Nested menus are
    nested `<ul>` elements.
  - Accordions: `<details>`.
  - Server-kept state can keep using `.is-active`.
- **htmx states come styled** ("htmx state"). A `.indicator` inside a
  request shows a spinner. `.htmx-request` dims and blocks a control, and
  swaps fade (except under reduced motion).

### Customising

- **Override with one plain rule** ("Cascade layers"). Everything lives
  in `@layer ui`, so your unlayered CSS always wins. Set component tokens
  (`.btn-primary { --btn-bg: … }`), not properties. If you also load
  Bootstrap or Tailwind, put it in a layer below `ui`.
- **Offer display settings** ("User display options",
  [`docs/components/experience.md`](docs/components/experience.md)). Render
  any of these on `<html>`:
  - `data-text-size`, `--density`, `data-contrast`, `data-motion`,
    `data-transparency`, `data-underline-links`.
  - `data-accent` for the theme's own accent swatches.
  - `.prefs` is a ready-made settings panel.

  The OS settings (reduced motion, more contrast, reduced transparency,
  forced colours) are honoured automatically.

### Icons, favicons and pages

- **Use the theme's icons** ("Icon system"). Point
  `<svg class="icon"><use href="…#icon-name">` at
  `dist/icons/<slug>.svg`. Every theme redraws the 178-icon core set in
  its own style, and the generic sprite holds 1,000+ ids. Markup that
  points at `assets/icons/icons.svg` still works and shows the generic
  shapes.
- **Use per-theme favicons and app icons** from `dist/favicons/`
  ("Favicons and share cards"): an SVG favicon, a maskable icon, and
  180/192/512 PNGs for the Apple touch icon and the PWA manifest.
- **Start from a template** ([`docs/templates.md`](docs/templates.md)).
  `auth`, `settings`, `master-detail`, `inbox`, `onboarding` and `pricing`
  are complete, JS-free pages: copy one, drop the demo picker, and replace
  the content.

### Beyond the web page

- **Themed emails**: `dist/email/<slug>/` holds welcome, verify-email,
  reset-password, receipt, alert and weekly-digest, as inline-styled HTML
  plus text ("Themed HTML emails").
- **Share images**: render `share-card.html?theme=<slug>&title=…`
  headless and screenshot it to get an Open Graph image.
- **Scheduling**: `assets/js/schedule.js` switches theme, variant or
  season by time or date ("Theme scheduling").

### Keep doing your part of accessibility

The library guarantees:
- 4.5:1 contrast in every theme.
- A visible focus ring.
- Target sizes.
- Reduced motion.

The app still owns:
- `lang` on `<html>`.
- Labels on icon-only buttons.
- Menu roles (`role="menu"`, `li role="none"`).
- `role="status"` on spinners.
- Real link targets instead of `href="#"`.

### Already have your own CSS?

You can adopt the palette without the components ("Adopting ftl-themes
in an existing app"):
- `dist/tokens.css` holds every theme's tokens in one file. Map them onto
  your own tokens with a bridge stylesheet.
- `dist/core.css` is the components with no theme baked in.

Move templates onto the classes one at a time.

### Optional scripts

None of these are part of the contract. They are small reference
snippets, and you can render the same attributes server-side instead.

| Script | Does |
|---|---|
| `assets/js/theme-loader.js` | The demo picker: `?theme=`, swaps the bundle, icon sprite and favicon |
| `assets/js/tint.js` | Theme tint colour control, saved per theme |
| `assets/js/prefs.js` | `.prefs` display-settings panel, applied before first paint |
| `assets/js/schedule.js` | Time and date theme scheduling |
| `assets/js/window.js` | Draggable, maximisable `.modal[data-drag]` windows (touch and keyboard) |
| `assets/js/controls.js` | Keeps `.knob` and `.fader` `--value` in step with their inputs |
| `assets/js/carousel.js` | Carousel arrows and dots without the page jump |

## Components and examples

Serve the repo root over HTTP and open any page; `?theme=<slug>` picks the
theme.

- **QA pages.** Every component in every state, with a theme picker,
  stepper, a "Compare two" mode, and the theme's README shown alongside as
  a checklist:
  - [`components.html`](components.html), the core components.
  - The v5 group pages, each documented in
    [`docs/components/`](docs/components/):
    - [`components-tables.html`](components-tables.html)
    - [`components-instruments.html`](components-instruments.html)
    - [`components-forms.html`](components-forms.html)
    - [`components-navigation.html`](components-navigation.html)
    - [`components-surfaces.html`](components-surfaces.html)
    - [`components-experience.html`](components-experience.html)
    - [`components-social.html`](components-social.html)
    - [`components-prose.html`](components-prose.html)
  - [`hud.html`](hud.html), [`planner.html`](planner.html) and
    [`player.html`](player.html) (game HUD, productivity and media).
  - [`nesting.html`](nesting.html), for menus, tables and surfaces inside
    each other.
- **Demo apps:**
  - [`dashboard.html`](dashboard.html)
  - [`marketing.html`](marketing.html)
  - [`ticketsystem.html`](ticketsystem.html)
  - [`powerstation.html`](powerstation.html)
  - [`soundmixer.html`](soundmixer.html)
  - [`media-decks.html`](media-decks.html), transport devices and animation states from reel-to-reel to MiniDisc
  - [`audio-components.html`](audio-components.html), with the [AudioCN component map and usage guide](docs/components/audio.md)
  - [`livechat.html`](livechat.html)
- **Templates to copy:**
  - [`auth.html`](auth.html)
  - [`settings.html`](settings.html)
  - [`master-detail.html`](master-detail.html)
  - [`inbox.html`](inbox.html)
  - [`onboarding.html`](onboarding.html)
  - [`pricing.html`](pricing.html)
  - [`404.html`](404.html)
- **[`gallery.html`](gallery.html)**: every theme at once, filterable,
  from the screenshots in `test/visual-baseline/`.
- **[`share-card.html`](share-card.html)**: the Open Graph card template.

## Component list

Every component every theme styles. Core components are documented in
[`CONTRACT.md`](CONTRACT.md) ("Component vocabulary", "Instrument
primitives", "Mixing-console primitives"); each v5 group links its own
docs. [`docs/components/index.json`](docs/components/index.json) lists
every class, token and source file for tools and agents.

### Core

- **Buttons:** `.btn` (primary, secondary, tertiary, ghost, danger, sizes),
  `.btn-icon`, `.btn-close`, `.toggle-btn`, `.badge-button`, `.segmented`.
- **Forms:** `.field`, `.label`, `.field-hint`, `.field-error`,
  `.field-row`, `.field-group`, `.input`, `.select`, `.textarea`
  (readonly, mirror, invalid and size states), `.input-group`, `.check`,
  `.radio-group`, `.switch`, `.slider` (and `.is-vertical`), `.dropzone`.
- **Surfaces:** `.panel`, `.card`, `.modal` (dialog and popover, sizes,
  window states: maximise, minimise, resize, focus stacking), `.drawer`,
  `.popover`, `.dropdown`, `.context-menu`, `.accordion`, `.tooltip`
  (`[data-tooltip]`), `.toast`, `.alert`.
- **Navigation:** `.app` shell (`.app-bar`, `.app-rail`, `.app-main`,
  `.app-status`), `.nav`, `.nav-item`, `.nav-brand`, `.nav-collapse`,
  `.tabs`/`.tab`, `.breadcrumbs`, `.pagination`, `.scrollspy`, `.taskbar`,
  `.toolbar`.
- **Tables and lists:** `.table` (sticky header, zebra, blank rows, sort
  indicator, row hover and selection, `.is-matrix`), `.list` and
  two-line `.list-item`s, `.log`.
- **Status and feedback:** `.badge`, `.status`, `.progress`, `.meter`,
  `.spinner`, `.skeleton`, `.empty-state`, `.schedule`, htmx request
  states (`.htmx-request`, `.indicator`).
- **Content:** `.avatar`, `.stat`, `.divider`, `.icon`, `.carousel`,
  `.thread`/`.message`, `.thread-divider`, `.typing`, `.attachment`,
  `.bar-chart`, `.value-row`, `.meter-bank`, `.hero`, `.band`, `.price`,
  `kbd`.
- **Instruments:** `.meter` (vertical, segmented LED ladder, gain
  reduction), `.readout`, `.transport`, `.lamp`.
- **Mixing console:** `.mixer`, `.strip`, `.knob`, `.fader`, `.scale`,
  `.key`, `.scribble`, `.eq-curve`.
- **Layout:** `.stack`, `.cluster`, `.grid`, `.container`, `.anchor`,
  `.ratio`, `.divide-y`, `.stretched-link`, gap and margin steps,
  truncation, `.visually-hidden`, themed scrollbars.

### v5 component groups

- **Forms** ([docs](docs/components/forms.md)): `.btn-clear`,
  `.btn-split`, `.fab`, `.toggle-group`, `.has-badge`, `.input-icon` and
  `.input-clear`, search field, native date and time pickers, date range,
  `.calendar`, `.combobox`/`.listbox`, `.tag-input`, `.stepper`, range
  `.slider.is-range`, `.rating`, `.swatches`, `.file-list`.
- **Tables** ([docs](docs/components/tables.md)): editable cells, small-screen
  stacking, frozen columns, column resize and reorder, row groups, tree rows,
  selection column and bulk-action bar, loading, empty and load-more rows,
  density.
- **Navigation** ([docs](docs/components/navigation.md)): closable and
  scrolling tabs, `ul.menubar` with nested menus, `ul.tree`, `.tabbar`,
  `.sheet`, `nav.nav-rail`, `ol.steps`, `.command` palette, `.split`
  pane, keyboard layer.
- **Surfaces** ([docs](docs/components/surfaces.md)): image cards
  `.card.has-media`, draggable windows `.modal[data-drag]`, brand sign-in
  buttons `.btn-brand`.
- **Instruments** ([docs](docs/components/instruments.md)): `.gauge-dial`,
  `.gauge-arc`, `.gauge-linear`, `.compass` and `.compass-strip`, `.map`
  with pins and legend, `.progress-ring`, `.sparkline`, `.donut`,
  `.legend`, `.heatmap`, `.timeline`, `dl.props`, `.battery`, `.signal`,
  `.clock`, `.countdown`, the library-neutral chart contract.
- **Metering** ([docs](docs/components/metering.md)): analogue `.vu`,
  `.ledbar` bargraphs, `.ledarc` loudness meter, `.meter-panel`, VFD
  `.vfd`, EQ display (`.eq-graph`, `.rta`, `.spectrogram`, `.eq-node`).
- **Media** ([docs](docs/components/media.md)): `.tracklist`/`.track`,
  play queue, `.equaliser`, `.media-toggle`, `.scrubber`, `.volume`,
  `.waveform`, `.now-playing`, `.album-grid`, `.lyrics`.
- **Media devices** ([docs](docs/components/media-devices.md)):
  `.media-deck` reels and states, `[data-when]` state text, deck lamps and
  HUD band, `.transport-keys`, `.seg7` seven-segment digits.
- **Graphs** ([docs](docs/components/graphs.md)): `.graph-grid`/`.graph-card`,
  uPlot bridge, `.system-pane`.
- **Live data** ([docs](docs/components/live.md)): `.is-updated`,
  `.is-up`/`.is-down`/`.is-flat`, `.is-stale`, `.connection`,
  `time.updated`, `.feed`, `.depth-bar`, page alert level `data-alert`,
  `.dashboard` of `.widget`s.
- **Experience** ([docs](docs/components/experience.md)): display settings
  (`data-text-size`, `-density`, `-contrast`, `-motion`, `-transparency`,
  `-underline-links`), forced colours, the `.prefs` panel, motion tokens
  and themed theme-switch exits (`--motion-leave`), accent swatches,
  seasons, `.splash`, foldable layouts, themed empty, error, offline and
  404 states.
- **Social** ([docs](docs/components/social.md)): per-user colours,
  avatar status, `.presence`, live cursors, comment anchors and
  `details.comment-thread`, `.mention`, `.typing`, `.notifications`,
  activity feed.
- **Prose** ([docs](docs/components/prose.md)): `.prose`, code palette,
  callouts, template pieces.
- **Planner** ([docs](docs/components/planner.md)): `.kanban`,
  `.calendar.is-planner`, `.gantt`, `.schedule-list`.
- **Game HUD** ([docs](docs/components/hud.md)): `.hud`, `.hud-bar`,
  `.hud-minimap`, `.hud-quests`, `.hud-slot`, `.hud-float`,
  `.hud-achievement`, `.hud-prompt`.
- **Vehicles** ([docs](docs/components/vehicles.md)): `.attitude`, `.tape`,
  `.radar` (with `.radar-line`, `.radar-vrm`, `.ownship`),
  `.annunciator` and `.annunciator-switch`, `.telltale`, `.tyres`,
  `.mfd`, `.guard`, `.checklist`, `.throttle`, `.pfd`, `.flight-hud`,
  `.dial-bug`, `.waterfall`, `.orbit`.
- **Operations** ([docs](docs/components/ops.md)): `[data-status]`
  colours, shaped `.map-pin`s, sketch map hooks, `.map-route`,
  `.camera-feed`, `.barcode`.
- **Desktop** ([docs](docs/components/desktop.md)): `.desktop` shells
  (icons, dock, launchers, monitor), `.start-menu`, taskbar tasks and
  tray, `.desktop-window`s.

The "v5 component groups" table in CONTRACT.md maps each group to its
docs and example page.

## Building a theme

Read [`docs/authoring-a-theme.md`](docs/authoring-a-theme.md), then follow
[`docs/contributing-a-theme.md`](docs/contributing-a-theme.md) (to hand
the job to an agent, use [`docs/agent-theme-brief.md`](docs/agent-theme-brief.md)).

- **Start:** `scripts/new-theme.sh <slug>`.
- **Before review:** `scripts/theme-ready.sh <slug>` runs the build, lint,
  rendered regressions, the v5 audit, axe and the budgets.
- **Write a README:** every theme has a `README.md` beside its CSS saying
  what it is trying to achieve and how to extend it without drifting. Its
  "Icons" section holds the theme's icon style rules.
- **References:** what each theme copies lives in
  [`references/`](references/README.md). There is one folder per theme
  (`references/<theme>/`) and one subfolder per palette variant, each
  with a `RESEARCH.md`. Image names are camelCase component names joined
  by `-` (`elbowFrame-pillButton.webp`).
- **Branding:** the style and branding guide and per-theme fidelity
  scores are in [`docs/branding-guide.md`](docs/branding-guide.md).

## Layout

```
CONTRACT.md                 token + component contract: the full reference
CHANGELOG.md                what changed, breaking changes called out
PLAN.md                     v5 plan and progress
core/                       reset.css, core.css, layout.css (shell + tiers)
core/components/<group>.css v5 component groups
themes/<slug>/theme.css     tokens + look-only overrides, one per theme
themes/<slug>/icons.svg     the theme's redrawn icon set
themes/<slug>/README.md     the theme's intent, tell-tales and icon rules
dist/<slug>.css             built bundle (reset + core + theme): the file apps link
dist/core.css               reset + core, no theme (colour-only adoption)
dist/tokens.css             every theme's tokens, for apps with their own markup
dist/themes.json            theme index for pickers, incl. build version
dist/icons/<slug>.svg       the theme's full icon sprite (generic.svg: no theme)
dist/favicons/              per-theme favicons and app icons
dist/email/<slug>/          themed transactional emails (.html + .txt)
assets/fonts/, assets/icons/  vendored fonts (NOTICE.md), generic sprite, core-set.txt
assets/js/                  optional reference scripts (see above)
docs/                       authoring, contributing, component docs, templates, branding
references/<slug>/          reference images + RESEARCH.md per theme
test/visual-baseline/       per-theme screenshots shown by gallery.html
scripts/build.sh            regenerates dist/ (bundles, icons, favicons, emails)
scripts/check.sh            contract lint (runs check.py: tokens, contrast, focus, dist sync)
scripts/theme-ready.sh      all quality gates for one theme
scripts/core_regressions.mjs, v5_audit.mjs, a11y_audit.mjs   rendered checks (Playwright)
scripts/screenshot_themes.py  regenerates gallery screenshots
scripts/new-theme.sh        scaffolds a new theme
```

No app-specific integration notes live in this repo. Those belong in each
consuming app's own repository.
