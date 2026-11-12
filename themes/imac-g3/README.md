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

- The pinstripe (a 90deg `repeating-linear-gradient`, a 2px white-8% /
  2px black-5% pair every 4px, strong enough to survive the gloss on top
  of it) sits on panels, cards, lists, menus and the app bar. It reads as
  vertical case ribbing, not the CRT scanlines a horizontal stripe made.
- Every gloss gradient is three stops (bright highlight → faint → the base
  surface colour), never a plain two-stop fade — that middle fade-out is
  what reads as translucent plastic rather than a painted highlight. The
  middle stop is the colorway's bright candy tone (`--imac-g3-candy`:
  Bondi `#0095b6`, Blueberry `#4a86ff`, Grape `#b06ae8`, Tangerine
  `#ff8a1f`) at 35%, glowing through the darker text-bearing surface, and
  `var(--surface)` is the opaque last layer, so overlapping windows never
  show through each other's title bars (`--modal-header-bg` has the same
  opaque base).
- **Bright candy edges.** Every panel and card carries
  `--imac-g3-edge-glow` inside its ice rim: a 2px ring of the candy tone
  at 75% and a soft 12px top glow, both inside the padding where no text
  sits, so the plastic refracts brightest at its edges (as the hardware
  does) while the text-bearing core stays `--surface`. The app bar's gloss
  peaks at 50% candy (white 4.8:1; Tangerine keeps 35%) and the backdrop
  vignette falls to `#0b6f86` rather than near-black.
- **The white chin.** The status foot is an ice band (`#f4fbfd` to
  `#d3eaf0`) with dark `#0f3a44` ink, like the hardware's white lower
  bezel; `.app-status` re-inks `--text`, `--muted`, `--link`,
  `--accent-text` and the state text tokens for everything it holds.
- **Platinum title bars.** Modal and desktop-window headers
  (`--modal-header-bg`) are Mac OS 8/9 Platinum title bars in ice: 1px
  horizontal pinstripes every 3px over an ice gradient, dark Charcoal-voice
  titles and the square Platinum close box at the start.
- **Ice.** The colour is set in frosted white plastic (`--imac-g3-ice`,
  `rgba(232,248,252,0.7)`): every panel and card has a 3px milky rim
  (`--panel-border`), menus, popovers, toasts, toolbars and grouped
  fieldsets have ice rims too, and the case body (`.app-main`) has 12px
  frosted side walls (4px on phones, where width is scarce) plus a 3px ice seam under the bar and over the
  status foot (4px under the bar), so the shell reads as one moulding,
  like the hardware's front bezel.
- **Every surface is moulded plastic.** Toolbars, context menus,
  dropdowns, popovers and toasts take the panel fill; table heads are a
  three-stop gloss with rounded top corners; alerts get a short gloss over
  `--surface-2`. Toolbars and fieldsets carry `--radius`. Logs take the
  gloss with a 3px ice rim, empty states are an ice-rimmed moulded well,
  skeletons are frosted ice, badges carry a 1px ice rim, and input addons
  are rounded gel beads (`--input-radius` outer corners, white label).
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
- The app bar and status foot carry the same candy mid-stop gloss as the
  panels (the candy tone at 35% over `--surface`, with a 1px inset white
  lip rather than a white stop, so nav text holds 4.5:1), so the most
  visible chrome is plastic too. Tangerine's bar GO label is white. Nav items and every `.nav-brand`
  are pure white (`--nav-brand-fg` is set at the root, not only in the bar).
- The case body (`--app-main-bg`) is 70% surface at the top, so the page
  title holds 4.5:1 under the vignette's bright crown, and it falls toward
  the colourway's gel (`--imac-g3-gel`) at the bottom, so the lower case
  glows rather than going flat dark. Tinted bands (`--band-tint-bg`) and
  media canvases (`--ratio-canvas-bg`) take the panel fill.
- Desktop windows keep their four dialog tabs on one row (they scroll
  rather than wrap) and use a 0.9rem fieldset radius, so the
  OK/Cancel/Apply footer fits the fixed window height.
- On touch and narrow screens (`pointer: coarse` or 600px and under) the
  panel's inset fall-off and top glow become unblurred lips, and every
  scrolling surface (panels, cards, lists, toolbars, toasts, menus) drops
  the pinstripe and the diagonal sheen for a single gloss over
  `--surface`, to keep scrolling within the render budget. The app bar
  keeps its ribbing.
- Tangerine keeps its card surface dark (`#8a3a00`, 7.8:1 under white)
  but puts real tangerine everywhere else: a true-orange `--surface-2`
  (`#a84a05`, white 5.8:1) under buttons, badges and banners, the candy
  edge glow on every card, a `#e8761f` to `#8a3a00`
  backdrop, a warmer `--bg` (`#9a4708`, white 5.0:1), a `#b5500f` gel that
  also lights the lower case body, and the `#ff8a1f` candy tone in the
  gloss, so it reads as orange plastic, not copper.
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
- **Do not present this as the Platinum OS look.** The reference software UI (`references/imac-g3/`) is light grey Platinum; this theme is the hardware-inspired shell, borrowing only Platinum's striped title bars, square close box and Charcoal title voice.

## Icons

`icons.svg` redraws the full core set (178/178). Rules: 24 grid, 2.4px stroke,
`round` caps and joins forced, and generous radii on every rect (about 0.3x
the short side, max 4.5; bars 4px or narrower become full pills). Line only:
nothing is filled, marker dots are r1.1 rings, colour is always
`currentColor`.

## Typography

`--font` is `Geneva, "Lucida Grande", "Helvetica Neue", Helvetica, Arial, sans-serif`: Geneva was Mac OS 8/9's small-text face, so body copy leads with the 1998 voice before the later Mac sans and the metric-compatible fallbacks. `--font-mono` is `Monaco, Menlo, Consolas, ui-monospace, monospace`. Headings (`h1`–`h3`), the brand (at 1.15em) and modal/window title bars use `--imac-g3-font-ui`: `Charcoal, Chicago, "Arial Narrow", "Liberation Sans Narrow", var(--font)` at weight 700 with `-0.015em` tracking. Charcoal and Chicago are named first for machines that have them (they are not free to vendor); elsewhere a narrow grotesque bold keeps Charcoal's bold, semi-condensed silhouette rather than a plain Arial. (Baloo 2 was dropped: a rounded modern display face with no tie to 1998 Apple. A Garamond like EB Garamond, closer to Apple's 1998 marketing voice, is not vendored in `assets/fonts/`.) Headings carry a moulded `0 1px 0 rgba(0,0,0,0.35)` drop rather than a white glow.

## Contrast honesty

The shell is a saturated mid-tone, so this theme sits near the floors and `python3 scripts/check.py` prints AAA warnings for it:

- **Body text (AAA warning):** `--text` white on `--surface` `#0c6478` is 6.8:1 (floor 7.0:1); on `--bg` `#0a545f` it is 8.58:1. It clears AA everywhere but not AAA on `--surface`.
- **Accent legibility:** `--accent` is `#3cc6e2`, 3.3:1 on `--surface` and 4.2:1 on `--bg`, so tab underlines, selected-row bars and segmented edges clear the 3:1 non-text floor (the earlier `#00b0d4` was 2.6:1).
- **Bondi lifted from the reference:** the verified hardware colour Bondi Blue is `#0095b6`; shipped `--accent` is `#3cc6e2`, the light aqua end of the same family; true Bondi is the candy tone in the gloss and edge glow. True Bondi is only 1.92:1 against `--surface`, so it cannot be used as text on this shell at all.
- **Surface-2 darkened:** `#0f7d92` left white at 4.81:1 and every tinted text token under 4.5:1 on context menus, toasts and readonly fields, so `--surface-2` is `#0d7489` (white 5.42:1, `--muted` `#f5fcfd` about 5.2:1). The button gel keeps the old `#0f7d92` stop (as `--imac-g3-gel`), so buttons look the same. Accent as text (badges, links, readouts, active tab, GO, `.schedule`) is `--accent-text` `#cff4f9`; raw `--accent` is 3.3:1 on `--surface`, below the 4.5:1 text floor. Selection frost is `rgba(255,255,255,0.12)` (was 0.25, white 3.1–3.9:1 on it) and series 6 is graphite `#8a9ba1` instead of near-white `--muted`, so white text on its tints passes.
- **Focus and select caret:** the focus ring is two-tone (`0 0 0 2px var(--input-fg), 0 0 0 4px #fff`), so it holds on the white wells and the coloured case alike, and the select caret is drawn in `--input-fg` on the white well (it was near-white `--muted`, about 1.05:1).
- **State text** uses pale tints (`--success-text` `#c9f8d6`, `--warning-text` `#ffebb9`, `--danger-text` `#ffe8e6`, each at least 4.6:1 on `--surface-2`) because the fills fail as text on the teal.
- **Lit pads and marker chips:** core mixes 30% accent over surface-2 there, which left white labels at 4.26:1; lit pads use 12% of the lifted accent (4.5:1+) and marker chips mix over `--surface` (4.9:1). A filled accent pill (`.pattern-nav [aria-current]`) labels in `--on-accent` (6.2:1), not the pale `--accent-text` (2.2:1 on the fill). Tinted accent badges label in white (core's 20% accent tint left `--accent-text` at 4.37:1), and secondary buttons in the brighter app bar label in white.
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
