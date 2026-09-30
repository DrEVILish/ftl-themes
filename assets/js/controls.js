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
    host.style.setProperty("--value", ((input.value - min) / (max - min)).toFixed(4));
  }
  document.addEventListener("input", function (e) { if (e.target.matches(SEL)) sync(e.target); });
  document.querySelectorAll(SEL).forEach(sync);
})();
