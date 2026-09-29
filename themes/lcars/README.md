# LCARS

> Star Trek TNG/DS9/Voyager on-screen computer — candy pills on black.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The **Library Computer Access/Retrieval System** as it appeared on screen
from 1987 onward: a black field organised by fat, rounded, candy-coloured
blocks, set in a tall condensed face, with sweeping elbow corners joining
horizontal bars to vertical rails.

The target is *recognisable at a glance from across a room* — someone
should identify it before reading a single word. If a screenshot needs a
caption to say which theme it is, it has failed.

## Core values

1. **Black is the substrate, not a colour choice.** LCARS is colour blocks
   floating on true black. Any grey "card" background is wrong.
2. **The elbow is the signature.** A horizontal bar that curves down into a
   vertical rail is the single most identifying shape in the whole system.
   The app shell's bar does exactly this (`--app-bar-radius`).
3. **Candy bars code by colour, not by meaning.** The orange/lavender/sky/
   rose/tan palette is decorative structure. Resist making every lavender
   block mean one semantic thing — that's a modern dashboard habit.
4. **Rounded ends, flat joins.** A block is a pill where it terminates and
   square where it meets its neighbour. Stand-alone buttons are full pills
   with the label pushed to the right-hand end; a row of tabs is touching
   square blocks, pill-capped only at the two ends of the row.
5. **Chunky, never dense.** This is a wall panel operated by hand, so
   `--density: 1.15`. A cramped LCARS is a wrong LCARS.
6. **Type is tall, condensed, uppercase.** Antonio stands in for the
   original's Swiss 911/Helvetica Compressed, and sets *everything*, body
   copy included.
7. **Text is coloured, never white.** Body copy is tan (`#ffcc99`),
   secondary text periwinkle (`#9999ff`), titles orange/gold.

## How the tokens carry that

| Token | Value | Why |
|---|---|---|
| `--bg` | `#000000` | True black. Not near-black — the blocks must float. |
| `--accent` | `#ff9900` | The canonical LCARS orange; the system's primary structural colour. Matches "atomic tangerine" in the documented Okuda reference palette exactly. |
| `--lcars-lavender` / `-sky` / `-rose` / `-tan` / `-peach` | `#cc99cc` `#6699ff` `#cc6699` `#ffcc99` `#ff9966` | The candy palette, namespaced so it can never collide with another theme's tokens. `-lavender` matches the reference palette's "lilac" exactly; `-sky` was corrected from an unsourced pastel periwinkle to sit close to the reference's saturated blue family ("mariner"/"bahama-blue") while still clearing the button-text contrast floor. |
| `--surface` | `#000000` | Panels have no fill; they are candy elbow frames on the black substrate. |
| `--text` / `--muted` | `#ffcc99` / `#9999ff` | Coloured text, as on screen. |
| `--radius` | `1.4rem` | Large by default — everything wants to be a pill. |
| `--on-accent` | `#000000` | Black text on candy fills. LCARS never sets light text on a colour block. |
| `--density` | `1.15` | Deliberately loose. |

Source: the Okuda-designed LCARS palette (Michael and Denise Okuda,
conceived for TNG starting 1987) as documented by the `trekcolors`
reference project — not a single "official" style sheet, since LCARS
predates CSS by a decade, but the closest thing to a canonical hex list
this catalog could verify against.

## Signature details

- **Panels are elbow frames.** `.panel`, `.card` and `.modal` get a thick
  candy leg down the left that sweeps round a curved elbow into a bar
  across the top (two borders; the inner curve falls out of the outer
  radius minus the border widths). A panel's `.panel-header` is pulled up
  into that bar and set black, flush right — the on-screen section-title
  position. Frame colours rotate orange → lavender → peach → periwinkle by
  position.

- **Meters** band in the *candy* palette (sky → orange → rose) rather than
  green/amber/red. A traffic-light meter instantly reads as a modern audio
  app wearing an LCARS costume.
- **Readouts** set in Antonio, large and blocky — the on-screen numerals.
- **The transport** is a black bar with a thick orange edge, and GO is a
  solid orange elbow (`0 1.4rem 1.4rem 0`), not an outline. On this theme
  the primary action is a *block*, consistent with everything else.
- **Lamps** are rounded rectangles, not circles: LCARS has few true circles.

### Icons

`themes/lcars/icons.svg` redraws six icons (home, settings, search,
close, user, bell) entirely out of LCARS' own geometric vocabulary —
pill-ended rounded rects, sharp elbow curves and solid `currentColor`
block fills — never naturalistic iconography. Settings becomes a plus of
pill segments around a dot (a targeting-reticle abstraction, not a gear),
and close is two pill bars crossed at 45°, matching the on-screen UI's
habit of representing every control as an abstract colour block rather
than a picture of the thing it does. The sprite ships 136 `<symbol>`s in total (`grep -c '<symbol'`), and each differs from the generic outline sprite in `assets/icons/icons.svg`; only the six above are described here, and the rest were not audited one by one for style.

## Layout — this theme moves the furniture

Selecting LCARS re-arranges the app shell, it does not merely recolour it:

- a **7rem candy rail** appears down the left (`--app-columns`), drawn
  entirely in CSS as fixed-height blocks (rem stops, so a long page doesn't
  stretch them into slabs) separated by black gaps, the top two carrying
  black block codes at their lower right, the last running on to the
  bottom;
- the **top bar becomes an orange elbow**: a thick leg over the rail that
  curves into a thin bar running right, ending in separate pill-capped
  segments; the brand becomes the large right-aligned screen title and nav
  items become pills on the black above the bar;
- the **status strip is the mirrored bottom elbow**, in tan, closing the
  frame.

On phones the rail becomes a horizontal colour strip under the bar rather
than disappearing — the colour coding is most of the identity.

`themes/lcars/chrome.css` additionally offers a richer, opt-in frame with
individually rounded rail bars and a real nav inside the rail, for apps
willing to add markup. Most apps should use the shell instead.

## Extending it

Do:
- Add new colours from the candy palette, namespaced `--lcars-*`.
- Keep black text on every coloured block.
- Let blocks touch with flat joins and terminate with pills.

Don't:
- Introduce grey surfaces, gradients, or drop shadows — LCARS is flat.
- Make it dense to "fit more".
- Circle-round the elbow corners uniformly; the asymmetry is the point.
- Use semantic red/green for meters or status blocks where a candy colour
  would do.

## Tell-tales of an inauthentic result

- Grey cards on a dark background → a generic dark theme with orange
  accents, not LCARS.
- Uniformly rounded pills everywhere → the elbow language is gone.
- Green/amber/red meters → an audio app in costume.
- Tight rows and small type → a spreadsheet wearing LCARS colours.

## Typography

- **Display:** Antonio (Regular 400 and Bold 700), **vendored** in `assets/fonts/` (SIL OFL 1.1, see `assets/fonts/NOTICE.md`). It drives the sweep bar (`--app-bar-font`), the big numeric readouts (`--readout-font`) and the other all-caps display spots in `theme.css`. It is a stand-in: the on-screen originals are usually described as Swiss 911 / Helvetica Compressed, but nothing in `references/lcars/` names a face, so that attribution is unverified.
- **Body:** `--font` is Antonio too (falling back to `"Arial Narrow"`/condensed system faces). A proportional humanist body face under Antonio headings read as a web page, not a panel.
- Labels are uppercase with `0.05em` tracking (`--label-transform`, `--label-tracking`). Lowercase Antonio at display size undoes the look.

## Contrast honesty

The palette follows the trekcolors/Okuda hexes, so almost nothing was lifted to reach AA; black-on-candy clears the 4.5:1 floor on its own. Measured ratios of the black `--on-*` text on each fill:

| Fill | Hex | Black text |
|---|---|---|
| orange (`--accent`) | `#ff9900` | 9.81:1 |
| peach | `#ff9966` | 10.0:1 |
| tan | `#ffcc99` | 14.35:1 |
| lavender | `#cc99cc` | 9.0:1 |
| rose | `#cc6699` | 5.93:1 (the tightest candy block) |
| sky | `#6699ff` | 7.57:1 |

- **Deviations from the reference:** `--lcars-sky` was moved *away* from an unsourced `#9999ff` (8.35:1) toward the palette's saturated blue family. The reference's own "mariner" `#3366cc` is only 3.91:1 under black text, so it cannot carry black button text; `#6699ff` is the compromise. `--danger` `#d15a5a` (5.32:1 under black) and the success/warning fills are not attested LCARS hexes — LCARS has no canonical red/green semantics, so these are catalogue additions.
- **Nav on the sweep bar:** the root nav tokens (orange brand, lavender items) measured 1.0:1 and 1.3:1 on the orange bar, so the bar overrides both to black (9.81:1).
- `--muted` `#9999ff` is 8.35:1 on the black `--surface`; `--text` `#ffcc99` is 14.35:1.

## Reference status

`references/lcars/` holds 10 captures (`475c60fc…jpg`, `Lcars_wallpaper.svg.webp`, `README-banner.png`, `README-sweep.png`, `Starship_LCARS_Interface_E_900_for_Site.webp`, `Tuvok-LCARS.webp`, `images.jpg`, `images-1.jpg`, `images-2.jpg`, `screenshot-1-500x300.png`) plus `RESEARCH.md`. The 2026-09-26 audit there calls them pure LCARS diagrams and schematics (pill blocks, elbows, master-systems displays), no people. `RESEARCH.md` records no hex values and no per-file mapping, so the candy hexes rest on the trekcolors palette (cited above), not on sampling these images. The two `README-*.png` files are not described in `RESEARCH.md`; their provenance is unverified.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
