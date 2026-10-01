# Liquid Glass

> Apple's 2025 design language (iOS 26, iPadOS 26, macOS Tahoe 26): translucent capsule controls with bright specular rims, floating inset over a vivid wallpaper while the content scrolls underneath.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

**Liquid Glass** as shipped at WWDC 2025. Apple separates the UI into two
layers: a **content layer**, and a **functional layer** of controls and
navigation made of a glass that "has no inherent color, and instead takes
on colors from the content directly behind it" (HIG, Color). The glass
floats: tab bars and toolbars are capsules inset from the screen edges,
sidebars are large rounded panes standing off the window, buttons are
pills or circles with a lit rim, and the content scrolls under all of it.
Recognisable at a glance by: capsules everywhere, a thin bright edge on
every piece of glass, the wallpaper's colour bleeding through, and nothing
touching the edge of the screen.

## Core values

1. **Glass is the functional layer only.** Bars, buttons, tabs, menus,
   sheets, toasts and the sidebar are Liquid Glass (blur + saturate +
   specular rim). Panels and cards in the content are a frosted *standard*
   material with a soft shadow and **no rim** — HIG: "Don't use Liquid
   Glass in the content layer."
2. **Float, never dock.** Every bar is inset from every edge with its own
   radius. A bar flush with the window edge, or a hairline under a bar, is
   iOS 7–18 (`ios-flat`), not this.
3. **Capsules and concentric corners.** Controls are `999px` capsules or
   circles; containers use radii that equal the child's radius plus the
   inset around it (window 28px around 0.6rem-inset capsules; menu 18px
   around 12px items with 6px padding).
4. **Content scrolls under the glass.** The toolbar and tab bar are
   `position: sticky` over the window, and the wallpaper is
   `background-attachment: fixed`, so the blur always has moving, colourful
   content behind it. Glass over a flat colour is just a grey pill.
5. **Legibility beats transparency.** Small controls use the *clear*
   weight; anything carrying body text uses the *regular* weight (a 70–80%
   white scrim), and the window pane under the content is 74–80% white so
   `--muted` text holds 4.5:1 over the darkest wallpaper blue. Headings
   that can land on the wallpaper carry a faint white halo.
6. **Colour is sparing.** One tint (systemBlue) for the prominent button,
   selected labels and focus; selection is a grey lens with a blue label,
   not a blue fill.

## Signature details

- `--lg-rim`: four inset shadows — top-left and bottom-right specular
  edges (light catching the curved bezel), a 0.5px white hairline, and a
  soft inner glow standing in for the refraction band.
- `backdrop-filter: blur(14px) saturate(160%) brightness(1.08)` on clear
  glass; `blur(28px)` on sheets and the window. The saturate is what makes
  controls pick up the wallpaper's colour.
- Prominent buttons are *tinted glass*: the accent fill keeps the rim and
  a lit top edge and casts a coloured bloom. On press glass **swells**
  (`scale(1.04)`) instead of sinking.
- Tabs, the nav and the status strip read as the iOS 26 tab bar: a glass
  capsule whose selected item is a grey lens with a blue label.
- The switch is the iOS 26 one: wider track, a capsule knob wider than it
  is tall, systemGreen when on. The slider thumb is Control Center's white
  capsule.
- The empty rail is drawn as a Tahoe sidebar: tall rounded glass with the
  three traffic lights (`#ff5f57 #febc2e #28c840`) in its corner and a
  selected-row lens.
- The page is a CSS sketch of the Tahoe wallpaper: pale sand top-left,
  deep blue sweeping waves, thin white crest arcs.

## Layout

A macOS Tahoe window over the desktop. The full-height glass **sidebar**
floats on the left; the content **window** is one large frosted pane
(radius 28px) to its right that spans all three shell rows; the capsule
**toolbar** floats inside its top edge and the capsule **tab bar**
(`.app-status`) floats centred inside its bottom edge, only as wide as its
items. Both bars are sticky, so content scrolls under them. Under 720px
the sidebar goes, the toolbar sits above the window instead of over it and
may wrap (as a 26px rounded rectangle).

## Variants

- `dark` — the same material over the Tahoe night wallpaper: smoked glass
  (`rgba(30–60,…,0.4–0.5)`), dimmer cool rims, dark HIG label colours
  (`#f5f5f7` / `#a1a1a6`, accent text `#4aa3ff`). It declares
  `color-scheme: dark` so native controls follow it.

## Tell-tales of an inauthentic result

- Bars or the sidebar touching the window edge, or rectangular bars.
- A hairline border under the toolbar or above the tab bar.
- Glass with no rim highlight, or a rim that is a uniform 1px grey border.
- Blue-filled selected tabs or nav items (that is iOS 7–18 or Material).
- Opaque grey buttons; square or 6px-radius buttons.
- Specular rims on content cards and panels (glass leaking into the
  content layer).
- A flat solid page background with nothing for the glass to refract.
- Linen, gloss gradients or stitching (that is `ios-skeuomorphic`).

## Don'ts

- **Don't remove `backdrop-filter`** to "fix" a perf report; use
  `prefers-reduced-transparency`, which this theme already honours.
- **Don't lower the white scrims** on `--lg-regular` or `--app-main-bg`;
  they are what keeps `--muted` at 4.5:1 over the dark wallpaper.
- **Don't set `--accent` to `#0088ff`** (iOS 26 systemBlue): white text
  on it is 3.5:1. It is used where no text sits on it (focus, progress,
  the switch caret, `--accent-2`).

## Typography

`--font` is `-apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro",
"Helvetica Neue", Inter, system-ui, sans-serif`; `--font-mono` starts with
`"SF Mono", ui-monospace, Menlo`. SF Pro is Apple-licensed and not
vendored, so it renders only on Apple platforms; elsewhere Helvetica Neue,
Inter or the system UI face stands in. Headings are bold with slight
negative tracking (the large-title voice); table headers are sentence-case
semibold, never uppercase.

## Contrast honesty

- `--accent` `#0071e3` (Apple's web action blue) under white text: 4.7:1.
  The iOS 26 systemBlue `#0088ff` (3.5:1 under white) is kept as
  `--accent-2` and `--focus`.
- `--danger` `#e0262b` is systemRed `#ff383c` deepened to 4.7:1 under
  white. `--success` keeps systemGreen `#34c759` with **dark** text
  (`#06240f`, 7.5:1) because white on it is 2.2:1.
- Glass surfaces are translucent; the lint measures text against the
  opaque `--surface` / `--surface-2` equivalents. The scrims are tuned so
  the rendered glass is at least as light as those over the wallpaper's
  darkest blue.
- `prefers-reduced-transparency: reduce` and `data-contrast="high"` swap
  every glass fill for the opaque surface.

## Reference status

`references/liquid-glass/` holds 14 Apple Newsroom WWDC25 press images
(12 shared, 2 in `dark/`) plus `RESEARCH.md` with credits, sampled hexes
and a component mapping. They cover the tab bar, toolbar, sidebar,
Control Center switches and sliders, menus, sheets, list/table, messages
and notifications. No reference shows a web-style data table header, a
meter, a toast in the ftl-themes sense or a form with validation errors.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders recoloured
with glass controls over the wallpaper, but without the window, sidebar
and floating bars. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status`
shell (CONTRACT.md "The app shell" / "Adoption levels") for the real
layout at **L1**.

`backdrop-filter` support: without it, every glass surface falls back to
its translucent white (or smoked, in `dark`) fill: no blur, still legible.
Real Liquid Glass also *refracts* (bends the content at the rim). An SVG
`feDisplacementMap` in `backdrop-filter` can fake that, but only Chromium
supports it and it needs inline SVG in the page, so this theme suggests
the lens with rim highlights instead.
