# Hot Wheels

> Blister-pack orange on track-black — flame stripes, checkered flag, no subtlety.

## What this theme is trying to achieve

The **Hot Wheels blister-pack and track aesthetic**: matte black asphalt,
flame orange, bold italic uppercase type, and the checkered-flag motif —
built to feel aggressive and fast, like packaging for a toy car, not a
calm productivity tool.

## Core values

1. **Black is the track, orange is the flame.** `--ftl-bg`/`--ftl-surface`
   stay near-black; `--ftl-accent` orange is the only thing allowed to be
   loud. A washed-out or pastel orange has missed the point entirely.
2. **Bold, italic, uppercase.** Headings lean into the logo's aggressive
   italic wordmark — `text-transform: uppercase`, `font-style: italic`,
   wide letter-spacing. Anything set in regular-weight title case reads
   as the wrong theme.
3. **Angles, not curves.** `--ftl-radius: 0.35rem` — enough to avoid razor
   edges, not enough to look soft. Buttons use an angled (`135deg`) flame
   gradient, not a vertical one.
4. **The flame stripe and the checkered flag are the signature shapes.**
   The app bar's diagonal orange-to-yellow band and the status bar's
   small black/white checker pattern are what read "Hot Wheels" before a
   single word does — losing either is losing the theme.
5. **Dark text on the bright fills.** `--ftl-on-accent`/`-danger`/`-success`
   are all near-black, not white — bright orange/red/green with white text
   reads as a generic dark dashboard instead of packaging.

## Signature details

- The app bar's flame stripe is a single angled gradient band, not a
  repeating pattern — one clean streak, like a paint job, not wallpaper.
- The status bar's checkered flag uses a small `0.6rem` tile size so it
  reads as a flag trim, not a full chessboard filling the strip.
- Table header text and active nav items pick up the accent color directly
  instead of just the border, so scanning a table still feels branded.

## Layout

The app shell becomes a **black track panel**: a 3px orange rule under the
bar (with the diagonal flame stripe cut across it), a plain black main
well, and a checkered-flag status strip along the bottom.

## Tell-tales of an inauthentic result

- Pastel or muted orange instead of the saturated flame color.
- Upright, regular-weight headings instead of bold italic uppercase.
- Rounded pill shapes anywhere — this is angles, not Barbie's curves.
- White text on the bright accent/danger/success fills.

## Adoption

This theme sets `--ftl-app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.ftl-app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
