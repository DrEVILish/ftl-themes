/* ftl-themes: keeps each .knob's and .fader's --value (0-1) in step with
 * its range input, which is the one thing CSS cannot read for itself: a
 * knob turns by it, and a theme can draw a fader track that fills to it.
 * Optional: an app that renders --value server-side (or has its own
 * control code) can leave this out. See CONTRACT.md "Mixing-console
 * primitives". */
(function () {
  var SEL = ".knob input, input.fader";
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
