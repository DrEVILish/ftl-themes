# Vehicle instruments (v5)

Source: `core/components/vehicles.css`. Example pages: `cockpit-car.html`,
`cockpit-plane.html`, `cockpit-jet.html`.

Generic cockpit parts for any vehicle: cars, airliners, fighters, boats,
submarines, spacecraft. A new cockpit page should need **no new CSS**: compose
these with the instruments group (`.gauge-dial`, `.gauge-arc`, `.compass`,
`.compass-strip`, `.map`) and core controls (`.fader`, `.toggle-group`,
`.toggle-btn`, `.tabset`).

Shared conventions (as in [instruments](instruments.md)):

- Values come in through inline custom properties: `--pitch`, `--roll`,
  `--value`, `--at`, `--from`/`--to`, `--bearing`/`--range`, `--x`/`--y`,
  `--sweep`. Nothing needs JavaScript; apps update the properties (and the
  text alternative).
- Every colour is a `--<component>-*` token falling back to base tokens
  (`--accent`, `--warning`, `--danger`, `--success`, `--surface-2`, `--bg`,
  `--text`), so all 45 themes paint them with zero theme edits. Themes may set
  any token at root scope: `html[data-theme="x"] { --radar-fg: … }`.
- State is never colour alone: blips differ by shape, lit captions by fill and
  glow, a closed guard by stripes and text.
- Motion (radar sweep, flashing master lights and indicators, horizon
  easing) runs only under `prefers-reduced-motion: no-preference`; core's
  `html[data-motion="reduced"]` pauses it. Without motion everything shows
  its lit/static state.
- Round instruments size everything in `cqi` of themselves, so one size
  token (`--attitude-size`, `--radar-size`) scales them and they shrink with
  `max-inline-size: 100%` on phones.

| Need | Use |
|---|---|
| Speedometer, tachometer (redline), N1, EGT, G meter | `.gauge-dial` with `--gauge-redline` |
| Fuel, coolant, battery level | `.gauge-arc`, `.gauge-linear`, `.battery` |
| Heading tape / HSI | `.compass-strip` / `.compass` |
| Nav map, route | `.map` + `.map-pin` (route as `.chart-series` in the SVG) |
| Levers (throttle, flaps, ballast, thrusters) | `.fader` inside `.throttle` |
| Switches, PRNDL, drive or master modes | `.toggle-group` (radios), `.toggle-btn` (checkboxes) |
| Display modes, pages | `.tabset`, or `.mfd` soft keys |
| Infotainment | `.now-playing.is-mini` |

---

## Artificial horizon `.attitude`

```html
<div class="attitude" style="--pitch:3.5; --roll:-12" role="img" aria-label="Pitch 3.5° up, banked 12° left">
  <div class="attitude-horizon">
    <ol class="attitude-ladder" aria-hidden="true">
      <li style="--at:20"></li><li style="--at:10"></li><li style="--at:-10"></li><li style="--at:-20"></li>
    </ol>
  </div>
</div>
```

- **Value API:** `--pitch` (degrees, nose up positive), `--roll` (degrees,
  right wing down positive). The horizon layer turns by `--roll` and slides
  perpendicular to itself by `--pitch`.
- **Parts:** `.attitude-horizon` (sky, ground, horizon line, ladder rungs every
  10° with 5° half-rungs, and the roll pointer, which stays on the roll ring
  whatever the pitch); `ol.attitude-ladder` labels: each `li` with an
  **integer** `--at` prints that number at both ends of its rung (CSS
  counters, so the `li` stays empty); `::before` the fixed bank scale (0, ±10,
  ±20, ±30, ±45, ±60); `::after` the aircraft symbol.
- **`.is-hud`:** a see-through head-up style that fills its positioned parent
  (used by `.flight-hud`, also a spacecraft window or a sub's periscope): no
  bank scale or symbol, rungs with a centre gap, ink and glow from
  `--flight-hud-ink`, a dark scene sky and ground.
- **Tokens:**

| Token | Default |
|---|---|
| `--attitude-size` | `16rem` |
| `--attitude-pitch-scale` | `1.6cqi` per degree (`1.2cqi` in `.is-hud`) |
| `--attitude-sky`, `--attitude-sky-top` | 50% `--accent` in `--bg`; darker at the top |
| `--attitude-ground`, `--attitude-ground-bottom` | 42% `--warning` in `--bg`; darker at the bottom |
| `--attitude-ink` | `var(--text)` (rungs, labels, horizon line) |
| `--attitude-horizon-line`, `--attitude-horizon-width` | `var(--attitude-ink)`, `2px` |
| `--attitude-scale-ink`, `--attitude-pointer` | `var(--attitude-ink)` |
| `--attitude-symbol`, `--attitude-symbol-edge` | `var(--warning)`, `var(--bg)` |
| `--attitude-rung`, `--attitude-rung-mask` | `30cqi`, `none` |
| `--attitude-label-size`, `--attitude-label-room` | `4.5cqi`, `9cqi` |
| `--attitude-border`, `-border-width`, `-radius`, `-shadow`, `-font`, `-speed` | `--border`, `1px`, `2 × --radius`, `none`, `--font-mono`, `0.4s` |
| `--attitude-hud-sky`, `-sky-top`, `-ground`, `-ground-bottom` | `.is-hud` scene colours (24% accent in bg, bg, 16% text in bg, bg) |

- **Accessibility:** `role="img"` and an `aria-label` with pitch and bank in
  words; update it at a calm rate.

## Moving tape `.tape`

```html
<div class="tape" role="meter" aria-label="Airspeed, knots" aria-valuenow="262" aria-valuemin="0" aria-valuemax="400"
     style="--value:262; --tape-span:80; --tape-major:20; --tape-minor:10">
  <span class="tape-unit">KT</span>                                 <!-- optional -->
  <ol class="tape-scale" aria-hidden="true"><li style="--at:240">240</li><li style="--at:260">260</li>…</ol>
  <span class="tape-band is-danger" style="--from:292; --to:400"></span>
  <span class="tape-bug" style="--at:270"></span>
  <span class="tape-readout">262</span>
</div>
<div class="tape is-end" style="--value:11640; --tape-span:1000; --tape-major:200; --tape-minor:100">…</div>
```

- A vertical scale that slides so `--value` sits behind the boxed readout:
  airspeed, altitude, vertical speed, depth, range rate, velocity. Bigger
  values are higher (for depth, feed negative numbers or label it so).
- **Value API:** `--value`, `--tape-span` (units visible, 100),
  `--tape-major` / `--tape-minor` (tick spacing in units, 20 / 10). Labels
  and marks take `--at` in the same units; any number of labels, the tape
  clips them. `.tape-band` takes `--from`/`--to`; `.tape-bug` parks at the
  edge when its `--at` is off scale.
- **Variants:** default ticks on the end edge (left-hand tape); `.is-end`
  mirrors it (right-hand tape). Bands: default `--success`, `.is-caution`,
  `.is-danger` (barber pole). `.tape-unit` prints a heading at the top and
  masks the scale under it.
- **Size:** `--tape-width` (`4.75rem`), `--tape-height` (`16rem`). It is a
  size container (`cqb` units), so in a grid that stretches it (as `.pfd`
  does) set `block-size: auto` and it takes the row height.
- **Tokens:** `--tape-bg` (`--surface-2`), `--tape-fg`, `--tape-tick` (`--text`),
  `--tape-border`, `-border-width`, `-radius`, `--tape-font` (`--font-mono`),
  `--tape-label-size` (`0.75rem`), `--tape-readout-bg` (`--bg`),
  `--tape-readout-fg` (`--readout-fg`, accent), `--tape-readout-border`
  (`--text`), `--tape-readout-size` (`1.05rem`), `--tape-bug` (`--flare`),
  `--tape-band`, `--tape-band-caution`, `--tape-band-danger`,
  `--tape-band-danger-alt`, `--tape-unit-fg` (`--muted`).
- **Accessibility:** `role="meter"` with `aria-valuenow/min/max` (or
  `aria-hidden` when the tape is part of a labelled `role="img"`, as in the
  HUD); the scale is `aria-hidden`.
- **Audit note:** scale labels slide past the tape's edges by design; mark
  the `ol.tape-scale` (and a `.compass-strip`) `data-audit-edge="ignore"` so
  `scripts/v5_audit.mjs` doesn't count them as text touching a box edge.

## Radar, sonar and threat scope `.radar`

```html
<div class="radar" style="--sweep:40" role="img" aria-label="Radar: hostile 35° right, 25 miles; wingman left">
  <span class="radar-blip is-foe" style="--bearing:35; --range:.62">B1</span>
  <span class="radar-blip is-friend" style="--bearing:-40; --range:.2">#2</span>
  <span class="radar-blip is-unknown" style="--x:30%; --y:70%">U</span>
  <span class="radar-blip">KAREL</span>     <!-- plain contact / waypoint -->
</div>
<div class="radar is-sector" …>…</div>      <!-- fan, origin bottom centre -->
<div class="radar is-rwr is-static" …>…</div> <!-- labels inside symbols, no sweep -->
```

- **Scope:** `--radar-rings` range rings (4), a cross through the origin and a
  sweep with a fading trail. The sweep rotates under motion (one turn per
  `--radar-speed`, 4s); otherwise it rests at `--sweep` (degrees).
- **Blips:** `--bearing` (degrees clockwise from up) and `--range` (0–1 of the
  radius), or `--x`/`--y` percentages. The text is the label, printed beside
  the marker. Shapes: plain dot (contact), `.is-friend` ring, `.is-foe`
  diamond, `.is-unknown` square; `.is-faint` dims an old or weak return.
- **Variants:** `.is-sector` is a `--radar-span` fan (120°) on a 2:1 box with
  the origin at the bottom centre (nose radar, weather radar, forward sonar);
  bearings and ranges work the same. `.is-static` removes the sweep (radar
  warning receiver, passive sonar). `.is-rwr` prints each label inside its
  symbol (threat codes, contact numbers).
- **Sonar:** the same markup; set `--radar-fg` (and `--radar-bg`) on the
  element or theme for a different phosphor, `--radar-speed: 8s` for a slow
  ping.
- **Tokens:** `--radar-size` (`14rem`), `--radar-bg` (7% fg in `--bg`),
  `--radar-fg` (accent text), `--radar-ring` (38% fg), `--radar-sweep`,
  `--radar-trail` (`70deg`), `--radar-border`, `-border-width`, `-shadow`,
  `--radar-font`, `--radar-blip` (plain contacts), `--radar-friend`
  (`--success`), `--radar-foe` (`--danger`), `--radar-unknown`
  (`--warning`), `--radar-blip-size` (`max(0.55rem, 3.6cqi)`),
  `--radar-label-size`, `--radar-label-fg`.
- **Accessibility / touch:** blips are not interactive (the scope is a
  size container, so popovers inside it would be clipped); describe the
  picture in the scope's `aria-label`, or give a contact table beside it.

## Annunciator panel `.annunciator` and master lights

```html
<ul class="annunciator" aria-label="Caution panel">
  <li>Fuel press</li>
  <li class="is-caution">Hyd 2 <span class="visually-hidden">(lit)</span></li>
  <li class="is-warning is-blinking">Eng fire <span class="visually-hidden">(lit)</span></li>
  <li class="is-advisory">APU avail</li>
  <li class="is-on">Seat belts</li>
</ul>
<label class="annunciator-master is-warning"><input type="checkbox"> Master warn</label>
<label class="annunciator-master is-caution"><input type="checkbox"> Master caution</label>

<ul class="annunciator is-gear" aria-label="Landing gear: down and locked">
  <li class="is-advisory">Nose</li><li class="is-advisory">Left</li><li class="is-advisory">Right</li>
</ul>
<ul class="annunciator is-fma" aria-label="Flight modes"><li class="is-advisory">Speed</li>…</ul>
```

- Unlit captions are dim, etched text ("dark cockpit"); lit ones fill with a
  tint of their colour, take its border and glow, and print full-contrast
  text (`--annunciator-lit-fg`, `--text`). The state colours' own text tokens
  fail contrast on the tint in many themes, so they colour the frame, not the
  words.
  States: `.is-caution` (`--warning`), `.is-warning` (`--danger`),
  `.is-advisory` (`--success`), `.is-on` (`--accent`); `.is-blinking` flashes
  a lit caption under motion.
- **Master light:** a push-to-reset `label` around a checkbox. Unchecked =
  lit and flashing; checked = acknowledged and dark. At least `--tap-min`.
- **Layouts:** default auto-fill grid (`--annunciator-min` 6.5rem per cell);
  `.is-gear` puts the first item (nose) centred above two mains; `.is-fma` is
  one row of equal boxes.
- **Tokens:** `--annunciator-bg` (`--bg`), `-border`, `-border-width`,
  `-radius`, `-gap` (3px), `-pad`, `-min`, `-cell-height` (2.6rem),
  `-cell-border` (`--hairline`), `-cell-radius`, `-font` (`--font-mono`),
  `-size` (0.7rem), `--annunciator-off` (`--surface-2`), `-off-fg`
  (`--muted`), `-on`, `-caution`, `-warning`, `-advisory`, `-lit-fg` (`--text`), `-lit-mix` (12%),
  `-glow`.
- **Accessibility:** a lit caption should say so in text
  (`<span class="visually-hidden">(lit)</span>`) or the list's label should
  name the lit ones. Under forced colours lit cells get a 3px Highlight
  border.

## Tell-tale lamp `.telltale`

```html
<span class="telltale is-on is-blinking" role="img" aria-label="Left indicator, flashing"><svg class="icon"><use href="assets/icons/icons.svg#icon-arrow-left"/></svg></span>
<span class="telltale is-on is-danger" role="img" aria-label="Seat belt unfastened">…</span>
<span class="telltale" role="img" aria-label="Engine check, off">…</span>
```

An icon lamp for a car cluster or a console. Off = faint; `.is-on` lights it
green, or `.is-info` (accent), `.is-warning`, `.is-danger`. `.is-blinking`
flashes a lit lamp (indicators, hazards). Tokens: `--telltale-size`
(1.9rem), `--telltale-off`, `--telltale-on`, `--telltale-info`,
`--telltale-warning`, `--telltale-danger`, `--telltale-glow`. Pages that
switch a lamp from a native control render both states and show one with
`:has()` (see `cockpit-car.html`).

## Tyre pressures `.tyres`

```html
<ul class="tyres" aria-label="Tyre pressures">
  <li>Front left <span class="readout readout-sm">2.4</span></li>
  <li>Front right <span class="readout readout-sm">2.4</span></li>
  <li>Rear left <span class="readout readout-sm">2.6</span></li>
  <li class="is-low">Rear right <span class="readout readout-sm">1.9</span><span class="visually-hidden">, low</span></li>
</ul>
```

Four corners round a top-down body outline; order FL, FR, RL, RR. `.is-low`
(caution) and `.is-flat` (warning) recolour the tyre and its text; add the
state in words. Tokens: `--tyres-body`, `--tyres-body-border`,
`--tyres-glass`, `--tyres-body-width` (5.5rem), `--tyres-row` (4.5rem),
`--tyres-ok`, `--tyres-low`, `--tyres-flat`.

## Multi-function display `.mfd`

```html
<div class="mfd" role="group" aria-label="Left display">
  <div class="mfd-keys is-top" role="radiogroup" aria-label="Format">
    <label class="mfd-key"><input type="radio" name="mfd-l" checked>RDR</label>
    <label class="mfd-key"><input type="radio" name="mfd-l">SMS</label>
  </div>
  <div class="mfd-keys is-start"><button class="mfd-key" type="button">RNG+</button>…</div>
  <div class="mfd-screen">
    <section class="mfd-page" aria-label="Radar">…</section>
    <section class="mfd-page" aria-label="Stores">…</section>
  </div>
  <div class="mfd-keys is-end">…</div>
  <div class="mfd-keys is-bottom">…</div>
</div>
```

- A screen framed by bezel soft keys on any of four edges. **Top keys are
  radios**: key n shows `.mfd-page` n (up to 6; none checked shows page 1),
  without JavaScript. Other keys are buttons (`aria-pressed`) or checkbox
  labels; pressed = checked.
- **Touch:** keys are at least `--tap-min` square with ≥ 8px between them,
  so a phone keeps the full ring. Up to 5 keys per edge fit a phone.
- `.mfd-screen` is an inline-size container: instruments inside size to it.
- **Tokens:** `--mfd-bezel` (`--surface-2`), `--mfd-border`, `-border-width`,
  `-radius`, `-shadow`, `-gap`, `-pad`, `--mfd-key-bg` (`--surface`),
  `-key-fg`, `-key-border`, `-key-radius`, `-key-shadow`, `-key-gap`,
  `--mfd-key-on`/`-key-on-fg` (accent), `--mfd-screen-bg` (`--bg`),
  `-screen-fg`, `-screen-border`, `-screen-radius`, `-screen-pad`,
  `-screen-min` (14rem), `--mfd-font`.

## Guarded switch `.guard`

```html
<div class="guard">
  <label class="guard-cover"><input type="checkbox" aria-label="Master arm guard">
    <span class="guard-closed">Safe · lift guard</span><span class="guard-open">Close guard</span></label>
  <label class="toggle-btn is-danger"><input type="checkbox">Master arm</label>
</div>
```

The striped cover sits over the switch until its checkbox is checked
(lifted); while closed the switch is `visibility: hidden`, so neither pointer
nor keyboard can reach it. Any control works as the guarded switch. Closing
the guard does not reset the switch (CSS can't); an app that needs that
resets it. Tokens: `--guard-color` (`--danger`), `--guard-stripes`,
`--guard-label-bg` (`--bg`), `--guard-label-fg` (`--text`), `--guard-radius`, `--guard-font`.

## Checklist `.checklist`

```html
<ol class="checklist">
  <li><label><input class="checkbox" type="checkbox"><span>Parking brake</span><b>Set</b></label></li>
</ol>
```

Challenge, leader dots, response. Rows are at least `--tap-min` tall; a done
row takes `--checklist-done` (success) and the checkbox shows it. Tokens:
`--checklist-font`, `--checklist-rule`, `--checklist-leader`,
`--checklist-response`, `--checklist-done`.

## Lever quadrant `.throttle`

```html
<div class="throttle" role="group" aria-label="Thrust levers">
  <div class="scale"><span style="--at:1">TOGA</span><span style="--at:.62" class="is-unity">CL</span><span style="--at:.2">IDLE</span></div>
  <label class="throttle-lever"><input class="fader" type="range" min="0" max="100" value="62" aria-label="Thrust lever 1"><span aria-hidden="true">1</span></label>
</div>
```

Houses core `.fader` levers (native vertical range inputs, keyboard and
touch for free) with a core `.scale` of detents. Tokens: `--throttle-height`
(14rem), `--throttle-bg`, `--throttle-border`, `--throttle-radius`,
`--throttle-gap`, `--throttle-handle`, `--throttle-handle-width`,
`--throttle-handle-height`.

## Primary flight display `.pfd`

```html
<div class="pfd" role="group" aria-label="Primary flight display">
  <ul class="annunciator is-fma">…</ul>
  <div class="tape">…speed…</div>
  <div class="attitude">…</div>
  <div class="tape is-end">…altitude…</div>
  <div class="tape is-end">…vertical speed…</div>
  <ol class="compass-strip">…</ol>
</div>
```

A layout: FMA row, speed tape, attitude (capped at `--pfd-attitude-max`,
22rem), altitude tape, a second `.is-end` tape as V/S, heading strip below.
Tapes stretch to the attitude's height; below a 26rem container they narrow.
Tokens: `--pfd-bg`, `--pfd-border`, `--pfd-radius`, `--pfd-gap`, `--pfd-pad`.

## Head-up display `.flight-hud`

```html
<div class="flight-hud" role="img" aria-label="HUD: heading 274°, 452 knots, 18,250 feet">
  <div class="attitude is-hud" style="--pitch:4; --roll:8">…</div>
  <ol class="compass-strip" style="--heading:274" aria-hidden="true">…</ol>
  <div class="tape" aria-hidden="true">…</div> <div class="tape is-end" aria-hidden="true">…</div>
  <span class="flight-hud-gun"></span>
  <span class="flight-hud-fpm" style="--x:53%; --y:46%"></span>
  <span class="flight-hud-target is-locked" style="--x:68%; --y:26%">TD 4.2</span>
  <div class="flight-hud-data"><span>M 0.86</span>…</div>
  <div class="flight-hud-data is-end">…</div>
</div>
```

- The attitude's `.is-hud` scene is the sky behind the glass; heading strip
  on top, speed and altitude tapes at the sides (made see-through), data
  blocks in the bottom corners. Everything wears `--flight-hud-ink` with a
  glow.
- **Symbols:** `.flight-hud-gun` (gun cross at `--flight-hud-boresight`,
  36% down), `.flight-hud-fpm` flight-path marker at `--x`/`--y`,
  `.flight-hud-target` designator box at `--x`/`--y` with its text as the
  label below (`.is-locked` adds the inner diamond).
- Below a 34rem container the HUD tightens, the tapes narrow and the pitch
  ladder spreads out so it stays readable on a phone.
- **Tokens:** `--flight-hud-ink` (accent text), `--flight-hud-glow`,
  `--flight-hud-border`, `-border-width`, `-radius`, `-pad`, `-font`,
  `-min-height` (26rem), `-center-min` (15rem), `-boresight`, plus the
  `--attitude-hud-*` scene tokens.
- **Accessibility:** one `role="img"` with a summary label; the parts are
  decorative (`aria-hidden`).
