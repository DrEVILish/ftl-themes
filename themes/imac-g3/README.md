# iMac G3

> Translucent ribbed plastic in Bondi Blue, with Blueberry/Grape/Tangerine variants.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The 1998 iMac's defining trick: consumer electronics as candy. Translucent
coloured plastic over a light gloss highlight, rounded everything, and a
sense that the interface is a physical object you could pick up.

## Core values

1. **Gloss is a highlight band, never a flat sheen.** A light-to-dark
   gradient with a bright top edge, the same trick Aqua uses, but with the
   base colour itself translucent rather than metal.
2. **Every colorway is the same shape.** The plastic case comes in four
   colours; the case itself never changes. Only tokens change between
   variants — gloss, radius and pinstripe rules are shared once.
3. **Big, round, friendly.** `--radius: 1.3rem`. Nothing here is sharp.
4. **White text on saturated colour**, always — this is a light-on-dark
   theme regardless of which fruit colour is active.

## Signature details

- The pinstripe (`repeating-linear-gradient` white-at-12% every 4px) sits
  on both `.panel` and `.app-bar` — it's a case texture, not a
  panel-only decoration.
- Every gloss gradient is three stops (bright highlight → faint → the base
  surface colour), never a plain two-stop fade — that middle fade-out is
  what reads as translucent plastic rather than a painted highlight.
- The app bar's gloss is an inset highlight rather than a gradient stop,
  so its white nav text sits on the solid case colour.
- Tangerine is a burnt tangerine (surface `#823a0a`, 8.2:1 under white per the `theme.css` comment), darker than the case it's
  named after: white text on the brighter orange was 3.8:1.
- The page backdrop is a radial vignette in the shell's own colour
  (`radial-gradient(ellipse at top, ...)`), so the case always appears to
  glow against a darker version of itself, never a neutral grey.

## Variants

Bondi Blue is the default (no attribute needed). Select the others with
`data-variant` on `<html>`:

| Variant | `data-variant` |
|---|---|
| Bondi Blue | *(default)* |
| Blueberry | `blueberry` |
| Grape | `grape` |
| Tangerine | `tangerine` |

A lighter option — an **accent swatch** picker (`data-accent="1..4"`) —
recolours only the accent, not the whole shell, for an app that wants a
color pick without a full theme change.

## Layout

The shell reads as **one plastic case**: a glossy rounded top bar, a
pinstriped body, and a rounded status foot — all one continuous rounded
shape (`0.75rem` outer padding, `1.3rem` corners top and bottom), floating
on a radial vignette of its own colour.

## Tell-tales of an inauthentic result

- A flat, opaque fill anywhere → the plastic stops reading as translucent.
- Sharp corners.
- A colorway that changes gloss or radius, not just palette tokens — the
  case is one shape in four colours, not four different cases.

## Don'ts

- **No flat opaque fills** where the plastic should read as translucent.
- **No sharp corners** (`--radius: 1.3rem`).
- **No colorway that changes shape**, gloss or radius — variants override colour tokens only.
- **No dark text on the saturated case colour**; white (or `--accent-text` on tints) only.
- **No neutral grey backdrop.** The vignette is always the case's own colour.
- **Do not present this as the Platinum OS look.** The reference software UI (`references/imac-g3/`) is light grey Platinum; this theme is the hardware-inspired shell, not that UI.

## Typography

`--font` is `"Chicago", "Charcoal", "Helvetica Neue", Helvetica, Arial, sans-serif`; `--font-mono` is `Monaco, Consolas, monospace`. Chicago (System 7) and Charcoal (Mac OS 8/9 Platinum's system face) are the reference faces; neither is vendored nor present on modern systems, so in practice **Helvetica Neue/Helvetica/Arial renders**. The Platinum captures show Charcoal-style type; the fallback is a lookalike at best. Headings carry a 1px white 40% `text-shadow` as an "embossed" cue.

## Contrast honesty

The shell is a saturated mid-tone, so this theme sits near the floors and `python3 scripts/check.py` prints AAA warnings for it:

- **Body text (AAA warning):** `--text` white on `--surface` `#0c6478` is 6.8:1 (floor 7.0:1); on `--bg` `#0a545f` it is 8.58:1. It clears AA everywhere but not AAA on `--surface`.
- **Accent legibility (warning):** `--accent` `#00b0d4` on `--surface` is 2.6:1 (soft floor 3.0:1); on `--bg` it is 3.34:1. The `theme.css` header comment says `#00b0d4` "clears 3.0:1" — that was measured against an earlier, darker surface; against the current `#0c6478` it does not.
- **Bondi lifted from the reference:** the verified hardware colour Bondi Blue is `#0095b6`; shipped `--accent` is `#00b0d4`, one step lighter. True Bondi is only 1.92:1 against `--surface`, so it cannot be used as text on this shell at all.
- **Muted:** `#f5fcfd` is 6.5:1 on `--surface` but only 4.63:1 on `--surface-2` `#0f7d92` (white is 4.81:1 there), so text placed directly on solid `--surface-2` uses `--accent-text` `#bff0f7` or `--on-accent`.
- **State text** uses pale tints (`--success-text` `#c3f7d2`, `--warning-text` `#ffe6a8`, `--danger-text` `#ffd9d5`) because the fills fail as text on the teal.
- **Tangerine variant** was darkened to `#823a0a` after the brighter oranges measured 3.8:1 and 2.7:1 with white.

## Reference status

`references/imac-g3/` has 5 captures plus `RESEARCH.md`: two Finder Preferences GIFs (`0201700042_ch04lev1sec2_image01/02.gif`), two Mac OS 9.x About/System Folder screenshots (`Mac_OS_9.0.4_emulated…png`, `5654e869….png`) and a Platinum Finder-windows webp. All are the **light Platinum software UI**; `RESEARCH.md` notes there is no Bondi/fruit hardware photo. So the translucent-plastic shell, the Bondi/fruit hexes and the pinstripe are backed by the RESEARCH text ("translucent Bondi Blue candy shell") and the verified `#0095b6` hardware colour, not by any image in the folder.

## v5 layout

- **Tiers.** No rail at any size; the rounded bar and status strip work unchanged on phones and tablets, where core stacks the brand and actions over a scrolling nav line.
- **Nesting.** The diagonal sheen is the surface's top background layer, not a clipped pseudo-element, so panels no longer need `overflow: hidden` (which cut off menus and popovers opened inside them). A panel or card inside another surface keeps the gloss and pinstripe but drops the streak: one streak per stack of plastic.
- **XL gutter art (1801px+).** The case continues past the screen as ribbed translucent plastic with one broad diagonal sheen, white at low alpha so every colorway tints it.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
