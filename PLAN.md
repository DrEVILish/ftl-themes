# ftl-themes v5.0 plan

Status: **in progress** (started 2026-10-02). Baseline 2026; new theme names agreed. v4 stays the base: the
token contract, the `@layer ui` bundles, the L0/L1 adoption levels and the
42 themes all carry forward (45 with the three new v5 themes). v5 is about three things v4 does not do well:

1. **Fluid mobile, tablet, desktop and wide-screen layouts**, natively, in
   core, so every theme gets them.
2. **Spacing that holds**: correct padding and margins in core and in every
   theme, with no overflow at any supported width.
3. **A bigger component library** (50 new components), with editable
   tables, nesting and nested menus handled properly.
4. **An experience layer**: user accessibility settings, per-theme motion
   and theme-switch transitions, accent and seasonal tints, splash screens,
   themed empty and error states, cursor packs, and installed-app (PWA and
   desktop wrapper) title bars. Added after the 2026-10-02 reviews (§10–24).

**Primary development theme: `blue-future`.** Every v5 change lands in core
first and is proven on `blue-future`. Then the change is rolled out to the
other 41 themes in batches (see [Rollout](#26-rollout)).

**Rule that does not change:** markup stays declarative and as plain as
possible: native elements, a class or two, standard attributes. Apps add
behaviour; ftl-themes styles states.

---

## 1. What v4 does today (the starting point)

| Area | v4 today | Problem for v5 |
|---|---|---|
| Breakpoints | One: `max-width: 720px` (12 rules in core, plus three one-off theme queries at 960/1000px) | No tablet tier, no wide-screen tier, and 720px splits the target devices badly (a 466px folded phone and a 700px tablet get the same layout). |
| Content width | `.container` caps at `--container-max` (64rem). The `.app` shell has no maximum. | On a 2560px screen the shell stretches edge to edge. |
| Touch | Nothing reacts to `pointer: coarse`. `.btn` padding is `0.5em × 1.1em` scaled by `--density`, so a button is ~32px tall. | Below the 44px touch target size Apple and WCAG 2.5.5 recommend. Hover-only affordances (row hover, tooltips) have no touch equivalent. |
| Spacing | A `--space-3xs`…`--space-2xl` scale exists, but only the utility classes use it. Components hard-code padding (`.modal` 1.5rem, `.app-bar` 0.6rem 1rem, …) and themes override those piecemeal. | No single place to tighten spacing for small screens. Themes drift, and long content overflows. |
| Layering | z-index values are scattered (`1`, `1000`, `1500`…). No `--z-*` scale. Popovers are positioned inside their parent. | Nested surfaces clash: a dropdown inside a sticky header was trapped (fixed in a94ea93, case by case). |
| Components | ~240 classes: buttons, forms, tables, modals, meters, knobs, faders, readouts, tabs, context menu, tooltip (`[data-tooltip]`), drawer, carousel… | No dial gauge, compass, map frame, date picker, tree, nested menus, inline-edit table cells or image cards. |
| Checks | `check.py` (token lint) and `core_regressions.mjs` (rendered, Chromium, 1280 + 390px). | Nothing checks overflow, touch target size or spacing at each tier. |

---

## 2. Breakpoints and target devices

### Tiers

| Tier | Width range | Pointer assumption | Shell layout |
|---|---|---|---|
| **Mobile** | 250px – 480px | coarse (touch) | Single column. Bar on top (brand + menu toggle), content, bottom tab/status bar. Rail hidden, or a slide-in drawer. |
| **Tablet** | 481px – 900px | coarse (touch) | Bar on top with inline nav when it fits. Optional collapsible rail (icon-only). Two-column content where panels allow. |
| **Desktop** | 901px – 1800px | fine (mouse), touch allowed | The full v4 L1 shell: bar, rail, main, status. |
| **XL display** | 1801px and up | fine | The desktop shell, capped at 1800px and centred. Each side gutter shows theme art (see §3). |

Boundary rule: the lower bound is inclusive and the upper bound exclusive,
except where noted. Exactly 480px is Mobile and 481px is Tablet; exactly
900px is Tablet and 901px is Desktop. Below 250px nothing is guaranteed.
The layout must still not overflow, but no design effort goes there.

CSS custom properties cannot be used inside `@media` conditions, so the
four tiers are fixed numbers in core, written once each. Themes do not set
breakpoints; they set per-tier tokens.

```css
/* core/layout.css — the only place tier widths appear */
@media (max-width: 480px)                         { :root { --tier: mobile; } }
@media (min-width: 481px) and (max-width: 900px)  { :root { --tier: tablet; } }
@media (min-width: 901px) and (max-width: 1800px) { :root { --tier: desktop; } }
@media (min-width: 1801px)                        { :root { --tier: xl; } }
```

### Viewport tiers for the shell, container queries for components

- **The app shell** (`.app`, bar, rail, status) changes with the
  **viewport** tier. Its job is to fit the screen.
- **Components** (panels, tables, forms, card grids, toolbars) respond to
  **their own container's width**, through `container-type: inline-size`
  on `.app-main`, `.panel`, `.card`, `.modal` and `.columns > *`. A form in a
  320px side panel on a 2560px desktop must lay out like a phone form, and
  only container queries get that right. This is also what makes nesting
  (§6) work: a table inside a card inside a two-column row adapts to the
  space it actually has.

Container tiers use the same numbers (`@container (max-width: 480px)` and
so on), so there is one mental model.

### Target devices

| Device | Viewport (CSS px) | Tier | What to verify |
|---|---|---|---|
| iPhone 15 Pro | 393 × 852 | Mobile | Touch targets, bottom bar clears the home indicator (`env(safe-area-inset-bottom)`), and no horizontal scroll. |
| "iPhone Duo", folded | 466 × 678 | Mobile | Close to the tier edge, with a short screen: the modal and the bottom bar must both fit. |
| "iPhone Duo", unfolded | 890 × 626 | Tablet | Landscape-ish and short: check that the bar plus content plus status fit in 626px. |
| MacBook Air | 1280 × 800 | Desktop | The v4 baseline. Nothing should regress. |
| 1440p desktop | 2560 × 1440 | XL | Content capped at 1800px and centred, with 380px gutters of theme art each side. |

> **Open question:** "iPhone Duo" isn't a shipping Apple device. The sizes
> given look like a book-style foldable. If it really is a dual-screen
> device (Surface Duo style, with a hinge), v5 should also handle
> `@media (horizontal-viewport-segments: 2)` and keep content off the hinge
> with `env(viewport-segment-*)`. Planned as optional unless confirmed.

These five sizes become the viewports of `core_regressions.mjs` and of
`screenshot_themes.py`, replacing the current single 1280 × 900.

---

## 3. Wide screens: 1800px cap and gutter art

- `.app` gets `max-inline-size: var(--app-max, 1800px)` and
  `margin-inline: auto`. Apps can lower `--app-max`; themes don't touch it.
- Above 1800px, the `body` background shows **gutter art** on both sides.
  It comes from a new theme property, `--app-gutter-art`: one or more
  background layers, CSS only (gradients, SVG data URIs), no bitmaps.

Gutter art rules (to be written into `authoring-a-theme.md` and linted):

1. **Never behind content.** It paints on `body` outside `.app`, and
   `.app` stays opaque.
2. **Low contrast.** Gutter art must stay within 1.5:1 of `--bg` on average,
   so the eye stays on the content. It is decoration, not a feature.
3. **Still by default.** Any motion only under
   `prefers-reduced-motion: no-preference`, slow (≥ 20s cycles), and never
   a flashing or looping element near the content edge.
4. **Fades in.** The art fades in from the content edge, so a 1900px
   screen shows a sliver and a 2560px screen the full composition.

Examples to build for the first themes:

| Theme | Gutter art idea |
|---|---|
| `blue-future` (first) | A faint starfield with slow-drifting telemetry grid lines in `--hairline` colour. |
| `lcars` | Dimmed candy-colour bar fragments, like out-of-focus neighbouring panels. |
| `windows95` | The teal desktop with a few greyed-out desktop icons. |
| `tokie` | The leather continues and the gold stitching runs down the edge. |
| `skyrim` | Knotwork border bands, very low contrast. |
| `steampunk` | Pipe runs and a slowly turning gear, half-hidden. |

Themes without gutter art fall back to plain `--bg`, which is still correct.

---

## 4. Touch and pointer

| Rule | Mobile and Tablet | Desktop and XL |
|---|---|---|
| Minimum target size | **44 × 44px** (`--tap-min: 44px`) for every interactive control: buttons, nav items, tabs, checkbox and radio hit areas, close buttons, pagination, menu items, table row actions. | Current (mouse-sized) sizes, but never below **24 × 24px** (WCAG 2.5.8 AA). |
| Spacing between targets | At least 8px around any target smaller than the minimum. Full-size (44px) targets may sit edge to edge, as menu items and list rows do (WCAG 2.5.8 only asks for spacing around undersized targets). | Current. |
| Any touch device | `@media (any-pointer: coarse)` raises the targets to 44px even on a desktop-width touch screen (a Surface or a touch laptop). | Same. |
| Hover | Hover-only reveals (row actions, tooltips) need a touch path: a visible control or `:focus-within`. Hover styles sit inside `@media (hover: hover)` so a tap doesn't leave a sticky hover state. | Same. |
| Tap delay | `touch-action: manipulation` on controls (no double-tap zoom delay). | Same. |
| Inputs | Font size at least 16px on mobile, or iOS Safari zooms in on focus. | Current. |
| Mouse cursor | Buttons, links, tabs and menu items keep the **arrow** cursor; core drops `cursor: pointer` (18 rules in core, plus 3 themes). Controls should feel like an application, not a web page. Text fields keep the I-beam; drag surfaces get `grab`/`grabbing`; disabled gets `not-allowed`. Theme cursor packs (§11) restyle these cursors but keep the same mapping. | Same. |
| Drag controls | Knobs, faders, sliders and window dragging use Pointer Events (`window.js` already does), with `touch-action: none` on the drag surface only. | Same. |

Hit area and visual size are separate: a 20px icon button gets a 44px hit
area through padding or a `::before` expander, so dense themes (`bloomberg`,
`msdos`) keep their look on desktop. A new `--hit-min` token per tier
drives this.

---

## 5. Spacing: padding and margins that hold

### Root cause in v4

Components hard-code their padding. Themes patch individual components,
and there is no per-tier spacing. v5 moves all spacing onto one scale:

1. **One scale, tier-aware.** `--space-3xs` … `--space-2xl` stay, but
   their values come from a per-tier step, e.g. `--space-m` is 0.75rem on
   Mobile, 1rem on Tablet and Desktop, and 1.25rem on XL.
   `--density` stays as the theme's multiplier on top.
2. **Every component reads the scale.** Each component gets named padding
   properties that default to the scale (`--modal-pad: var(--space-l)`,
   `--panel-pad`, `--card-pad`, `--cell-pad-x/y`, `--app-bar-pad`…). No
   literal rem values left in core for spacing.
3. **Themes set intent, not pixels.** A theme sets `--density` and, at
   most, a component's `--*-pad`. Theme rules that set raw `padding` or
   `margin` on core components get audited and either become tokens or
   are deleted.
4. **Flow spacing between siblings.** `.stack > * + *` style spacing
   (one rule) replaces per-component `margin-bottom`. This stops margins
   collapsing differently inside panels, modals and table cells.
5. **No overflow, by rule.** Every component gets `min-inline-size: 0`
   where it is a flex or grid child. Long words get
   `overflow-wrap: anywhere` in text containers. Tables scroll inside
   their own wrapper, never the page. Media is `max-inline-size: 100%`.

### Enforced by a check

`core_regressions.mjs` grows an **overflow and spacing pass**. For every
theme, at all five target viewports, on every example page (including the
new nesting page):

- **No horizontal overflow:** `document.documentElement.scrollWidth` is at
  most the viewport width, and no element sticks out of its scroll
  container.
- **Touch targets:** every interactive element meets the tier minimum.
- **Minimum gap** between adjacent interactive elements on touch tiers.
- **Text never touches a container edge:** at least `--space-2xs` of
  padding between text and a bordered or filled box.

A theme is "v5 ready" when it passes all of these. The gallery shows the
status per theme.

---

## 6. Nesting and layering

### The nesting example page (`nesting.html`)

A new example page, generated like the others, that puts every container in
every other container. It is a QA harness, not a demo: if a combination
breaks, it shows here first. Planned permutations:

**Containers in containers**

- panel > panel; panel > card > panel; card > card > card (three deep)
- modal > panel; modal > tabs > panel; drawer > card
- columns (2, 3, 4) > panel > table
- columns > columns (nested grid) > card
- accordion > accordion; accordion > table; tabs > accordion > form
- popover > form; dropdown > nested list

**Tables**

- table in modal (including a `.modal-lg` with a 12-column table)
- table in card in a two-column row (forces container-query layout)
- table in table (an expanded row's detail table)
- sticky-header table in a scrolling panel inside a modal
- table with every editable cell type (see §7) in each state
- table inside `.columns` on Mobile (stacked card form)

**Forms**

- field > input-group (icon + input + button)
- field-row with mixed widths inside a card on Mobile
- form in a modal in a drawer
- inputs inside table cells, inside a modal

**Layering**

- dropdown in a sticky table header in a scrolling modal
- context menu with three levels of submenu near the right and bottom edges
- tooltip on a button in a toolbar in a sticky bar
- toast over an open modal
- popover anchored inside a transformed or `overflow: hidden` parent

### The layering fix

- A **`--z-*` scale** in core: `--z-base`, `--z-sticky`, `--z-dropdown`,
  `--z-drawer`, `--z-modal`, `--z-popover`, `--z-toast`, `--z-tooltip`. Every
  z-index in core and themes moves onto it (lint-enforced).
- **Top layer first.** Floating surfaces (dropdown, popover, context
  menu, tooltip, modal) use the native `popover` attribute and `<dialog>`
  where possible. Top-layer elements can't be clipped by `overflow` or
  trapped by stacking contexts, so this removes the clash problem at the
  root instead of case by case.
- **CSS anchor positioning** (`anchor-name`, `position-anchor`,
  `position-try-fallbacks: flip-block, flip-inline`) places those surfaces
  next to their trigger and flips them at screen edges, with no JS.
  Chromium supports it today; others get a fallback that sits below the
  trigger.
- **Nested surfaces step down visually.** A panel in a panel uses
  `--surface-2`, and a third level uses a new `--surface-3`. Inner radius =
  outer radius − padding (concentric corners), computed in core.

---

## 7. Editable tables (inline input cells)

Apps handle the behaviour (double-click or tap to edit, Enter to save,
Esc to cancel, saving). ftl-themes styles every **state** so it looks
native in each theme.

### Markup (declarative, no wrapper divs)

```html
<td class="is-editable">Road trip</td>                     <!-- idle: shows it can be edited -->
<td class="is-editing"><input class="input" value="Road trip"></td>
<td class="is-editing"><select class="select">…</select></td>
<td class="is-editing"><input class="input" type="date"></td>
<td class="is-editing"><input class="input" type="number"></td>
<td class="is-editing"><input type="checkbox" class="checkbox"></td>
<td class="is-dirty">Road trip 2</td>                     <!-- changed, unsaved -->
<td class="is-saving">Road trip 2</td>                    <!-- request in flight (htmx-request works too) -->
<td class="is-editing"><input class="input" aria-invalid="true"><span class="field-error">Required</span></td>
<td class="is-editable" aria-readonly="true">Locked</td>  <!-- read-only -->
```

### What core styles

- **Idle editable:** a subtle affordance (dotted underline or faint inset
  on hover and focus) and `cursor: text`. On touch tiers, a visible pencil
  affordance, since there is no hover.
- **Editing:** the input fills the cell exactly: no row height jump, no
  column width jump, same font, cell padding moved onto the input. The
  focus ring stays inside the cell so it isn't clipped by the table
  wrapper.
- **Dropdown, date and combobox in a cell:** the open list uses the top
  layer (§6), so it can't be clipped by the table's scroll container or a
  sticky header.
- **Dirty, saving, saved, error and read-only:** each has a theme token
  (`--cell-dirty-bg`, `--cell-error-border`…) with a sensible default
  from the semantic colours.
- **Row-level editing:** `<tr class="is-editing">` styles a whole row in
  edit mode, with row actions (save and cancel) in the last cell.
- **Keyboard:** visible focus on cells (`td:focus-visible`), so an app can
  do spreadsheet-style arrow navigation with `tabindex`.

**Touch note:** `dblclick` is unreliable on touch screens. The plan
recommends that apps open the editor on tap of an `.is-editable` cell on
touch tiers. CSS can't decide this, so CONTRACT.md will document it.

### Tables on small screens

- **Default:** the table scrolls sideways inside its own container, with
  the first column sticky.
- **Opt-in `.table.is-stacked`:** below the Tablet tier (container query),
  each row becomes a card, and each cell shows its column name from
  `<td data-label="Status">`. This works with editable cells too.

---

## 8. Nested context menus (and menu bars)

Nested `<ul>` lists, so the structure is the markup:

```html
<ul class="context-menu" role="menu" popover id="row-menu">
  <li><button role="menuitem">Rename</button></li>
  <li><button role="menuitem">Duplicate</button></li>
  <li class="has-submenu">
    <button role="menuitem" aria-haspopup="menu">Move to</button>
    <ul role="menu">
      <li><button role="menuitem">Inbox</button></li>
      <li class="has-submenu">
        <button role="menuitem" aria-haspopup="menu">Projects</button>
        <ul role="menu">…</ul>
      </li>
    </ul>
  </li>
  <li role="separator"></li>
  <li><button role="menuitem" class="is-danger">Delete</button></li>
</ul>
```

- **Desktop:** submenus open on hover and on keyboard focus
  (`:focus-within`), flyout to the side, and flip at the screen edge
  (anchor positioning).
- **Touch tiers:** submenus expand **inline** below their item (like an
  accordion). Flyouts are unusable on a phone.
- The same nested-list markup drives a desktop **menu bar**
  (`<ul class="menubar">`, File / Edit / View) and a **tree view**
  (`<ul class="tree">`).
- The v4 button-based `.context-menu` keeps working (deprecated in v5,
  removed in v6).
- Apps provide the JS for arrow-key navigation, as they do today.

---

## 9. 50 new components

Grouped by area. ✱ = explicitly requested. "Partly exists" means v4 has a
piece that gets finished rather than rewritten.

### Instruments and data display

| # | Component | Class / markup | Notes |
|---|---|---|---|
| 1 | ✱ Dial gauge with a needle (rev counter, speedometer) | `.gauge-dial` + `<meter>` or `style="--value:.7"` | CSS conic-gradient arc, a rotated needle, tick marks, red zone (`--gauge-redline`). Optional numbers via a `<ol class="gauge-ticks">`. Theme-styled needle (`steampunk` brass, `blue-future` glowing cyan). |
| 2 | ✱ Arc gauge (semi-circle) | `.gauge-arc` | Fuel or level style, no needle. |
| 3 | ✱ Linear gauge with markers | `.gauge-linear` | Min, max, target and warning markers; extends `.meter`. |
| 4 | ✱ Compass | `.compass` + `style="--heading:215"` | Rotating rose or a heading strip (Skyrim-style bar variant `.compass-strip`). |
| 5 | ✱ Map frame | `.map` | Not a map engine: a themed frame for an `<img>`, `<svg>` or `<iframe>` map. Includes zoom controls, a scale bar, an attribution line and a north arrow. |
| 6 | ✱ Map markers and pins | `.map-pin` positioned by `--x/--y` | With label and popover. |
| 7 | Map legend | `.map-legend` | Reuses chart legend. |
| 8 | Progress ring | `.progress-ring` | Circular progress, determinate and indeterminate. |
| 9 | Sparkline | `.sparkline` (inline SVG polyline) | Styling only, themed stroke. |
| 10 | Donut chart | `.donut` with `--segments` | conic-gradient, with legend. |
| 11 | Chart legend | `.legend` | Shared by bar chart, donut and map. |
| 12 | Heatmap grid | `.heatmap` with `--v` per cell | Calendar-style activity grid. |
| 13 | Timeline | `.timeline` (an `<ol>`) | Vertical, with horizontal on desktop. |
| 14 | Description list / property grid | `<dl class="props">` | Key/value inspector rows. |
| 15 | Battery and signal indicators | `.battery`, `.signal` | Status-strip glyphs (`silo`, `ios-*` already draw them privately). |
| 16 | Clock and countdown | `.clock` (analog), `.countdown` | Analog face reuses the dial. |

### Buttons and icons

| # | Component | Class / markup | Notes |
|---|---|---|---|
| 17 | ✱ Transparent button | `.btn-clear` | No fill and no border at rest; tinted on hover, focus and press. Distinct from `.btn-ghost`, which keeps a hover fill. |
| 18 | ✱ Transparent icon button | `.btn-icon.is-clear` | Partly exists (`.btn-icon`). |
| 19 | ✱ Icon + label button | `<button class="btn"><svg class="icon">…</svg> Save</button>` | Partly exists. v5 fixes icon size, gap and alignment for every size and theme, and adds an icon-after variant. |
| 20 | Split button | `.btn-split` | A main action plus a menu caret. |
| 21 | Floating action button | `.fab` | Touch tiers. Respects safe area. |
| 22 | Toggle button group | `.toggle-group` | Partly exists (`.toggle-btn`, `.segmented`). Adds multi-select. |
| 23 | Notification dot or count on an icon | `.has-badge` with `data-count` | For the bell, the tabs and the nav. |

### Forms and inputs

| # | Component | Class / markup | Notes |
|---|---|---|---|
| 24 | ✱ Leading icon in an input | `.input-group > .input-icon + .input` | Partly exists (`.input-addon`). Adds an icon inside the field and a trailing clear button. |
| 25 | Search field | `<input type="search" class="input">` | Icon, clear button and shortcut hint. |
| 26 | Date picker | `<input type="date" class="input">` + `.calendar` | Native input styled per theme (including the picker indicator). Plus a `.calendar` month grid for apps that render their own. |
| 27 | Time picker | `<input type="time">` | Native, styled. |
| 28 | Date range | two date inputs in `.input-group` | |
| 29 | Combobox / autocomplete | `<input list>` + `<datalist>`, or `.combobox` with a listbox popover | |
| 30 | Tag / multi-select input | `.tag-input` with `.tag` chips | Removable chips inside the field. |
| 31 | Number stepper | `.stepper` | − / value / +, touch sized. |
| 32 | Dual-handle range slider | `.slider.is-range` | Two `<input type="range">`. |
| 33 | Rating | `.rating` | Radio-based stars or theme glyphs. |
| 34 | Colour swatch picker | `.swatches` | Radio-based. |
| 35 | File list (upload queue) | `.file-list` | Pairs with `.dropzone`, with per-file progress. |
| 36 | Inline-edit table cells | `td.is-editable` / `.is-editing` | §7. |

### Navigation and structure

| # | Component | Class / markup | Notes |
|---|---|---|---|
| 37 | ✱ Closable tabs | `.tab` + `.btn-close` inside | Close button per tab, overflow scrolling, and an add-tab button. Built on `.tabs`. |
| 38 | ✱ Nested context menu | `ul.context-menu` | §8. |
| 39 | Menu bar | `ul.menubar` | §8. |
| 40 | Tree view | `ul.tree` with `<details>` | Expand and collapse with no JS. |
| 41 | Bottom tab bar | `.tabbar` | The mobile primary nav. The status strip becomes this on the Mobile tier. |
| 42 | Bottom sheet | `.sheet` (`<dialog>`) | Mobile counterpart of the modal and dropdown. |
| 43 | Collapsible rail / sidebar | `.app-rail.is-collapsible` | Icon-only on Tablet, full on Desktop. |
| 44 | Stepper / wizard progress | `.steps` (an `<ol>`) | |
| 45 | Command palette | `.command` (`<dialog>` + search + list) | |
| 46 | Split pane / resizer | `.split` | CSS `resize`, plus a drag handle for apps that want JS. |

### Surfaces and media

| # | Component | Class / markup | Notes |
|---|---|---|---|
| 47 | ✱ Image card | `.card.has-media` > `<img>` | Ratio-locked media, overlay title variant, and a lazy-load skeleton. |
| 48 | ✱ Table in a modal | `.modal > .table-wrap > .table` | The modal body scrolls, the table header stays sticky inside it, and widths follow the modal size. |
| 49 | ✱ Draggable window | `.modal[data-drag]` | `window.js` becomes a supported part of the contract: touch drag, kept inside the viewport, double-click the title bar to maximize, and keyboard move (Alt+arrows) for accessibility. |
| 50 | ✱ Brand sign-in and connect buttons | `.btn-brand.is-github`, `.is-google`, `.is-apple`, `.is-microsoft`, `.is-spotify`… | Logos from `assets/logos/`, only for companies that publish brand guidelines allowing this use, and drawn exactly to those rules. That means fixed colours and clear space, so these buttons are deliberately **not** re-themed. See the licensing rules in `assets/logos/README.md`. |

Also from the request, handled as cross-cutting work rather than new
components:

- ✱ **Layering and nesting without clashes:** §6.
- ✱ **Every theme holds its padding and margins with no overflow:** §5,
  enforced by the check.
- ✱ **Theme-accurate, working modal close (×) button.** The first pass
  shipped in a94ea93 (title-bar colour, plus XP, LCARS, MS-DOS and
  Prometheus placements). v5 audits all 42 themes for a
  period-correct close control: the Windows 95 bevelled grey square, the
  Aqua red traffic light, the XMB "○ Back" hint and so on, through
  `--btn-close-glyph` and the existing `--btn-close-*` tokens.

---

## 10. Accessibility controls (a settings panel in core)

v4 already honours `html[data-motion="reduced"]`, `html[data-contrast="high"]`
and the OS media queries. v5 completes the set and ships the UI for it.

### Attributes (on `<html>`, all optional)

| Attribute | Values | Effect |
|---|---|---|
| `data-text-size` | `s`, `m` (default), `l`, `xl` | Scales the root font size; every component is in rem, so layout follows. |
| `data-density` | `compact`, `default`, `comfortable` | Multiplies `--density` on top of the theme's own value. |
| `data-contrast` | `default`, `high` (exists), `more` | `high` raises text and border contrast within the theme's palette (AAA text, 3:1 borders). |
| `data-motion` | `full`, `reduced` (exists), `none` | `none` also stops theme ambient motion (gutter art, glows). |
| `data-transparency` | `default`, `reduced` | Glass and translucent themes (`liquid-glass`, `win7-aero`, `xmb`) go opaque. |
| `data-pointer` | `auto`, `touch` | Force touch-size targets on any screen (a desktop user with a touch screen or motor needs). |
| `data-underline-links` | present / absent | Always underline links, for themes that rely on colour alone. |

Each attribute **defaults to the OS preference** when unset
(`prefers-reduced-motion`, `prefers-contrast`, `prefers-reduced-transparency`,
`pointer: coarse`), so the panel only needs to store overrides.

**Forced colors (Windows High Contrast):** every theme must stay usable under
`@media (forced-colors: active)`. Core maps components to system colours
(`Canvas`, `ButtonText`, `Highlight`…), keeps borders that themes draw with
shadows or gradients, and keeps focus rings. Added to the rendered check.

### The panel: `.prefs`

A declarative, themed settings panel an app drops into a modal, drawer or
page. ftl-themes styles it; a ~20-line reference script
(`assets/js/prefs.js`, like `window.js`) writes the attributes and stores
them in `localStorage`. Apps can store them server-side instead.

```html
<form class="prefs">
  <fieldset class="field-group">
    <legend class="field-group-title">Text size</legend>
    <div class="segmented">
      <label class="segmented-item"><input type="radio" name="text-size" value="s"> A</label>
      <label class="segmented-item"><input type="radio" name="text-size" value="m" checked> A</label>
      …
    </div>
  </fieldset>
  <label class="switch"><input type="checkbox" name="motion" value="reduced"> Reduce motion</label>
  <label class="switch"><input type="checkbox" name="transparency" value="reduced"> Reduce transparency</label>
  …
</form>
```

The panel previews each change immediately, includes the accent picker
from §12, and every control is reachable by keyboard and screen reader.

## 11. Theme motion, switching transitions and cursor packs

### A motion language per theme

Each theme declares how things move, not just how they look, through a
small set of motion tokens: `--motion-enter`, `--motion-exit`,
`--motion-duration-s|m|l`, `--motion-ease`, plus named keyframes the theme
owns. Examples:

| Theme | Motion character |
|---|---|
| `blue-future` (first) | Fast fades with a brief glow-in on live data; modals scale in from 98%. |
| `matrix` | Modals "decode" in (glyph scramble through a `steps()` animation). |
| `windows95` | No easing at all: windows snap open; menus open with the classic slide. |
| `liquid-glass` | Springy scale with an overshoot; glass blurs in. |
| `msdos` / `teletext` | Instant, or a line-by-line reveal. |
| `silo` / `weyland-yutani` | A CRT power-on: a horizontal line expands to the full screen. |

Rules: every animation sits inside `prefers-reduced-motion: no-preference`
and stops under `data-motion="reduced"`; nothing animates longer than
400ms for routine UI; no animation blocks input.

### Switching themes

Switching theme runs through the **View Transitions API**
(`document.startViewTransition`) in `theme-loader.js`: a cross-fade by
default, and a theme can supply its own *entrance* (the incoming theme's
motion character) with `::view-transition-new(root)`. Without the API, or
under reduced motion, the switch is instant, as today.

### Cursor packs

Optional per-theme cursors, shipped as small SVG cursors in
`themes/<slug>/cursors/` (or `assets/cursors/` when shared), referenced with
a fallback: `cursor: url(…) 0 0, default`.

| Role | Native fallback | Example (windows95) |
|---|---|---|
| Default / controls | `default` (the arrow; see §4) | The black-outlined 95 arrow. |
| Text | `text` | The 95 I-beam. |
| Busy | `progress` / `wait` | The hourglass (`aqua`: the spinning beach ball). |
| Drag | `grab` / `grabbing` | The move cross. |
| Not allowed | `not-allowed` | The 95 circle-slash. |
| Resize | `*-resize` | The 95 double arrows. |

Cursors are off under `data-contrast="high"` and `forced-colors` (where
the OS cursor size and colour settings must win), and all cursor art stays
within the 32×32px that browsers reliably accept.

## 12. Accent and seasonal tinting

- **Who chooses:** the app sets a default accent; the end user can pick
  from the swatches the theme allows (in the `.prefs` panel).
- **The theme decides what is allowed.** Each theme declares an approved
  swatch list (generalising today's `data-accent="1".."4"` on `imac-g3`),
  not a free colour picker, so LCARS stays in its candy palette and every
  swatch is pre-checked for contrast by `check.py`. A theme can also declare
  "no accent choice" (`teletext`'s 8 broadcast colours are the identity).
- **Derived colours follow.** Choosing a swatch re-derives `--accent`,
  `--on-accent`, hover and focus tints with `color-mix()`, so a theme
  doesn't hand-write every variant.
- **Seasonal palettes:** optional named palettes per theme
  (`data-season="winter|spring|summer|autumn|halloween|festive"`),
  switched on by the app (for example by date). They tint accents and
  gutter art only, never the base surfaces, so the theme stays
  recognisable. Off by default.

## 13. Boot and splash screens

A declarative `.splash` component per theme, used two ways:

1. **Real loading** (default): shown while the app is genuinely loading
   (first htmx request, PWA launch). It never adds delay; it is removed
   the moment the app is ready.
2. **Optional timed intro:** an app may play the theme's full boot
   sequence for a set time, as a deliberate flourish:
   `<div class="splash" data-intro="2s">`. Always skippable (any key,
   click or tap), shown at most once per session by the reference script,
   and reduced to a static frame under reduced motion.

| Theme | Splash idea |
|---|---|
| `blue-future` (first) | Telemetry channels initialising one by one, then a cyan "SYSTEM NOMINAL". |
| `msdos` | A BIOS POST: memory count, then `C:\>` with a blinking cursor. |
| `winxp-luna` | The XP boot screen with the three-block progress bar. |
| `windows95` | The clouds splash with the bottom progress strip. |
| `skyrim` | A loading screen: a slowly rotating 3D-ish emblem and a lore tip line. |
| `lcars` | "LCARS ACCESS" with the bars sweeping in. |
| `xmb` | The PS3 wave fading up. |

Markup is plain (`<div class="splash" role="status" aria-live="polite">` with
an optional `<progress>` and message), and all art is CSS or inline SVG.

## 14. Empty, error, offline and 404 states

v4 has a generic `.empty-state`. v5 gives every theme its own voice for the
states users actually hit:

| State | Markup | Example (windows95) |
|---|---|---|
| Empty list or table | `.empty-state` (exists) | A grey folder with nothing in it. |
| Error | `.empty-state.is-error` | The 95 error dialog icon (the red circle and X). |
| Offline | `.empty-state.is-offline` | Unplugged network-cable icon. |
| Not found (404) | `.empty-state.is-404` or a full `404.html` example page | "The page cannot be found" in IE4 style. |
| No permission | `.empty-state.is-locked` | A padlock. |
| Loading | `.empty-state.is-loading` | The hourglass. |

Illustrations are CSS or inline SVG in each theme's language, sized for
Mobile and Desktop, with `alt` text for screen readers. Copy stays the
app's job; the theme supplies only the look (and an optional suggested
heading via `content:` that apps can override).

A ready-made `404.html` example page joins the demo pages, so the Pages
site has a themed 404 too.

## 15. Installed apps: PWA and desktop wrappers

### PWA (`display-mode: standalone` / `window-controls-overlay`)

- Detect installed mode with `@media (display-mode: standalone)` and
  adjust: no browser chrome, so the app bar becomes the title bar.
- Safe areas: `env(safe-area-inset-*)` on the bar, the bottom tab bar
  (§9 #41) and floating buttons, for notched and rounded screens.
- **Window Controls Overlay:** the theme draws the whole title bar,
  using `env(titlebar-area-x|y|width|height)` so content avoids the OS
  controls area, and `app-region: drag` on the bar (with `no-drag` on its
  buttons).
- `theme-color` meta and the manifest's colours follow the active theme
  (a reference snippet updates the meta tag on theme switch).

### Desktop wrappers (Electron, Tauri)

- Frameless windows: the same title-bar layout as the PWA overlay, with
  `-webkit-app-region: drag` regions.
- **Themed window controls:** a declarative `.window-controls` group
  (minimise, maximise/restore, close) that each theme draws in its own
  period style: Windows 95 bevelled grey squares, Windows XP's blue and red
  Luna buttons, Aqua traffic lights on the left, LCARS pills, Liquid Glass
  traffic lights. These reuse the existing `.btn-min`/`.btn-max`/`.btn-close`
  so in-page windows and the real app window match.
- Which side the controls sit on follows the theme (Aqua and Liquid Glass
  on the left, Windows themes on the right), overridable by the app to
  match the host OS.
- The wrapper wires the buttons to the native window API; ftl-themes
  only provides the markup contract and styles.

## 16. Theme families

### Families (theme inheritance)

Several themes are generations of one design: `windows95` → `winxp-luna` →
`win7-aero`; `ios-skeuomorphic` → `ios-flat` → `liquid-glass`; `lcars` and
the `star-trek-*` reference sets; `aqua` and `imac-g3`. Today each one
copies structure and drifts independently.

- A theme declares its parent in its header comment:
  `* Extends: windows95`.
- `build.sh` builds the child bundle as **parent rules + child rules**,
  rewriting the parent's selectors from `html[data-theme="windows95"]` to
  the child's slug. The child overrides only what changed. There is no
  runtime cost: the result is one flat bundle, as today.
- `check.py` lints the chain (no cycles, the parent exists, the child
  still sets every required token, directly or through the parent).
- Each theme's README gains a "Family" line, and the gallery groups
  families together.
- First candidates: the Windows line and the iOS line. Each family's base
  theme is refactored so that structure lives in the base and
  period-specific paint in the children.

## 17. Fidelity scoring

A tool that measures how close each theme is to its references, and
reports it. It does **not** fail the build.

- **Inputs:** each theme's `references/<theme>/` images and RESEARCH.md
  (which already list sampled hex values, fonts and component mappings).
- **Measures:**
  - Palette match: the sampled reference colours against the rendered
    theme's dominant colours (ΔE distance).
  - Typography: whether the fonts named in RESEARCH.md are in use, and
    whether case, tracking and weight match.
  - Signature details: a per-theme checklist from the README's
    "Tell-tales of an inauthentic result", checked on the rendered page
    where it can be automated, and scored by hand where it can't.
  - Component coverage: which components have a matching reference image.
    This also generates the "references wanted" list.
- **Output:** a score out of 10 per theme and per component, shown on its
  gallery card and in its README. A drop between releases is flagged in
  the check output but doesn't fail anything.

## 18. Data and dashboards

### Advanced tables (beyond inline editing, §7)

| Feature | Markup | Notes |
|---|---|---|
| Column resize handle | `<th class="is-resizable">` | Styled handle and resize cursor; the app does the resizing. |
| Column reorder | `<th draggable="true">` | Drag ghost, drop indicator between columns. |
| Frozen columns | `.table.is-frozen-1` / `-2` | Sticky first one or two columns, with a shadow edge when scrolled. |
| Row grouping | `<tbody class="table-group">` with a group header row | Collapsible through `<details>`-style toggle; group totals row. |
| Tree rows | `<tr data-level="2">` | Indentation and expand/collapse markers from the level. |
| Selection column | checkbox in the first cell, `<tr aria-selected="true">` | Plus a **bulk-action bar** (`.bulk-bar`) that appears above the table while rows are selected (Playlist Lab already builds one). |
| States | `.table.is-loading`, `.table-empty`, `.table-more` | Skeleton rows, an empty row with `.empty-state`, and an infinite-scroll "loading more" row. |
| Density | `.table.is-compact` / `.is-comfortable` | Ties into `data-density` (§10). |

### Charts: a library-neutral styling contract

ftl-themes doesn't pick or bundle a chart library. It defines how a chart
*looks* in each theme, through tokens and plain SVG/HTML hooks that any
library, or hand-written SVG, can use.

**The contract:**

1. **A `.chart` container** sets `color` to the theme's chart foreground,
   so anything drawn with `currentColor` (axes, ticks, labels, grid) follows
   the theme, and gives the plot a transparent background.
2. **Series colours:** every theme defines a validated six-colour
   categorical palette, `--chart-1` … `--chart-6`. They are distinct from
   each other, at least 3:1 against the chart background, and still
   distinguishable under the common colour-vision deficiencies.
   `check.py` validates all of it. Themes with tiny palettes (`teletext`,
   `nokia-3310`) also define `--chart-dash-1..6` dash patterns so series
   stay distinguishable beyond the colours.
3. **Sequential and diverging scales** for heatmaps and choropleths:
   `--chart-seq-0..8` and `--chart-div-neg|mid|pos`.
4. **Chart chrome tokens:** grid line, axis line, tick text, plot frame,
   crosshair, selection and focus highlight, annotation, and the tooltip
   (which reuses the existing `--tooltip-*` tokens). Themes can add a
   signature frame (an oscilloscope graticule for `blue-future`, a
   phosphor glow for `matrix`).
5. **Plain-SVG class hooks** for libraries and hand-written SVG that emit
   classes: `.chart-grid`, `.chart-axis`, `.chart-series` with
   `data-series="1..6"`, `.chart-point`, `.chart-label`, `.chart-legend`.
   Core styles them from the tokens.
6. **Adapters are recipes, not dependencies.** CONTRACT.md documents how
   to feed the tokens to popular libraries, each a few lines of CSS or
   config: TanStack Charts (map `--ts-chart-1..6` and
   `--ts-chart-tooltip-*` onto ftl tokens), Chart.js and ECharts (read the
   tokens with `getComputedStyle` into their options), and Observable Plot
   and D3 (use the class hooks). None of them ships in ftl-themes.
7. **CSS-only charts stay:** today's `.bar-chart` plus the donut (§9 #10)
   cover bar, column, stacked and donut with no JS and no library.
8. **A `charts.html` example page** draws the same charts in plain inline
   SVG using the class hooks, in every theme, each with its accessible
   data table (required for every chart example).

Reviewed while designing this: [TanStack Charts](https://github.com/TanStack/charts)
(MIT, alpha). Its approach (inherit `currentColor`, transparent
background, colours as CSS custom properties overridable at any container)
is the model for this contract, and it gets an adapter recipe like the
others.

### Live-data states

| State | Markup | Look |
|---|---|---|
| Value changed | `.is-updated` (app adds, removes after ~1s) | A brief theme flash (cyan glow for `blue-future`, inverse flash for `msdos`), with reduced motion: a static marker. |
| Up / down change | `.is-up` / `.is-down` | Semantic colour plus an arrow, never colour alone. |
| Stale | `.is-stale` + `data-age="5m"` | Dimmed, with an "out of date" marker. |
| Connection | `.connection` with `data-state="live|reconnecting|offline"` | A lamp plus label, for the bar or status strip. |
| Last updated | `<time class="updated">` | "Updated 5s ago" styling; the app updates the text. |
| Streaming feed | `.log` (exists) + `.feed` | New lines slide in; auto-scroll pause marker when the user scrolls up. |

### Dashboard widget grid

- `.dashboard` is a CSS grid of `.widget`s that each span
  `--cols`/`--rows`, reflowing per tier (§2): one column on Mobile, two or
  three on Tablet, up to twelve on Desktop and XL.
- Styled edit mode for apps that let users rearrange: `.dashboard.is-editing`
  shows drag handles, resize corners, drop placeholders and an add-widget
  tile. The app moves things; ftl-themes styles every state.
- Widgets use container queries, so each one lays itself out for its
  actual size (a stat tile at 1×1 versus 2×2).
- Saved-layout states: unsaved changes marker, reset-to-default control.

## 19. Component kits

Kits are groups of components for one kind of app, built from core
components and themed like everything else. Each gets its own example
page.

### Music and media (Playlist Lab first)

Track rows (number, art, title, artist, duration, hover play button),
album-art grid, now-playing bar (with progress scrubber and volume),
play queue, waveform scrubber, shuffle/repeat/like toggle states, lyrics
view with the current line highlighted, and a mini-player. The existing
`.transport` controls and `soundmixer.html` become part of this kit. A new
`player.html` example page.

### Game HUD

Health, mana and stamina bars (generalising `skyrim`'s), a minimap frame
(using `.map`, §9), quest tracker, hotbar and inventory slots with
rarity colours, floating damage numbers, achievement toast, and key-prompt
hints ("[E] Open"). Fits `skyrim`, `pipboy`, `xmb`, `cassette-futurism`;
any theme can use it. A new `hud.html` example page.

### Collaboration

Presence avatar stack ("3 people viewing"), live cursors with name
labels, comment threads with replies and resolved state, @mention chips
and suggestion list, and the existing typing indicator (`.typing`).

### Notifications and activity

A notification centre (panel or drawer) with unread and read states,
grouped notifications ("3 new comments on…"), per-item actions, a
do-not-disturb state, an activity feed timeline, and the unread badge on
the bell (§9 #23).

## 20. Tooling and docs

### Component docs site

The Pages site gains a page per component: live example, every state, a
theme picker, the markup to copy, the tokens a theme can set, and
accessibility notes. Generated from one source per component, so docs,
`components.html` and CONTRACT.md can't drift. The gallery links into it.

### Keyboard layer

- `.shortcuts` overlay (opened by `?`), listing the app's shortcuts in
  the theme's style.
- `<kbd>` hints in menus, tooltips and buttons, with platform-aware
  symbols (⌘ vs Ctrl) chosen by the app.
- Roving-focus styles for grids, lists, toolbars, tabs and menus, so arrow
  -key navigation shows clearly where focus is.
- Visible focus is checked on every new component.

### Performance budgets

- `check.py` gains size budgets: per theme bundle (gzipped), per font file
  and total fonts per theme. A theme over budget is reported, then fails
  once v5 ships.
- Fonts subset to the characters each theme uses (Latin plus the theme's
  glyphs), done by `build.sh`.
- Render cost: the rendered check measures frame time with heavy effects
  (backdrop blur, glow, large shadows) on a scrolling page, and flags
  themes that drop frames on the Mobile tier. `prefers-reduced-transparency`
  and `data-transparency="reduced"` remain the escape hatch.

### Theme scheduling and easter eggs

- **Scheduling:** apps can switch theme, variant or seasonal palette by
  time of day or date through `theme-loader.js`
  (`schedule: [{ from: "19:00", variant: "night" }, …]`), and the user's own
  `.prefs` choice always wins.
- **Easter eggs: off unless the app opts in**
  (`<html data-easter-eggs>`). Harmless, skippable, and never block input.
  Ideas: the Konami code turns on `lcars` red alert; a Windows 95 "It looks
  like you're writing a letter" helper on long text areas; the Matrix
  digital rain behind an idle screen; a Skyrim "arrow to the knee" toast
  after the 10th error. Each lives in the theme's own folder, with a list
  in its README.

## 21. New themes for v5

Three new themes, built with the same process as `tokie`, `silo`,
`westworld` and `skyrim` (reference images first, then the theme), and v5
ready from the start: all tiers, touch, spacing tokens, chart palette,
gutter art and the experience layer.

| Slug | Source | Signature details | Layout idea |
|---|---|---|---|
| `teenage-engineering` | Teenage Engineering OP-1 / OP-Z | Off-white aluminium surfaces, tiny monochrome display graphics, the four colour-coded encoders (blue, green, white, orange) as the accent set, playful pixel animations, tight grotesque type. | The display is a dark inset "screen" panel in a light hardware body; the four encoder colours drive tabs, sliders and chart series. Knobs (`.knob`) become the signature control. |
| `cyberpunk-2077` | Cyberpunk 2077 HUD and menus | Red/cyan on near-black, angular cut corners, glitch offsets on hover and alerts, scanline noise, the netrunner breach grid for tables, heavy condensed caps. | Angular cut panels, a top HUD bar, and a breach-grid table style. Glitch motion only under full motion settings. |
| `motorsport-telemetry` | Broadcast F1-style timing graphics and a modern car dash | Tyre-compound colours (soft red, medium yellow, hard white) as semantic colours, purple/green/yellow sector times, delta bars, rev-light strips, carbon-fibre texture, tabular figures everywhere. | A timing-tower rail on the left, the dial gauge (§9 #1) as a rev counter, and the live-data states (§18) as the default look. |

Notes:

- **Brands:** these themes are *inspired by* the source UIs. They don't use
  the companies' logos or trademarks (no F1 logo, no Teenage Engineering or
  CD PROJEKT marks); that is why the motorsport theme is named
  generically. References follow the same rules as today: credited,
  openly licensed or fair-use reference stills, kept in
  `references/<slug>/`.
- **References wanted** lists get produced as part of building each theme,
  as they were for the last eight.

## 22. Content, page templates and kits

### Prose and Markdown (`.prose`)

A `.prose` wrapper that styles raw HTML from Markdown or a CMS, with no
classes inside: headings, paragraphs, lists (nested), block quotes,
footnotes, definition lists, tables, images and figures with captions,
horizontal rules, `<kbd>`, `<mark>`, `<abbr>`, and `<details>`.

- **Readable measure:** text capped at about 70 characters per line, with
  wide media and tables allowed to break out to the container width.
- **Vertical rhythm** from the spacing scale (§5), per tier.
- **Code blocks:** `<pre><code class="language-*">` styled with a **per-theme
  code palette** (`--code-keyword`, `--code-string`, `--code-comment`,
  `--code-number`, `--code-function`, …), library-neutral like charts:
  it targets the class names that Prism, highlight.js and Shiki emit,
  without bundling any of them. Line numbers, highlighted lines, a copy
  button style, and diff (`+`/`-`) lines.
- **Callouts:** `> [!NOTE]` / `[!WARNING]`-style blocks (GitHub's syntax,
  which most Markdown renderers output as `<blockquote>` or `<div>`
  markers), mapped to the alert colours.

### Page templates

Ready, responsive example pages that combine existing components. Each
one is a plain HTML file apps can copy, and each passes the tier checks:

| Template | Contents |
|---|---|
| `auth.html` | Sign in, sign up, forgot password, 2FA code entry (a one-time-code input with per-digit boxes), and "check your email". |
| `settings.html` | A settings page with section nav (sidebar on Desktop, a list that drills in on Mobile), forms, toggles, the `.prefs` panel (§10) and a danger zone. |
| `master-detail.html` | A list and a detail pane side by side on Desktop; on Mobile the detail slides over the list with a back button. |
| `inbox.html` | A three-pane split view (folders, list, reading pane) that collapses per tier. |
| `onboarding.html` | A stepper (§9 #44) wizard with progress, skip and back. |
| `pricing.html` | Plan cards with a highlighted plan, feature comparison table, and billing toggle. |
| `404.html` | The themed not-found page (§14). |

### Productivity kit

Built on the same declarative approach as the other kits (§19), with a
`planner.html` example page:

- **Kanban board:** columns, cards with labels, assignees and due dates,
  WIP limits, drag states (the app moves cards), and horizontal scrolling
  on Mobile.
- **Calendar:** month, week and day views, with events spanning days,
  overlapping events side by side, "today" and the current-time line,
  and an agenda list on Mobile. Shares the `.calendar` grid of the date
  picker (§9 #26).
- **Gantt timeline:** task bars on a time axis, dependencies as connectors,
  milestones, progress fill, and a today marker. Horizontal scroll with
  the task list frozen.
- **Schedule list:** time-blocked agenda rows (`.schedule` exists and is
  extended).

### Themed HTML emails

Transactional email templates that match the app's theme: welcome,
verify email, reset password, receipt/invoice, alert or notification,
and weekly digest.

- **Built for email clients:** table-based layout, all CSS inlined at
  build time, no custom properties, web fonts or `@layer` (email clients
  don't support them), 600px wide, images with fallbacks, and plain-text
  versions.
- **Theme-flavoured, not theme-perfect:** each theme's email keeps its
  palette, header style and one signature detail (an LCARS elbow header
  image, a Windows 95 title bar), since effects like blur and glow don't
  survive email clients.
- **Generated:** `build.sh` resolves each theme's tokens to literal values
  and writes `dist/email/<slug>/*.html`.
- Tested against the common clients' rules (Gmail, Outlook, Apple Mail),
  including their dark-mode rewriting.

## 23. Theme identity across the catalogue

### Custom icon sets for every theme

Today the generic sprite has about 1,000 icons; 24 themes redraw between 54
and 205 of them, and 18 themes redraw none (including all eight newest).
v5 gives **every theme a full redraw of the core UI set** (the icons
components use: navigation, actions, status, media, files, about 150),
in its own style: pixel icons for `msdos`, line glyphs for `lcars`,
debossed gold for `tokie`, Futura-style rune-like strokes for `skyrim`.

- The build reports coverage per theme; a theme is "icon complete" when it
  redraws the whole core set.
- `docs/icon-library-roadmap.md` gets the per-theme style rules (stroke
  width, grid, corner style) so redraws stay consistent.

### Signature navigation per theme

Each theme can offer its source's own navigation pattern, opt in, on top
of the standard shell. The markup stays the same nested `<ul>` used for
menus (§8), so an app switches pattern without changing markup:

| Theme | Signature navigation |
|---|---|
| `windows95` / `winxp-luna` / `win7-aero` | The Start menu (nested `ul` with cascading submenus) and the taskbar. |
| `xmb` | The cross media bar: categories across, items down. |
| `lcars` | Panel buttons down the rail with the elbow. |
| `skyrim` | The skills constellation for a top-level map of sections. |
| `ios-*` / `liquid-glass` | The home-screen icon grid and the dock. |
| `pipboy` | STAT / INV / DATA top tabs with sub-tabs. |
| `aqua` | The Dock with magnification. |

A theme without a signature pattern falls back to the standard nav. On
Mobile, every pattern reduces to a touch-friendly equivalent.

### Authentic fonts

Many themes use stand-ins (Antonio for LCARS's Swiss 911 and for Skyrim's
Futura, Tahoma for MS Sans Serif, Arial for Helvetica). v5 replaces stand-ins
with **open-licensed faces closer to the originals** where one exists, for
example a pixel MS Sans Serif-style face for `windows95` and a geometric
Futura-like face for `skyrim`.

- Only fonts under the SIL OFL or an equally permissive licence, recorded in
  `assets/fonts/NOTICE.md` as today.
- Subset to what each theme uses, within the font budgets (§20).
- A theme's README records the original face, the chosen substitute, and
  why.

### Favicons and share cards

- A **per-theme favicon and app icon set** (SVG favicon plus PNG sizes and a
  maskable icon for PWAs), generated from one SVG template per theme;
  `theme-loader.js` swaps the favicon with the theme.
- An **Open Graph share-image template** per theme (1200×630), as an HTML
  page apps can screenshot or render server-side with their own title, so
  shared links look on-theme.

## 24. Quality and contributing

### Firefox and WebKit testing

The rendered checks (`core_regressions.mjs`, the tier and overflow checks)
and the screenshot baselines run in **Chromium, Firefox and WebKit**
through Playwright. WebKit matters most: every iPhone browser uses it.
Engine-specific differences get a known-issue list rather than silent
failures.

### Automated accessibility audits

**axe-core** runs on every example page, in every theme, at the Mobile and
Desktop tiers, alongside the existing contrast and target-size checks.
Results are reported per theme in the gallery and in the check output;
serious and critical issues fail the check once v5 ships.

### Browser support policy

**Baseline 2026**: every feature v5 relies on must be Baseline (available
in Chrome, Edge, Firefox and Safari on desktop and mobile) by 2026.
Anything newer is progressive enhancement with a tested fallback.
Statuses below come from the `web-features` data (checked 2026-10-02):

| Feature | Baseline since | Used for | Fallback |
|---|---|---|---|
| Container queries (size) | 2023 | Component tiers (§2) | Not needed. |
| `:has()` | 2023 | State styling | Not needed. |
| Popover API | 2025 | Menus, dropdowns, modals (§6) | Not needed. |
| `::details-content` | 2025 | `.nav-collapse` | Not needed (v4's display rule kept for older engines). |
| View transitions (same-document) | 2025 | Theme switching (§11) | Not needed. |
| Invoker commands (`command`/`commandfor`) | 2025 | Opening dialogs and popovers with no JS (§6, §9) | Not needed. |
| `@starting-style`, `transition-behavior` | 2024 | Enter/exit motion | Not needed. |
| Container **style** queries | **2026** | Components reading `--tier` directly: `@container style(--tier: mobile)` | Not needed. |
| `field-sizing: content` | **2026** | Auto-growing inputs in editable cells and textareas (§7) | Not needed. |
| `sibling-count()` / `sibling-index()` | **2026** | Staggered motion, avatar stacks, spacing that depends on item count | Not needed. |
| CSS anchor positioning | not yet | Placing and flipping popovers (§6) | Below the trigger, no flipping. |
| Cross-document view transitions | not yet | Transitions between pages | Instant navigation. |
| Customizable `<select>` (`appearance: base-select`) | not yet | Fully themed select lists | v4's styled native select. |
| `interpolate-size` / `calc-size()` | not yet | Animating to `height: auto` (accordions) | Instant open. |
| Scroll-driven animations | not yet | Scroll-linked effects | None (static). |

The rendered checks run in all three engines (above), so a feature that
isn't Baseline is caught by its fallback being tested.

### Theme contribution kit

A documented path for adding a theme, based on how the last eight were
built:

1. `docs/contributing-a-theme.md`: the checklist from brief to merge.
2. **Reference gathering:** what to collect, naming
   (`references/<slug>/` with camelCase component filenames, variant
   subfolders), licences and credits, and RESEARCH.md's required sections.
3. **The agent brief** used for `tokie`, `silo`, `westworld` and `skyrim`,
   cleaned up as a reusable template, including the rule to vendor fonts in
   `assets/fonts/`.
4. **`scripts/theme-ready.sh <slug>`:** runs the lint, the rendered checks
   at all tiers, axe, the budgets and the fidelity score, and prints a
   "ready for review" report.
5. The gallery's "references wanted" list as the place contributors can
   help without building a theme.

## 25. Considered and not planned

From the same review, these were offered and **not chosen** for v5. They
are recorded so they can be revisited:

- A live **theme builder** page with token export.
- Opt-in per-theme **UI sound packs**.
- **Integration** work (no preference given): Go + htmx partials library,
  W3C design-tokens export, versioned CDN/npm packages, and per-component
  split bundles. v5 keeps today's distribution (git submodule, `dist/`).
- **RTL and i18n** font fallbacks, and theme-specific **print/PDF** styles.
- **Light/dark pairs for every theme** (a `data-scheme="light|dark|auto"`
  axis alongside palette variants). Deferred for now; v4's existing dark
  and light variants (e.g. `ios-flat`, `liquid-glass`) stay as they are.
- **Bundling or depending on a chart library.** Chart styling stays
  library-neutral (§18).
- **Scoped / nested themes** (`data-theme` on any element, so a Windows 95
  window can sit inside an LCARS page). Not chosen; themes stay
  page-wide. Note that the family build (§16) keeps this possible later,
  since bundles stay selector-based.

## 26. Rollout

**Progress (2026-10-03):** phases 0–4b done and on the live site: harness,
core layout (tiers, XL cap and gutter art, spacing, `--z-*`, container
queries, top-layer popovers), touch and hover gating, tables and nested
menus, the six component groups, the experience layer, CSS-only tabs,
panes and selection. All 41 themes rolled out to v5 layout. Phase 4d/4e
partly done: social/collaboration, game HUD (`hud.html`), media
(`player.html`) and productivity (`planner.html`) kits; `.prose`, code
palettes and six page templates; themed emails (`dist/email/`); theme
scheduling; Firefox/WebKit switches, axe (`a11y_audit.mjs`), budgets,
render cost and `theme-ready.sh` with the contribution kit; and the three
new themes `teenage-engineering`, `cyberpunk-2077` and
`motorsport-telemetry` (45 themes). In progress: the per-theme
colour-contrast sweep from the axe audit. Still to do: theme families
(§16), fidelity scoring (§17), live-data states and the dashboard grid
(§18), the docs site (§20), easter eggs, and the rest of the §23 identity work (fonts,
signature navigation). Done in §23: every theme icon complete (178-icon
core set), per-theme favicons and app icons, share-card template.

| Phase | Work | Done when |
|---|---|---|
| **0. Harness** | `nesting.html`. The five target viewports in `screenshot_themes.py` and `core_regressions.mjs`. The overflow, target-size and spacing checks (§5) reporting only, not failing yet. | A report shows every theme × viewport × page, and how far each is from passing. |
| **1. Core layout** | Tier media queries, container queries, the 1800px cap, the `--z-*` scale, top-layer popovers and the spacing scale with component `--*-pad` tokens. Proven on `blue-future` only. | `blue-future` passes every check at all five viewports, and its README documents the tiers. |
| **2. Touch** | `--tap-min`/`--hit-min`, `any-pointer: coarse`, hover gating and `touch-action`. | `blue-future` passes the target-size check on Mobile and Tablet. |
| **3. Tables and menus** | Editable cells (§7), stacked tables and nested menus, menubar and tree (§8). | Those sections of `nesting.html` pass on `blue-future`. |
| **4. New components** | The 50 components, in the order of the tables above: instruments first, because they carry the most theme personality. | Each one is on `components.html`, documented in CONTRACT.md, and passes on `blue-future`. |
| **4b. Experience layer** | Accessibility attributes and the `.prefs` panel (§10), forced-colors support, motion tokens and theme-switch transitions (§11), the arrow-cursor change (§4), accent swatches (§12). Proven on `blue-future`. | `blue-future` passes the checks in every `.prefs` combination and under forced colors. |
| **4c. Personality and installed apps** | `.splash` (§13), themed empty/error/404 states (§14), cursor packs (§11), PWA and wrapper title bars with `.window-controls` (§15). | `blue-future` and three contrasting themes (`windows95`, `liquid-glass`, `lcars`) ship all of them. |
| **4d. Data, kits and tooling** | Theme families (§16), advanced tables, the library-neutral `.chart` contract and `charts.html`, live-data states, the dashboard grid (§18), the four kits with `player.html` and `hud.html` (§19), the keyboard layer, budgets and scheduling (§20). The fidelity tool (§17) and docs site (§20) run from here on. | `blue-future` passes every check; Playlist Lab can build its player and tables from the music kit. |
| **4e. Content, identity and quality** | `.prose` and code palettes, the page templates, the productivity kit and the email build (§22); icon redraws, signature navigation, font replacements, favicons and share cards (§23); Firefox and WebKit, axe, the support policy and the contribution kit (§24). The three new themes (§21) are built with the contribution kit, which proves it. | `teenage-engineering`, `cyberpunk-2077` and `motorsport-telemetry` ship v5-ready, and all checks run in three engines. |
| **5. Theme rollout** | Port the other 41 themes in batches of about 8, most-used first. Each batch: spacing tokens, gutter art, close button, motion tokens, accent swatches, chart palette, code palette, full icon set, signature navigation (where the source has one), font review, favicon, email template, splash, empty states, cursors (where the source had distinctive ones), window controls, per-tier check, fidelity score. | Each theme is "v5 ready" in the gallery. The checks switch from reporting to failing per theme once it's ported. |
| **6. Release** | MIGRATING-v5.md, CHANGELOG, and a `v4` branch kept for apps that pin it, as `v3` was. | Tagged v5.0.0. |

## 27. Breaking changes to expect (for MIGRATING-v5.md)

- The 720px breakpoint becomes four tiers. Apps that wrote their own
  `@media (max-width: 720px)` overrides around the shell must re-check
  them.
- `--app-areas-sm` (the one small-screen layout) is replaced by
  `--app-areas-mobile` and `--app-areas-tablet`.
- Default control heights grow to 44px on touch devices. Pages with fixed
  pixel heights around buttons may need adjusting.
- `.app` is capped at 1800px.
- The button-based `.context-menu` is deprecated in favour of the `ul`
  form (it still works in v5).
- Buttons, links and other controls no longer switch to the hand
  pointer; they keep the arrow. Apps that relied on the hand cursor as an
  affordance should rely on the themed hover and focus states instead.
- Themes in a family are rebuilt from a shared base, so small visual
  differences between, say, `winxp-luna` and `win7-aero` may move.
- `theme-loader.js` switches themes through a view transition; apps that
  swap the stylesheet themselves get no transition (but nothing breaks).
- Components gain `container-type`, which makes them containment
  contexts. Apps positioning things relative to the viewport from inside
  a panel should check for side effects.

## 28. Open questions

1. **"iPhone Duo":** a book foldable or a hinged dual-screen device?
   (Decides whether viewport-segment support is in scope.)
2. **Brand buttons (#50):** which companies does Playlist Lab actually
   need? The licensing rules mean each one is added individually.
3. **Dial gauge (#1):** values from `<meter>` (semantic, but no decimals
   in the needle angle) or from a `--value` custom property (precise,
   needs an inline style)? The plan supports both, with `<meter>` as the
   documented default.
4. **Bottom tab bar on Mobile:** should every L1 theme's status strip
   become a tab bar on phones, or only themes whose source had one (iOS,
   Liquid Glass)? Proposed: every theme gets the layout, and each theme
   styles it in its own language.
5. **Accessibility panel storage:** is `localStorage` in the reference
   script enough, or does Playlist Lab want the preferences saved to the
   user's account (so they follow them between devices)?
6. **Timed intros:** should there be a global cap on intro length (e.g.
   3s), even when an app asks for longer?
7. **Cursor packs:** which themes have cursors distinctive enough to be
   worth it? Proposed first set: `windows95`, `winxp-luna`, `aqua`,
   `msdos`, `skyrim`, `steampunk`.
8. **Window controls side:** follow the theme (Aqua left, Windows right)
   or the user's actual OS by default?
9. **Families:** which family first, the Windows line or the iOS line?
10. **Easter eggs:** any you specifically want, or any themes that must
    never have them (for example themes used in professional dashboards)?
11. **Emails:** which email templates does Playlist Lab send today, so
    those come first?
