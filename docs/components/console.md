# Console: rack, faceplates, GEQ, patchbay, sends and dynamics curves (v5)

Source: `core/components/console.css`; script `assets/js/console.js`.
Live example: [`proseries.html`](../../proseries.html) (best in the
`proseries` theme, but every theme draws it).

The parts of a digital mixing console the mixer primitives in core
(`.mixer`, `.strip`, `.knob`, `.fader`, `.key`, `.meter`, `.scribble`) and
metering.css (`.eq-graph`, `.eq-node`) didn't cover. Everything is native
inputs: rack units, patch points and soft keys are radios and checkboxes;
knobs, faders and GEQ bands are range inputs.

## What `assets/js/console.js` does

CSS can't compute a filter response or a compressor curve, so this small
reference script (not part of the contract) does the maths:

- **`[data-peq]`** — a parametric EQ. Range inputs with `data-band="1..n"`
  and `data-param="f"` (0–1, log position 20 Hz–20 kHz), `"g"` (dB) and
  `"q"`; optional checkboxes `data-param="shelf"` (first band low shelf,
  last band high shelf) and `data-param="on"` (EQ in). It redraws the
  `.eq-graph-curve` path and moves each `.eq-node[data-band]`. `data-range`
  is the displayed ± dB (default 15).
- **`[data-dyn="comp"|"gate"]`** — inputs (or `data-*` attributes on the
  group) named `threshold`, `ratio`, `range`; it redraws every
  `.dyn-graph-line` and `.dyn-graph-threshold` inside, over −60…0 dB. A
  `.dyn-bypass` checkbox that is off dims the curve (CSS).
- **`<output for="id" data-unit="dB" data-format="hz">`** shows the
  input's value as it moves.
- **`data-link="name"`** keeps inputs with the same name in step (a
  faceplate knob and its twin on the assignable controls).

- **`[data-tap-tempo]`** buttons set a tempo from taps; `[data-tempo-out="ms"|"s"]`
  shows it and `<html>` gets `--tempo`.
- **`[data-scene-step="1"|"-1"]`** moves to the next or previous radio in the group
  named by `data-scene-group` (default `ps-scene`).
- **`[data-history]`** on a container makes its checkboxes undoable; buttons with
  `data-for="<id>"` and one of `data-undo`, `data-redo`, `data-checkpoint`,
  `data-restore`, `data-clear` act on it.

`assets/js/controls.js` turns knobs by dragging and keeps `--value`.
Pages, units and tabs in the example switch with radios and `:has()`.


## Name tags: a scribble strip filled with the channel colour

```html
<div class="scribble" data-color="3"><span class="scribble-name">Mic3</span></div>
```

With data-color the whole tag takes the per-user colour and dark text, as console channel names do.

## .sends — a channel's aux send levels

```html
<div class="sends" role="group" aria-label="Mic1 aux sends">
  <p class="sends-title">Auxes 1-8</p>
  <ol><li style="--send:.6"><span>1</span></li>…<li class="is-active" style="--send:.4">…</li></ol>
</div>
```

Each row is a wedge as long as its --send (0–1). .is-active marks the aux being edited; .is-pre a pre-fader send. Put a range input in a row to make it adjustable (controls.js keeps --value; use style="--send: var(--value)").

## .dyn-graph — a dynamics transfer curve

```html
<svg class="dyn-graph" viewBox="0 0 100 100" role="img" aria-label="Compressor curve">
  <path class="dyn-graph-line" d="M0 100 L60 40 L100 25"/>
</svg>
```

Input level across, output up; a 1:1 diagonal under the curve. console.js redraws the path from the controls in the same [data-dyn] group (see the docs). Small as a strip thumbnail, large on a detail page.

## .rack — an equipment rack of .rack-units

```html
<div class="rack" aria-label="Effects rack">
  <label class="rack-unit" data-finish="teal" style="--u: 2">
    <input type="radio" name="fx" value="reverb"><span class="rack-unit-name">Chamber Reverb</span>…
  </label>
</div>
```

A flight case with rails; each unit is --u rack units high (1–4) on a finish: data-finish="silver|black|blue|teal|red|purple|green|grey". A unit holding a radio is selectable (outlined when chosen); a .rack-unit.is-empty is a blank panel.

## .assignable — the blue soft-key panel under every unit

```html
<div class="assignable" role="group" aria-label="Assignable controls">
  <div class="assignable-col"><span>faders 1</span>
    <label class="assignable-key"><input type="checkbox"><span class="visually-hidden">…</span></label>
    <label class="knob">…</label><span>dB 20Hz</span></div>…
  <p class="assignable-caption">assignable controls</p>
</div>
```

Eight columns: a caption, a square soft key (lit when on), a knob, and its unit and name.

## .geq — a graphic EQ faceplate

```html
<div class="geq" role="group" aria-label="GEQ A">
  <div class="geq-scale" aria-hidden="true"><span>+12</span><span>0</span><span>-12</span></div>
  <div class="geq-group is-active"><label class="geq-band"><input type="range" min="-12" max="12" step="0.5" value="0" aria-label="20 Hz"><span>20</span></label>…</div>…
</div>
```

Bands in groups (the console's eight fader groups). Each band is a native vertical range input; a group marked .is-active is the one on the assignable controls.

## .patchbay — device blocks of patch points

```html
<section class="patch-device" aria-labelledby="dl251a">
  <header><span class="patch-id">ID 1</span><span class="patch-name" id="dl251a">DL251A 1</span></header>
  <div class="patch-grid"><label class="patch-point"><input type="checkbox" checked><span class="visually-hidden">A1</span></label>…</div>
</section>
```

A checked point is patched (green, or data-kind="aes" yellow); grey is free. .patch-grid takes --patch-cols (default 8).

## Tokens

`--assignable-bg`, `--assignable-border`, `--assignable-fg`, `--assignable-key-bg`, `--assignable-key-border`, `--assignable-key-on`, `--dyn-graph-bg`, `--dyn-graph-border`, `--dyn-graph-grid`, `--dyn-graph-line`, `--dyn-graph-line-off`, `--dyn-graph-line-width`, `--dyn-graph-threshold`, `--dyn-graph-unity`, `--faceplate-bg`, `--faceplate-border`, `--faceplate-display-bg`, `--faceplate-display-fg`, `--faceplate-group-active`, `--faceplate-group-border`, `--geq-bg`, `--geq-cap`, `--geq-fg`, `--geq-group-active`, `--geq-group-bg`, `--geq-group-border`, `--geq-height`, `--geq-slot`, `--geq-zero`, `--patch-aes`, `--patch-cols`, `--patch-device-bg`, `--patch-device-border`, `--patch-free`, `--patch-on`, `--rack-bg`, `--rack-finish`, `--rack-frame`, `--rack-frame-width`, `--rack-radius`, `--rack-rail`, `--rack-selected`, `--rack-trim`, `--rack-u`, `--scribble-tag-fg`, `--sends-active`, `--sends-bar`, `--sends-bar-pre`, `--sends-bg`, `--sends-border`, `--sends-fg`. Each falls back to a value that suits any theme.

## Accessibility

- Every knob, fader and GEQ band is a labelled range input; rack units,
  soft keys and patch points are labelled radios or checkboxes with visible
  focus. Transfer curves are `role="img"` with a name.
- Meters are `role="meter"` with values. The patchbay's state is the
  checkboxes, so a screen reader hears which points are patched.
- Forced colours: patched points, lit soft keys and the selected unit use
  the system highlight.

## Also in console.css

- **`.led-list`** — radios shown as a list with a small LED that lights when
  chosen (`.is-green` for green LEDs): program lists, detector and display modes.
- **`.scribble[data-tag]`** — the sixteen channel tag colours: `black`, `dblue`,
  `dgreen`, `flesh`, `lblue`, `lgreen`, `lpurple`, `lyellow`, `mint`, `orange`,
  `pink`, `purple`, `red`, `teal`, `white`, `yellow` (tokens `--tag-<name>`).
- **`.key[data-tone]`** — extra lit colours `cyan`, `blue`, `orange`, `brown`,
  `mauve`, `grey`, `white`.
- **`.knob.is-led`** — a gain pot in a ring of LED segments (red and yellow for too
  little gain, then green) lit to `--value`.
- **`.dyn-graph-fill`** — the shaded area under a dynamics curve.
- **`.assignable-page`**, **`.assignable-col.is-off`**, **`.assignable-nav`** — the
  panel's page counter, unassigned columns and its six navigation keys.
