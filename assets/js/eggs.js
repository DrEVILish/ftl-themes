/* ftl-themes: easter eggs (PLAN.md §20) — a reference snippet, not part of
 * the library contract (like window.js and prefs.js).
 *
 * Off unless the page opts in with <html data-easter-eggs>; an app should
 * offer a switch for it. This only sets data attributes; each theme draws
 * its own eggs in CSS, listed in its README:
 *   - the Konami code toggles data-alert="red" (every theme);
 *   - a textarea starting "Dear" gets data-egg-letter (Windows 95);
 *   - a minute without input sets data-egg-idle on <html> (Matrix rain);
 *   - every tenth failed form check sets data-egg-knee for 6s (Skyrim).
 * Nothing blocks input, and any key or pointer move clears the idle egg. */
(function () {
  var html = document.documentElement;
  if (!html.hasAttribute("data-easter-eggs")) return;
  var konami = "arrowup arrowup arrowdown arrowdown arrowleft arrowright arrowleft arrowright b a", keys = [];
  addEventListener("keydown", function (e) {
    keys = keys.concat(String(e.key).toLowerCase()).slice(-10);
    if (keys.join(" ") !== konami) return;
    if (html.dataset.alert === "red") delete html.dataset.alert; else html.dataset.alert = "red";
  });
  addEventListener("input", function (e) {
    if (e.target.matches && e.target.matches("textarea")) e.target.toggleAttribute("data-egg-letter", /^\s*dear\b/i.test(e.target.value));
  });
  var idle;
  function wake() {
    html.removeAttribute("data-egg-idle");
    clearTimeout(idle);
    idle = setTimeout(function () { html.setAttribute("data-egg-idle", ""); }, 60000);
  }
  ["keydown", "pointermove", "pointerdown", "wheel", "scroll"].forEach(function (t) { addEventListener(t, wake, { capture: true, passive: true }); });
  wake();
  var errors = 0, knee;
  addEventListener("invalid", function () {
    if (++errors % 10) return;
    html.setAttribute("data-egg-knee", "");
    clearTimeout(knee);
    knee = setTimeout(function () { html.removeAttribute("data-egg-knee"); }, 6000);
  }, true);
})();
