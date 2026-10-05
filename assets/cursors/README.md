# Cursor pack format

Place optional cursor artwork at `assets/cursors/<theme>/<role>.png`. Use a
static, transparent PNG no larger than 32×32 px, with its hotspot metadata in
the theme's `--cursor-*` declarations. Keep the pointer tip inside the image.
Avoid animation; reduced motion and cursor accessibility are user-controlled.

```css
html[data-theme="windows95"] {
  --cursor-default: url("assets/cursors/windows95/arrow.png") 2 1, default;
  --cursor-text: url("assets/cursors/windows95/ibeam.png") 15 15, text;
  --cursor-not-allowed: url("assets/cursors/windows95/no.png") 15 15, not-allowed;
}
```

The final keyword is required as a native fallback. Role variables are defined
in `core/cursors.css`; themes without artwork keep OS cursors. Static PNG is
the simplest cross-browser source format; static SVG and platform formats may
be added as optional fallbacks when a pack needs them. Browsers and operating
systems may impose a smaller effective size. Cursor art is disabled in high
contrast and forced-colors modes.
