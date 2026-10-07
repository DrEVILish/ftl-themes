# Media deck devices

Live example: [media-decks.html](../../media-decks.html). The page includes a reel-to-reel transport based on Pi9696's MIT-licensed SVG, plus original vinyl, portable cassette and MiniDisc illustrations.

## State contract

Put one state class on `.media-deck` — or, with no JavaScript, check one radio inside its
`.transport-keys` (`value="playing|recording|paused|stopped"`); `:has()` reads it and every
rule below follows. Don't combine a state class with a checked state radio on one deck.

| Class | Result |
|---|---|
| `.is-playing` | Spools/disc rotate, tape animates, play lamp lights |
| `.is-recording` | Transport animates, tape/head and lamp use danger color |
| `.is-paused` | Motion stops and the current readout remains visible |
| none (stopped) | Unlit at rest |

The reel drawing, metalwork and tape use the deck tokens already defined by `blue-future`: `--deck-face`, `--deck-trim`, `--deck-hub`, `--deck-well`, `--deck-spoke`, `--deck-tape` and `--deck-shadow`. Accent, success and danger colors come from the current theme. All motion is disabled for reduced-motion preferences and `data-motion="reduced"`.

The SVGs only present transport state. Wire your own player/recorder state to the class on `.media-deck`; no audio engine is included. The example page's buttons only change the visual state.

```html
<section class="media-deck is-playing" aria-label="Tape transport">
  <!-- Inline SVG for the selected deck -->
</section>
```

## State text `[data-when]`

Elements inside the deck with `data-when="playing"` (space-separated list: `playing recording
paused stopped`) are shown only in those states. Add `.is-annunciator` to keep them in place and
dim them instead (VFD annunciators). This is how the demo prints "Playing / Recording / Paused /
Stopped" without script.

## Lamps and the HUD band

```html
<div class="deck-hud">
  <span class="deck-lamp" data-lamp="sys">SYS</span>
  <span class="deck-lamp is-on" data-lamp="link">Link</span>
  <span class="deck-lamp" data-lamp="rec">Rec</span>
  <span class="status status-ok" data-when="playing">Playing</span>
</div>
<!-- inside the SVG -->
<circle data-lamp="sys" cx="54" cy="256"/>  <circle data-lamp="rec" cx="384" cy="20"/>
```

- `data-lamp="sys"`: green while moving, red while recording, amber paused, unlit stopped.
- `data-lamp="rec"`: red while recording, drawn 1.6× larger and with a wider glow.
- Any other `data-lamp` (e.g. `link`) is app-driven: `.is-on` (success), `.is-warn`, `.is-error`.
- SVG lamps get their radius from CSS (`r`), so leave the `r` attribute off.
- Lamps are steady (never pulse), so they stay readable under reduced motion.

| Token | Default |
|---|---|
| `--deck-lamp-r` | `4px` (lamp radius; the HTML lamp is 2r wide) |
| `--deck-lamp-rec-r` | `calc(var(--deck-lamp-r) * 1.6)` |
| `--deck-lamp-glow`, `--deck-lamp-rec-glow` | `4px`, `9px` |
| `--deck-lamp-on`, `--deck-lamp-off` | `var(--success)`, muted at 40% |
| `--deck-hud-bg`, `--deck-hud-fg` | `var(--surface-2)`, `var(--text)` |
| `--deck-annunciator-off` | `.18` (opacity of an unlit annunciator) |

## Transport keys `.transport-keys`

Built on core `.key`. CSS-only (radios):

```html
<div class="transport-keys" role="radiogroup" aria-label="Tape transport">
  <label class="key key-rec"><input type="radio" name="tape" value="recording"><svg class="icon" aria-hidden="true"><use href="assets/icons/icons.svg#icon-player-record"/></svg>Rec</label>
  <label class="key key-stop"><input type="radio" name="tape" value="stopped"><svg …#icon-player-stop/>Stop</label>
  <label class="key key-play"><input type="radio" name="tape" value="playing" checked><svg …#icon-player-play/>Play</label>
  <label class="key key-pause"><input type="radio" name="tape" value="paused"><svg …#icon-player-pause/>Pause</label>
</div>
```

App-driven: `<button class="key key-play">` and put the state class on the key set or any
ancestor (the `.media-deck`). Both the long (`.is-recording/.is-playing/.is-paused`) and short
(`.is-rec/.is-play/.is-pause`, as on core `.transport`) names work.

- Unlit at rest. A checked key sits pressed-in but is not lit.
- `.key-rec` lit red only while recording; `.key-play` lit green while playing and flashing at
  2 Hz while paused (`steps()`); `.key-pause` lit amber while paused; `.key-stop` never lights.
- Reduced motion (OS setting or `html[data-motion="reduced"|"none"]`): the paused Play key is
  steadily lit with a **dashed** edge instead of flashing.
- Tokens: `--transport-key-rec|play|pause` (danger/success/warning), `--transport-key-size`
  (`2.6rem`, never below `--tap-min`), `--transport-key-width`, `--transport-key-border-width`
  (`2px`), `--transport-key-glow` (`.8em`), `--transport-key-flash` (`.5s` period).

## Seven-segment digits `.seg7`

```html
<span class="seg7" role="img" aria-label="00:12:34:17">
  <i data-d="0"></i><i data-d="0"></i><b></b><i data-d="1"></i><i data-d="2"></i><b></b>
  <i data-d="3"></i><i data-d="4"></i><b></b><i data-d="1"></i><i data-d="7"></i>
</span>
```

- One `<i>` per digit, `data-d` = `0`–`9`, `-` or empty (blank). `<b>` is a colon
  (`<b class="is-off">` ghosts it). Any count of digits, so `HH:MM:SS` and `HH:MM:SS:FF` both work.
- **Updating:** the app changes `data-d` on the digits that moved and the `aria-label`:
  `digits.forEach((el, i) => el.dataset.d = text.replace(/:/g, '')[i]);`
- Unlit segments stay faintly visible (ghosts). Size is the font size (digit = `.6em × 1em`).
- In the deck head window, put it in `<foreignObject class="device-counter-slot" x y width height><div>…</div></foreignObject>`;
  `--deck-counter-size` (`30px`, SVG user units) sets its size. While recording it turns red
  (`--deck-counter-rec`, default `var(--danger)`).
- **VFD:** inside `.vfd`, with `.is-vfd`, or in a theme with `--meter-style: vfd` (blue-future)
  the digits take `--vfd-ink` and bloom. `.seg7.is-themed` opts out of the theme-wide VFD.

| Token | Default |
|---|---|
| `--seg7-lit` | `var(--accent)` (VFD: `var(--vfd-ink)`) |
| `--seg7-unlit` | lit colour at `--seg7-ghost` (`13%`; VFD `--vfd-ghost`, `10%`) |
| `--seg7-skew` | `-7deg` (skewX; `0deg` for upright) |
| `--seg7-gap` | `.14em` |
| `--seg7-glow` | `.04em` (VFD: `--vfd-glow`, `.1em`) |
| `--seg7-brightness` | `1` (VFD: `--vfd-brightness`, `1.1`) |

`--vfd-glow`, `--vfd-brightness` and `--vfd-ghost` are new VFD tokens with fallbacks; the
`.vfd` window, `.is-vfd` and the `--vfd-ink` / `.is-amber` / `.is-blue` colours are in
[metering.md](metering.md). For an amber VFD in a retro theme set
`html[data-theme="x"] { --vfd-ink: var(--vfd-amber); }`.

## Pi9696 reference

The reel-to-reel plate, spool construction, tape route and head arrangement are adapted from [drevilish/pi9696](https://github.com/drevilish/pi9696), `remote.go`'s dashboard template. Its state model spins the reels and pulses tape while playing or recording, holds still while paused, and highlights the head red during recording. This component keeps that geometry and motion model while replacing literal blue colors with this library's theme tokens. Copyright and MIT license terms are in [`THIRD_PARTY_NOTICES.md`](../../THIRD_PARTY_NOTICES.md).
