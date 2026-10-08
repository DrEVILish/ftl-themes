# Music and media kit (v5)

Source: `core/components/media.css`. Live examples: `player.html`. Covers
PLAN.md §19 "Music and media" (Playlist Lab first): track rows, the playing
equaliser glyph, shuffle/repeat/like/mute toggles, the seek scrubber and
volume, the now-playing bar and mini player, the play queue, the waveform
scrubber, the album grid and lyrics. Builds on core's `.btn` /
`.btn-icon` / `.btn-ghost`, `.transport` + `.btn-go`, `.badge`, `.knob`,
`.context-menu` and surfaces.css's `.card.has-media`.

Tokens are listed as `token: default`. Set them on `html[data-theme="x"]` like
every other component token. Everything on the page works without
JavaScript (toggles, repeat cycling, scrubber fill, waveform played colour)
except the waveform hover preview, region dragging and marker seeking,
which `assets/js/controls.js` handles.

For the wider audio-control map (meters, mixers, devices and trigger pads), see
the [audio component guide](audio.md) and [audio showcase](../../audio-components.html).

---

## Track rows `.tracklist` > `.track`

```html
<ol class="tracklist">
  <li class="track">
    <button class="track-play" aria-label="Play Night Drive">
      <span class="track-num">1</span>
      <svg class="icon"><use href="assets/icons/icons.svg#icon-play"/></svg>
    </button>
    <img src="art.jpg" alt="" width="40" height="40">
    <span class="track-main">
      <span class="track-title">Night Drive</span>
      <span class="track-artist"><span class="badge is-explicit" role="img" aria-label="Explicit">E</span>Lumen Coast</span>
    </span>
    <span class="track-album">Harbour Lights</span>
    <label class="btn btn-ghost btn-icon media-toggle is-like">
      <input type="checkbox" aria-label="Like Night Drive">
      <svg class="icon"><use href="assets/icons/icons.svg#icon-heart"/></svg>
    </label>
    <time class="track-time" datetime="PT4M3S">4:03</time>
    <button class="btn btn-ghost btn-icon" popovertarget="track-menu" aria-label="More options for Night Drive">
      <svg class="icon"><use href="assets/icons/icons.svg#icon-more-horizontal"/></svg>
    </button>
  </li>
</ol>
```

- **Cells** (all optional except `.track-main`, in this order): `.track-handle`
  (queue), `.track-play`, `<img>` (art), `.track-main` (title over artist),
  `.track-album`, like toggle, `.track-time`, action buttons. Rows in one list
  should carry the same cells so the columns line up. The row is flex: the
  title takes 2 parts of the free width, the album 1; long text truncates.
- **Play button**: shows the number at rest and the play icon on row hover
  or keyboard focus. On touch (no hover) the number *is* the visible button.
  A `.track-play` with no `.track-num` always shows its icon, unless the row
  is playing (the glyph shows then).
- **Row actions**: `.btn-ghost` children (like, more, remove) appear on row
  hover or focus on devices that can hover; a pressed toggle (a liked track)
  stays visible. Touch devices always show them.
- **Explicit**: `.badge.is-explicit` (needs `role="img"` + `aria-label`).

### States

| Markup | Result |
|---|---|
| `.track.is-playing` (or `aria-current="true"`) | Title in the accent; the equaliser glyph replaces the number (bars move only when motion is allowed). Render `#icon-pause` in its button and label it "Pause …". |
| `.track.is-playing.is-paused` | Current track, paused: the glyph holds still. |
| `.track.is-active`, or a checked direct-child radio or checkbox (`[aria-selected="true"]` too, but only where the list really is a `listbox`/`grid` with `option`/`row` items) | Selected: `--row-selected-bg` plus the inset marker (never colour alone); text switches to `--row-selected-fg`. |
| `.track.is-dragging` | Lifted (queue drag in progress). |
| `.track.is-drop-target` | A drop line along the top edge: the dragged row lands above this one. |

### Tokens

| Token | Default |
|---|---|
| `--tracklist-gap` | `0` |
| `--track-gap` | `var(--space-s)` (`--space-xs` in narrow lists) |
| `--track-pad` | `var(--space-2xs) var(--space-xs)` |
| `--track-radius` | `var(--radius)` |
| `--track-fg` | `var(--text)` |
| `--track-meta-fg` | `var(--muted)` (artist, album, time) |
| `--track-meta-fg-active` | `var(--row-selected-fg, var(--text))` (meta text on a selected row) |
| `--track-num-fg` | `var(--muted)` |
| `--track-num-size` | `2em` (play cell; never under `--tap-min`) |
| `--track-art-size` | `2.5rem` |
| `--track-art-radius` | `var(--radius)` |
| `--track-bg-hover` | `var(--row-hover-bg, color-mix(in srgb, var(--text) 6%, transparent))` |
| `--track-bg-selected` | `var(--row-selected-bg, color-mix(in srgb, var(--text) 14%, transparent))` |
| `--track-selected-marker` | `var(--row-active-marker, inset 0.25rem 0 0 var(--accent))` |
| `--track-playing-fg` | `var(--accent-text, var(--accent))` |
| `--track-handle-fg` | `var(--muted)` |
| `--track-drag-bg` | `var(--surface-2)` |
| `--track-drag-shadow` | `0 0.5rem 1.5rem rgba(0, 0, 0, 0.35)` |
| `--track-drop-color` / `--track-drop-width` | `var(--accent)` / `2px` |

### Tier and touch

`.tracklist` is a size container: under 480px wide it hides the album and
time columns. The play button, like and action buttons are `--tap-min`
squares (44px on touch). There is no hover on touch, so the number is the
play control and row actions stay visible.

### Accessibility

Label the play button with the track ("Play Night Drive"); its number is
then decorative. Liked state lives in the checkbox (or `aria-pressed`).
Set `aria-current="true"` on the playing row if you want assistive tech to
know which one it is (it is styled the same as `.is-playing`). For
spreadsheet-style selection and bulk actions use tables.md's `.table` and
`.bulk-bar` instead; `.tracklist` is the playback view.

---

## Play queue

A queue is track rows with a drag handle and a remove button, grouped
under plain headings ("Now playing", "Next in queue", "Next from: …"):

```html
<li class="track">
  <span class="track-handle" aria-hidden="true"></span>
  <button class="track-play" aria-label="Play Glass Hours"><svg class="icon"><use href="…#icon-play"/></svg></button>
  <img src="art.jpg" alt="">
  <span class="track-main">…</span>
  <time class="track-time" datetime="PT3M58S">3:58</time>
  <button class="btn btn-ghost btn-icon" aria-label="Remove Glass Hours from queue"><svg class="icon"><use href="…#icon-close"/></svg></button>
</li>
```

`.track-handle` is a visual: 2 × 3 dots, `cursor: grab`, `touch-action:
none`, the full `--tap-min` tall. The app does the dragging (Pointer
Events) and sets `.is-dragging` / `.is-drop-target`. Keep the handle a
plain, non-focusable span and give keyboard users "Move up/down" items in
the row menu instead.

---

## Equaliser glyph `.equaliser`

```html
<span class="equaliser" aria-hidden="true"></span>
<span class="equaliser is-paused" aria-hidden="true"></span>
```

Three bars drawn as background layers in `currentColor`. They bounce only
under `prefers-reduced-motion: no-preference` and stop with
`html[data-motion="reduced"]`; `.is-paused` holds them still. A playing
track row draws the same glyph in its play button, with no extra markup.

| Token | Default |
|---|---|
| `--equaliser-color` | `var(--accent-text, var(--accent))` |
| `--equaliser-size` | `0.9em` |
| `--equaliser-speed` | `0.9s` (one cycle) |

---

## Media toggles `.media-toggle` (shuffle, repeat, like, mute)

A state layer on an icon button, so it matches the theme's `.btn-ghost`:

```html
<!-- Shuffle: a checkbox, no JS -->
<label class="btn btn-ghost btn-icon media-toggle">
  <input type="checkbox" aria-label="Shuffle">
  <svg class="icon"><use href="…#icon-shuffle"/></svg>
</label>

<!-- Or a button the app flips -->
<button class="btn btn-ghost btn-icon media-toggle" aria-pressed="true" aria-label="Shuffle">…</button>

<!-- Repeat off / all / one with no JS: three radios, a click hits the next -->
<span class="btn btn-ghost btn-icon media-toggle" role="radiogroup" aria-label="Repeat">
  <input type="radio" name="repeat" value="off" aria-label="Repeat off" checked>
  <input type="radio" name="repeat" value="all" aria-label="Repeat all">
  <input type="radio" name="repeat" value="one" aria-label="Repeat one">
  <svg class="icon"><use href="…#icon-repeat"/></svg>
</span>
<!-- App-driven repeat: aria-pressed="true" for all, plus .is-one for one -->

<!-- Like: a filled heart -->
<label class="btn btn-ghost btn-icon media-toggle is-like"><input type="checkbox" aria-label="Like">…#icon-heart…</label>

<!-- Two icons swap: volume / muted -->
<label class="btn btn-ghost btn-icon media-toggle">
  <input type="checkbox" aria-label="Mute">
  <svg class="icon"><use href="…#icon-volume"/></svg><svg class="icon"><use href="…#icon-volume-mute"/></svg>
</label>
```

### States

| State | Look |
|---|---|
| Off | `--media-toggle-fg` (muted). |
| On (`aria-pressed="true"`, a checked checkbox, or any radio but the first) | `--media-toggle-on` plus a dot under the icon: never colour alone. |
| Repeat one (`.is-one`, or the third radio) | Also a small "1" at the icon's top-right corner. |
| Like on | Filled heart in `--media-like-on`, no dot. |
| Two icons | The second icon replaces the first when on. |

The box never changes size with its state ("stable widths"): the dot and
the "1" are absolutely positioned. The input covers the whole button, so
the hit area is the button (`--tap-min` on touch).

**How the repeat cycle works:** the radios are stacked over the button and
only the one after the checked one (the first, after the last) takes
pointer events, so each click checks the next state. Keyboard: Tab reaches
the group, arrow keys step through off/all/one. The app listens for
`change` on the radios.

| Token | Default |
|---|---|
| `--media-toggle-fg` | `var(--muted)` |
| `--media-toggle-on` | `var(--accent-text, var(--accent))` |
| `--media-like-on` | `var(--media-toggle-on)` (set `var(--danger)` for a red heart) |
| `--media-repeat-one-glyph` | `"1"` |

Accessibility: name every input (`aria-label`); the radio group needs its
own name ("Repeat"). Focus shows the core ring on the button.

---

## Scrubber `.scrubber` and volume `.volume`

```html
<div class="scrubber">
  <time>1:46</time>
  <input type="range" min="0" max="312" value="106" aria-label="Seek" aria-valuetext="1:46 of 5:12">
  <time>-3:26</time>
</div>

<div class="volume">
  <label class="btn btn-ghost btn-icon media-toggle">…mute…</label>
  <input type="range" min="0" max="100" value="70" aria-label="Volume">
</div>
```

Real range inputs. The played fill needs **no script and no `--value`**:
the thumb's `border-image` paints the track out to both sides (fill before
the thumb, track after it) and the input clips the overflow. The app only
moves `value` as the track plays and updates the times and
`aria-valuetext`. The input is `--tap-min` tall; the drawn track stays
thin. Under forced colours it falls back to the native slider.

A `.knob` (CONTRACT.md "Mixing-console primitives") works as a volume
control too, for console-style themes; it needs `assets/js/controls.js`.

| Token | Default |
|---|---|
| `--scrubber-height` | `0.25rem` (drawn track) |
| `--scrubber-fill` | `var(--accent)` |
| `--scrubber-track` | `color-mix(in srgb, var(--text) 25%, transparent)` |
| `--scrubber-thumb` | `var(--text)` |
| `--scrubber-thumb-size` | `0.75rem` |
| `--scrubber-thumb-radius` | `50%` |
| `--scrubber-time-fg` | `var(--muted)` |
| `--volume-size` | `6rem` |

---

## Waveform scrubber `.waveform`

```html
<div class="scrubber">
  <time>1:28</time>
  <div class="waveform">
    <input type="range" min="0" max="243" value="88" aria-label="Seek" aria-valuetext="1:28 of 4:03">
    <span class="waveform-bars" aria-hidden="true">
      <i style="--level:.42"></i><i style="--level:.8"></i>…   <!-- one per bar, 0–1 -->
    </span>
  </div>
  <time>-2:35</time>
</div>
```

- **Value APIs** (inline styles): `--level` (0–1) on each bar, from the
  app's peak data; `--hover` (0–1) on `.waveform`, the pointer position.
- **Units:** the seek input (and every region edge) uses **seconds** as its
  `min`/`max`/`value`, so times line up across the whole control.
- **How it paints:** the range input sits underneath and paints played /
  unplayed (the same thumb trick as `.scrubber`, full height), so dragging
  or arrow keys recolour the bars live with no script. The bars on top are
  windows cut into a `--waveform-bg` mask, so the waveform is always its
  own filled box. `--hover` tints from the start to the pointer
  (`--waveform-preview`) under the mask: the hover preview.
- Bars don't take pointer events; the input gets every click and drag.
- **Variants and states:** `.is-bottom` (bars rise from the bottom edge),
  `.is-envelope` (no gaps: a solid outline), `.is-loading` (a shimmer in
  place of the bars), and a disabled seek input dims the whole waveform.
- **Hover time:** with `data-hover-time="1:55"` on `.waveform`, a chip
  shows that text at `--hover`. `assets/js/controls.js` sets both from the
  pointer and the seek input's range; without it, set them yourself.

### Regions and markers

```html
<div class="waveform">
  <input type="range" min="0" max="180" step="0.1" value="12" aria-label="Seek" aria-valuetext="0:12 of 3:00">
  <span class="waveform-bars" aria-hidden="true">…</span>
  <div class="waveform-region" role="group" aria-label="Ad break" data-color="2" style="--start:.3444;--end:.5278">
    <input type="range" min="0" max="180" step="0.1" value="62" aria-label="Ad break start">
    <input type="range" min="0" max="180" step="0.1" value="95" aria-label="Ad break end">
    <span class="waveform-region-label">Ad break</span>
  </div>
  <button class="waveform-marker" type="button" data-time="110" style="--at:.6111">Chapter 2</button>
  <span class="waveform-marker is-end" style="--at:.9333">Outro</span>
</div>
```

- **Region** `.waveform-region`: a tinted span from `--start` to `--end`
  (0–1) with an optional label. Its two range inputs are the edges: drag a
  handle or focus it and use the arrow keys (one `step`), Page Up / Page Down (a tenth of the clip) or Home / End. Both inputs span the **whole
  clip** (the seek input's `min`/`max`), which is what keeps each handle
  over the right moment: don't narrow one edge's `min`/`max` to the other
  edge's value, clamp instead.
- **Moving a region:** drag its body. `.is-static` keeps the edges
  draggable but not the body (clicks inside then seek). A region with no
  inputs is a fixed highlight; mark it `aria-hidden` and describe it
  elsewhere, or keep the label as visible text.
- **Markers** `.waveform-marker`: a chip at the top with a line down the
  waveform at `--at` (0–1). A `<button>` marker seeks (with `data-time` in
  seconds, `controls.js` does it); a `<span>` is a label only; an empty
  marker is just the line. `.is-end` puts the chip on the left, for
  markers near the end.
- **Colour:** `data-color="1..6"` on a region or marker picks one of the
  six per-user colours (social.css), so overlapping regions stay apart.
- **What `controls.js` does:** keeps `--start`/`--end` in step with the
  edges, keeps the edges in order at least `data-min-length` seconds apart
  (default: one `step`), sets each edge's `aria-valuetext` to `m:ss`, moves
  the region when its body is dragged (firing `input` then `change` on both
  edges), seeks for marker buttons, and sets the hover preview. Listen for
  `change` on the edges to save a region. Without the script, set the
  values and custom properties server-side.
- **What the app owns:** creating and deleting regions, snapping, looping
  playback inside a region, saving, and the bar data for a zoomed window.

### Gain, ghost and fades

- **`--gain`** (0–1) on a bar scales it: the visible height is `--level ×
  --gain`. Set it to the engine's fade gain at that bar and the waveform
  shows what will be heard. Outside a cue's trim, leave bars at full level
  (that is the material you choose trim points from); where two fades
  overlap, use the lower gain.
- **`.waveform.has-ghost`** keeps each bar's full `--level` as a faint
  ghost behind the gained bar (`--waveform-ghost`), so the gap is what the
  fade removes.
- **Fade regions:** `.waveform-region.is-fade-in` / `.is-fade-out` draw
  their tint in the shape of the fade, from `data-curve`: `linear`
  (default), `smooth` (t²(3−2t)), `log` (log10(1+9t)) or `exp`
  ((e^3t−1)/(e³−1)). Mirror the engine's curve exactly; a picture that
  differs from what plays is worse than none. Give a fade region one
  range input to make its length draggable: on a fade-in the input is the
  end, on a fade-out the start (`controls.js` sets `--end` / `--start`);
  the app keeps the other edge on the trim point and recomputes `--gain`.
- **Marker rows:** `data-row="2"` (or `3`) puts a marker's chip on a lower
  row (`--waveform-marker-row`, 1.1rem each), so fade chips and time chips
  don't collide. Its line still runs the full height.

```html
<div class="waveform has-ghost">
  <input type="range" min="0" max="180" step="0.1" value="40" aria-label="Seek cue">
  <span class="waveform-bars" aria-hidden="true"><i style="--level:.6;--gain:.35"></i>…</span>
  <div class="waveform-region is-fade-in" data-curve="smooth" role="group" aria-label="Fade in, smooth" style="--start:.0333;--end:.0667">
    <input type="range" min="0" max="180" step="0.1" value="12" aria-label="Fade in ends">
  </div>
  <span class="waveform-marker" data-row="2" style="--at:.0667">Fade in 6 s</span>
</div>
```

### Zoom

```html
<div class="waveform" id="cue-wave">…seek input, bars, regions, markers…</div>
<div class="waveform-ruler" data-for="cue-wave" aria-hidden="true"></div>
<div class="waveform waveform-overview is-envelope" data-overview-for="cue-wave">
  <span class="waveform-bars" aria-hidden="true">…whole clip…</span>
  <div class="waveform-region waveform-window" role="group" aria-label="Visible part" style="--start:0;--end:1">
    <input type="range" min="0" max="180" step="0.1" value="0" aria-label="Visible part starts">
    <input type="range" min="0" max="180" step="0.1" value="180" aria-label="Visible part ends">
  </div>
</div>
<div class="waveform-zoom btn-group" role="group" aria-label="Zoom" data-for="cue-wave">
  <button class="btn btn-sm" type="button" data-zoom="in">Zoom in</button>
  <button class="btn btn-sm" type="button" data-zoom="out">Zoom out</button>
  <button class="btn btn-sm" type="button" data-zoom="fit">Zoom to selection</button>
  <button class="btn btn-sm" type="button" data-zoom="select" aria-pressed="false">Box zoom</button>
  <button class="btn btn-sm" type="button" data-zoom="reset">Show the whole clip</button>
</div>
```

- **The window** is `--zoom-from` / `--zoom-to` on the `.waveform`, as
  0–1 of the clip. CSS stretches the seek input, the regions and the bars
  to the whole clip at that scale and slides them left, so **no input's
  `min`, `max` or `value` ever changes**: the browser never clamps an edge
  that is out of view, a save reads true times, and dragging a region's
  body still works while zoomed. Markers map `--at` into the window; region
  labels stay inside it. The change animates unless motion is reduced.
- **`controls.js`** sets the window from the `.waveform-zoom` buttons
  (`in` halves it around its centre, `out` doubles it, `fit` frames the
  `.is-selected` or focused region, `select` arms a box zoom: drag across
  the waveform to zoom into that span, `reset` shows the whole clip), the
  mouse wheel (pans a zoomed waveform) and the overview's window region.
  It fires **`waveform-view`** on the `.waveform` with `detail` `{from, to}`
  in seconds and `{fromFraction, toFraction}`, so the app can fetch finer
  peaks; `window.ftlWaveformView(waveform, from, to)` sets it from code
  (fractions). Out-of-view region edges leave the tab order and get
  `aria-description` "before/after the visible part"; the region draws an
  arrow at that side (`.is-before` / `.is-after`). Out-of-view markers are
  `hidden`. `.waveform-ruler[data-for]` gets labels whose step widens with
  the window (0.1 s up to 1 h). `data-min-zoom` (default 0.005) limits how
  far in it goes.
- **Bars:** by default the clip's bars stretch with the window. For finer
  detail, put bars for just the window in `.waveform-bars.is-window` on
  each `waveform-view`, reusing the `<i>` nodes (set `--level` on them)
  rather than rebuilding them, so the zoom stays smooth.

| Token | Default |
|---|---|
| `--waveform-height` | `3rem` (≥ 44px, a full touch target) |
| `--waveform-bg` | `var(--surface-2)` (box and bar mask) |
| `--waveform-played` | `var(--accent)` |
| `--waveform-unplayed` | `var(--muted)` |
| `--waveform-preview` | `color-mix(in srgb, var(--waveform-played) 45%, transparent)` |
| `--waveform-head` / `--waveform-head-width` | `var(--waveform-played)` / `2px` |
| `--waveform-gap` | `2px` |
| `--waveform-radius` | `var(--radius)` |
| `--waveform-region` | `var(--accent)` (region tint and handles, unless `data-color`) |
| `--waveform-region-alpha` | `22%` (tint strength) |
| `--waveform-region-fg` | `var(--on-accent)` (region label text) |
| `--waveform-handle-width` / `-touch` | `0.5rem` / `1.25rem` on coarse pointers |
| `--waveform-handle-radius` | `2px` |
| `--waveform-marker` | `var(--warning)` (unless `data-color`) |
| `--waveform-marker-fg` / `--waveform-marker-width` | `var(--text)` / `2px` |
| `--waveform-ghost` | 72% `--waveform-bg` (the ghost above a gained bar) |
| `--waveform-fade` / `--waveform-fade-alpha` | `var(--waveform-region)` / `38%` |
| `--waveform-marker-row` | `1.1rem` (height of a marker row) |
| `--zoom-from` / `--zoom-to` | `0` / `1` (the visible window) |
| `--waveform-select` | `var(--accent)` (box zoom span) |
| `--waveform-ruler-fg` / `--waveform-ruler-rule` | `var(--muted)` / `var(--hairline)` |
| `--waveform-overview-height` | `max(1.6rem, 24px)` (never under the 24px target size) |

Accessibility: the seek input is the control (`aria-label`,
`aria-valuetext` with times); the bars are `aria-hidden`. Focus draws the
ring around the whole waveform, or around a region handle. Give each
region a `role="group"` and `aria-label`, and each edge its own label
("Ad break start"). Marker buttons need an accessible name that includes
the time when the chip text alone doesn't say it. In forced-colours mode
regions draw as outlines and handles in the system highlight colour.

For a multitrack waveform timeline, compose one decorative `.waveform` clip
per region with `.key` mute/solo controls, `.transport`, and a labelled
`.scrubber` for the playhead. [The audio showcase](../../audio-components.html)
includes a two-lane example. This library styles the controls and clip
presentation; the consuming app owns clip editing, zoom, selection, snapping,
and synchronization.

---

## Now-playing bar `.now-playing`

```html
<footer class="now-playing" aria-label="Now playing">   <!-- a direct child of .app -->
  <img src="art.jpg" alt="" width="56" height="56">
  <span class="track-main"><span class="track-title">Undertow</span><span class="track-artist">Marisol Vega</span></span>
  <label class="btn btn-ghost btn-icon media-toggle is-like">…</label>
  <div class="transport is-play" role="group" aria-label="Playback">
    …shuffle toggle…
    <button class="btn btn-ghost btn-icon" aria-label="Previous">…#icon-skip-back…</button>
    <button class="btn btn-go btn-icon" aria-label="Pause">…#icon-pause…</button>
    <button class="btn btn-ghost btn-icon" aria-label="Next">…#icon-skip-forward…</button>
    …repeat toggle…
  </div>
  <div class="scrubber">…</div>
  <div class="now-playing-extras">
    <button class="btn btn-ghost btn-icon" aria-label="Lyrics">…</button>
    <button class="btn btn-ghost btn-icon" aria-label="Queue">…</button>
    <div class="volume">…</div>
  </div>
</footer>
```

- **In the shell:** as a direct child of `.app` it takes the shell's
  `status` grid area (use it *instead of* `.app-status`) and is
  `position: sticky` to the bottom of the screen at every tier, so it sits
  in the status position on desktop and docks on phones and tablets. Its
  bottom and side padding add `env(safe-area-inset-*)`, so it clears the
  home indicator (the page needs `viewport-fit=cover`). It sits at
  `--z-sticky`. Being in flow, it never covers the end of the page.
- **Anywhere else** (a panel, a sidebar) it is an ordinary box in the flow.
- **Transport:** core's `.transport` with its chrome zeroed (bg, border,
  edge, padding, shadow) inside the bar; `.btn-go.btn-icon` is the play
  button. A theme that styles `.transport` directly still paints it here.

### Layouts (viewport tier; `.is-mini` forces the phone layout)

| Tier | Layout |
|---|---|
| Desktop, XL | Art, title and like · transport over the scrubber · extras (volume, other buttons) on the right. |
| Tablet (481–900) | Art, title, like, full transport on one row; the scrubber on its own row; extras hidden (hardware volume keys). |
| Mobile (≤ 480) and `.is-mini` | Art, title, like, play and the control after it (next); scrubber row. Shuffle, previous and repeat hide. |

The layout follows the viewport, not a container: the bar is shell-level
furniture, and a grid can't change its own template from a container query.
For a bar in a narrow box on a wide screen, use `.is-mini`.

### Mini player `.now-playing.is-mini`

The phone layout at any width, as a card (border, radius, panel shadow,
capped at `--now-playing-mini-max`). For a sidebar, a picture-in-picture
corner or a popover; the app positions it.

| Token | Default |
|---|---|
| `--now-playing-bg` | `var(--surface)` |
| `--now-playing-fg` | `var(--text)` |
| `--now-playing-rule` / `--now-playing-rule-width` | `var(--border)` / `1px` |
| `--now-playing-shadow` | `none` |
| `--now-playing-pad-block` / `--now-playing-pad-inline` | `var(--space-xs)` / `var(--space-m)` |
| `--now-playing-gap` | `var(--space-s)` |
| `--now-playing-art-size` | `3.5rem` (`2.75rem` mini) |
| `--now-playing-art-radius` | `var(--radius)` |
| `--now-playing-mini-max` | `24rem` |
| `--now-playing-mini-radius` | `var(--radius)` |
| `--now-playing-mini-shadow` | `var(--panel-shadow, none)` |

Plus `--go-*` for the play button and the scrubber/toggle tokens above.

Accessibility: name the region (`aria-label="Now playing"`) and the
transport group; keep the play button's label in step with its icon
("Play" / "Pause").

---

## Album grid `.album-grid`

```html
<ul class="album-grid">
  <li><article class="card has-media">
    <div class="card-media">
      <img src="cover.jpg" alt="" width="300" height="300" loading="lazy">
      <button class="btn btn-go btn-icon card-play" aria-label="Play Harbour Lights">…#icon-play…</button>
    </div>
    <div class="card-body">
      <a class="stretched-link" href="/album/harbour-lights">Harbour Lights</a>
      <span class="text-muted">Lumen Coast · 2024</span>
    </div>
  </article></li>
</ul>
```

Square image cards (surfaces.md's `.card.has-media`, `--card-media-ratio: 1`
set by the grid) in an auto-fill grid. `.card-play` sits in the art's
bottom corner, above the stretched link, filled with the accent. It shows
on card hover or focus, always on touch, and always on a playing album
(`.card.is-playing`; render `#icon-pause` and "Pause …"). Loading covers use
the image card's `aria-busy="true"` skeleton.

| Token | Default |
|---|---|
| `--album-min` | `9.5rem` (smallest column) |
| `--album-gap` | `var(--space-m)` |
| `--card-play-bg` / `--card-play-fg` | `var(--accent)` / `var(--on-accent)` |
| `--card-play-shadow` | `0 0.25rem 0.75rem rgba(0, 0, 0, 0.4)` |

---

## Lyrics `.lyrics`

```html
<div class="scroll" style="--scroll-max: 16rem" tabindex="0" role="region" aria-label="Lyrics">
  <ol class="lyrics">
    <li>Headlights on the harbour wall</li>
    <li></li>                                  <!-- instrumental gap -->
    <li aria-current="true">So hold the line, hold the line</li>
    <li>the static sounds like you to me</li>
  </ol>
</div>
```

The current line (`aria-current="true"`) is full-strength text with an
inset marker (not colour alone); other lines are `--lyrics-fg`. An empty
`<li>` shows `--lyrics-gap-glyph` (♪ ♪ ♪). The app moves `aria-current` and
calls `scrollIntoView({ block: "center" })`; `scroll-margin-block` keeps the
line off the edge. Colour changes ease only when motion is allowed.

| Token | Default |
|---|---|
| `--lyrics-fg` | `var(--muted)` |
| `--lyrics-current-fg` | `var(--text)` |
| `--lyrics-current-marker` | `inset 0.25rem 0 0 var(--accent)` |
| `--lyrics-size` / `--lyrics-weight` | `1.375rem` / `700` |
| `--lyrics-gap` | `var(--space-2xs)` |
| `--lyrics-scroll-margin` | `35%` |
| `--lyrics-gap-glyph` | `"♪  ♪  ♪"` |

---

## Icons

All from the shared sprite: `play`, `pause`, `skip-back`, `skip-forward`,
`shuffle`, `repeat`, `heart`, `volume`, `volume-mute`, `more-horizontal`,
`close`, `playlist`, `microphone`.
