# Audio component guide

Source: `core/components/audio.css` (with `.waveform` in media.css and meters in core and metering.css). ftl-themes is a server-rendered HTML/CSS design system, not a React package or audio engine. AudioCN’s catalogue is a useful model for audio workflows; use these existing themed primitives rather than adding a second component vocabulary. Live examples: [audio components](../../audio-components.html), [sound mixer](../../soundmixer.html), [media player](../../player.html), [instruments](../../components-instruments.html).

## Component map

Every AudioCN registry item, checked against [audiocn/ui](https://github.com/audiocn/ui)'s
`registry.json` (25 components, 6 blocks, 18 hooks). Classes marked **new**
live in `core/components/audio.css` (this guide's group) unless noted.

### Components

| AudioCN component | ftl-themes |
|---|---|
| dB Scale | `.scale.is-meter` beside a fader or meter; app-specific dB tick labels |
| dB Readout | `.readout` + `.readout-unit` (tabular figures, so the width never jumps); update text at a readable rate |
| Clip Indicator | **new** `.clip` button: lit with `aria-pressed="true"` or `.is-clipped`, `.clip-count`; the app holds and resets it |
| Level Meter | `.meter` (horizontal) / `.meter-v` with `--meter-level` and `--meter-peak`; **new** `.meter-rms` core (`--meter-rms`), `.meter.is-gradient`, `.meter-pair` for stereo; `.is-segmented`; zones via `--meter-warn-at`/`--meter-peak-at`; also `.ledbar`, `.ledarc`, `.vu` ([metering](metering.md)) |
| Bar Visualizer | **new** `.visualizer` of `<i style="--level">` bars: bottom or `.is-mirror`, `.is-idle`, `.is-loading` |
| Electric Bar Visualizer | **new** `.visualizer.is-electric` (white-hot filaments, glow, crackle; still under reduced motion) |
| Electric Waveform | **new** `.trace.is-electric` on an app-drawn SVG path |
| Smooth Waveform | **new** `.trace` with a smoothed `.trace-line` and optional mirrored `.trace-fill` |
| Live Waveform | **new** `.trace` (current frame as a line) or `.visualizer` (scrolling level history as bars); the app writes the samples |
| Waveform | `.waveform` + native seek input in seconds; bars, `.is-bottom`, `.is-envelope`; `.is-loading`; disabled; hover time (`data-hover-time`) ([media](media.md)) |
| Waveform region | `.waveform-region`: two edge range inputs (drag or arrow keys), tint, label, body drag, `.is-static`, fixed highlights, `data-color` ([media](media.md#regions-and-markers)) |
| Waveform marker | `.waveform-marker`: seeking `button` (`data-time`) or `span` label, `.is-end`, `data-color` |
| Fader | `.fader` native range (dB taper and −∞ are the app's); double-click resets to the default (`controls.js`); `.scale` for detent marks |
| Parameter Slider | **new** `.param`: label, `.slider` with `<datalist>` marks, number input with unit, `.param-reset`; `controls.js` mirrors and resets |
| Knob | `.knob` around a native range: vertical drag, Shift for fine, double-click reset (`controls.js`) |
| Pan Control | **new** `.slider.is-bipolar` (fills from the centre, centre detent) or `.knob.is-bipolar` |
| Channel Toggle | `.key.key-mute`, `.key.key-solo`, `.key.key-sel` (monitor), each with its own lit colour |
| Volume Control | `.volume`: mute `.media-toggle` + range ([media](media.md)) |
| Audio Device Select | **new** `.device-select` with `data-state="ready|loading|prompt|denied|none|disconnected"`, a live `.meter` slot and a status line |
| Channel Strip | `.strip` (console column) or **new** `.channel` (a row: head and status, meter and fader, value, keys, `.channel-notice`; stacks when narrow) |
| Mixer | `.mixer` of `.strip`s with `.strip.is-master`, or **new** `.channel-list` of `.channel` rows; keyboard movement between strips is the app's (roving tabindex) |
| Audio Player | `.now-playing`, `.transport`, `.scrubber` (**new** `.has-buffer` + `--buffered`), `.volume`, repeat/shuffle `.media-toggle`s; rate is a small `.select` ([player](../../player.html)) |
| Track List | `ol.tracklist` of `.track`s with `.is-active` / `.is-playing` ([media](media.md)) |
| Sound Pad | **new** `.pad` with `data-mode="one-shot|hold|toggle|loop"`, `kbd` hotkey, `--progress`, `data-color`; toggle and loop latch with a checkbox |
| Spectrum | `.rta` bars, `.rta.is-line`, **new** `.rta.is-area`; peak caps, `.eq-graph` grid and frequency labels ([metering](metering.md)) |

### Blocks

Compositions, shown on [audio-blocks.html](../../audio-blocks.html):

| AudioCN block | Built from |
|---|---|
| System audio mixer | `.channel-list` of `.channel` rows (mic, system, music, pads) + a master row with `.meter-pair`, `.clip` |
| Mic setup | `.device-select` + `.visualizer` live preview + `.param` gain + mute `.key` + level-check `.meter` and `.alert` |
| System audio settings | `.field-row` + `.switch`, a `.channel`, explanatory `.field-hint` |
| Quick audio popover | toolbar `.btn` holding a five-bar `.visualizer`, opening a `[popover]` with `.channel` rows |
| Soundboard | `.soundboard` of `.pad`s, master `.volume`, stop-all button, per-pad `.context-menu` |
| Music player | `.tracklist` + `.waveform` seek with `.waveform-marker`s + `.transport` + rate `.select` + `.volume` + a ducking `.check` |

### Hooks and engine

AudioCN's `core` library and its hooks (`use-audio-context`, `use-gain-node`,
`use-audio-analyser`, `use-audio-devices`, `use-microphone`,
`use-system-audio`, `use-mixer`, `use-web-audio-mixer`, `use-audio-player`,
`use-sound`, `use-waveform-data`, `use-level`, `use-clip-hold`,
`use-frame-source`, `use-visibility`, `use-reduced-motion`,
`use-demo-signal`, `use-audio-config`) are React and Web Audio code. They
stay in your app: they produce the numbers (`--level`, `--meter-*`,
`--progress`, `--buffered`, region seconds, `data-state`) that this markup
shows. Two small things they do have native equivalents here: reduced
motion is handled in CSS, and `controls.js` keeps inputs and custom
properties in step.

## Usage

Load one theme bundle, then use ordinary HTML. Put range inputs inside knobs so keyboard, touch and screen-reader operation comes from the native control. Include `assets/js/controls.js` only when the app wants it to sync `.knob` visuals and mixer readouts; the app can instead update `--value` itself.

```html
<label class="knob knob-sm is-bipolar" style="--value:.5">
  <input type="range" min="-1" max="1" step=".01" value="0" aria-label="Channel pan">
  <span class="knob-dial"></span><span class="knob-label">Pan</span>
</label>
<div class="meter meter-v is-segmented" role="meter" aria-label="Output level"
     aria-valuenow="-6" aria-valuemin="-60" aria-valuemax="0"
     style="--meter-level:78%;--meter-peak:91%">
  <div class="meter-fill"></div><div class="meter-peak"></div>
</div>
```

Meters and visualizers consume data supplied by the application. Audio capture, analyser setup, playback state, device enumeration, clip hold, and parameter-to-audio wiring are app responsibilities; ask for microphone permission only in response to a user action. Honor reduced motion and provide text labels or values for visual-only output.

## Waveform timelines

The library provides a seekable waveform with draggable regions and seeking markers, not a complete audio editor. For a multitrack timeline, compose waveform clips with track labels, a time ruler, the existing transport and range controls, and `.key` mute/solo controls. The example on [audio-components.html](../../audio-components.html) shows that composition with two tracks. Selections and loops are `.waveform-region`s (their edges are seconds on the clip's own timeline), and cue points are `.waveform-marker`s. Keep clip positions, zoom, snapping, splitting, fades, looping playback and synchronization in the host app; expose playback position through a labelled native range input and label each decorative waveform with its track and time span. Use `.strip` and `.mixer`, or `.channel` rows, when each track also needs gain, pan and metering.

## Tokens

New in `audio.css`, each falling back to the base palette: `--channel-accent`, `--channel-bg`, `--channel-border`, `--channel-padding`, `--clip-border`, `--clip-glow`, `--clip-off`, `--clip-off-fg`, `--clip-on`, `--clip-on-fg`, `--clip-radius`, `--clip-width`, `--device-meter-width`, `--meter-pair-gap`, `--meter-rms`, `--meter-rms-fg`, `--pad-bg`, `--pad-color`, `--pad-fg`, `--pad-glow`, `--pad-height`, `--pad-lit-alpha`, `--pad-min`, `--pad-progress-height`, `--pad-radius`, `--param-value-width`, `--scrubber-buffer`, `--slider-centre`, `--soundboard-gap`, `--trace-axis`, `--trace-axis-dash`, `--trace-core`, `--trace-fg`, `--trace-fill-alpha`, `--trace-height`, `--trace-width`, `--visualizer-core`, `--visualizer-fg`, `--visualizer-filament`, `--visualizer-gap`, `--visualizer-height`, `--visualizer-min`, `--visualizer-radius`, `--visualizer-smoothing`. Values set by the app: `--level`, `--meter-rms`, `--progress`, `--buffered`, `--value`.

## Existing examples

- [audio-components.html](../../audio-components.html): meters, clip, visualisers, traces, knobs and parameters, pan, channel rows, device states, sound pads, waveform regions and markers, and a multitrack timeline.
- [audio-blocks.html](../../audio-blocks.html): the six AudioCN blocks.
- [soundmixer.html](../../soundmixer.html): channel strips, EQ, input keys, gain reduction, pan, faders and meter banks.
- [player.html](../../player.html): player transport, track list, waveform seeking and volume.
- [dashboard.html](../../dashboard.html): general-purpose level meters in a data dashboard.

AudioCN is a React 19 / Tailwind v4 shadcn registry; its hooks (`useMicrophone`, `useAudioAnalyser`, mixer/player hooks and others) do not transfer to this framework-free library. See [AudioCN](https://github.com/audiocn/ui) and its [documentation](https://www.audiocn.dev/docs).
