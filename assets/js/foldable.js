/* CSS owns segment detection and layout; this bridge only reflects its mode
   into an attribute for app code and forwards the optional OS posture. */
(function () {
  var html = document.documentElement;
  if (!matchMedia("(display-mode: standalone)").matches) return;
  function update() {
    var mode = getComputedStyle(html).getPropertyValue("--folding-mode").trim();
    if (mode === "book" || mode === "tabletop") html.dataset.foldMode = mode;
    else delete html.dataset.foldMode;
    var posture = navigator.devicePosture && navigator.devicePosture.type;
    if (posture) html.dataset.foldPosture = posture;
    else delete html.dataset.foldPosture;
  }
  update();
  addEventListener("resize", update, { passive: true });
  if (navigator.devicePosture && navigator.devicePosture.addEventListener)
    navigator.devicePosture.addEventListener("change", update);
})();
