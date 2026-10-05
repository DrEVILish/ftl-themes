# Media deck devices

Live example: [media-decks.html](../../media-decks.html). The page includes a reel-to-reel transport based on Pi9696's MIT-licensed SVG, plus original vinyl, portable cassette and MiniDisc illustrations.

## State contract

Put one state class on `.media-deck`:

| Class | Result |
|---|---|
| `.is-playing` | Spools/disc rotate, tape animates, play lamp lights |
| `.is-recording` | Transport animates, tape/head and lamp use danger color |
| `.is-paused` | Motion stops and the current readout remains visible |

The reel drawing, metalwork and tape use the deck tokens already defined by `blue-future`: `--deck-face`, `--deck-trim`, `--deck-hub`, `--deck-well`, `--deck-spoke`, `--deck-tape` and `--deck-shadow`. Accent, success and danger colors come from the current theme. All motion is disabled for reduced-motion preferences and `data-motion="reduced"`.

The SVGs only present transport state. Wire your own player/recorder state to the class on `.media-deck`; no audio engine is included. The example page's buttons only change the visual state.

```html
<section class="media-deck is-playing" aria-label="Tape transport">
  <!-- Inline SVG for the selected deck -->
</section>
```

## Pi9696 reference

The reel-to-reel plate, spool construction, tape route and head arrangement are adapted from [drevilish/pi9696](https://github.com/drevilish/pi9696), `remote.go`'s dashboard template. Its state model spins the reels and pulses tape while playing or recording, holds still while paused, and highlights the head red during recording. This component keeps that geometry and motion model while replacing literal blue colors with this library's theme tokens. Copyright and MIT license terms are in [`THIRD_PARTY_NOTICES.md`](../../THIRD_PARTY_NOTICES.md).
