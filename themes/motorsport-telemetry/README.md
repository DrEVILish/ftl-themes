# Motorsport Telemetry

> The pit wall and the broadcast timing graphics: carbon panels, a timing
> tower down the left, purple/green/yellow sector colours, tyre-compound
> chips, rev-light strips and tabular figures everywhere.

**Requires: L1** — the timing-tower rail, the rev-light bar and the
race-control strip are the shell (`--app-*`). At L0 the theme still reads as
itself through its colours, carbon panels, chips and instruments, but the
tower is gone. See CONTRACT.md "Adoption levels".

## What this theme is trying to achieve

The screens a race engineer and a broadcast viewer read: dense black timing
tables where colour is information, not decoration. Purple means the fastest
anyone has gone, green a personal best, yellow slower. A coloured ring tells
you which tyre a car is on. The car's own dash adds the instruments: a rev
counter, a row of shift lights that fill green, red, then blue, and big
white figures in a black window. All of it sits on carbon fibre. Generic on
purpose (PLAN.md §21): no series, team, tyre-maker or broadcaster names or
marks, and no real driver codes, not even in the decorative tower.

References and credits: `references/motorsport-telemetry/RESEARCH.md`.

## Core values

1. **Colour is data.** Purple, green and yellow keep their sector meanings
   (accent/selection, success, warning); red, yellow, white, green and blue
   keep their compound meanings. Don't use them as decoration elsewhere.
2. **Every number is tabular.** Titillium Web's digits are fixed-width and
   the root sets `tabular-nums`. A lap time that jitters as it updates is
   wrong.
3. **Black screens, white figures.** Values are white and bold; labels are
   muted, tracked caps. The chrome stays dark so the data is the brightest
   thing on screen.
4. **Carbon is a material, not a pattern.** The twill is a few percent over
   black. If you can see a checkerboard behind body text, it's too strong.
5. **Thin, hard-edged marks.** 2px traces, 1-2px radii, no gloss, no glow.
   Broadcast graphics are flat; only the rev lights are lit.

## Signature details

- The **timing tower** in the rail: "LAP 34/57" over positions 1-20 (the
  leader boxed in white), a neutral stripe per car, interval bars (one
  purple for the fastest lap), and a tyre ring per car. Painted as one SVG
  data URI; the rail stays empty and `aria-hidden`.
- The **rev-light strip** under the bar: 15 LEDs, 5 green, 5 red, 5 blue,
  11 lit.
- **Tyre chips**: every `.badge` is a dark disc with a 2px compound ring:
  default hard white, `.badge-warning` medium yellow, `.badge-danger` soft
  red, `.badge-success` intermediate green, `.badge-accent` purple.
- **Panel headers** with a slanted purple tab at the left and bold italic
  caps; modals carry a 3px purple top edge.
- **Rev counter**: `.gauge-dial` with a green working band (yellow on
  `.is-warn`, red on `.is-error`), a red redline sector and a red needle.
- **Close** is a square black steering-wheel key with a cross; it lights
  soft red on hover.
- Table heads sit on a 2px purple rule; the selected row is purple with a
  4px purple bar, as the fastest lap is on a timing screen.
- The status strip is race control on a 2px green "track clear" rule.
- Tooltips are white caption boxes (the lower-third look).

## Token rationale

- `--accent #8b3ff0` is a purple deep enough for white text (5.2:1);
  `--accent-text #c18cff` is the same hue for text on carbon (7.5:1).
- `--danger #e8002d` is the soft-compound red as a fill; `--danger-text
  #ff4d5e` is the readable text version (5.7:1).
- `--success #1fcf6b` and `--warning #ffd60a` are bright enough to be text
  as well as fills, so their `-text` tokens are the same.
- `--flare #2fa8ff` is the blue shift light, used for meter peaks and the
  wet compound.
- `--chart-series-1..6` are the telemetry trace hues stepped into the
  dark-mode lightness band and ordered so red never sits beside green; they
  pass the dataviz palette validator against `--surface`.
- The `@font-face` blocks override ascent/descent so Titillium's tall
  default line box doesn't push text onto the edges of chips, readouts and
  small buttons.

## What not to change

- The sector and compound meanings of the colours.
- The tower must stay abstract: no driver codes, team names or real
  liveries in the rail.
- No logos or wordmarks of any series, team, tyre-maker or broadcaster.
- Don't brighten the carbon or the XL gutter traces.

## Icons

`icons.svg` redraws the whole core set (178/178) as broadcast / pit-wall
pictograms (see `references/motorsport-telemetry/`):

- 24×24 grid, 2.25 stroke, square caps, mitred joins, sharp corners.
- Every glyph leans -8° (`skewX`) like the italic broadcast type; marks
  that must stay symmetric (plus, close, minus, grid, stop, pause, sun,
  settings, snowflake, hash, frame, maximize, minimize, more) stay upright.
- Simple silhouettes (bookmark, play, filter, bar chart, phone, star) are
  solid fills; arrows get solid heads. Small lettering (PDF, PNG) drops to
  1.6 so it survives inside the heavy page outline.
- `currentColor` everywhere. No team, series or tyre-maker marks.

## Tell-tales of an inauthentic result

- Proportional digits in tables or readouts (columns of times that don't
  line up).
- Purple used for something that isn't "best/selected", or green and yellow
  swapped.
- Glow, gloss, rounded pill buttons, or a visible checkerboard behind text.
- Red as the primary accent (that's a series' brand, not the timing
  language).
- A team-coloured or logo-bearing rail.
- Light theme. Timing screens are black.

## v5 layout

- **Desktop (901-1800px):** bar across the top with the rev lights; the
  timing tower (4.75rem) down the left beside main and status; main padded
  1.25rem 1.5rem.
- **Tablet (481-900px) and phone (≤480px):** the tower packs away through
  `--app-rail-display-tablet|-mobile: none`, so content gets the full width;
  core puts brand and actions on line one and the nav scrolling on line two,
  with the rev-light strip under it. Main padding steps to 1rem/0.75rem and
  headings step down on phones. No width media queries of the theme's own
  except that heading step and the bar padding, at the core tier numbers.
- **XL (≥1801px):** the shell is capped at 1800px; the gutters show a
  data-analysis screen continuing beside it: stacked speed, throttle and
  brake channel traces over a faint grid with dashed sector splits, about
  1.2:1 over `--bg`. The traces scroll one tile every three minutes, only
  under `prefers-reduced-motion: no-preference` and not with
  `data-motion="reduced"`.
- **Nesting:** a panel or card inside a panel, card, modal or drawer drops
  the carbon weave, the header tab, the sheen and the shadow and becomes a
  flat `--surface-2` box with a hairline; a modal inside a surface keeps
  only a light shadow.
