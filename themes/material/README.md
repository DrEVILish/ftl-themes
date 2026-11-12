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
   fill) that thickens to a 2px accent line on focus. Distinct from every
   boxed-input theme in the catalog.
4. **Uppercase button labels.** Buttons set their text
   `text-transform: uppercase` in Medium weight with MD2's 1.25px
   (0.089em) tracking, on a 36px-tall button — the MD2 button-label voice.
5. **The app bar is a flat accent slab.** No gradient, no rule — just the
   accent color and its own elevation shadow lifting it above the content.

## Signature details

- Elevation levels are visible: cards rest at dp1, panels and buttons at
  dp2, the app bar at dp4 (buttons rise to dp4 on hover), menus and
  popovers at dp8, the FAB at dp6, and the modal at dp24 (the heaviest
  shadow in the catalog).
- Pressing a button grows a 16% currentColor ripple from its centre (the
  growth animates only when motion is allowed).
- Menus, context menus and popovers are borderless white sheets; toasts
  are the MD2 snackbar (dark #323232, white text, #bb86fc links), keeping
  their state as a 4px leading bar.
- The switch is the MD2 switch: a borderless track (accent at 50% on,
  42% black off) under a larger thumb that overhangs it and casts a
  shadow. Sliders are a 4px accent track at 38% with an accent thumb.
- `.btn-primary.btn-icon` is the mini FAB: 40px, baseline secondary teal
  (#03dac6) with black icon.
- Table headers are sentence-case Medium at body size, on roomier rows.
- Headings follow MD2 weights: h1-h3 Regular, h4-h6 Medium.
- Primary buttons fill solid `--accent` with white text; secondary and
  ghost buttons drop the shadow entirely — Material's "text button" and
  "outlined button" variants have no elevation.
- Selected/active table rows tint with a translucent accent wash rather
  than a hard fill, keeping to flat-color discipline.

## Layout

The shell keeps the page background flat and puts all its depth into the
**app bar**, which floats above the content on its own elevation shadow —
no border, no gradient, just color and shadow.

## Tell-tales of an inauthentic result

- Any gradient or gloss highlight on a button or panel.
- Boxed (bordered-on-all-sides) text inputs instead of the underline.
- Title-case or lowercase button labels instead of tracked uppercase.
- A flat, shadowless app bar — the elevation is the point.

## v5 layout

- **Tiers.** No rail. The flat purple app bar gets a little block padding up to 900px so its two lines (brand and actions, then the scrolling nav) don't touch its edges; its items pack tighter and the brand keeps at least a few readable characters before it truncates. A field on the bar is a translucent white fill with a white underline.
- **Nesting.** A panel or card inside another surface is an outlined 0dp sheet rather than a second dp4 slab.
- **XL gutter art (1801px+).** Overlapping sheets of paper at angles, each edge marked by a soft elevation shadow, in very low contrast.

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
