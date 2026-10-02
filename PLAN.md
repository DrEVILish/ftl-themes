# ftl-themes v5.0 plan

Status: **proposal**, nothing below is built yet. v4 stays the base: the
token contract, the `@layer ui` bundles, the L0/L1 adoption levels and the
42 themes all carry forward. v5 is about three things v4 does not do well:

1. **Fluid mobile, tablet, desktop and wide-screen layouts**, natively, in
   core, so every theme gets them.
2. **Spacing that holds**: correct padding and margins in core and in every
   theme, with no overflow at any supported width.
3. **A bigger component library** (50 new components), with editable
   tables, nesting and nested menus handled properly.
4. **An experience layer**: user accessibility settings, per-theme motion
   and theme-switch transitions, accent and seasonal tints, splash screens,
   themed empty and error states, cursor packs, and installed-app (PWA and
   desktop wrapper) title bars. Added after the 2026-10-02 reviews (§10–20).

**Primary development theme: `blue-future`.** Every v5 change lands in core
first and is proven on `blue-future`. Then the change is rolled out to the
other 41 themes in batches (see [Rollout](#22-rollout)).

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
| Spacing between targets | At least 8px between adjacent targets. | Current. |
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

## 16. Theme families and light/dark pairs

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

### Light/dark pairs (as a variant axis)

Every theme gains its opposite scheme, designed in the theme's own
language rather than inverted (a light `blue-future` is a daylight console
with navy text on pale grey glass, not white-on-cyan).

- Delivered as a **variant**: one slug, one README, one reference set.
  Because several themes already use `data-variant` for palettes
  (`win7-aero`'s 15 colours), the scheme is its own axis,
  `data-scheme="light|dark|auto"`. It composes with palette variants
  (`win7-aero` + `ruby` + dark).
- `auto` (the default) follows `prefers-color-scheme`. Apps can pin it,
  and the `.prefs` panel (§10) offers it.
- Themes whose identity *is* one scheme (`matrix`, `teletext`, `msdos`,
  `death-star`) may declare `scheme: fixed` and skip the pair. The gallery
  says so.
- `check.py` runs every contrast rule on both schemes. `dist/themes.json`
  lists each theme's supported schemes.

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

### Charts: built on TanStack Charts' styling contract

Reviewed: [TanStack Charts](https://github.com/TanStack/charts) (MIT,
v0.18.0, **alpha**: 0.x minor releases may break). What matters for
ftl-themes:

- **It inherits the page instead of bringing a theme.** Axes, text and
  grid use `currentColor`; the chart background is transparent.
- **Colours are CSS custom properties**, overridable at any container:
  six categorical colours `--ts-chart-1` … `--ts-chart-6`, and tooltip
  chrome `--ts-chart-tooltip-background`, `-color`, `-border`,
  `-border-radius`, `-shadow`, `-padding`, `-font`, `-max-width`.
- **Data stays as the app's own arrays and objects**; the chart
  definition maps fields to channels (`x: 'month', y: 'value'`), with
  scales, guides and marks layered on top.
- **Rendering:** SVG (server-renderable) or an opt-in Canvas renderer,
  which re-reads the CSS custom properties when `data-theme`, the colour
  scheme, forced colours or the viewport change.
- **Framework-free:** besides React, Vue and others, it has a **vanilla
  DOM host**, Alpine and Lit adapters. That suits Go + htmx apps, which
  render in the browser (its server-side SVG needs a JavaScript server).
- **Accessibility:** every chart requires an `ariaLabel`, keyboard focus
  across points, and recommends a table when exact values matter.
  Legends use real buttons with `aria-pressed` and 44px targets.

**Plan:**

1. **ftl-themes doesn't bundle a chart library.** It ships the styling
   contract that TanStack Charts (and anything else) reads.
2. A `.chart` container in core sets `color` to the theme's chart
   foreground and maps theme tokens onto TanStack's variables:
   `--ts-chart-1..6` ← the theme's categorical palette
   (`--chart-1..6`), `--ts-chart-tooltip-*` ← `--tooltip-*`. Any app using
   TanStack Charts inside `.chart` is themed with no chart-side code.
3. **Every theme gets a validated six-colour categorical palette**
   (`--chart-1..6`): distinct from each other, at least 3:1 against the
   chart background, and still distinguishable under the common colour-
   vision deficiencies. `check.py` validates all of it. Themes with tiny
   palettes (`teletext`, `nokia-3310`) use patterns or dashes for series
   beyond their colours, which TanStack's mark styles support.
4. **Chart chrome per theme:** tokens for grid lines, axis text, tick
   marks, selection and focus highlights, plus the plot's frame (e.g. an
   oscilloscope graticule for `blue-future`, a phosphor glow for
   `matrix`).
5. **Simple charts stay CSS-only:** today's `.bar-chart` remains for
   bar, column, stacked and donut (§9 #10) with no JS. TanStack is the
   path for line, area, scatter, dense and interactive charts.
6. **A `charts.html` example page** with a pinned, vendored copy of TanStack
   Charts (an exact version, per their alpha policy), showing the same
   charts in every theme, each with its accessible data table.
7. Watch items: alpha API changes (pin and re-test on upgrade), and Canvas
   charts can't be styled by CSS selectors, only through the variables,
   which is fine because ftl-themes is token-based.

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

- **Scheduling:** apps can switch scheme, variant or seasonal palette by
  time of day or date through `theme-loader.js`
  (`schedule: [{ from: "19:00", scheme: "dark" }, …]`), and the user's own
  `.prefs` choice always wins.
- **Easter eggs: off unless the app opts in**
  (`<html data-easter-eggs>`). Harmless, skippable, and never block input.
  Ideas: the Konami code turns on `lcars` red alert; a Windows 95 "It looks
  like you're writing a letter" helper on long text areas; the Matrix
  digital rain behind an idle screen; a Skyrim "arrow to the knee" toast
  after the 10th error. Each lives in the theme's own folder, with a list
  in its README.

## 21. Considered and not planned

From the same review, these were offered and **not chosen** for v5. They
are recorded so they can be revisited:

- A live **theme builder** page with token export.
- Opt-in per-theme **UI sound packs**.
- **Integration** work (no preference given): Go + htmx partials library,
  W3C design-tokens export, versioned CDN/npm packages, and per-component
  split bundles. v5 keeps today's distribution (git submodule, `dist/`).
- **RTL and i18n** font fallbacks, and theme-specific **print/PDF** styles.
- **Scoped / nested themes** (`data-theme` on any element, so a Windows 95
  window can sit inside an LCARS page). Not chosen; themes stay
  page-wide. Note that the family build (§16) keeps this possible later,
  since bundles stay selector-based.

## 22. Rollout

| Phase | Work | Done when |
|---|---|---|
| **0. Harness** | `nesting.html`. The five target viewports in `screenshot_themes.py` and `core_regressions.mjs`. The overflow, target-size and spacing checks (§5) reporting only, not failing yet. | A report shows every theme × viewport × page, and how far each is from passing. |
| **1. Core layout** | Tier media queries, container queries, the 1800px cap, the `--z-*` scale, top-layer popovers and the spacing scale with component `--*-pad` tokens. Proven on `blue-future` only. | `blue-future` passes every check at all five viewports, and its README documents the tiers. |
| **2. Touch** | `--tap-min`/`--hit-min`, `any-pointer: coarse`, hover gating and `touch-action`. | `blue-future` passes the target-size check on Mobile and Tablet. |
| **3. Tables and menus** | Editable cells (§7), stacked tables and nested menus, menubar and tree (§8). | Those sections of `nesting.html` pass on `blue-future`. |
| **4. New components** | The 50 components, in the order of the tables above: instruments first, because they carry the most theme personality. | Each one is on `components.html`, documented in CONTRACT.md, and passes on `blue-future`. |
| **4b. Experience layer** | Accessibility attributes and the `.prefs` panel (§10), forced-colors support, motion tokens and theme-switch transitions (§11), the arrow-cursor change (§4), accent swatches (§12). Proven on `blue-future`. | `blue-future` passes the checks in every `.prefs` combination and under forced colors. |
| **4c. Personality and installed apps** | `.splash` (§13), themed empty/error/404 states (§14), cursor packs (§11), PWA and wrapper title bars with `.window-controls` (§15). | `blue-future` and three contrasting themes (`windows95`, `liquid-glass`, `lcars`) ship all of them. |
| **4d. Data, kits and tooling** | Theme families and the light/dark axis (§16), advanced tables, the `.chart` contract with TanStack Charts and `charts.html`, live-data states, the dashboard grid (§18), the four kits with `player.html` and `hud.html` (§19), the keyboard layer, budgets and scheduling (§20). The fidelity tool (§17) and docs site (§20) run from here on. | `blue-future` passes every check in both schemes; Playlist Lab can build its player and tables from the music kit. |
| **5. Theme rollout** | Port the other 41 themes in batches of about 8, most-used first. Each batch: spacing tokens, gutter art, close button, motion tokens, accent swatches, light/dark pair, chart palette, splash, empty states, cursors (where the source had distinctive ones), window controls, per-tier check, fidelity score. | Each theme is "v5 ready" in the gallery. The checks switch from reporting to failing per theme once it's ported. |
| **6. Release** | MIGRATING-v5.md, CHANGELOG, and a `v4` branch kept for apps that pin it, as `v3` was. | Tagged v5.0.0. |

## 23. Breaking changes to expect (for MIGRATING-v5.md)

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
- A new `data-scheme` attribute (default `auto`) means themes can now
  render light or dark depending on the OS setting. Apps that relied on a
  theme always being dark must pin `data-scheme="dark"`.
- Themes in a family are rebuilt from a shared base, so small visual
  differences between, say, `winxp-luna` and `win7-aero` may move.
- `theme-loader.js` switches themes through a view transition; apps that
  swap the stylesheet themselves get no transition (but nothing breaks).
- Components gain `container-type`, which makes them containment
  contexts. Apps positioning things relative to the viewport from inside
  a panel should check for side effects.

## 24. Open questions

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
9. **Charts:** TanStack Charts is alpha. Is a pinned 0.x version
   acceptable for Playlist Lab, or should the `.chart` contract stay
   library-neutral, with TanStack only on the example page?
10. **Families:** which family first, the Windows line or the iOS line?
11. **Fixed-scheme themes:** agree the list that skips a light/dark pair?
    Proposed: `matrix`, `teletext`, `msdos`, `death-star`, `pipboy`.
12. **Easter eggs:** any you specifically want, or any themes that must
    never have them (for example themes used in professional dashboards)?
