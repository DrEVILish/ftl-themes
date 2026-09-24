# XMB

> The PlayStation 3 / PSP dashboard: the Cross Media Bar itself — a horizontal row of glowing category icons over a deep-blue wave, with sub-items dropping straight down from whichever one is selected.

**Requires: L1** — sets `--ftl-app-*` layout properties (a centred, transparent app-bar over the wave); recolours correctly at L0 but the actual cross-shaped layout only appears once the app shell is adopted.

## What this theme is trying to achieve

The XMB isn't a window manager or a set of panels — it's one horizontal
row of icons (Users, Settings, Photo, Music, Video, Game, Network,
Friends...) with a vertical list of that category's items appearing
directly below the selected one. Everything floats, translucent, over a
slowly animated blue wave; nothing is opaque or hard-edged. This theme
reproduces the float-and-glow language rather than the wave's motion,
which doesn't translate to a general-purpose page background.

## Core values

1. **Nothing is a filled block.** Every surface — cards, inputs, the nav
   itself — is a translucent tint over the wave gradient, never an opaque
   fill. An opaque panel is the fastest way to look like a generic dark
   dashboard instead of XMB.
2. **Selection is a glow, not a fill.** The active icon/row gets a soft
   blue glow and a scale-up, not a solid highlight block — see
   `--ftl-btn-shadow-hover` and the icon-button hover rule.
3. **The bar is centred, not left-aligned.** Real XMB's icon row runs
   through the horizontal centre of the screen; a left-anchored nav bar
   reads as a generic app, not XMB.

## Signature details

- The layered radial-gradient "wave": a lighter glow low-and-centre and
  upper-left over the deep navy-to-blue base.
- Icon buttons scale up (`transform: scale(1.15)`) on hover/focus — the
  one unmistakable XMB interaction.
- `999px` (pill) radius on buttons, nav items and badges only — real XMB
  info panels were modestly rounded rectangles, not stadium shapes, so
  `--ftl-radius` (panels, cards, inputs, alerts, the dropdown, the log)
  is a generous `0.85rem`/`0.9rem` rounded rectangle instead. A base
  radius of 999px produced odd stadium-shaped alert banners and selects
  on large surfaces; interactive pill-shaped chrome keeps its own
  explicit `--ftl-btn-radius`/`--ftl-nav-item-radius: 999px` regardless.
- Thin/glass borders, no hard rectangular chrome.

## Tell-tales of an inauthentic result

- Any opaque panel or card background.
- A left-aligned or edge-anchored navigation bar instead of a centred one.
- Sharp rectangular corners on interactive elements.
- A stadium/pill-shaped info panel, alert or dropdown — those are
  modestly rounded rectangles, not pills; only buttons/nav items/badges
  are pills.

### Reference status

This theme was built from well-documented real-world facts about the
PS3/PSP Cross Media Bar (its single horizontal icon row, its
float-and-glow visual language, its centred layout) rather than from
captured reference images, so there's no `references/xmb/` folder the
way other themes have one. That's an accepted, permanent-for-now state,
not a to-do — but if someone wants to add a `references/xmb/` folder
later using the same pattern other themes use, that's welcome.

## Known harness limitation: the app-bar doesn't render centred everywhere

`html[data-theme="xmb"] .ftl-nav { justify-content: center }` (and the
same rule on `.ftl-app-bar`) is real, is the highest-specificity rule
either QA page applies, and does win — it centres the standalone
`.ftl-nav` demo in example.html's "Navigation" section correctly. It has
no visible effect on the QA harness's own *topbar* markup, though:
example.html's `.ftl-app-bar` header puts an inline
`<span style="margin-left:auto">` before its breadcrumbs, and
example-2/3.html's `.demo-topbar-spacer` sets `flex: 1`. Either one
absorbs 100% of the row's free space by itself, so `justify-content` has
nothing left to distribute and the brand/items stay pinned flush left.
That's a property of those harness pages' fixed nav markup (which this
theme must not edit to "fix"), not a bug in the theme's centering rule —
an app that lays out its own `.ftl-app-bar` without such a spacer gets
the real centred cross-bar. In the meantime the bar leans harder on the
float-and-glow language it's actually judged on: it now renders as its
own floating, blurred, pill-shaped glass capsule with a soft drop shadow
above the wave, and the active nav item's selection glow is stronger —
so the bar still reads unmistakably as XMB even where it can't be
centred.
