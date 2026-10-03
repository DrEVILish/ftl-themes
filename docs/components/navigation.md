# Navigation and structure (v5)

Source: `core/components/navigation.css` (built into every bundle after
`core.css`). Live page: `components-navigation.html`. Scope: PLAN.md §9
#37, #39–#46 and the §20 keyboard layer.

Shared rules for everything below:

- Markup is native elements plus a class or two. State lives in standard
  attributes (`aria-current`, `aria-selected`, `aria-expanded`,
  `aria-checked`) or an `.is-*` class. The app supplies the behaviour:
  closing tabs, filtering, arrow keys, dragging.
- Every control reaches `--tap-min` (44px on touch tiers and coarse
  pointers, 24px on desktop) without changing how it looks.
- Hover styles sit inside `@media (hover: hover)`. Each one has a
  `:focus-visible`, `:focus-within` or attribute equivalent.
- Motion only runs under `prefers-reduced-motion: no-preference`, and
  `html[data-motion="reduced"]` stops it.
- Every token falls back to the base tokens, so a theme that sets nothing
  still gets a correct result.

---

## Closable tabs (`.tab` + `.btn-close`, `.tabs.is-scroll`, `.tab-add`)

```html
<div class="tabs is-scroll" role="tablist" aria-label="Open files">
  <div class="tab is-active">
    <button role="tab" aria-selected="true" aria-controls="p1">index.html</button>
    <button class="btn-close" tabindex="-1" aria-label="Close index.html"></button>
  </div>
  <div class="tab is-dirty">
    <button role="tab" aria-selected="false" tabindex="-1">app.css</button>
    <button class="btn-close" tabindex="-1" aria-label="Close app.css (unsaved)"></button>
  </div>
  <button class="tab-add" aria-label="New tab"></button>
</div>
```

A button can't contain a second button, so a closable `.tab` is a
wrapper. Its first child is the tab and the `.btn-close` sits next to it.
Plain `<button class="tab">` tabs still work in the same strip.

**States:** `.is-active` (core). `.is-dirty` puts a dot before the name,
so unsaved changes are shown by a shape as well as colour. Long names
truncate at `--tab-max`. `.tabs.is-scroll` keeps the strip on one row and
scrolls it sideways on every tier. `.tab-add` sticks to the end of the
strip while it scrolls. Put an `.icon` inside `.tab-add` to replace the
`+` glyph.

| Token | Default |
|---|---|
| `--tab-max` | `14rem` (label width before truncation) |
| `--tab-dirty-glyph` / `--tab-dirty-fg` | `"●"` / `currentColor` |
| `--tab-close-fg` | `inherit` (the tab's text colour, so it reads on filled tabs) |
| `--tab-add-glyph` | `"+"` |
| `--tab-add-bg` / `--tab-add-bg-hover` / `--tab-add-fg` | `--surface` / `--surface-2` / `--muted` |
| all `--tab-*` from core | unchanged |

**Touch:** the tab button, the close button and the add button each
reach `--tap-min`. On a touch tier the close button is a full 44px target
inside the tab.

**Accessibility:** give each close button `tabindex="-1"` and a name that
includes the tab's name. Let Delete (or Ctrl+W) on the focused tab close
it. This is the pattern browsers and editors use. It keeps the tablist
holding only tabs in the Tab order.

---

## Menu bar (`ul.menubar`)

```html
<ul class="menubar" role="menubar" aria-label="Editor">
  <li role="none" class="has-submenu">
    <button role="menuitem" aria-haspopup="menu" aria-expanded="false">File</button>
    <ul role="menu">
      <li role="none"><button role="menuitem">New file <kbd>Ctrl+N</kbd></button></li>
      <li role="none" class="has-submenu"><button role="menuitem" aria-haspopup="menu">Open recent</button>
        <ul role="menu"><li role="none"><button role="menuitem">index.html</button></li></ul></li>
      <li role="separator"></li>
      <li role="none"><button role="menuitem" aria-disabled="true">Save all</button></li>
    </ul>
  </li>
  <li role="none" class="has-submenu is-end">…</li>
</ul>
```

This is the same nested-list markup as the `.context-menu`. Core's "v5
nested menus" rules show and hide the submenus and draw the separators.
This component styles the bar and its dropdown panels.

**States:**

- A top item opens its panel on hover, on keyboard focus or a tap
  (`:focus-within`), or when the app sets `aria-expanded="true"`. That
  attribute works on nested items as well, and in `.context-menu`.
- The open top item is highlighted.
- `li.is-end` aligns a panel to the item's end edge, for the last menu
  near the right edge.
- `aria-disabled="true"` or `disabled` dims an item.
- `role="menuitemcheckbox"` and `role="menuitemradio"` with
  `aria-checked="true"` show a tick. These two rules also apply to the ul
  `.context-menu`.
- A `<kbd>` inside an item prints the shortcut at the item's end (see
  [Keyboard layer](#keyboard-layer)).

**Tiers:** on desktop with a hovering pointer, deeper levels fly out to
the side. On touch tiers they expand inline under their item, as core
does for the context menu. The top-level panel always drops down.

| Token | Default |
|---|---|
| `--menubar-bg` / `--menubar-fg` | `--surface` / `--text` (transparent inside `.app-bar`) |
| `--menubar-rule` / `--menubar-rule-width` | `--border` / `1px` |
| `--menubar-pad` / `--menubar-gap` | `--space-3xs` / `0` |
| `--menubar-font-size` | `0.9em` |
| `--menubar-item-radius` | `--radius` |
| `--menubar-item-bg-active` / `--menubar-item-fg-active` | `--accent` / `--on-accent` |
| `--menubar-panel-min` | `12rem` |
| `--menu-check-glyph` | `"✓"` |
| panels and items | `--context-menu-*`, then `--dropdown-*` (shared with the context menu) |

**Accessibility:** the app implements the WAI-ARIA menubar keyboard
model (Left and Right between menus, Down to open, Esc to close) and
keeps `aria-expanded` in sync. Without JS the menus still work with Tab
and hover, through `:focus-within`.

---

## Tree view (`ul.tree`)

```html
<ul class="tree" aria-label="Files">
  <li><details open><summary><svg class="icon"><use href="…#icon-folder"/></svg>src</summary>
    <ul>
      <li><a href="/app.js" aria-current="page">app.js</a></li>
      <li><span>LICENSE</span></li>
    </ul></details></li>
</ul>
```

`<details>`/`<summary>` expand and collapse branches with no JS. Rows are
the `<summary>` and any `a`, `button` or `span` placed directly in an
`<li>`. Leaves line up with the branch labels, and each level draws a
guide line.

**Selected:** set `aria-current` (links), `.is-selected`, or
`aria-selected="true"` on an `<li role="treeitem">`. The selected row
gets a background, a leading marker and bold text, so it doesn't rely on
colour alone.

**With roles** (only for an app that adds arrow-key navigation):
`ul[role=tree] > li[role=treeitem][aria-expanded][aria-selected] >
details > summary`, with nested `ul[role=group]`. Without that JS, leave
the roles off. Plain nested lists of disclosures are already accessible.

| Token | Default |
|---|---|
| `--tree-font-size` | `0.9em` |
| `--tree-indent` | `0.5em` (added to the marker column) |
| `--tree-guide` | `--hairline` |
| `--tree-glyph` / `--tree-glyph-fg` | `"▸"` (rotates when open) / `--muted` |
| `--tree-item-fg` / `--tree-icon-fg` | `--text` / `--muted` |
| `--tree-item-radius` | `--radius` |
| `--tree-item-bg-selected` / `--tree-item-fg-selected` | `--row-selected-bg` / `--row-selected-fg` |
| `--tree-selected-marker` | `inset 0.2rem 0 0 var(--accent)` |

**Touch:** each row is `--tap-min` tall, so a phone tree is roomier than
a desktop tree.

---

## Bottom tab bar (`.tabbar`)

```html
<nav class="tabbar" aria-label="Primary">
  <a href="/" aria-current="page"><svg class="icon">…</svg><span>Home</span></a>
  <a href="/inbox"><svg class="icon">…</svg><span>Inbox</span><span class="badge badge-accent">3</span></a>
</nav>

<!-- as the shell's status row -->
<nav class="app-status tabbar" aria-label="Primary">…</nav>
```

The mobile primary nav. Items share the width equally and show the icon
over the label. Labels truncate. The children can be `<a>` or
`<button>`.

**States:** active is `aria-current`, `aria-selected="true"` or
`.is-active`. It changes the colour and weight and adds a top indicator
bar. A `.badge` sits on the icon's corner.

**Safe area:** padding includes `env(safe-area-inset-*)`, so the bar
clears the home indicator. This needs `viewport-fit=cover` in the
viewport meta, otherwise the insets are 0.

| Token | Default |
|---|---|
| `--tabbar-bg` / `--tabbar-fg` | `--surface` / `--muted` |
| `--tabbar-fg-active` / `--tabbar-fg-hover` | `--accent-text` → `--accent` / `--text` |
| `--tabbar-indicator` / `--tabbar-indicator-width` | `currentColor` / `2px` |
| `--tabbar-rule` / `--tabbar-rule-width` | `--border` / `1px` |
| `--tabbar-height` | `3.25rem` (never below `--tap-min`) |
| `--tabbar-icon-size` / `--tabbar-label-size` | `1.5rem` / `0.7rem` |

The bar doesn't hide itself on desktop. An app that switches between a
tab bar and a rail by tier does that in its own layout.

---

## Bottom sheet (`.sheet`)

```html
<button class="btn" commandfor="share" command="show-modal">Share</button>
<dialog class="sheet" id="share" aria-labelledby="share-title">
  <div class="sheet-header">
    <h2 id="share-title">Share</h2>
    <button class="btn-close" aria-label="Close" commandfor="share" command="close"></button>
  </div>
  …
</dialog>

<!-- light-dismiss form -->
<div class="sheet" popover id="actions" aria-label="Actions">…</div>
```

The mobile counterpart of `.modal` and `.dropdown`. It is anchored to the
bottom edge and is full width up to `--sheet-max` (centred on wider
screens). It has rounded top corners, a drag-handle mark, its own scroll
(`overscroll-behavior: contain`) and safe-area padding at the bottom. It
opens with `showModal()`, the `commandfor`/`command` invokers, or as a
`popover`. When motion is allowed it slides up as it opens. The handle
is only a visual: swipe-to-dismiss is the app's job. `.sheet-header`
lays out a title and a `.btn-close`.

| Token | Default |
|---|---|
| `--sheet-bg` / `--sheet-border` | `--modal-bg` → `--panel-bg` → `--surface` / `--modal-border` → `--border` |
| `--sheet-radius` | `calc(var(--radius) * 3)` (square themes stay square) |
| `--sheet-pad` | `--space-m` (published as `--surface-pad`) |
| `--sheet-max` / `--sheet-max-height` | `40rem` / `85dvh` |
| `--sheet-shadow` | `0 -4px 24px rgba(0,0,0,.3)` |
| `--sheet-handle` / `--sheet-handle-width` | `--border` / `2.25rem` |
| `--sheet-header-fg` | `inherit` |
| backdrop | `--overlay-bg`, `--overlay-blur` (same as the modal) |

**Accessibility:** a modal `<dialog>` traps focus and closes on Esc
natively. Give it `aria-labelledby` pointing at its title.

---

## Collapsible nav rail (`nav.nav-rail`)

```html
<nav class="nav-rail" aria-label="Sections">
  <h3>Mail</h3>
  <a class="nav-item" href="/inbox" aria-current="page"><svg class="icon">…</svg><span>Inbox</span><span class="badge">12</span></a>
  <a class="nav-item" href="/starred"><svg class="icon">…</svg><span>Starred</span></a>
</nav>
```

**Why not `.app-rail.is-collapsible`?** In the shell contract `.app-rail`
is decorative, `aria-hidden` and `pointer-events: none`. Themes paint it
with element selectors, and LCARS even writes labels into it with
`::before`/`::after`. A navigation list inside it would sit under that
artwork and lose to the themes' specificity. So the rail that navigates
is its own element, built from core's `.nav-item`. Place it wherever the
app's layout wants, for example beside the content in a `.row`, or as a
sticky first column inside `.app-main`. The shell's `.app-rail` stays
the theme's decoration.

**Tiers:** labels show on desktop and XL. At 900px and below the rail is
icon-only. Labels are visually hidden but stay the links' accessible
names. Badges move to the icon's corner. `.is-collapsed` forces icon-only
at every width, and `.is-expanded` forces labels. Use these for the
app's own toggle button, with `aria-expanded` on that button. Headings
(`h2`–`h4` or `.nav-rail-heading`) hide when the rail is collapsed.

**States:** `.is-active` or `aria-current` adds a background and a
leading marker bar.

| Token | Default |
|---|---|
| `--nav-rail-width` / `--nav-rail-collapsed-width` | `14rem` / `max(--tap-min, 2.75rem)` + padding |
| `--nav-rail-bg` | `--surface` |
| `--nav-rail-rule` / `--nav-rail-rule-width` | `--border` / `1px` |
| `--nav-rail-pad` | `--space-xs` |
| `--nav-rail-marker` | `--accent` |
| items | `--nav-item-*` from core |

On Mobile, most apps swap the rail for a `.tabbar`. The rail still works
there, icon-only.

---

## Stepper (`ol.steps`)

```html
<ol class="steps" aria-label="Checkout">
  <li class="is-done"><a href="/account">Account</a></li>
  <li aria-current="step">Billing <small>Card or invoice</small></li>
  <li class="is-error">Shipping <small>Address not found</small></li>
  <li>Review</li>
</ol>
```

**States:** a step is upcoming by default (a numbered outline marker).
`.is-done` shows a tick on an accent fill, and the line to the next step
fills in. `aria-current="step"` gives an accent ring, bold text and the
number. `.is-error` shows `!` on a danger fill with danger text. Each
state has its own glyph, so colour is never the only signal. Done steps
can be links back. The link's hit area reaches `--tap-min` through an
invisible expander, so the label stays level with its marker.

**Layout:** steps run horizontally, sharing the width with connectors
between the markers. `.is-vertical` stacks them, with markers down the
start edge and labels beside them. Steps also stack automatically in a
480px or narrower screen, or in a 480px or narrower query container
(`.modal`, `.drawer` or `.cq`).

| Token | Default |
|---|---|
| `--steps-marker-size` | `1.75rem` |
| `--steps-gap` | `--space-xs` |
| `--steps-fg` / `--steps-fg-done` / `--steps-fg-current` | `--muted` / `--text` / `--text` |
| `--steps-marker-bg` / `--steps-marker-border` / `--steps-marker-radius` | `--surface` / `--muted` / `50%` |
| `--steps-line` / `--steps-line-done` | `--border` / `--accent` |
| `--steps-done-bg` / `--steps-done-fg` / `--steps-done-glyph` | `--accent` / `--on-accent` / `"✓"` |
| `--steps-current` / `--steps-current-fg` / `--steps-current-halo` | `--accent` / `--accent-text` / `transparent` (a theme glow) |
| `--steps-error-glyph` | `"!"` (fill `--danger`, text `--danger-text`) |

---

## Command palette (`.command`)

```html
<dialog class="command" id="palette" aria-label="Command palette">
  <div class="command-search">
    <svg class="icon"><use href="…#icon-search"/></svg>
    <input class="input" type="search" role="combobox" aria-expanded="true"
           aria-controls="palette-list" aria-activedescendant="o1" aria-label="Search commands">
  </div>
  <div class="command-list" role="listbox" id="palette-list" aria-label="Results">
    <ul role="group" aria-labelledby="g1">
      <li role="presentation" id="g1">Files</li>
      <li role="option" id="o1" aria-selected="true"><svg class="icon">…</svg>
        <span><mark>nav</mark>igation.css</span><span class="command-hint">core/components</span></li>
      <li role="option" id="o2" aria-selected="false"><span>Settings</span><kbd>Ctrl+,</kbd></li>
    </ul>
  </div>
  <div class="command-footer"><span><kbd>↑</kbd><kbd>↓</kbd>move</span><span><kbd>↵</kbd>open</span><span><kbd>Esc</kbd>close</span></div>
</dialog>
```

The dialog opens near the top of the screen (`--command-top`, 12dvh, and
close to the top on phones). Focus stays in the search field, and the
app moves `aria-selected` plus `aria-activedescendant` as the arrow keys
are pressed.

**States:**

- The highlighted option gets the menu hover colours and a leading
  marker bar.
- `aria-disabled="true"` dims an option.
- `<mark>` highlights the matched characters (bold and underlined, not
  colour alone).
- `.command-hint` is a muted secondary label.
- For no results, put an `.empty-state` inside `.command-list`.
- `.command-footer` lists the key hints.

| Token | Default |
|---|---|
| `--command-width` / `--command-top` | `40rem` / `12dvh` (`--space-s` on Mobile) |
| `--command-bg` / `--command-border` / `--command-radius` / `--command-shadow` | `--modal-*` → panel → base |
| `--command-rule` | `--hairline` |
| `--command-list-max` | `min(22rem, 55dvh)` |
| `--command-item-bg-active` / `--command-item-fg-active` | `--dropdown-item-bg-hover` / `--dropdown-item-fg-hover` |
| `--command-item-radius` | `--radius` |

---

## Split pane (`.split`)

```html
<!-- CSS only: the first pane has the browser's resize grip -->
<div class="split" style="--split-size: 35%">
  <section>…</section>
  <section>…</section>
</div>

<!-- app-driven handle -->
<div class="split" style="--split-size: 40%">
  <section>…</section>
  <div class="split-handle" role="separator" tabindex="0" aria-orientation="vertical"
       aria-valuemin="10" aria-valuemax="90" aria-valuenow="40" aria-label="Resize"></div>
  <section>…</section>
</div>
```

The first pane starts at `--split-size` and resizes with CSS `resize`,
using the browser's grip in its bottom corner. It is limited to
`--split-min` on either side. With a `.split-handle` between the panes,
the native grip turns off. The app then updates `--split-size` and
`aria-valuenow` on drag or arrow keys, and can add `.is-dragging` while
dragging. The handle draws a grip mark and turns accent on hover, focus
and drag. Its hit area is `--tap-min` wide. `.is-vertical` stacks the
panes, with `--split-height` setting the box height. Side-by-side panes
stack in a screen or query container 480px wide or less (the handle
hides there). Panes scroll on their own and wrap long words.

| Token | Default |
|---|---|
| `--split-size` / `--split-min` / `--split-height` / `--split-min-height` | `50%` / `6rem` (`4rem` vertical) / `24rem` / `12rem` |
| `--split-border` / `--split-border-width` / `--split-radius` | `--border` / `1px` / `--radius` |
| `--split-rule` / `--split-rule-width` | `--border` / `1px` |
| `--split-pad` | `--space-s` |
| `--split-handle-size` / `--split-handle-bg` / `--split-handle-bg-active` | `0.5rem` / `--surface-2` / `--accent` |
| `--split-grip` / `--split-grip-active` | `--muted` / `--on-accent` |

---

## Keyboard layer

**Key hints.** `<kbd>` keeps core's key-cap look in running text. Inside
these components it adapts:

- **Menus** (`.menubar`, `.context-menu`, `.dropdown`): plain text at the
  end of the item, in the item's own colour. `--menu-kbd-fg` overrides it.
- **Buttons, tabs and command results:** a small outlined key in the
  control's text colour. `--kbd-hint-border` and `--kbd-hint-bg` set it.
- **Key combinations:** nest the keys, as the HTML spec suggests:
  `<kbd><kbd>Ctrl</kbd>+<kbd>S</kbd></kbd>`. Only the inner keys get a
  box.
- **Attribute tooltips:** they can't hold markup, so a shortcut goes in
  its own attribute: `<button data-tooltip="Save" data-shortcut="Ctrl+S">`.

The app picks the platform's symbols (`⌘S` or `Ctrl+S`). CSS can't tell
which one is right.

**Shortcuts overlay** (`.shortcuts`, opened by `?`):

```html
<dialog class="modal modal-lg shortcuts" id="shortcuts" aria-labelledby="sc-title">
  <div class="modal-header"><h2 id="sc-title">Keyboard shortcuts</h2>
    <button class="btn-close" aria-label="Close" commandfor="shortcuts" command="close"></button></div>
  <div class="shortcuts-groups">
    <section><h3>General</h3><dl>
      <dt>Command palette</dt><dd><kbd><kbd>Ctrl</kbd>+<kbd>K</kbd></kbd></dd>
      <dt>Go to inbox</dt><dd><kbd>G</kbd> then <kbd>I</kbd></dd>
    </dl></section>
  </div>
</dialog>
```

`.shortcuts` reuses `.modal` for the dialog, or a `.panel` or `.sheet`.
It styles the groups: a responsive grid (`--shortcuts-col`, 16rem),
label-style headings, and `dt`/`dd` rows with the keys at the end and a
`--shortcuts-rule` hairline between rows. The app binds `?` to
`showModal()`.

**Roving focus.** Composite widgets (lists, trees, menus, the menubar,
tab strips, segmented controls, toolbars, button groups, tables, and
anything with role `grid`, `listbox`, `toolbar` or `tablist`) draw the
focus ring inset (`outline-offset: -2px`). Focus moved there by arrow
keys therefore shows fully, even inside a box that clips or scrolls. A
`.list-item` with a `tabindex` reaches `--tap-min`. For the
roving-tabindex pattern, give the current item `tabindex="0"` and the
rest `-1`, then call `.focus()` on arrow keys. `:focus-visible` follows.
For the `aria-activedescendant` pattern (the command palette), the
highlighted option shows through `aria-selected`.
