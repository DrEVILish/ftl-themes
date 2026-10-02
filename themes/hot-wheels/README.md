# Hot Wheels

> Blister-pack orange on track-black — flame stripes, checkered flag, no subtlety.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The **Hot Wheels blister-pack and track aesthetic**: matte black asphalt,
flame orange, bold italic uppercase type, and the checkered-flag motif —
built to feel aggressive and fast, like packaging for a toy car, not a
calm productivity tool.

## Core values

1. **Black is the track, orange is the flame.** `--bg`/`--surface`
   stay near-black; `--accent` orange is the only thing allowed to be
   loud. A washed-out or pastel orange has missed the point entirely.
2. **Bold, italic, uppercase.** Headings lean into the logo's aggressive
   italic wordmark — `text-transform: uppercase`, `font-style: italic`,
   wide letter-spacing. Anything set in regular-weight title case reads
   as the wrong theme.
3. **Angles, not curves.** `--radius: 0.35rem` — enough to avoid razor
   edges, not enough to look soft. Buttons use an angled (`135deg`) flame
   gradient, not a vertical one.
4. **The flame stripe and the checkered flag are the signature shapes.**
   The app bar's diagonal orange-to-yellow band and the status bar's
   small black/white checker pattern are what read "Hot Wheels" before a
   single word does — losing either is losing the theme.
5. **Dark text on the bright fills.** `--on-accent`/`-danger`/`-success`
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

## Don'ts

- **No white text on the orange, red or green fills.** Use the near-black `--on-*` tokens.
- **No pastel or muted orange.**
- **No rounded pills**; radius is `0.35rem`.
- **No upright, regular-weight, title-case headings.** Bold italic uppercase only.
- **No vertical gradients on buttons;** the flame runs at `135deg`.
- **No second brand colour beyond orange/yellow** (with blue only where the blister pack calls for it).

## Typography

`--font` is `"Arial Black", Impact, Arial, sans-serif`; `--font-mono` is `"Courier New", Consolas, monospace`. All **system fonts, none vendored** — Arial Black and Impact are near-universal on Windows/macOS but missing on many Linux installs, where plain Arial renders and loses the heavy weight. The reference is an italic chrome-style wordmark (the game menu capture); the theme approximates it with heavy weight plus `font-style: italic` and uppercase, not the real logo lettering.

## Contrast honesty

- **The orange was not lifted; the text colour was flipped.** `--accent` `#ff5f00` is unchanged, but white on it is only 3.05:1. Instead of darkening the orange until white passed (which would turn it brown), `--on-accent` is near-black `#1a0900` (6.36:1). The same choice applies to `--danger` `#ff2d2d` (`#1a0000`, 5.43:1) and `--success` `#29d17a` (`#04220f`, 8.46:1). There is no before/after hex pair for the fills themselves.
- **The orange hex is not measured from a capture:** `RESEARCH.md` records no hex ("track orange"), so `#ff5f00` is the theme's number.
- **On dark surfaces** `--accent` is 6.49:1 on `--bg`, 5.94:1 on `--surface`; `--muted` `#9a9a9a` is 6.43:1 on `--surface` and 5.59:1 on `--surface-2`.
- **Red as text:** `--danger` is 5.34:1 on `--bg`; `--danger-text` `#ff6e6e` is the lighter variant for small copy.

## Reference status

`references/hot-wheels/` has 3 captures plus `RESEARCH.md`: `Hot-Wheels-Unleashed05282022-…jpg` (game menu: flame logo, orange track, italic chrome type), `aa470424….jpg` (flame-logo wallpaper) and the 1999 PC set webp (blue/yellow flame hardware). They back the orange track, flame motif and italic type. `RESEARCH.md` states there is no blister-pack card capture, so the blister-pack colours are not backed by a file, and although the outsider read in `RESEARCH.md` names a checkered-flag finish, no capture is described as showing one (unverified).

## v5 layout

- **Tiers.** No rail at any size. On phones and tablets (up to 900px) core puts the brand and the app's actions on the bar's first line and the black nav strip on a second, sideways-scrolling line. The brand's blue logo badge keeps its own width there instead of stretching across the free space, and tightens its padding on phones.
- **Nesting.** Nothing is drawn per surface beyond the orange outline, so nested panels and cards need no step-down rules.
- **XL gutter art (1801px+).** A length of orange track runs down each side, raised lips and dark joints every 120px, burnt down to within about 1.3:1 of the black.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
