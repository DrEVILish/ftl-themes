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

- The pinstripe (`repeating-linear-gradient` white-at-7% every 4px) sits
  on both `.panel` and `.app-bar` — a faint case texture under the
  colour, not an Aqua-strength stripe.
- Every gloss gradient is three stops (bright highlight → faint → the base
  surface colour), never a plain two-stop fade — that middle fade-out is
  what reads as translucent plastic rather than a painted highlight. The
  middle stop is the colorway's bright candy tone (`--imac-g3-candy`:
  Bondi `#0095b6`, Blueberry `#4a86ff`, Grape `#b06ae8`, Tangerine
  `#ff8a1f`) at 35%, glowing through the darker text-bearing surface, and
  `var(--surface)` is the opaque last layer, so overlapping windows never
  show through each other's title bars (`--modal-header-bg` has the same
  opaque base).
- **Ice.** The colour is set in frosted white plastic (`--imac-g3-ice`,
  `rgba(232,248,252,0.7)`): every panel and card has a 3px milky rim
  (`--panel-border`), menus, popovers, toasts, toolbars and grouped
  fieldsets have ice rims too, and the case body (`.app-main`) has 4px
  frosted side walls plus a 3px ice seam under the bar and over the
  status foot, so the shell reads as one moulding, like the hardware's
  front bezel.
- **Every surface is moulded plastic.** Toolbars, context menus,
  dropdowns, popovers and toasts take the panel fill; table heads are a
  three-stop gloss with rounded top corners; alerts get a short gloss over
  `--surface-2`. Toolbars and fieldsets carry `--radius`.
- **A soft, broad streak.** The 115deg sheen peaks at only 0.28 white and
  spans about half the surface, so it reads as light on thick plastic
  rather than a chrome stripe. (A viewport-fixed streak shared across
  cards was tried and dropped: it repaints every panel on scroll.) Panels also carry an inner
  top lip and a deep bottom fall-off (`--panel-shadow`, an inset of the
  surface mixed 35% with black) so the case reads as thick plastic with
  darker internals behind it.
- **The gel follows the colourway.** The button gel's base stop is
  `--imac-g3-gel`, set per variant, as are `--accent-2` and `--accent-text`,
  so no Bondi teal survives on a Blueberry, Grape or Tangerine case.
- Rails and lists (`--nav-rail-bg`, `--list-bg`) use the same pinstripe +
  three-stop gloss as panels, without a streak; the rail gets `--radius`
  corners.
- Sliders sit in a recessed ice groove drawn on core's content box (the
  hit area stays `--tap-min`) with a gel-bead thumb. Checkboxes are
  rounded (0.35rem) white wells that fill with the colourway's button gel
  and a white tick when checked; radios are white wells.
- The app bar's gloss is an inset highlight rather than a gradient stop,
  so its white nav text sits on the solid case colour.
- Tangerine keeps its text-bearing surface dark (`#8a3a00`, 7.8:1 under
  white) but puts real tangerine where no text sits: a `#e8761f` backdrop
  glow, a `#b5500f` button gel and the `#ff8a1f` candy tone in the
  gloss, so it reads as orange plastic, not wood.
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

## Icons

`icons.svg` redraws the full core set (178/178). Rules: 24 grid, 2.4px stroke,
`round` caps and joins forced, and generous radii on every rect (about 0.3x
the short side, max 4.5; bars 4px or narrower become full pills). Line only:
nothing is filled, marker dots are r1.1 rings, colour is always
`currentColor`.

## Typography

`--font` is `"Helvetica Neue", Helvetica, Arial, sans-serif`; `--font-mono` is `Monaco, Menlo, Consolas, ui-monospace, monospace`. No free rounded body face is vendored, so the body falls back to the platform sans where Helvetica Neue is missing. Headings (`h1`–`h3`) and the bar's brand (at 1.15em) use **Baloo 2 Bold** (SIL OFL, vendored in `assets/fonts/`), the "big, round, friendly" voice of the candy case. Chicago and Charcoal are the Platinum software's faces, but they are not free to vendor and this theme is the hardware shell, not Platinum, so they are not named in the stack. Headings carry a moulded `0 1px 0 rgba(0,0,0,0.35)` drop rather than a white glow.

## Contrast honesty

The shell is a saturated mid-tone, so this theme sits near the floors and `python3 scripts/check.py` prints AAA warnings for it:

- **Body text (AAA warning):** `--text` white on `--surface` `#0c6478` is 6.8:1 (floor 7.0:1); on `--bg` `#0a545f` it is 8.58:1. It clears AA everywhere but not AAA on `--surface`.
- **Accent legibility (warning):** `--accent` `#00b0d4` on `--surface` is 2.6:1 (soft floor 3.0:1); on `--bg` it is 3.34:1. The `theme.css` header comment says `#00b0d4` "clears 3.0:1" — that was measured against an earlier, darker surface; against the current `#0c6478` it does not.
- **Bondi lifted from the reference:** the verified hardware colour Bondi Blue is `#0095b6`; shipped `--accent` is `#00b0d4`, one step lighter. True Bondi is only 1.92:1 against `--surface`, so it cannot be used as text on this shell at all.
- **Surface-2 darkened:** `#0f7d92` left white at 4.81:1 and every tinted text token under 4.5:1 on context menus, toasts and readonly fields, so `--surface-2` is `#0d7489` (white 5.42:1, `--muted` `#f5fcfd` about 5.2:1). The button gel keeps the old `#0f7d92` stop (as `--imac-g3-gel`), so buttons look the same. Accent as text (badges, links, readouts, active tab, GO, `.schedule`) is `--accent-text` `#cff4f9`; raw `--accent` is 2.6:1 on `--surface`. Selection frost is `rgba(255,255,255,0.12)` (was 0.25, white 3.1–3.9:1 on it) and series 6 is graphite `#8a9ba1` instead of near-white `--muted`, so white text on its tints passes.
- **State text** uses pale tints (`--success-text` `#c9f8d6`, `--warning-text` `#ffebb9`, `--danger-text` `#ffe8e6`, each at least 4.6:1 on `--surface-2`) because the fills fail as text on the teal.
- **Lit pads and marker chips:** core mixes 30% accent over surface-2 there, which left white labels at 4.26:1; lit pads use 18% (4.6:1+) and marker chips mix over `--surface` (4.9:1). A filled accent pill (`.pattern-nav [aria-current]`) labels in `--on-accent` (6.2:1), not the pale `--accent-text` (2.2:1 on the fill).
- **Tangerine variant** surface is `#8a3a00` (7.8:1 with white) after the brighter oranges measured 3.8:1 and 2.7:1; its gel `#b5500f` holds white button labels at 5.1:1.

## Reference status

`references/imac-g3/` has 5 captures plus `RESEARCH.md`: two Finder Preferences GIFs (`0201700042_ch04lev1sec2_image01/02.gif`), two Mac OS 9.x About/System Folder screenshots (`Mac_OS_9.0.4_emulated…png`, `5654e869….png`) and a Platinum Finder-windows webp. All are the **light Platinum software UI**; `RESEARCH.md` notes there is no Bondi/fruit hardware photo. So the translucent-plastic shell, the Bondi/fruit hexes and the pinstripe are backed by the RESEARCH text ("translucent Bondi Blue candy shell") and the verified `#0095b6` hardware colour, not by any image in the folder.

## v5 layout

- **Tiers.** No rail at any size; the rounded bar and status strip work on phones and tablets, where core stacks the brand and actions over a scrolling nav line. Under 480px the case lip slims (0.9rem corners, tighter status padding and gap) so the status foot's last readout clears its rounded corner.
- **Nesting.** The diagonal sheen is the surface's top background layer, not a clipped pseudo-element, so panels no longer need `overflow: hidden` (which cut off menus and popovers opened inside them). A panel or card inside another surface keeps the gloss and pinstripe but drops the streak: one streak per stack of plastic.
- **XL gutter art (1801px+).** The case continues past the screen as ribbed translucent plastic with one broad diagonal sheen, white at low alpha so every colorway tints it.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
