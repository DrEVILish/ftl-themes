/* ftl-themes: the theme-tint control for the demo pages.
 *
 * A theme whose themes.json entry carries `tint: {token, default, label}`
 * has a user-chosen colour (CONTRACT.md "Theme tint"), e.g. Windows 7's
 * Window Color. This puts a colour input beside the theme picker for such
 * a theme, sets the token inline on <html>, and remembers it per theme.
 * Choosing a preset sub-theme clears the custom colour so the preset
 * shows. ?tint=%23rrggbb sets it for screenshots. A real app wires the
 * same three steps into its own appearance settings.
 */
(function () {
  var html = document.documentElement;
  var input = null, entry = null, applied = null;
  var hex = /^#[0-9a-f]{6}$/i;
  function key(slug) { return "example-tint:" + slug; }
  function store(slug, v) { try { v ? localStorage.setItem(key(slug), v) : localStorage.removeItem(key(slug)); } catch (e) {} }
  function stored(slug) { try { return localStorage.getItem(key(slug)); } catch (e) { return null; } }
  function set(token, v) {
    if (applied) html.style.removeProperty(applied);
    applied = v ? token : null;
    if (v) html.style.setProperty(token, v);
  }
  // Show what's in effect: the custom colour, else the preset/default the
  // stylesheet declares (read once it has loaded).
  function showValue() {
    if (!input || !entry || !entry.tint) return;
    var v = getComputedStyle(html).getPropertyValue(entry.tint.token).trim();
    input.value = hex.test(v) ? v : entry.tint.default;
  }

  // picker: the theme <select>; theme: the themes.json entry now applied;
  // presetChanged: true when the user just picked a different sub-theme.
  window.themeTint = function (picker, theme, presetChanged) {
    entry = theme;
    var t = theme && theme.tint;
    if (!input && picker) {
      input = document.createElement("input");
      input.type = "color";
      input.className = "tint-picker";
      picker.insertAdjacentElement("afterend", input);
      input.addEventListener("input", function () {
        if (!entry || !entry.tint) return;
        set(entry.tint.token, input.value);
        store(entry.slug, input.value);
      });
      var link = document.getElementById("theme-link");
      if (link) link.addEventListener("load", showValue);
    }
    if (input) {
      input.hidden = !t;
      if (t) input.title = input.ariaLabel = t.label || "Theme tint";
    }
    if (!t) { set(null, null); return; }
    if (presetChanged) store(theme.slug, null);
    var v = new URLSearchParams(location.search).get("tint") || stored(theme.slug);
    set(t.token, v && hex.test(v) ? v : null);
    showValue();
  };
})();
