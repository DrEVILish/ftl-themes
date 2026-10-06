# Metering (v5.2)

Source: `core/components/metering.css`. Example page: [metering.html](../../metering.html); also used in
[soundmixer.html](../../soundmixer.html) (master VU, EQ with RTA). Extends the core `.meter`, `.scale`,
`.lamp`, `.key`, `.readout` and `.eq-curve` primitives; see [audio](audio.md) for the wider audio map.

Shared conventions:

- Values are inline custom properties: `--value` (0–1) and `--peak` (0–1). The app maps its units
  (dB, LUFS) to 0–1 and keeps the ARIA values in step; nothing here needs JavaScript.
- Each meter copies `--value` into its own typed `--metering-v` (registered with `@property`), so a
  change glides with VU ballistics (`--metering-speed`, 0.3 s). Do not register `--value` itself: gauges,
  knobs and HUD bars read it as a plain inherited property.
- Motion (ballistics, `.is-demo-live`) runs only under `prefers-reduced-motion: no-preference` and
  stops under `html[data-motion="reduced"]`.
- Zones are fractions of the travel: `--zone-warn` (0.6), `--zone-over` (0.85), and with `.is-reference`
  a red band from `--zone-ref-from` (0.5) to `--zone-ref-to` (0.56). Colours default to the core meter
  tokens `--meter-low` / `--meter-mid` / `--meter-high`.
- Under `forced-colors: active` meters keep their colours (`forced-color-adjust: none`): the colour is the
  data, and every meter also carries its value as ARIA text.

---

## Analogue VU `.vu`

```html
<div class="vu" role="meter" aria-label="Left" aria-valuenow="-3" aria-valuemin="-20"
     aria-valuemax="3" aria-valuetext="−3 VU">
  <ol class="vu-scale" aria-hidden="true">
    <li style="--at:0">20</li><li style="--at:.165">10</li><li style="--at:.264">7</li>
    <li style="--at:.352">5</li><li style="--at:.463">3</li><li style="--at:.529"></li>
    <li style="--at:.603"></li><li class="is-over" style="--at:.686">0</li>
    <li class="is-over" style="--at:.779"></li><li class="is-over" style="--at:.883"></li>
    <li class="is-over" style="--at:1">3</li>
  </ol>
  <span class="vu-legend">VU</span>
  <span class="vu-needle" style="--value:.463"></span>
  <span class="vu-peak">Peak</span>
</div>
```

- **Scale.** Each `li` is a mark at `--at` (0–1 along the sweep) with its own tick; an empty `li` is a
  minor tick; `.is-over` prints it in the zone colour.
- **dB mapping.** A VU needle is linear in voltage: `--value = (10^(dB/20) − 0.1) / 1.3125` for a
  −20…+3 scale (0 VU = 0.686, which is the default `--vu-zone-at`).
- **States:** `.is-peak` lights the peak LED. `.is-pair` takes two `.vu-needle`s (each with its own
  `--value` and `role="meter"`; put `role="group"` on the `.vu`); the second is drawn in the zone colour.
  `.is-ppm` is a peak programme meter (white on black, 1–7, no red zone).
- **Faces:** the default face is cream "paper" in light-scheme themes and theme-tinted in dark ones
  (`light-dark()`). `.is-backlit` forces the lamp-lit paper face, `.is-themed` the theme's face.
- **Tokens:** `--vu-size` (18rem), `--vu-aspect` (16/10), `--vu-face`, `--vu-ink`, `--vu-zone`,
  `--vu-zone-ink`, `--vu-zone-at`, `--vu-needle`, `--vu-needle-r`, `--vu-needle-width`, `--vu-glow`
  (backlight), `--vu-bezel`, `--vu-bezel-width`, `--vu-corner`, `--vu-shadow`, `--vu-font`,
  `--vu-sweep` (96deg), `--vu-radius` (50cqi), `--vu-pivot-y` (66cqi), `--vu-label-size`,
  `--vu-legend-size`. Sizes inside are `cqi` of the face, so one `--vu-size` scales it all.
- **Accessibility:** `role="meter"` with `aria-valuenow/min/max` and an `aria-valuetext` in VU; the
  printed scale is `aria-hidden`.

## LED bargraph `.ledbar`, `.ledbar-pair`, `.ledbar-scale`

```html
<div class="ledbar-pair" style="--ledbar-segments:40;--ledbar-height:19rem">
  <ol class="ledbar-scale" aria-hidden="true"><li style="--at:1">0</li>…</ol>
  <div class="ledbar is-reference" role="meter" aria-label="Left" aria-valuenow="-14"
       aria-valuemin="-40" aria-valuemax="0" style="--value:.65;--peak:.75"></div>
  <ol class="ledbar-scale" aria-hidden="true"><li class="is-ref" style="--at:.5">R</li>…</ol>
  <div class="ledbar is-reference is-over" …></div>
</div>
```

- **Drawing.** An empty element: zones are a gradient, segments a repeating mask, the lit part a
  clip-path snapped to whole segments, the peak-hold segment a second clip. Unlit segments stay visible
  as dim tints of their zone colour (`--ledbar-unlit`, 24%).
- **States:** `.is-over` lights the overs cap (top, or end when horizontal); `.is-horizontal` lays it
  across; `.is-reference` adds the reference band.
- **Pair:** `.ledbar-pair` lines up any run of bars and `.ledbar-scale` columns (scale | L | centre scale
  | R | scale), all the same height; `.ledbar-pair.is-horizontal` stacks them. Scale marks sit at
  `--at` (the top of that segment), `li.is-ref` in the reference colour.
- **Tokens:** `--ledbar-segments` (30), `--ledbar-width` (0.9rem), `--ledbar-height` (12rem),
  `--ledbar-length` (100%, horizontal), `--ledbar-gap` (2px), `--ledbar-cap` (0.45rem), `--ledbar-bg`,
  `--ledbar-low/-mid/-high/-ref`, `--ledbar-over`, `--ledbar-unlit`, `--ledbar-radius`,
  `--ledbar-shadow`, `--ledbar-pair-gap`, `--ledbar-scale-width/-font/-size/-fg/-ref`.

## Arc loudness meter `.ledarc`

```html
<div class="ledarc is-reference" role="meter" aria-label="Left loudness" aria-valuenow="-15"
     aria-valuemin="-40" aria-valuemax="0" style="--value:.62;--peak:.7">
  <ol class="ledarc-scale" aria-hidden="true"><li style="--at:.05">-38</li>…</ol>
  <ol class="ledarc-scale is-lower" aria-hidden="true"><li style="--at:.1">5</li>…</ol>
  <span class="ledarc-legend">Loudness</span>
</div>
```

- A shallow arc of a large circle cut into `--ledarc-segments` (40) segments, the same zones, lit level,
  peak segment and `.is-reference` band as `.ledbar`. Upper and lower (`.is-lower`) scales follow the
  arc. Put it in a dark housing (`.vfd`, a panel) for the broadcast look.
- **Tokens:** `--ledarc-size` (100%), `--ledarc-aspect` (100/40), `--ledarc-sweep` (64deg),
  `--ledarc-radius` (80cqi), `--ledarc-thickness` (9cqi), `--ledarc-gap` (0.45deg), `--ledarc-face`,
  `--ledarc-ink`, `--ledarc-font`, `--ledarc-label-size`, `--ledarc-legend-size`, `--ledarc-ref-fg`,
  plus the `--ledbar-*` colours.

## Meter panel `.meter-panel`, `.meter-controls`

Peak / Overs / Meter-mode keys are radios inside `.key` labels; the panel redraws its meters with
`:has()`. Give each meter a reading per mode: `--value-2`/`--peak-2`, `--value-3`/`--peak-3`.

```html
<section class="meter-panel">
  … meters …
  <div class="meter-controls">
    <fieldset><legend>Peak</legend><div class="keys">
      <label class="key"><input type="radio" name="peak" data-peak="auto">Auto</label>
      <label class="key"><input type="radio" name="peak" data-peak="hold" checked>Hold</label>
      <label class="key"><input type="radio" name="peak" data-peak="off">Reset</label></div></fieldset>
    <fieldset><legend>Overs</legend>… data-overs="on" / data-overs="off" …</fieldset>
    <fieldset><legend>Meter mode</legend>… data-mode="3" / "2" / "1" …</fieldset>
  </div>
</section>
```

- `data-peak="off"` hides peak segments, `data-overs="off"` clears overs caps and any
  `.lamp.is-overs-lamp`, `data-mode="2"|"3"` switches readings (with ballistics).
- Keys are at least `--tap-min` square. Static `aria-valuenow` describes the default mode; an app that
  switches modes for real updates it.

## VFD `.is-vfd`, `.vfd`

- `.is-vfd` on `.vu`, `.ledbar`, `.ledarc` or `.readout`: smoked glass, phosphor ink (`--vfd-ink`,
  #3ff5d0), glow, ghosted unlit segments, a fine grid mesh and slightly soft edges. A VFD `.ledbar` uses
  thin bar segments. `.is-amber` / `.is-blue` switch phosphor (`--vfd-amber`, `--vfd-blue`); the hot
  zone is `--vfd-hot`.
- `.vfd` is the glass window: padding, glass, sheen, a mesh over everything inside, phosphor text and
  scales (`.vfd-label`, `.vfd-label.is-dim` for an unlit annunciator).
- `.readout.is-vfd[data-ghost="88.88"]` prints the unlit segments behind the value (same character count).
- **Theme opt-in:** a theme setting `--meter-style: vfd` at root draws every `.vu`, `.ledbar` and
  `.ledarc` as VFD (container style query; browsers without style queries keep the normal look).
  `.is-backlit` / `.is-themed` faces are left alone. Set in blue-future.
- **Tokens:** `--vfd-ink`, `--vfd-amber`, `--vfd-blue`, `--vfd-hot`, `--vfd-glass`, `--vfd-padding`,
  `--vfd-radius`, `--vfd-shadow`.

## EQ display `.eq-graph`, `.spectrogram`, `.rta`, `.eq-node`

```html
<div class="eq-editor">
  <!-- Analyser controls: radios and checkboxes anywhere inside .eq-editor -->
  <div class="segmented" role="radiogroup" aria-label="RTA source">
    <label class="segmented-item"><input type="radio" name="rta-view" data-rta-view="pre">Pre</label>
    <label class="segmented-item"><input type="radio" name="rta-view" data-rta-view="both" checked>Pre + Post</label>
    <label class="segmented-item"><input type="radio" name="rta-view" data-rta-view="post">Post</label>
  </div>
  <!-- data-rta-range="30|60", data-rta-decay="slow|med|fast",
       data-rta-mode="peak|rms|avg|peak-rms|peak-avg", data-spectro="theme|scale|mono|thermal"
       follow the same pattern -->
  <label class="key key-on"><input type="checkbox" data-eq-show="spectrogram" checked>On</label>
  <span>Post <label class="switch"><input type="checkbox" data-spectro-src aria-label="Spectrogram from the pre-EQ signal">
    <span class="switch-track"><span class="switch-thumb"></span></span></label> Pre</span>

  <div class="eq-graph">
    <div class="spectrogram" aria-hidden="true"><i style="--v:.4"></i>… or <canvas></canvas></div>
    <div class="spectrogram is-pre" aria-hidden="true">…</div>
    <ol class="rta is-pre" aria-hidden="true"><li style="--v:.6;--avg:.55;--peak:.7"></li>…×31</ol>
    <ol class="rta" aria-hidden="true"><li style="--v:.6;--avg:.55;--peak:.7"></li>…×31</ol>
    <svg class="eq-graph-curve" viewBox="0 0 1000 400" preserveAspectRatio="none" aria-hidden="true">
      <path class="is-band" data-series="3" d="…"/><path d="…"/></svg>
    <ol class="eq-freqs" aria-hidden="true"><li style="--f:0">20</li>…<li style="--f:1">20k</li></ol>
    <ol class="eq-gains" aria-hidden="true"><li style="--g:.667">+12</li>…</ol>
    <ol class="eq-levels" aria-hidden="true"><li style="--l:1" data-r60="0" data-r30="0"></li>…
      <li style="--l:0" data-r60="-60 dB" data-r30="-30 dB"></li></ol>
    <fieldset class="eq-nodes"><legend class="visually-hidden">Selected band</legend>
      <label class="eq-node" style="--f:.42;--g:-.25" data-series="3"><input type="radio" name="band" checked>
        <span class="visually-hidden">Band 3, bell, 380 Hz, −4.5 dB</span><span aria-hidden="true">3</span></label>
    </fieldset>
  </div>
  <div class="eq-bands"><section class="eq-band" data-series="3">…knobs, select, key…</section></div>
</div>
```

- **Grid:** log frequency 20 Hz–20 kHz (one decade pattern repeated three times) and dB lines every
  1/`--eq-gain-lines` (6) with a stronger 0 dB line. `--f` = `log10(f / 20) / 3`; `--g` is −1…1 of the
  displayed EQ range (the app prints `.eq-gains`). `.eq-levels` prints the RTA scale on the right edge
  and switches its text with the range.
- **Layers, back to front:** `.spectrogram`, `.rta.is-pre`, `.rta` (both drawn as bars with a top edge
  and peak-hold caps, both at `--rta-opacity` 0.75), the EQ curve (`path.is-band` dashed per band in
  `--series`), labels, then the `.eq-node` handles, always on top.
- **RTA data:** each band `<li>` carries `--v` (RMS), `--avg` and `--peak`, all 0–1 over a 60 dB window
  (1 = 0 dBFS). `.is-line` draws only the band tops.
- **RTA controls** (radios inside `.eq-editor`):
  - `data-rta-view="pre|both|post"`: a linked three-way selector; Pre + Post shows both layers.
  - `data-rta-range="30|60"`: the window; at 30 dB the bars and caps show the top half
    (`--rta-k: 2`).
  - `data-rta-decay="slow|med|fast"`: bars and caps ease to new values over `--rta-decay`
    (1.2 s / 0.45 s / 0.12 s) when the app updates them. No easing under reduced motion.
  - `data-rta-mode`: `peak` (bars from `--peak`), `rms` (`--v`), `avg` (`--avg`), `peak-rms`
    (default: RMS bars + peak caps) or `peak-avg` (average bars + peak caps).
- **Spectrogram:** cells' `--v` (0–1) picks a colour on a five-step scale, floor → signal detected →
  low → medium → high → peak. A cell under ~0.2 shows the floor (`--spectro-floor`, transparent).
  - **Theme colours:** `--spectro-signal`, `--spectro-low`, `--spectro-mid`, `--spectro-high`,
    `--spectro-peak`. The default per theme is its own palette: `--accent`, then `--success` →
    `--warning` → `--danger`. blue-future sets cyan, green, yellow, amber and red.
  - **Presets:** `data-spectro="theme|scale|mono|thermal"` radios switch to the theme's
    `--chart-seq-*` scale, an accent ramp, or a fixed thermal scale.
  - **Source:** a `data-spectro-src` switch shows `.spectrogram.is-pre` instead of the post one; the
    spectrogram is always one or the other. `data-eq-show="spectrogram"` turns it off.
  - An app may put a `<canvas>`, `<img>` or `<video>` inside `.spectrogram` instead of cells.
- **Selection:** nodes are radios; the checked one is highlighted and the Nth `.eq-band` shows while the
  Nth `.eq-node` is checked (up to 8). `.eq-node.is-off` dashes a bypassed band.
- **v5.2 toggles still work:** an unchecked `data-eq-show="rta|pre|spectrogram"` checkbox hides that
  layer.
- **Tokens:** `--eq-graph-aspect` (5/2), `--eq-bg`, `--eq-border`, `--eq-radius`, `--eq-grid`,
  `--eq-grid-major`, `--eq-zero`, `--eq-gain-lines`, `--eq-line`, `--eq-fill`, `--eq-graph-line-width`,
  `--eq-label-fg`, `--eq-label-size`, `--spectrogram-opacity` (0.45), `--spectro-*`, `--rta-color`,
  `--rta-pre-color`, `--rta-peak`, `--rta-fill` / `--rta-fill-top`, `--rta-opacity`, `--rta-gap`,
  `--rta-decay`, `--rta-k`, `--eq-node-bg`, `--eq-node-active`, `--eq-node-active-fg`.
- **Touch:** each node's hit area is `max(--tap-min, 1.9rem)`; the drawn handle is 1.6rem.
- **Accessibility:** the drawing is `aria-hidden`; each node's radio carries the band in text. Band
  controls are labelled native ranges and selects (`.knob`, `.select`, `.key`).

## Demo motion `.is-demo-live`

Put `.is-demo-live` on a container to make its meters breathe around their `--value` and its RTA bars
flicker (CSS keyframes on the registered properties, staggered by `nth-of-type`). Showcase only; a live
app sets `--value` itself and gets the ballistics transition.
