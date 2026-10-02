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

## Variants

The frame is the same across the shows; the paint changed. The default is
plain **LCARS** — the orange-led palette. Select the others with `data-variant` on `<html>` (CONTRACT.md
"Palette variants"):

| `data-variant` | Era | Palette |
|---|---|---|
| *(none)* | LCARS | Orange-led candy: orange, lavender, peach, tan. |
| `voyager` | Voyager / DS9 | Gold-tan `#cc9966` structure with blue-violet `#9999cc`/`#6688cc` and brick `#cc6666`. |
| `picard` | Picard (2399) | Cold blue `#5588ee` structure, ice-blue text `#ddeeff`, red `#ee5555`/orange `#ff8844` accents. |

Every fill keeps black text at 4.5:1 or better (lowest: `#cc6666` 5.66:1).

## Core values

1. **Black is the substrate, not a colour choice.** LCARS is colour blocks
   floating on true black. Any grey "card" background is wrong.
2. **The elbow is the signature.** A horizontal bar that curves down into a
   vertical rail is the single most identifying shape in the whole system.
   The app shell's bar does exactly this (`--app-bar-radius`).
3. **Five colours, each with a job** (see `references/lcars/RESEARCH.md` §8). The orange/lavender/periwinkle/
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
7. **Two text colours, three sizes.** Normal text is tan (`#ffcc99`), the
   highlight orange (`--accent`) — nothing else, never white. Type comes
   in three sizes only: main title (2.4rem), sub header (1.25rem), normal
   data (0.95rem); only printed ruler numerals on scales are exempt.

## How the tokens carry that

| Token | Value | Why |
|---|---|---|
| `--bg` | `#000000` | True black. Not near-black — the blocks must float. |
| `--accent` | `#ff9900` | The canonical LCARS orange; the system's primary structural colour. Matches "atomic tangerine" in the documented Okuda reference palette exactly. |
| `--lcars-lavender` / `-periwinkle` / `-peach` / `-tan` | `#cc99cc` `#9999ff` `#ff9966` `#ffcc99` | With `--accent` `#ff9900`, the five structural colours: orange = active/real-time, lavender = idle controls, periwinkle = information, peach and tan = frame (tan is also the text colour). `--lcars-sky`, `-rose` and `-gold` survive only as aliases into these five, so no sixth hue appears. `--danger` is the one alert colour. |
| `--surface` | `#000000` | Panels have no fill; they are candy elbow frames on the black substrate. |
| `--text` / `--muted` | `#ffcc99` / `#ffcc99` | One normal text colour; the highlight is `--accent`. |
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

- **Meters** are MSD-panel gauges — black tubes with a lavender tick ruler, filled from the bottom — banded periwinkle → orange → alert red rather than
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
| periwinkle | `#9999ff` | 8.35:1 |

- **Deviations from the reference:** none in the structural palette — all five fills are documented Okuda hexes. `--danger` `#d15a5a` (5.32:1 under black) and the success/warning fills are catalogue additions for state; LCARS has no canonical red/green semantics.
- **Nav on the sweep bar:** the root nav tokens (orange brand, lavender items) measured 1.0:1 and 1.3:1 on the orange bar, so the bar overrides both to black (9.81:1).
- `--text` / `--muted` `#ffcc99` is 14.35:1 on black; the `--accent` highlight `#ff9900` is 9.81:1.

## Reference status

`references/lcars/` holds 237 captures plus `RESEARCH.md`: the default (TNG) look at the top level and in `tng/` and `tng-films/`, the `voyager` variant's DS9 panels in `voyager/`, and the `picard` variant's capture in `picard/`. Every file is named by the UI components it shows (`elbowFrame-pillButton.webp`) and scored in `INDEX.md`, which also maps each old filename. No people in any of them. No hex values were sampled from these images, so the candy hexes rest on the trekcolors palette (cited above).

## v5 layout

- **Tiers.** Phones and tablets (up to 900px): the rail becomes a horizontal colour strip under the bar (a 7rem rail would cost a tablet its content width), and the frame's leg slims to 2.5rem. In the bar the app's actions and the screen title share line 1 (the title keeps its place at the right end and truncates) and the nav pills run along line 2, scrolling sideways. The split frame's second bar and the block codes are desktop-only. `chrome.css` collapses its optional rail at the same 900px tier.
- **Nesting.** Panel titles are pulled into the bar using core's `--surface-pad`, so they land in the bar at every tier. A frame inside a frame steps down to the thin card weights and keeps clear of the content above it. A scrolling panel's title sits under its bar (a scroller clips anything pulled out of it), and a header holding form controls becomes a full-width control row under the bar. Stacked-table labels use `--muted`.
- **XL gutter art (1801px+).** Out-of-focus neighbouring panels: dimmed candy bar fragments and elbows, within about 1.3:1 of the black.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.

## Frame fidelity against the originals (2026-09 audit)

Checked against the TNG wallpaper frame and the Sovereign-class display in
`references/lcars/`. Differences found, and what changed:

1. **Split double frame.** The originals stack two frames: the header's
   elbow opens *down*, and below a black gap a second elbow opens *up*
   out of the rail's first block into a bar over the content. The shell
   had only the first. Now `.app-main` carries the lower bar and the
   inner curve, the rail's top block rounds into it, and the column gap
   is gone so the bar runs flush out of the rail.
2. **Segmented bars.** Original bars break along their whole run — long
   runs, short blocks, thin strips riding one edge, black gaps. Both the
   header bar and the new lower bar now do.
3. **Titles in a break in the bar.** Original titles are coloured text
   on black set into a gap in the bar, taller than the bar — not black
   text printed on it. Panel titles now are, in the frame's colour.
4. **Bracket frames.** Original frames are brackets: leg, top bar *and*
   a bottom bar with its own elbow. Panels, cards and modals now close
   along the bottom too.
5. **No strokes.** LCARS has no outlines or hairlines, only fills. Inputs
   are dark wells with a candy pill cap, the log/switches/toggles lose
   their outlines, table rules and hairlines are gone, strips are filled
   blocks.
6. **Labels bottom-right.** Button labels now sit in the bottom-right
   corner of taller blocks, as on every LCARS key.

Known remaining difference: original rails label *every* block with a
code; the shell rail is one empty element with two pseudo-elements, so
only its top two blocks carry codes.

## Reference rules pass (against `references/lcars/RESEARCH.md`)

Reviewed every demo page against the guideline and manifesto rules:

- **Frame thickness** — panels now run a thick leg (1.6rem) into thin
  bars (0.8rem top, 0.5rem foot); cards 1rem into 0.4/0.3rem.
- **Three sizes / two text colours / five colours** — enforced as above.
- **Vector look** — knobs are flat discs with a black pointer, fader caps
  flat lavender blocks with a black centre line, lit keys no longer glow.
- **No strokes** — dropdowns, context menus, popovers, tooltips,
  dropzones and keycaps lost their outlines (dark wells / lavender pills).
- **Two spacing constants** — 0.3rem inside a frame (segments, rail
  blocks, tabs), 0.6rem between frames (the upper and lower frame).
- **3:1 buttons** — 6.9rem × 2.3rem minimum, labels bottom-right, never
  wrapped. Long labels still stretch the pill: CSS can't see label
  length, so choosing the flat-ended variant for them is the app's call.
- **Modal titles** sit on black under the bar (a modal scrolls, so a
  title pulled into its border would be clipped).
- **Data displays** — meters are gauges; the EQ curve is a glowing
  periwinkle trace on a black grid inside a `[ ]` bracket.

## Corner geometry pass

- One elbow rule everywhere: outer radius `(leg + r) × (bar + r)`, inner
  curve a true circle of radius `r` (shell r = 1.5rem, panels 0.8rem,
  cards/transport 0.5rem). The shell's upper elbow, lower (rail) elbow,
  status elbow and every panel/card/transport bracket now follow it; the
  lower elbow's inner fillet is sized to its own r instead of a fixed
  1.25rem.
- Every other corner is square: `--radius` is 0, so dropdowns, menus,
  popovers, tooltips, dropzones, meters, logs, mixer strips and EQ
  fields are cut flat. Only buttons, tabs, badges, keys and caps are
  round.
- Bar arms end flat; a panel's top arm then carries a separate cap (gap,
  then a full semicircle), and both shell bars end in a short capped
  segment after a gap — the cap is the full stop, never a rounded bar.
- The transport is a bracket (thick leg, thin arms, square ends) instead
  of a left edge with one rounded corner.

## Per-page review (theme vs markup)

Fixed in the theme:

- **Modals clipped** (powerstation, livechat, marketing, components): an
  LCARS modal ran 30-70px taller than other themes', so fixed-height demo
  stages cut its top and bottom bars off. Modals are now compact.
- **Panel titles** ran into the bar's cap in narrow panels, and headers
  with a sub-line or buttons (ticket header) lost their controls; titles
  now stop short of the cap, sub-lines sit inline and shrink first,
  header buttons drop their minimum width.
- **Button rows overflowed** their frame (ticket actions): minimum widths
  are smaller and long labels break onto a second line, bottom-right.
- **Tabs** wrapped into two rows (caps mid-run); they now stay one row and
  scroll sideways.
- **Horizontal meters** (tables, cards) had no visible track; only
  vertical meters are ruler tubes now.
- **One face**: logs, codes and table figures were Consolas; now Antonio
  with tabular figures.
- **Zebra rows**, **plain accordion rows** and **plain section links**:
  no grey bands; accordion rows are lavender bar segments with caps (open
  = orange); section links are lavender codes.
- **Pages without the app shell** (marketing) had no frame at all; the
  free-standing top nav is now an elbow with the brand as screen title.

Needs markup (left as is):

- Demo stages are fixed-height; marketing's is too small even for Aqua.
- The ticket inbox column and chat presence list are not in panels, so
  they get no frame; the chat's narrow side columns squeeze names.
- Long button labels should switch to the flat-ended variant — an app
  decision, not visible to CSS.
- Only two rail blocks can carry codes without rail markup.

