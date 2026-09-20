# ftl-themes contract

`ftl-themes` is an app-agnostic design system and theme library for Go +
HTMX (or any server-rendered, htmx-swapped) applications. It defines a
small vocabulary of CSS component classes and design tokens; a consuming
app writes ordinary server-rendered HTML using those classes, links one
compiled theme file, and gets a fully switchable look with no JavaScript
framework and no per-app CSS of its own required.

This file contains no references to any specific application. If you're
integrating `ftl-themes` into an app and need integration notes, write
them in that app's own repo — they don't belong here.

## Loading a theme

Each theme ships as a single compiled file at `dist/<theme-name>.css`
(built by `scripts/build.sh` from `core/` + `themes/<name>/`). Link it and
set `data-theme` on `<html>` before first paint:

```html
<html data-theme="blue-future">
  <head>
    <link rel="stylesheet" href="/path/to/dist/blue-future.css">
  </head>
  ...
```

To let a user switch themes at runtime, swap the `<link href>` and the
`data-theme` attribute together (store the choice in `localStorage`/a
cookie and re-apply on load — see `docs/authoring-a-theme.md` for a
minimal example switcher). Themes are mutually exclusive: load exactly
one `dist/*.css` file at a time.

## Design tokens (`--ftl-*`)

Every theme defines all of these under `html[data-theme="<name>"]`.
`core/ftl-core.css` also defines fallback values at `:root` so unstyled
use (no theme loaded) still renders coherently.

| Token | Meaning |
|---|---|
| `--ftl-bg` | Page background, the deepest layer. |
| `--ftl-surface` | Cards, panels, modals — one step up from the page background. |
| `--ftl-surface-2` | Nested/recessed surfaces: input fields, dropdown menus, table stripes. |
| `--ftl-border` | Default visible border/outline color. |
| `--ftl-hairline` | A quieter divider than `--ftl-border` — table row separators, subtle rules. |
| `--ftl-text` | Primary text color. |
| `--ftl-muted` | Secondary text: labels, captions, disabled-adjacent text. |
| `--ftl-accent` | Primary interactive color: links, primary buttons, focus rings, active state. |
| `--ftl-accent-2` | Secondary accent: hover states, a second data series, complementary highlight. |
| `--ftl-danger` | Destructive/error actions and error states. |
| `--ftl-success` | Confirmatory/healthy states. |
| `--ftl-warning` | Caution/attention states, non-blocking. |
| `--ftl-radius` | Base corner radius. Themes with sharp corners (Windows 95, TRON) set this to `0`. |
| `--ftl-font` | Primary UI font stack. |
| `--ftl-font-mono` | Monospace font stack, for tabular/technical values. |
| `--ftl-flare` | A theme's single "extra" decorative color — a glow tint, a rare accent — used sparingly, not on every component. |

A theme may also define its own additional tokens for flourishes specific
to it (LCARS's `--ftl-lcars-*` candy-bar palette is the existing example)
— namespace them `--ftl-<theme>-*` so they can never collide with another
theme's or the core contract's names.

## Component vocabulary (`.ftl-*`)

`core/ftl-core.css` defines the structural/layout half of every component
below (sizing, spacing, flex/grid shape, focus mechanics) once, so it
never needs to be redeclared per theme. A theme file supplies the *look*
(color, shape override, motion) for the same classes. Full class list and
markup shape:

### Buttons
```html
<button class="ftl-btn ftl-btn-primary">Primary</button>
<button class="ftl-btn ftl-btn-secondary">Secondary</button>
<button class="ftl-btn ftl-btn-danger">Delete</button>
<button class="ftl-btn ftl-btn-success">Confirm</button>
<button class="ftl-btn ftl-btn-ghost">Ghost</button>
<button class="ftl-btn ftl-btn-sm ftl-btn-primary">Small</button>
```
State: `:disabled`, `:hover`, `:active`, `:focus-visible` are all styled
by `core.css`/the theme automatically — don't add extra classes for them.

### Form controls
```html
<input class="ftl-input" type="text">
<select class="ftl-select">...</select>
<input class="ftl-checkbox" type="checkbox">
<label class="ftl-switch">
  <input type="checkbox">
  <span class="ftl-switch-track"><span class="ftl-switch-thumb"></span></span>
</label>
<input class="ftl-slider" type="range">
```

### Surfaces
```html
<div class="ftl-panel">...</div>

<div class="ftl-modal">
  <div class="ftl-modal-header">Title</div>
  <p>Body content.</p>
  <div class="ftl-modal-footer">
    <button class="ftl-btn ftl-btn-secondary">Cancel</button>
    <button class="ftl-btn ftl-btn-primary">Save</button>
  </div>
</div>
<!-- Wrap .ftl-modal in your own fixed-position overlay element; overlay
     positioning is layout, not look, so it isn't part of this contract. -->

<div class="ftl-dropdown">
  <a class="ftl-dropdown-item" href="#">Item</a>
</div>
```

### Tables
```html
<table class="ftl-table">
  <thead><tr><th>Name</th><th>Status</th></tr></thead>
  <tbody>
    <tr class="is-selected"><td>Row</td><td>...</td></tr>
    <tr class="is-active"><td>Row</td><td>...</td></tr>
  </tbody>
</table>
```

### Navigation
```html
<nav class="ftl-nav">
  <span class="ftl-nav-brand">App Name</span>
  <a class="ftl-nav-item is-active" href="#">Home</a>
  <a class="ftl-nav-item" href="#">Settings</a>
</nav>
```

### Badges, progress, status
```html
<span class="ftl-badge ftl-badge-accent">New</span>
<span class="ftl-badge ftl-badge-danger">Failed</span>
<div class="ftl-progress"><div class="ftl-progress-bar" style="width:60%"></div></div>
<span class="ftl-status ftl-status-ok">Connected</span>
<span class="ftl-status ftl-status-error">Disconnected</span>
```

## Adopting ftl-themes in an existing app

If your app already has its own CSS with its own class/token names, you
don't have to rewrite every template. Add one small bridge stylesheet,
loaded after your existing CSS and before the `dist/<theme>.css` file,
that aliases the `--ftl-*` tokens onto your existing custom properties:

```css
/* your-app/static/css/ftl-bridge.css — maintained in your own repo */
:root {
  --ftl-bg: var(--your-background-token);
  --ftl-surface: var(--your-surface-token);
  --ftl-accent: var(--your-primary-token);
  /* ...map every --ftl-* token your app already has an equivalent for */
}
```

Then adopt the `.ftl-*` component classes incrementally, component by
component, rather than all at once — each one you switch over immediately
themes correctly across every `dist/<theme>.css` file, with no further
per-theme work.

## Adding a new theme

See `docs/authoring-a-theme.md`. In short: `scripts/new-theme.sh <slug>`,
fill in the scaffold, `scripts/build.sh`, add a row below and to
`demo.html`.

## Theme index

| Slug | Name | Reference |
|---|---|---|
| `blue-future` | Blue Future | Original futuristic sci-fi HUD default. |
| `cue-lab` | Cue Lab | Flat live-show console (QLab-style). |
| `lcars` | LCARS | Star Trek TNG/DS9/Voyager on-screen computer. Pair with `docs/lcars-chrome.md` for the decorative frame. |
| `windows95` | Windows 95 | Beveled 3D gray classic dialog chrome. |
| `matrix` | The Matrix | Green phosphor cascade on black. |
| `tron` | TRON | Cyan/orange line-grid, glowing sharp edges. |
| `aqua` | Aqua (Snow Leopard) | Brushed metal, glossy candy buttons. |
| `winamp-classic` | WinAmp Classic | Steel-gray skinned player chrome. |
| `wmp11` | Windows Media Player 11 | Black glass, cool blue glow. |

Planned (see `docs/theme-backlog.md` for the full list and notes,
including the open iOS-era question): Windows XP Luna/Royale/Olive/Silver,
Windows 7 Aero, Barbie, Alienware, Weyland-Yutani, Material, Ubuntu,
general Skeuomorphism, iOS (skeuomorphic and modern, as two entries),
Hot Wheels, Coca-Cola Classic, Cassette Futurism, and the Batch 3
suggestions (Amiga/BeOS, Commodore 64/Teletext, Vaporwave/Synthwave,
PlayStation XMB, Xbox 360 Blades, Nokia dumbphone, NASA Mission Control,
Bloomberg Terminal, Braun/Dieter Rams, Cyberpunk Netrunner).
