/* App-owned readiness hook for the CSS-themed boot/loading screen. */
(function () {
  var screen = document.querySelector(".splash[data-boot-screen]");
  if (!screen) return;
  var app = document.querySelector(".app-main, main");
  if (app) app.setAttribute("aria-busy", "true");
  document.addEventListener("ftl:app-ready", function () {
    if (app) app.removeAttribute("aria-busy");
    screen.hidden = true;
    document.documentElement.dataset.appReady = "";
  }, { once: true });
  window.ftlAppReady = function () {
    document.dispatchEvent(new Event("ftl:app-ready"));
  };
})();
