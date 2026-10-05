/* Optional PWA enhancement. CSS keeps segment geometry; JS exposes posture
   metadata to themes and apps that need to choose a fold-aware layout. */
(function () {
  var html = document.documentElement;
  if (!matchMedia("(display-mode: standalone)").matches) return;
  function update() {
    var segments = window.viewport && window.viewport.segments;
    if (!segments || segments.length < 2) {
      delete html.dataset.foldMode;
      delete html.dataset.foldPosture;
      return;
    }
    var a = segments[0], b = segments[1];
    var mode = Math.abs(a.left - b.left) > Math.abs(a.top - b.top) ? "book" : "tabletop";
    html.dataset.foldMode = mode;
    html.dataset.foldPosture = navigator.devicePosture && navigator.devicePosture.type || "unknown";
  }
  update();
  addEventListener("resize", update, { passive: true });
  if (navigator.devicePosture && navigator.devicePosture.addEventListener)
    navigator.devicePosture.addEventListener("change", update);
})();
