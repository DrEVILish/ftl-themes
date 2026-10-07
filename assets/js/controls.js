/* ftl-themes: keeps each .knob's, .fader's and .slider.is-bipolar's --value (0-1) in step with
 * its range input, which is the one thing CSS cannot read for itself: a
 * knob turns by it, and a theme can draw a fader track that fills to it.
 * Optional: an app that renders --value server-side (or has its own
 * control code) can leave this out. See CONTRACT.md "Mixing-console
 * primitives". */
(function () {
  var SEL = ".knob input, input.fader, input.is-bipolar";
  function sync(input) {
    var host = input.closest(".knob") || input;
    var min = +input.min || 0, max = input.max === "" ? 100 : +input.max;
    host.style.setProperty("--value", max > min ? ((input.value - min) / (max - min)).toFixed(4) : "0");
  }
  document.addEventListener("input", function (e) { if (e.target.matches(SEL)) sync(e.target); });
  document.querySelectorAll(SEL).forEach(sync);
})();

/* Knobs turn by dragging up and down, the way hardware-style rotaries are
 * used on touch screens and mixing desks (a native range input drags
 * sideways). Up raises the value; a full sweep is 200px, Shift for fine.
 * Anything with data-for="<range input id>" (a readout showing the value)
 * drags the same way, as does a mixer strip's [data-fader-readout] for its
 * fader. The input still gets keyboard arrows and fires "input" as usual. */
(function () {
  var SWEEP = 200;
  function targetOf(el) {
    var knob = el.closest(".knob");
    if (knob) return knob.querySelector("input[type=range]");
    var src = el.closest("[data-for], [data-fader-readout]");
    if (!src) return null;
    if (src.dataset.for) return document.getElementById(src.dataset.for);
    var strip = src.closest(".strip");
    return strip && strip.querySelector("input.fader");
  }
  document.addEventListener("pointerdown", function (e) {
    if (e.button !== 0) return;
    var input = targetOf(e.target);
    if (!input || input.disabled) return;
    var min = +input.min || 0, max = input.max === "" ? 100 : +input.max;
    if (!(max > min)) return;
    e.preventDefault();
    input.focus({ preventScroll: true });
    var step = input.step === "any" ? 0 : (+input.step || 1);
    var y0 = e.clientY, v0 = +input.value, host = e.target;
    host.setPointerCapture(e.pointerId);
    document.documentElement.classList.add("is-dragging-value");
    function move(ev) {
      var span = (max - min) * (ev.shiftKey ? 0.1 : 1);
      var v = v0 + (y0 - ev.clientY) / SWEEP * span;
      if (step) v = Math.round((v - min) / step) * step + min;
      v = Math.min(max, Math.max(min, v));
      if (v !== +input.value) {
        input.value = v;
        input.dispatchEvent(new Event("input", { bubbles: true }));
      }
    }
    function up() {
      host.removeEventListener("pointermove", move);
      host.removeEventListener("pointerup", up);
      host.removeEventListener("pointercancel", up);
      document.documentElement.classList.remove("is-dragging-value");
      input.dispatchEvent(new Event("change", { bubbles: true }));
    }
    host.addEventListener("pointermove", move);
    host.addEventListener("pointerup", up);
    host.addEventListener("pointercancel", up);
  });
})();

/* Waveform regions (docs/components/media.md): each region's two range
 * inputs are its edges, in seconds over the whole clip. This keeps
 * --start/--end (0–1) in step, keeps the edges in order with at least
 * data-min-length seconds between them (default: one step), labels each
 * edge with its time, and moves the whole region when its body is dragged
 * (not on .is-static). Both inputs fire "input" and "change" as usual.
 * A button.waveform-marker with data-time seeks the waveform's input there.
 * Over any .waveform it also sets the hover preview: --hover (0–1) and
 * data-hover-time ("m:ss", from the seek input's min and max). */
(function () {
  var SEL = ".waveform-region > input[type=range]";
  function time(s) {
    s = Math.max(0, Math.round(+s));
    return Math.floor(s / 60) + ":" + String(s % 60).padStart(2, "0");
  }
  function edges(region) { return region.querySelectorAll(":scope > input[type=range]"); }
  function sync(region, moved) {
    var e = edges(region), a = e[0], b = e[1];
    if (!a || !b) return;
    var min = +a.min || 0, max = a.max === "" ? 100 : +a.max, span = max - min || 1;
    var gap = +region.dataset.minLength || +a.step || 0;
    if (moved === a && +a.value > +b.value - gap) a.value = Math.max(min, +b.value - gap);
    if (moved === b && +b.value < +a.value + gap) b.value = Math.min(max, +a.value + gap);
    region.style.setProperty("--start", ((a.value - min) / span).toFixed(4));
    region.style.setProperty("--end", ((b.value - min) / span).toFixed(4));
    a.setAttribute("aria-valuetext", time(a.value));
    b.setAttribute("aria-valuetext", time(b.value));
  }
  document.addEventListener("input", function (e) {
    if (e.target.matches(SEL)) sync(e.target.parentElement, e.target);
  });
  document.querySelectorAll(".waveform-region").forEach(function (r) { sync(r); });
  // A marker button with data-time (seconds) seeks there.
  document.addEventListener("click", function (e) {
    var m = e.target.closest && e.target.closest("button.waveform-marker[data-time]");
    var seek = m && m.parentElement.querySelector(":scope > input[type=range]");
    if (!seek) return;
    seek.value = m.dataset.time;
    seek.dispatchEvent(new Event("input", { bubbles: true }));
    seek.dispatchEvent(new Event("change", { bubbles: true }));
  });
  // Hover preview: --hover (0–1) and data-hover-time from the seek input.
  document.addEventListener("pointermove", function (e) {
    var wf = e.target.closest && e.target.closest(".waveform");
    document.querySelectorAll(".waveform[data-hover-time]").forEach(function (w) {
      if (w !== wf) { w.style.removeProperty("--hover"); w.removeAttribute("data-hover-time"); }
    });
    var seek = wf && wf.querySelector(":scope > input[type=range]");
    if (!seek) return;
    var r = wf.getBoundingClientRect(), f = Math.min(1, Math.max(0, (e.clientX - r.left) / r.width));
    var min = +seek.min || 0, max = seek.max === "" ? 100 : +seek.max;
    wf.style.setProperty("--hover", f.toFixed(3));
    wf.setAttribute("data-hover-time", time(min + f * (max - min)));
  });
  document.addEventListener("pointerdown", function (e) {
    var region = e.target;
    if (e.button !== 0 || !region.matches(".waveform-region:not(.is-static)")) return;
    var e2 = edges(region), a = e2[0], b = e2[1];
    if (!a || !b || a.disabled) return;
    e.preventDefault();
    var min = +a.min || 0, max = a.max === "" ? 100 : +a.max;
    var perPx = (max - min) / region.getBoundingClientRect().width;
    var x0 = e.clientX, a0 = +a.value, len = b.value - a.value;
    region.setPointerCapture(e.pointerId);
    region.classList.add("is-dragging");
    function move(ev) {
      var start = Math.min(max - len, Math.max(min, a0 + (ev.clientX - x0) * perPx));
      a.value = start;
      b.value = +a.value + len;
      sync(region);
      a.dispatchEvent(new Event("input", { bubbles: true }));
      b.dispatchEvent(new Event("input", { bubbles: true }));
    }
    function up() {
      region.removeEventListener("pointermove", move);
      region.removeEventListener("pointerup", up);
      region.removeEventListener("pointercancel", up);
      region.classList.remove("is-dragging");
      a.dispatchEvent(new Event("change", { bubbles: true }));
      b.dispatchEvent(new Event("change", { bubbles: true }));
    }
    region.addEventListener("pointermove", move);
    region.addEventListener("pointerup", up);
    region.addEventListener("pointercancel", up);
  });
})();

/* Parameter controls (docs/components/audio.md): a .param's slider and
 * number input mirror each other; its .param-reset button, or a
 * double-click on a knob, fader or parameter slider, returns the control
 * to its default (the value attribute). A .slider.is-bipolar snaps to its
 * centre within 2% of it, the detent a pan control has. */
(function () {
  function set(input, v) {
    if (String(input.value) === String(v)) return;
    input.value = v;
    input.dispatchEvent(new Event("input", { bubbles: true }));
    input.dispatchEvent(new Event("change", { bubbles: true }));
  }
  document.addEventListener("input", function (e) {
    var t = e.target, param = t.closest && t.closest(".param");
    if (t.matches("input.is-bipolar")) {
      var min = +t.min || 0, max = t.max === "" ? 100 : +t.max, mid = (min + max) / 2;
      if (+t.value !== mid && Math.abs(t.value - mid) < (max - min) * 0.02) set(t, mid);
    }
    if (!param) return;
    var slider = param.querySelector("input[type=range]"), num = param.querySelector("input[type=number]");
    if (slider && num) (t === slider ? num : slider).value = t.value;
  });
  function reset(root) {
    root.querySelectorAll("input[type=range], input[type=number]").forEach(function (i) { set(i, i.defaultValue); });
  }
  document.addEventListener("click", function (e) {
    var btn = e.target.closest && e.target.closest(".param-reset");
    if (btn) reset(btn.closest(".param"));
  });
  document.addEventListener("dblclick", function (e) {
    var host = e.target.closest && e.target.closest(".knob, .param, input.fader");
    if (host && host.matches("input")) set(host, host.defaultValue);
    else if (host) reset(host);
  });
})();
