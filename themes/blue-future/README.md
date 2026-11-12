# Blue Future

> A futuristic sci-fi HUD: deep-space navy with cyan neon glow.

**Requires: L1** — sets `--app-*` layout properties; recolors correctly at L0 (tokens only) but only reaches its intended layout once the app shell is adopted. See "Adoption" below.

## What this theme is trying to achieve

An **advanced spacecraft computer** — or a high-end industrial control
system. Precise, uncluttered, dark. The reading should be "this instrument
is telling me the truth about a machine," not "this website has a neon
aesthetic."

The reference look is a live recorder/telemetry dashboard: a dark navy
shell, monospaced readouts, thin cyan rules, and glow used to mark what is
*live* rather than to decorate what is merely present.

## Core values

1. **Glow is a signal, not a decoration.** A glow means energized, live,
   selected, or focused. If everything glows, nothing is live. This is the
   rule most often broken when extending the theme.
2. **Telemetry is monospaced.** Any raw machine value — timecode, counts,
   IDs, sample rates, file sizes — sets in `--font-mono` with tabular
   figures (`.mono`). Proportional digits that jitter as they count
   break the instrument illusion.
3. **Cyan means live data; blue means interactive.** `--accent` (cyan)
   carries live/active/telemetry. `--accent-2` (blue) carries
   interactive-but-not-live. If both land on the same element, that's a bug.
   So a selected or pressed control (toggle, segment, current page, filter
   or reaction chip, active tab, open menu item, current nav item, selected desktop icon) is a blue-tinted cell
   (`--accent-2` at 35% over the panel) with a blue edge and `--text`
   label, never a solid cyan slab; solid cyan is kept for the primary
   action and live readouts.
4. **Structure over ornament.** Headings are tracked and uppercase. The
   page and section titles (`h1`, `h2`) are bright and step up in size so
   the panel has a title level; `h3`/`h4` are *dim* labels on a panel. The
   content is the bright thing; the chrome recedes. Reading content
   (`.prose`, `article`) keeps its own case.
5. **No gradients on interactive surfaces.** A flat fill plus a glow reads
   as energized. A gradient reads as a web button from 2012.

## Provenance

The palette is not invented: it is reconciled against the reference
implementation this theme is named for — a 1U rack recorder's telemetry
dashboard. Those values (`#00d9ff` cyan, `#0a1526` panel, `#0f3a5c` rule,
`#cfeeff` text, Consolas) are copied from the device, so selecting this
theme on that device reproduces its own look rather than approximating it.
Changing them is a change to the reference, not a matter of taste.

## How the tokens carry that

| Token | Value | Why this value |
|---|---|---|
| `--bg` | `#020509` | Near-black, faintly blue: a panel in a dark rack room. |
| `--surface` / `-2` | `#0a1526` / `#08192b` | Two steps up, both still very dark. The surface ladder is shallow on purpose — depth comes from hairlines and glow, not from lightening slabs. |
| `--border` / `--hairline` | `#0f3a5c` / `#0a2942` | Visible rules are blue-cast, and the hairline is dimmer: dense data needs separators that don't add up to a cage. |
| `--accent` | `#00d9ff` | Electric cyan. The live/telemetry color. |
| `--accent-2` | `#4d7dff` | Electric blue. Interactive/selected. |
| `--text` / `--muted` | `#cfeeff` / `#6f9cba` | Text is blue-white, never pure white — reserve pure white for a genuinely critical value. Muted is a real step down so labels recede below data. |
| `--font` | Consolas | Monospace as the *primary* UI font, not just for values. This single choice does more for the "spacecraft computer" feel than any color. |
| `--radius` | `0.25rem` | Almost square. Rounded corners read as consumer software. |
| `--flare` | `#d85cff` | Magenta, used almost nowhere. Held in reserve for a single rare emphasis so it keeps its force. |
| `--btn-*` | three levels | Primary is a solid 80% cyan with black text at 1.1em: the one bright action on the panel. Secondary is tinted: cyan text and border over a 25% fill (40% and a glow on hover). Tertiary is the cyan outline with no fill until hover. Danger and success are tinted in red and green; plain buttons are blue-cast cells (`--accent-2` at 14% over the panel, blue border) because blue means interactive. A lit outline on dark glass, in keeping with "a flat fill plus a glow". |

## Instruments

This theme exists for surfaces that meter something, so the instrument
primitives carry its identity more than the buttons do:

- **Meters** use true VU banding — `#0aff9d` green, `#ffe400` amber,
  `#ff2a2a` red, white peak-hold. These are deliberately *not* the theme's
  semantic `--success`/`-warning`/`-danger`: a meter is reporting signal
  level, not application state, and the eye reads the classic broadcast
  ramp faster than a palette-matched one.
- **Readouts** glow cyan and track slightly wide. A counter is the thing
  you read across the room.
- **Lamps** are round, dark-navy when off, cyan and blooming when on.
- **The transport** (GO bar) repeats the panel's corner-bracket language, and GO
  blooms rather than filling — an energized outline, not a painted button.

## Layout

A flat instrument panel: a full-width dark bar, **no rail**, edge-to-edge
content, and a status strip along the bottom for telemetry. Screen area
belongs to data, so the chrome is as thin as it can be while still framing.
This is the deliberate opposite of LCARS's chunky rail — switching between
the two should visibly move the furniture.

## Signature details

1. **Backdrop.** A fixed radial vignette (ellipse at top, `#0a1a2e` to
   `#020509` at 70%) under a faint cyan 2rem grid (`rgba(47,214,255,0.04)`
   1px lines): the interface reads as a panel in a space, not wallpaper.
   On touch screens (`pointer: coarse`) it scrolls with the page and
   drops the grid, keeping the vignette only, so phones do not repaint a
   tiled grid over a long document every frame.
2. **Corner brackets** on `.panel`, `.modal` and `.transport` (the GO bar):
   18px L-marks, 2px stroke, 0.8 opacity, top-left and bottom-right,
   inset 4px from the corner like registration marks engraved on a bezel.
   Panel and modal titles start 1.75rem in so they clear the mark, a
   panel titled by an in-body heading included, and a dialog title is
   tracked uppercase like a panel's (a
   desktop window's title bar pads its start so the icon clears it), and a
   panel title sits on a cyan-cast hairline, the bezel's engraved rule.
   Only the focused desktop window is energized: a cyan hairline under its
   title bar, while the others dim their title to `--muted`. They
   are painted as background layers (`--brackets` inside `--panel-bg`,
   `--modal-bg`, `--transport-bg`), not positioned pseudo-elements, so no
   surface gains a `position` and popovers, dropdowns and context menus
   keep anchoring to their true offset parent; they also stay put when a
   modal scrolls. Cards (KPI tiles, pricing, slides) set `--card-bg` to a
   plain surface with no outer glow: they are hairline cells, and the
   L-marks stay on the instruments. A featured list card or spotlighted
   question takes a 1px cyan edge with an inner glow, not a heavy frame.
   Bar charts are instrument bargraphs: a 30% tinted column under a 2px
   bright cap, so bars never outshine the live readouts. On touch screens
   panel, card and transport glows are dropped to keep scrolling smooth. The status bar and `.app-main` are isolated stacking
   contexts so a menu spilling out of the page never covers the bar's
   buttons.
3. **Buttons** are dark blue-cast cells with 0.05em tracking (dropped to
   0 on phones, where the wide mono face needs the room). Icon buttons are
   square like everything else. Primary carries only a faint
   `0 0 0.4rem rgba(47,214,255,0.2)` at rest (no glow at all on touch), its full
   `0 0 1rem` glow on hover, so readouts and lamps stay brightest; secondary/outline hover recolours the
   border to the glow and adds `0 0 8px`; `:disabled` is an unlit cell: no
   fill, `--muted` text and dashed `--muted` edge at 0.7 opacity, no
   shadow (present but off, never a dimmed primary). All via
   `--btn-*` tokens.
4. **Inputs** are `#08192b` cells with a `#2a6a9a` edge (3:1 on the field,
   so a field still shows inside a panel); focus recolours the border,
   keeps the outline and adds `0 0 8px rgba(0,217,255,0.35)`.
5. **Tables**: dim, 0.08em-tracked uppercase headers, hairline row rules,
   and an accent select bar (`inset 0.35rem`) on active and selected rows.
   Selected rows and list items fill blue like every other selection
   (`--accent-2` at 20% over the panel, quieter than a control's 35% so
   red and amber status text on them holds 4.5:1); cyan stays for live data. The current page
   is a roomier cell (2.4em, or the touch target) so its digit clears the blue edge; disabled
   page and carousel arrows are dashed unlit cells; carousel arrows are
   square bordered cells like the page cells. A dirty (unsaved) cell is
   marked by its amber edge alone, no tint, so it stays legible on a
   selected row. Unchecked checkboxes and radios are `#08192b` field cells
   with the `#2a6a9a` field edge (radios stay round, like lamps); checked
   ones keep the native cyan mark.
6. **Headings** are uppercase: `h1` 1.4em and `h2` 1.05em, 0.12em-tracked
   in `--text`; `h3`/`h4` 0.8em, 0.2em-tracked and `--muted` (panel labels).
   Headings inside `.prose`/`article` keep their case. Under 480px the
   `h3`/`h4` tracking drops to 0.08em so panel labels do not wrap to
   three lines.
7. **Glow range inputs**: a dim 4px `#0e3a5c` to `#1d5c8f` rail (an
   unlit scale: the rail cannot know the value, so the glow lives only
   on the thumb) (a vertical
   fader ramps bottom to top and keeps the same 4px rail inside its
   full-size hit area), 14px
   near-square `#02050a` thumb with a glow border and glow shadow
   (`--slider-*`).
8. **`.sci-switch`** (theme-scoped: `html[data-theme="blue-future"]
   .sci-switch`, invisible to every other theme): a 4.4em x 1.9em dark
   track, a sliding square thumb carrying a status LED (dim white off,
   glowing cyan on), and a readout drawn from `data-off` / `data-on`
   (dim and recessed off, glowing on). Markup:
   `<label class="sci-switch" data-on="ONLINE" data-off="OFFLINE"><input type="checkbox"><span></span></label>`.
   Slides only under `prefers-reduced-motion: no-preference`. Core's
   `.switch` carries the same look through tokens: a square 3px track on
   `#02050a`, a square thumb, cyan when on. Badges, chips and scrollbars
   are squared to 2px too: nothing on the panel is a pill. Avatars are
   2px-square blue-cast cells with a 1px `--border` ring.
   Meters sit in a `--deck-trim` (`#1d5c8f`) window edge, the same metal
   as the transport. Tabs inside a window or dialog drop to 0.02em
   tracking so a four-tab strip stays on one row.
   On phones the bar is two 44px target rows with no padding between
   them (brand and actions, then the nav), about 106px.
9. **Telemetry strip**: `.app-status` uses tabular figures and lights a
   small glowing cyan lamp before its first item, so every page carries
   one live readout.
   **Status helpers**: `.status-ok` (success), `.status-error` (danger),
   `.status-rec` or `.status-error.is-rec` (bold danger plus glow),
   `.status-idle` (success, a ready recorder is green).
10. **Type** is monospace-first (see Typography).
11. **Flare `#d85cff`** magenta is declared and held in reserve: nothing in
    this theme uses it.

Also: the meters, readouts, lamps and transport described under
"Instruments" above.

## Typography

`Consolas, "BF Inconsolata", "Cascadia Mono", Inconsolata, "IBM Plex Mono",
"SFMono-Regular", "Roboto Mono", "Noto Sans Mono", monospace` (`--font-mono`
is the same stack). Consolas is the reference face but ships only with
Windows and Microsoft Office, so Inconsolata (SIL OFL, the open
Consolas-inspired mono) is vendored as `BF Inconsolata`, regular and bold
Latin woff2 (`assets/fonts/Inconsolata-*.woff2`), with `size-adjust: 110%`
so its 0.5em cell matches Consolas's 0.55em advance and x-height. Every
machine without Consolas renders the same compact instrument face instead
of the ~9% wider DejaVu Sans Mono.

## Contrast note

`--text` and filled controls clear 4.5:1 (enforced by `scripts/check.py`).
`--muted` (`#6f9cba`) carries the dim headings, table headers and switch
readout at roughly AA, not AAA: deliberately, because "chrome recedes,
content is bright" is the theme's point. Do not brighten it.

## Reference status

Restored from the original CuTePi default ("Future SciFi") spec, with the
reconciled telemetry-dashboard palette. There are no `references/blue-future/`
captures yet.

## Extending it

Do:
- Reach for `--accent` only when the thing is genuinely live.
- Add glow via `--*-shadow` properties so it stays tunable.
- Keep new readouts monospaced and tabular.

## Don'ts

- Add a gradient to an interactive control (the slider track is a meter,
  not a button).
- Brighten `--muted` to "improve readability": the contrast floor is
  already verified by `scripts/check.py`; a label that seems too dim is
  probably one that shouldn't compete with data.
- Round the corners.
- Use `--flare` more than once on a screen.
- Put `position` on `.panel`/`.modal` to add decoration: it moves the
  anchor for popovers and context menus.
- Set `background`/`color` directly on `.btn`; use `--btn-*` tokens.

## Tell-tales of an inauthentic result

- Everything glows → nothing reads as live.
- Proportional digits in a counter → the layout twitches as it counts.
- Bright white headings → the chrome shouts over the data.
- A rounded, gradient-filled primary button → consumer web, not instrument.

## Adoption

This theme sets `--app-*` layout properties (manifest `shellAware:
true`). At **L0** (link the CSS, no shell markup) it renders correctly
recolored, but as the shell's *default* arrangement — not its intended
layout. Adopt the `.app`/`-bar`/`-rail`/`-main`/`-status` shell
(CONTRACT.md "The app shell" / "Adoption levels") to get this theme's real
layout at **L1**.

## Reference implementation & stays-app-side

The palette, deck-metalwork values and `.sci-switch` readout come from a
rack recorder's telemetry dashboard (PI9696). That dashboard consumes this
theme opt-in; with no theme it renders its own identical built-in look.

Deliberately NOT themed (app-owned, do not add hooks for these):

- OLED bezel and mirror: a hardware representation, not chrome.
- Reel-deck SVG geometry and tape animation: flat fills are exposed as
  `--deck-*` for reskinning, but the drawing itself is the device.
- Round icon buttons and transport geometry: state colors are covered by
  `.transport.is-rec/.is-play/.is-pause`, sizes stay app-side.
- uPlot chart internals: the app reads bridge tokens via
  `getComputedStyle` with identical fallbacks.
- Brand logo and modal sheet layout.

## Icons

`icons.svg` redraws the whole core set (178/178) as instrument-panel
legends:

- 24×24 grid, 1.5px hairline stroke, butt caps, mitred joins.
- Square corners on every box (no rounding, like the panels); true circles
  and arcs stay round, like the theme's lamps.
- Line only. Solid marks are reserved for indicators: a dot, a level bar,
  a list marker.
- `currentColor` everywhere, so icons follow text, `--accent` and selected
  states; no hard-coded colours.
