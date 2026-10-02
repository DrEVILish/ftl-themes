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
4. **Structure over ornament.** Headings are tracked, uppercase, *dim* —
   they are labels on a panel, not titles on a page. The content is the
   bright thing; the chrome recedes.
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
2. **Corner brackets** on `.panel`, `.modal` and `.transport` (the GO bar):
   14px L-marks, 2px stroke, 0.55 opacity, top-left and bottom-right. They
   are painted as background layers (`--brackets` inside `--panel-bg`,
   `--modal-bg`, `--transport-bg`), not positioned pseudo-elements, so no
   surface gains a `position` and popovers, dropdowns and context menus
   keep anchoring to their true offset parent; they also stay put when a
   modal scrolls.
3. **Buttons** are dark cells with 0.05em tracking. Primary carries
   `0 0 0.7rem rgba(47,214,255,0.3)`; secondary/outline hover recolours the
   border to the glow and adds `0 0 8px`; `:disabled` is flat at 0.35
   opacity with no shadow. All via `--btn-*` tokens.
4. **Inputs** are `#08192b` cells; focus recolours the border, keeps the
   outline and adds `0 0 8px rgba(0,217,255,0.35)`.
5. **Tables**: dim, 0.08em-tracked uppercase headers, hairline row rules,
   and an accent select bar (`inset 0.35rem`) on active and selected rows.
6. **Headings** are 0.8em, 0.2em-tracked, uppercase and `--muted`.
7. **Glow range inputs**: 4px `#0e3a5c` to cyan gradient track, 14px
   near-square `#02050a` thumb with a glow border and glow shadow
   (`--slider-*`).
8. **`.sci-switch`** (theme-scoped: `html[data-theme="blue-future"]
   .sci-switch`, invisible to every other theme): a 4.4em x 1.9em dark
   track, a sliding square thumb carrying a status LED (dim white off,
   glowing cyan on), and a readout drawn from `data-off` / `data-on`
   (dim and recessed off, glowing on). Markup:
   `<label class="sci-switch" data-on="ONLINE" data-off="OFFLINE"><input type="checkbox"><span></span></label>`.
   Slides only under `prefers-reduced-motion: no-preference`.
9. **Status helpers**: `.status-ok` (success), `.status-error` (danger),
   `.status-rec` or `.status-error.is-rec` (bold danger plus glow),
   `.status-idle` (success, a ready recorder is green).
10. **Type** is monospace-first (see Typography).
11. **Flare `#d85cff`** magenta is declared and held in reserve: nothing in
    this theme uses it.

Also: the meters, readouts, lamps and transport described under
"Instruments" above.

## Typography

`Consolas, "IBM Plex Mono", "SFMono-Regular", monospace`. Consolas is the
reference face but ships only with Windows and Microsoft Office; nothing is
vendored. IBM Plex Mono and SFMono are used only if installed locally, so on
most Linux/Android devices the final generic `monospace` (DejaVu Sans Mono,
Roboto Mono, ...) renders. Metrics are close but not identical.

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
