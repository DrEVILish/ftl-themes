# Material

> Google Material Design — flat color, layered elevation shadows.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

**Google's Material Design language (MD2 era)**: bold flat color, no
gradients, and depth expressed entirely through a layered "elevation"
shadow system instead of gloss or bevel. Paper that lifts off the page,
not plastic or glass.

## Core values

1. **Elevation, not gloss.** Depth comes from `box-shadow` stacks at
   increasing "dp" levels (resting vs. hover vs. modal) — never a
   gradient fill. This is the deliberate contrast point against
   `aqua`/`winxp-luna`'s gloss and `win7-aero`'s blur: three different
   answers to "how does this surface show depth."
2. **Flat fills, bold color.** `--accent` is a saturated flat purple,
   painted solid — no gradient, no gloss highlight.
3. **Underlined text fields.** Inputs are MD2 filled fields: a #f5f5f5
   fill with no box border, only a 1px underline at 42% black (3:1 on the
   fill) that thickens to a 2px accent line on focus. Input-group addons
   and attached text buttons
   share the same fill and underline, and an invalid field keeps the grey
   fill, turning only its underline red. Distinct from every boxed-input
   theme in the catalog. Fields are 40px tall, and one-time-code cells
   are drawn as the same filled fields (fill and underline, no box).
4. **Uppercase button labels.** Buttons set their text
   `text-transform: uppercase` in Medium weight with MD2's 1.25px
   (0.089em) tracking, on a 36px-tall button — the MD2 button-label voice.
5. **The app bar is a flat accent slab.** No gradient, no rule — just the
   accent color and its own elevation shadow lifting it above the content.

## Signature details

- Type is Roboto, MD2's own family: Regular 400 and Medium 500 plus Roboto
  Mono are vendored (SIL OFL, `assets/fonts/NOTICE.md`), so the Medium
  button, tab and title roles keep their weight on every platform.

- Resting shadows (cards, panels, buttons) use two layers, the full
  three-layer MD2 stacks only on hover, menus, the FAB and the modal, to
  keep phone paint cost down.
- Elevation levels are visible: cards rest at dp1, panels and buttons at
  dp2, the app bar at dp4 (buttons rise to dp4 on hover), menus and
  popovers at dp8, the FAB at dp6, and the modal at dp24 (the heaviest
  shadow in the catalog).
- Pressing a button grows a 16% currentColor ripple from its centre (the
  growth animates only when motion is allowed).
- Menus, context menus and popovers are borderless white sheets; toasts
  are the MD2 snackbar (dark #323232, white text, #bb86fc links) with no
  state bar; a stated toast shows only a small leading dot.
- The switch is the MD2 switch: a borderless track (secondary at 50% on,
  42% black off) under a larger white thumb that overhangs it, with the
  MD2 thumb shadow and a 12% ring. Checkboxes, radios and the on switch
  take the baseline secondary in its darker variant #018786 (3:1 on
  white). Sliders are a 4px accent track at 55% (3.2:1 on the page; MD2's
  inactive track is 24%) with an accent thumb; Firefox also fills the
  active track in solid accent.
- `.btn-primary.btn-icon` is the mini FAB: 40px, baseline secondary teal
  (#03dac6) with black icon.
- Table headers are sentence-case Medium at body size, on roomier rows.
- Headings follow MD2 weights: h1-h3 Regular, h4-h6 Medium.
- Elevated cards and panels have no outline, only their shadow; a sheet
  nested in another surface drops to 0dp and draws a 1px outline instead.
  At phone width resting buttons and sheets use one shadow layer, and
  non-primary buttons inside sheets and tables none, to keep scrolling
  cheap.
- Primary buttons fill solid `--accent` with white text; secondary and
  ghost buttons drop the shadow entirely — Material's "text button" and
  "outlined button" variants have no elevation. A ghost or clear button is
  the MD2 text button with an accent label (ghost icon buttons stay neutral).
- `.btn-go` is an extended FAB: filled accent, pill-shaped, dp6, Medium
  tracked label, no outline.
- Filter chips are 32px pills with 14px Medium text; on touch the 44px
  target extends invisibly past the painted chip.
- Selected filter chips and the selected range button are a 12% accent
  tint with accent text, never a solid fill. The bulk-selection bar is the
  contextual action bar: a 12% accent tint with no outline.
- Featured and status list cards show their
  state as a 4px leading bar (status cards add an 8% tint).
- Pagination items are 36px squares; the active one is filled accent.
- Selected/active rows, list items and nav items tint with a translucent
  accent wash, never a leading accent bar.
- Card, panel and dialog titles (including a card's leading h2) are Headline 6: 20px Medium in the text
  color, with no rule under them. Dialog actions are text buttons
  (accent label, no outline or fill).
- Segmented controls and toggle groups are one 12%-black outlined strip;
  the selected segment is a 12% accent tint with accent text. Range
  button groups are outlined, not raised.
- Tabs are MD2 tabs: uppercase Medium with 1.25px tracking. Inside a
  window body the strip scrolls on one row rather than wrapping.
- Alerts are white dp1 sheets with the state as a 4px leading bar (no
  boxed outline); banners are white with a 12% divider below.
- Setting rows (`.field-row`) are list items with only a 12% divider
  and 12px block padding;
  navigation lists are borderless drawer lists, the active item an 8%
  accent tint with accent text.
- Disabled contained buttons are 12% black with a 38% black label.
- KPI values (`.stat-value`) are Headline 5: 24px Regular in the UI font.
- The modal scrim is MD2's 32% black.
- At XL (1801px+) the purple app bar still spans the full viewport.
- Actions on the app bar are borderless: buttons take a translucent white
  fill, icon buttons none. At phone width (600px and below) the bar's
  action cluster joins the title row as icons (search drops its label and
  shortcut), the nav takes the second row and any field the third.

## Layout

The shell keeps the page background flat and puts all its depth into the
**app bar**, which floats above the content on its own elevation shadow —
no border, no gradient, just color and shadow.

## Known gaps

- Field labels sit above the filled field, not inside it as MD2 floating
  labels; that needs markup or core support. Fields are 40px, not MD2's
  56px, so dense layouts don't grow much.
- Outside Firefox the slider has no filled (active) track left of the
  thumb: core exposes no value-driven fill token.

## Tell-tales of an inauthentic result

- Any gradient or gloss highlight on a button or panel.
- Boxed (bordered-on-all-sides) text inputs instead of the underline.
- Title-case or lowercase button labels instead of tracked uppercase.
- A flat, shadowless app bar — the elevation is the point.

## v5 layout

- **Tiers.** No rail. The flat purple app bar gets a little block padding up to 900px so its two lines (brand and actions, then the scrolling nav) don't touch its edges; at 600px and below the action icons share the title row; its items pack tighter and the brand keeps at least a few readable characters before it truncates. A field on the bar is a translucent white fill with a white underline.
- **Nesting.** A panel or card inside another surface is an outlined 0dp sheet rather than a second dp4 slab.
- **XL gutter art (1801px+).** Declared only inside the XL media query. Overlapping sheets of paper at angles, each edge marked by a soft elevation shadow, in very low contrast.

## Icons

`icons.svg` redraws all 178 core-set icons in the 2014 to 2018 system-icon
grammar, filled style (own geometry, not Google's Material Icons artwork):

- 24dp grid with 2dp padding; 2dp lines with butt caps and mitred joins.
- Object icons (mail, folder, file, calendar, lock, settings, info, user,
  devices) are solid bodies with 2dp cut-outs (`fill-rule="evenodd"`);
  line glyphs (arrows, chevrons, close, search, refresh) stay 2dp strokes.
- Square-ish corners: radius 2 on bodies, 1 on small parts; no gloss,
  no tint.
- `currentColor` only. Ids outside the core set fall back to the generic
  outline set.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
