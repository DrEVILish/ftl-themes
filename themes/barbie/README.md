# Barbie

> Hot-pink glamour — glossy pill chrome, gold sparkle, all-caps confidence.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

The **Barbie brand aesthetic**: hot pink as the dominant color, not an
accent; everything glossy, rounded, and a little oversized, like packaging
for a toy rather than a productivity tool. The target is "confident and
glamorous," not "pastel and quiet" — this theme is loud on purpose.

## Core values

1. **Pink is the substrate.** `--accent` carries the whole identity;
   it shows up on every button, every active state, every header. A
   version of this theme with a muted or desaturated pink has missed the
   point.
2. **Round, everywhere, generously.** `--radius: 1.4rem`, pill buttons,
   pill badges, pill sliders. Nothing here has a hard corner.
3. **Gloss over flat.** Every filled surface gets a light highlight band —
   the same "shiny plastic" cue as the button chrome, panels, and the app
   bar. Losing the highlight reads as a cheaper, flatter knockoff.
4. **Gold is the sparkle, not the workhorse.** `--flare` (gold) shows
   up in heading glow only — it's the tiara, not a token you build
   components out of.
5. **Deep pink text, not black.** Body text is `#7a1250`, a pink-shifted
   dark plum — legible, but never plain black, which would read as a
   generic light theme wearing a pink accent.

## Signature details

- Headings are uppercase with a gold glow, the poster-title voice.
- The accent (`#c81b7a`) is one step darker than "true" Barbie Pink
  (`#e0218a`) — purely because the true value fails 4.5:1 against white
  button text; it's the minimum shift that clears the floor while still
  reading as the same pink.
- Success state uses Barbie mint (`#3ddc97`) with dark text, not a generic
  green with white text — mint is too light for white to pass, and a
  generic green would clash with the palette.

## Layout

The app shell becomes a **glossy pink ribbon**: a rounded pink gradient
bar on top, a matching sparkle-gradient status strip on the bottom, and a
soft pale-pink backdrop (`radial-gradient`) that makes the white content
card in the middle pop — box art, not a dashboard.

## Tell-tales of an inauthentic result

- Pastel/muted pink instead of the saturated hot pink.
- Sharp corners on any button, panel, or badge.
- Plain black body text.
- A generic green success state instead of the mint/dark-text pairing.

## Don'ts

- **No hard corners.** Buttons, badges and sliders are pills (`--btn-radius: 999px`); panels are `1.4rem`.
- **No black text.** Body copy is plum `#7a1250`; plain black reads as a generic light theme.
- **No pastel or desaturated pink.** A washed-out accent is the failure the theme exists to avoid.
- **No matte flat fills** on primary chrome: keep the highlight band.
- **No gold as a component colour.** `--flare` gold is heading glow only.
- **No script face on body or buttons.** Pacifico is for the wordmark and `h1` only.
- **No generic green success with white text**; keep mint with dark text.

## Typography

- **Body/UI:** `"Baloo 2"`, then `"Segoe UI", "Helvetica Neue", Arial, sans-serif`. Baloo 2 **Bold (700)** is **vendored** (`assets/fonts/Baloo2-Bold.woff2`, SIL OFL, see `assets/fonts/NOTICE.md`); only that weight exists, so headings and buttons sit at 700. If it fails to load, the stack falls to Segoe UI/Arial, which is not rounded.
- **Wordmark voice:** `"Pacifico", cursive` (Regular, **vendored**) on `h1` and the nav brand only. The brand's wordmark is a cursive script (`barbie-wordmark-2023-logo.png`), which Pacifico approximates; it is not the actual logo lettering. Fallback is the browser's generic `cursive`.
- `--font-mono` is `Consolas, monospace` (system).

## Contrast honesty

- **Accent lifted:** true "Barbie Pink" `#e0218a` (web reference from `RESEARCH.md`; the brand spec is Pantone 219C, which has no exact sRGB) is 4.42:1 under white text. Shipped `--accent` is `#c81b7a`, 5.39:1 — one step darker, the minimum that clears 4.5:1.
- **`--muted` lifted:** `#b5507e` (3.5:1) to `#9b416a` (5.32:1 on `--bg`, 6.25:1 on white, 4.63:1 on `--surface-2`).
- **Mint success:** `--success` `#3ddc97` is too light for white, so the foreground is dark `#052e1c` (8.40:1) instead of dulling the fill. As text, `--success-text` `#146c46`.
- **Nav gradient:** the pink-to-magenta bar range was chosen so white nav text stays 4.5:1 at every stop (per the `theme.css` comment: white bottomed out at 2.1:1 on earlier lighter stops and the darkest plum at 3.2:1).
- `--accent` on the pale `--bg` is 4.59:1: fine for large/UI use; `--accent-2` `#ff5cad` is 2.42:1 on `--bg` and is a decorative highlight only.

## Reference status

`references/barbie/` has 5 files plus `RESEARCH.md`: three PD logo files (`barbie-wordmark-2023-logo.png`, `barbie-the-movie-logo.png`, `barbie-mattel-seal-logo.png`) plus `Barbie_Logo.svg` and `s-l1200.png`, which `RESEARCH.md` does not describe (provenance unverified). The logos back the gloss-pink pill/script identity and rounded type. `RESEARCH.md` states an honest gap: no people-free pink product or packaging photo exists in the set, so packaging colour beyond the logo (gold sparkle, backdrop pinks, mint) is design judgement, not sampled. The 2023-era pink fill in the logos is not measured against `#c81b7a`.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.
