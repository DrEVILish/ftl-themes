# Steampunk

> Victorian brass, mahogany and copper, with gear-driven dials.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

Victorian-era heavy industry as furniture: mahogany-dark wood panels,
polished brass fittings, and copper-toned readouts, as though the
interface were machined rather than rendered.

## Core values

1. **Brass is metal, not paint.** Buttons and accents are a light-to-dark
   gradient with a warm highlight — a cast, polished surface.
2. **Riveted plating.** Panels carry corner rivets (small brass dots) —
   the one recurring decorative motif, used consistently and nowhere else.
3. **Serif type, small-caps headings.** This is Victorian print, not a
   sans-serif dashboard.
4. **Warm and dark.** Mahogany brown surfaces, never grey or cool-toned.

## Signature details

- Rivets are two `::before`/`::after` pseudo-elements per panel — 6px
  radial-gradient circles at each top corner, zero markup, pure CSS.
- Headings use `font-variant: small-caps`, not `text-transform:
  uppercase` — genuine small capitals, the Victorian-print detail every
  uppercase-heading theme elsewhere in the catalog skips.
- Buttons carry a three-stop vertical gradient (`#d9ab4a` → `#a97a24` →
  `#7a5416`) — brass needs the extra middle stop other themes' two-stop
  gloss buttons don't bother with, or it reads as plastic, not metal.

## Layout

A gradient brass-edged bar and a matching wood-panel status strip — the
console reads as a cabinet fitted with brass hardware.

## Tell-tales of an inauthentic result

- Flat, ungraded brass — metal needs its highlight to read as metal.
- A sans-serif or a cool grey palette.
- Rivets missing from panels, or appearing somewhere they shouldn't
  (buttons, inputs) — they belong to panel corners only.

## v5 layout

Tiers (core): mobile ≤480px, tablet 481–900px, desktop 901–1800px, XL ≥1801px (shell capped at 1800px, centred). On a phone the bar's gear train is dropped (it would sit on the actions), and so is the space reserved for it; tablets keep it. The `h1` steps down on a phone. Nested plates are plain leather, without rivets or scrollwork, and carry a smaller, flatter brass name tag. Cards get extra padding to clear their scrollwork, and dialogs end their content above the lower scrollwork. On XL the gutters show the plant room: copper pipe runs with flange collars and a large, half-hidden flywheel gear at each outer edge, dimmed into the leather (about 1.1:1). The gutter art is still; only the bar's small gears turn.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.

## Steam-age furniture

- **Type:** IM Fell English SC (vendored, OFL — see `assets/fonts/NOTICE.md`)
  sets headings, panel nameplates, buttons, tabs, the brand and stat
  figures; headings are engraved (dark cut below, faint polish above).
  Body copy stays a book serif.
- **Brass nameplates:** every `.panel-header` is a pale polished-brass
  plate with engraved dark lettering and a slotted screw at each end.
- **Steam pipes:** a copper pipe with bolted flanges every 220px runs
  along the foot of the app bar and the head of the status strip.
- **Gear train:** a brass and a copper cog mesh at the bar's right end
  and turn slowly in opposite directions (only under
  `prefers-reduced-motion: no-preference`); hidden on phones.
- **Controls are plant, not widgets:** knobs are valve handwheels (enamel
  rim and five spokes in the band colours — oxblood, racing green, navy,
  walnut — round a brass hub, turning with the value); faders are sight
  glasses whose copper liquid stands at the fader's level, worked by a
  brass T-handle; progress bars and sliders are horizontal sight glasses;
  console keys are brass-bezelled push-buttons that glow like a filament
  lamp when lit; scribble strips are brass nameplates; the EQ curve is
  inked on a chart recorder's parchment roll.
- **Nixie tubes** for counters and timecode: `.readout-lg` and a
  transport's readout glow orange in a smoked-glass envelope with the
  tube's honeycomb mesh (Antonio stands in for the tall neon numerals).
  Smaller readouts keep the brass dial.
- **Needle gauges**: a horizontal `.meter` is an edgewise panel meter, an
  ivory scale with engraved ticks, a red zone above 70% and a red needle
  at the level. Vertical meters stay sight glasses (a boiler's level
  gauge); segmented meters keep their lamps.
- **Knife switches**: `.switch` is a copper blade with a black handle,
  hinged on a slate base; off, it stands raised at 32 degrees; on, it
  lies seated in the copper clip.
- **Filigree**: cards are brass-scrollwork plates (panels keep their
  rivets); dialogs carry the scrolls in their lower corners under the
  brass title band.


## Icons

`icons.svg` redraws the whole core set (178/178) as engraved brass
instrument glyphs, after the brass icon buttons and gauges in
`references/steampunk/`:

- 24×24 grid, 1.4 stroke, round caps and joins, true curves and arcs.
- Engraving: on plate-like glyphs (devices, lock, save, search lens,
  info, archive, cash…) the main box or circle gets a fine 0.7 inner rule,
  so it reads as a double line; big plates also get a rivet in each
  corner. Dials (clock, compass, gps, coin, album) get a toothed gear rim
  instead. Busy glyphs (calendar, table, globe…) stay plain.
- Silhouettes (bookmark, heart, shield…) carry a 35% etched tint under
  the line. Transport legends (play, pause, stop, skip) are solid castings.
- `currentColor` everywhere, so icons follow brass text, engraved plates
  and selected states.
