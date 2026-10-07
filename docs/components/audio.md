# Audio component guide

ftl-themes is a server-rendered HTML/CSS design system, not a React package or audio engine. AudioCN’s catalogue is a useful model for audio workflows; use these existing themed primitives rather than adding a second component vocabulary. Live examples: [audio components](../../audio-components.html), [sound mixer](../../soundmixer.html), [media player](../../player.html), [instruments](../../components-instruments.html).

## Component map

| AudioCN component | ftl-themes equivalent / integration |
|---|---|
| Level Meter | `.meter` / `.meter-v`, `--meter-level`, `--meter-peak`; ARIA `role="meter"` for live div meters |
| dB Scale | `.scale.is-meter` inside `.strip-fader`; provide app-specific dB tick labels |
| dB Readout | `.readout` and `.readout-unit` |
| Clip Indicator | `.lamp.is-error`, `.status.status-error`, or `.badge`; app owns clip hold/reset state |
| Bar Visualizer | `.bar-chart` or app-fed bars, as in the audio showcase |
| Electric Bar Visualizer | App-fed bars with app-specific decoration; no electric animation primitive is shipped |
| Electric Waveform | `.waveform` for seekable media; custom SVG/canvas when the electric treatment is required |
| Smooth Waveform | `.waveform` for stored peaks, or SVG/canvas for a live trace |
| Live Waveform | App-fed SVG/canvas; `.waveform` is the seekable clip control |
| Waveform | `.waveform` + native range input (seconds), played fill and playhead, `.is-bottom` / `.is-envelope` variants, `.is-loading`, disabled; see [media](media.md) |
| Waveform hover | `--hover` + `data-hover-time` on `.waveform` (set by `controls.js`) |
| Waveform region | `.waveform-region` with two edge range inputs, `--start`/`--end`, label, `data-color`, body drag (`controls.js`), `.is-static`, fixed highlights |
| Waveform marker | `.waveform-marker` (`button` seeks via `data-time`, `span` labels), `--at`, `.is-end`, `data-color` |
| Waveform timeline | Compose `.waveform` clips, `.scrubber`, `.transport`, `.track`/`.strip`, and mute/solo `.key` controls; see the multi-track example below |
| Spectrum / RTA | `.rta` in `.eq-graph` (31 third-octave bands, peak caps, `.is-pre`, `.is-line`); see [metering](metering.md) |
| Spectrogram | `.spectrogram` cells on `--chart-seq-*`, or an app `<canvas>`/`<img>`, behind the EQ curve |
| VU meter | `.vu` needle meter (−20…+3 scale, peak LED, 300 ms ballistics), `.vu.is-pair` stereo, `.vu.is-ppm` |
| LED bargraph | `.ledbar` / `.ledbar-pair` + `.ledbar-scale`: zones, reference band, peak hold, overs |
| Loudness arc | `.ledarc` with upper/lower scales; `.meter-panel` for Peak / Overs / Meter-mode keys |
| VFD display | `.is-vfd` on `.vu`, `.ledbar`, `.ledarc`, `.readout`; `.vfd` window; theme opt-in `--meter-style: vfd` |
| Fader | `.fader` native range input; app supplies the dB taper |
| Parameter Slider | `.slider` + `.field`, optional adjacent `.readout` |
| Knob | `.knob` wrapping a labelled native range input |
| Pan Control | `.knob.is-bipolar` with centre value zero |
| Channel Toggle | `.key.key-mute`, `.key.key-solo`, `.key.key-sel`, or `.toggle-btn` |
| Volume Control | `.volume` in the player, or `.knob` / `.slider` |
| Audio Device Select | Native `<select class="select">`; app handles permissions and device changes |
| Channel Strip | `.strip` with `.strip-section`, `.strip-fader`, `.scribble` |
| Mixer | `.mixer` containing strips; see [sound mixer](../../soundmixer.html) |
| Audio Player | `.now-playing`, `.transport`, `.scrubber`, `.volume`; see [player](../../player.html) |
| Track List | `.tracklist` and `.track`; see [media](media.md) |
| Sound Pad | `.key` buttons or `.btn`; app owns triggering, progress and hotkeys |

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

The library provides a seekable single-waveform control, not a complete audio editor. For a multitrack timeline, compose waveform clips with track labels, a time ruler, the existing transport and range controls, and `.key` mute/solo controls. The example on [audio-components.html](../../audio-components.html) shows that composition with two tracks. Keep clip positions, zoom, selection gestures, snapping, splitting, fades, and synchronization in the host app; expose playback position through a labelled native range input and label each decorative waveform with its track and time span. Use `.strip` and `.mixer` when each track also needs gain, pan and metering.

## Existing examples

- [audio-components.html](../../audio-components.html): controls, meters, spectrum sketch, device selector and trigger pads.
- [soundmixer.html](../../soundmixer.html): channel strips, EQ, input keys, gain reduction, pan, faders and meter banks.
- [player.html](../../player.html): player transport, track list, waveform seeking and volume.
- [dashboard.html](../../dashboard.html): general-purpose level meters in a data dashboard.

AudioCN is a React 19 / Tailwind v4 shadcn registry; its hooks (`useMicrophone`, `useAudioAnalyser`, mixer/player hooks and others) do not transfer to this framework-free library. See [AudioCN](https://github.com/audiocn/ui) and its [documentation](https://www.audiocn.dev/docs).
