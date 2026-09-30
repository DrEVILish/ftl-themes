/* ftl-themes: keeps each .knob's --value (0-1) in step with its range
 * input, which is the one thing CSS cannot read for itself. Optional: an
 * app that renders --value server-side (or has its own control code) can
 * leave this out. See CONTRACT.md "Mixing-console primitives". */
(function () {
  function sync(input) {
    var knob = input.closest(".knob");
    if (!knob) return;
    var min = +input.min || 0, max = input.max === "" ? 100 : +input.max;
    knob.style.setProperty("--value", ((input.value - min) / (max - min)).toFixed(4));
  }
  document.addEventListener("input", function (e) { if (e.target.matches(".knob input")) sync(e.target); });
  document.querySelectorAll(".knob input").forEach(sync);
})();
