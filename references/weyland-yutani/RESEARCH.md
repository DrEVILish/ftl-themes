# Weyland-Yutani: research notes

Palette, shape language and type guidance only. No logo, artwork or
screenshots are reproduced or vendored. Research was done by web search in
this session (2026-09-29); the egress proxy blocked Wikipedia, Fonts In Use,
Typeset In The Future, PC Gamer and martin-fieber.de for direct fetch, so
everything below rests on **search-result summaries, not full pages**.

## Verified (as far as search snippets allow)

| Claim | Source | Used for |
|---|---|---|
| The corporate wordmark "WEYLAND-YUTANI CORP" is all-caps Eurostile / Microgramma Bold Extended; the slogan "Building Better Worlds" is lettering derived from Letraset's *Transmission* (Martin Wait, 1983, a horizontally striped semi-slab), not available digitally. | Fonts In Use, "Weyland-Yutani Corp logo and slogan in Aliens (1986)" https://fontsinuse.com/uses/35613/weyland-yutani-corp-logo-and-slogan-in-aliens (search snippet; page fetch blocked) | Extended, wide-tracked uppercase sans for headings and labels. Stack starts with Eurostile / Bank Gothic. The striped slogan face is not imitated. |
| Ron Cobb designed the Nostromo (Alien, 1979) interiors and, for Aliens (1986), the Sulaco interior; the Nostromo is described as more organic/friendly than the rigid, militarised Sulaco. Cobb also devised the wall iconography "Semiotic Standard For All Commercial Trans-Stellar Utility Lifter And Heavy Element Transport Spacecraft". | Xenopedia https://avp.fandom.com/wiki/Ron_Cobb ; Typeset In The Future, Alien https://typesetinthefuture.com/2014/12/01/alien/ ; AvP Central https://www.avpcentral.com/aliens-1986 (snippets) | Square, blocky, pictogram-like icon overrides; rigid, flat, radius-0 shell. |
| Nostromo typography reads as Helvetica-like with some elements Futura-like. | Typeset In The Future (snippet) | Neutral geometric/grotesque fallbacks (Century Gothic, Segoe UI, Arial) behind the Eurostile-class faces. |
| MU/TH/UR 6000 is a text-only terminal with scan lines and ASCII graphics on CRT; screens are green/amber phosphor on black. | Boing Boing on a fan recreation https://boingboing.net/2025/08/11/recreation-of-muthur-6000-computer-system-from-alien.html ; RPF thread https://www.therpf.com/forums/threads/muthur-6000-aka-mother-interactive-nostromo-os.364956/ ; Propstore MU/TH/UR panel https://propstore.com/product/alien-1979/large-screen-matched-mu-th-ur-6000-panel/ (snippets) | Monospace amber readouts on glass-black, faint scanlines. Green kept as `--success`. |
| Alien: Isolation (2014) deliberately mimics the 1979 film's lo-fi 1970s "analogue, low-tech, clunky" future: CRT consoles, chunky keyboards, reel-to-reel tape; Creative Assembly re-recorded UI through VHS and a CRT for authenticity. | Wikipedia, Alien: Isolation https://en.wikipedia.org/wiki/Alien:_Isolation ; PC Gamer https://www.pcgamer.com/why-i-love-the-low-fi-tech-of-alien-isolation/ ; Rely on Horror https://www.relyonhorror.com/latest-news/alien-isolation-features-a-retro-future-and-its-beautiful/ (snippets) | Static, subtle scanlines; heavy, clunky buttons; no glossy modern effects. |
| Michroma (Vernon Adams) is a Eurostile/Microgramma-influenced face under SIL OFL 1.1. | Font Squirrel licence page https://www.fontsquirrel.com/license/michroma (snippet) | Considered for vendoring; **not vendored** (see below). |

## Not verified / honest gaps

- **Exact hexes.** No source gave official Weyland-Yutani or Nostromo colour
  values. The amber (`#ffa81f`) is a tuned P3-style amber phosphor, not a
  measured value; the beige plate (`#d4cbb1`) and bone text (`#e4dcc8`)
  are my reading of "off-white/beige industrial hardware" and were not
  sampled from a source.
- **Hazard striping.** The yellow/black 45deg hazard tape is a generic
  industrial convention and the backlog's requirement. I could not confirm
  from a fetched page where it appears on screen in Alien/Aliens, so it is
  applied as a design choice, on danger states only.
- **Rocker switches.** Chunky rocker switches are in the brief; no source
  fetched supports specific proportions. The button's thick edge and dark
  underside lip is an interpretation.
- **Amber vs green.** Sources say green/amber phosphor. The 1979 film's
  terminals are commonly remembered as green; amber is chosen per the backlog
  and to sit apart from `matrix` (green).
- **Fonts not vendored.** Michroma's OFL 1.1 licence was seen only in a
  search snippet, and the font file could not be fetched under the egress
  proxy, so it is not in `assets/fonts/`. The stack names Eurostile (macOS)
  and Bank Gothic (Windows with Office); elsewhere the Century Gothic /
  Segoe UI / Arial fallbacks apply.
- **Isolation UI details** (button shapes, exact palette) were not
  verifiable from snippets.

## Screen references (supplied October 2026)

Frames supplied by the project owner, filed beside this file. They show
the terminals themselves rather than the hardware around them, and they
are what the three palette variants follow. Some are fan-made recreations
of the film screens, marked as such below.

| File | Source | What it shows |
|---|---|---|
| `mother/mother-6000-query-green.jpg` | MU/TH/UR 6000 web interface (Alien: Covenant promo, 2017) | Green phosphor text on black inside a single thin green frame; tracked caps header; underlined query links. |
| `mother/terminal-green-home-control.jpg` | Fan recreation | Green MU/TH/UR-style dashboard: label/value rows, big readout ("74°"), outlined button cells. |
| `mother/terminal-green-logo-boot.webp` | Fan recreation | Green boot screen with the wordmark: phosphor on black, nothing else. |
| `mother/terminal-green-scan.jpg` | Fan recreation | Green grid scope and radar ring over a row of small square soft keys. |
| `nostromo-cyan-targeting.jpg` | Alien (1979) | Cyan wireframe targeting display on the Nostromo bridge. |
| `emergency/alien-vs-bladerunner-environ-purge.webp` | Alien (1979) / Blade Runner (1982) | The same "ENVIRON CTR PURGE" red screen in both films: inverse-video red block with large tracked caps. |
| `emergency/terminal-red-hyperdyne-boot.jpg`, `emergency/terminal-red-inventory.jpg`, `emergency/terminal-red-logo-boot.jpg` | Fan recreations | Red phosphor terminals: a red title band across the top, thin red outlines, and a bottom row of outlined function keys ("F1 F2 F3 F4 F5 SELECT"). |
| `terminal-amber-destination.jpg` | Fan recreation | Amber/yellow terminal: header rows of label/value pairs over double horizontal rules. |
| `terminal-cyan-two-screens.webp` | Fan recreation | Cyan terminal pair: text column, side key column, bar chart. |
| `earth/earth-kirsh-specimen-monitor.jpg`, `earth/earth-kirsh-monitor-in-set.jpg` | Alien: Earth (2025) | Cyan specimen monitors: header rows of label/value pairs, a large outlined image box and an outlined DESCRIPTION box, condensed tracked caps throughout. |
| `romulus-colony-work-contract.webp` | Alien: Romulus (2024) | Colony work contract display: amber-beige segmented counters ("12 032 HRS / 17 354 HRS") in outlined boxes. |
| `login-amber-glow.jpg` | Fan wallpaper | Glowing orange wordmark and LOG IN / PASSWORD fields. |
| `phone-app-amber.webp`, `corp-mobile-register.png`, `corp-website-romulus.webp` | Romulus marketing | Corporate yellow-on-navy app and website mock-ups. Not used: they are 2024 marketing, not in-universe screens. |
| `building-better-worlds-emblem.webp` | Romulus marketing | "Building Better Worlds" globe emblem. Not reproduced. |

### What the variants take from them

- **One phosphor per screen.** Every terminal uses a single colour on
  black. Status colours are the only other hues.
- **Thin outlines in that phosphor**, not filled panels.
- **Inverse-video bands** for titles ("PRIVATE TERMINAL", "PURGE"): solid
  phosphor with black text. The variants use this for the modal title and
  tooltips in place of the beige plate.
- **A soft-key row** of outlined boxes along the bottom of the screen.
  All four palettes render the status strip this way.
- **Glow** on large text only.
