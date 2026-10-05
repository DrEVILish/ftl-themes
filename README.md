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

> **Versions.** `main` follows the latest work. v5 (screen tiers, touch,
> CSS-only state, 50+ new components, templates, icons, favicons, emails)
> is on `main` and listed under "Unreleased" in [`CHANGELOG.md`](CHANGELOG.md).
> v4.0.0 was **breaking**: the `ftl-` prefix was removed everywhere and
> every bundle sits in `@layer ui`. Migrate with `scripts/migrate-v4.py`
> ([`docs/MIGRATING-v4.md`](docs/MIGRATING-v4.md)). The last v3 release
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

Component groups beyond the core set: editable tables, gauges and charts,
date pickers and comboboxes, menubars, trees and command palettes, image
cards and windows, presence and comments, game HUD, kanban, calendar,
gantt, media player, and prose/code. The "v5 component groups" table in
CONTRACT.md maps each group to its docs and page. Instrument and
mixing-console primitives (`.meter`, `.readout`, `.lamp`, `.knob`,
`.fader`) are in CONTRACT.md too.

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
