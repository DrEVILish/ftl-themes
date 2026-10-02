/* ftl-themes: reference script for the .prefs panel and .splash intro
 * (PLAN.md §10, §12, §13). Not part of the contract: an app can render
 * the same data-* attributes on <html> server-side instead.
 *
 * Load it in <head>, after the theme stylesheet, so stored choices apply
 * before first paint. It writes each .prefs control to data-<name> on
 * <html> as it changes, stores the overrides in localStorage, and leaves
 * a setting unset (following the OS) until the user picks something.
 * A control with data-media="(media query)" starts checked when the OS
 * already asks for it; a switch with data-off="value" writes that value
 * when unchecked against the OS (e.g. transparency "default"). */
(function () {
  var html = document.documentElement, KEY = "display-prefs", prefs = {};
  var NAMES = /^(text-size|density|contrast|motion|transparency|pointer|underline-links|accent)$/;
  try { prefs = JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) {}
  try { if (sessionStorage.getItem("splash-seen")) html.setAttribute("data-splash-seen", ""); } catch (e) {}
  function os(el) { return !!el.dataset.media && matchMedia(el.dataset.media).matches; }
  function swatch(n, part) { return getComputedStyle(html).getPropertyValue("--accent-swatch-" + n + (part || "")).trim(); }
  function attr(name, v) { v ? html.setAttribute("data-" + name, v) : html.removeAttribute("data-" + name); }
  // A swatch the current theme doesn't declare is never applied.
  function apply() { for (var k in prefs) if (NAMES.test(k)) attr(k, k === "accent" && !swatch(prefs[k]) ? "" : prefs[k]); }
  function each(fn) { document.querySelectorAll(".prefs [name]").forEach(function (el) { if (NAMES.test(el.name)) fn(el); }); }
  function sync() {
    each(function (el) { el.checked = prefs[el.name] == null ? el.defaultChecked : el.value === prefs[el.name]; });
    each(function (el) { if (prefs[el.name] == null && os(el)) el.checked = true; });
  }
  function accents() {
    document.querySelectorAll("[data-prefs-accents]").forEach(function (box) {
      box.querySelectorAll("[data-swatch]").forEach(function (l) { l.remove(); });
      for (var n = 1; n <= 6; n++) if (swatch(n)) {
        var l = document.createElement("label");
        l.className = "prefs-swatch";
        l.dataset.swatch = n;
        l.style.cssText = "--swatch: var(--accent-swatch-" + n + "); --on-swatch: var(--on-accent-swatch-" + n + ")";
        l.innerHTML = '<input type="radio" name="accent" value="' + n + '"><span class="visually-hidden"></span>';
        l.lastChild.textContent = swatch(n, "-name").replace(/^["']|["']$/g, "") || "Accent " + n;
        box.appendChild(l);
      }
      box.closest(".prefs-item").hidden = !box.querySelector("[data-swatch]");
    });
    apply(); sync();
  }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(prefs)); } catch (e) {} }
  apply();
  document.addEventListener("change", function (e) {
    var el = e.target;
    if (!el.closest || !el.closest(".prefs") || !NAMES.test(el.name)) return;
    var v = el.checked ? el.value : (el.dataset.off && os(el) ? el.dataset.off : "");
    if (v) prefs[el.name] = v; else delete prefs[el.name];
    attr(el.name, v); save();
  });
  document.addEventListener("reset", function (e) {
    if (!e.target.matches(".prefs")) return;
    for (var k in prefs) attr(k, "");
    prefs = {}; save(); setTimeout(sync);
  });
  document.addEventListener("themechange", accents); // fired by theme-loader.js
  document.addEventListener("DOMContentLoaded", function () {
    accents();
    var s = document.querySelector(".splash[data-intro]:not([hidden])");
    if (s && html.hasAttribute("data-splash-seen")) s.hidden = true;
    else if (s) intro(s);
  });
  // Timed intro: hide after data-intro ("2s", "800ms"), or on any key,
  // click or tap; remembered for the session.
  function intro(s) {
    var t = parseFloat(s.dataset.intro) * (/ms$/.test(s.dataset.intro) ? 1 : 1000) || 0;
    function end() {
      s.hidden = true;
      try { sessionStorage.setItem("splash-seen", "1"); } catch (e) {}
      removeEventListener("keydown", end); removeEventListener("pointerdown", end);
    }
    html.removeAttribute("data-splash-seen");
    s.hidden = false;
    setTimeout(end, t); addEventListener("keydown", end); addEventListener("pointerdown", end);
  }
  window.playSplash = intro;
})();
