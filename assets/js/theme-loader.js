/* ftl-themes: shared theme-loader for the example-*.html pages.
 *
 * Not part of the library contract — a real app wires this however it
 * wants (server-rendered data-theme attribute, a cookie, whatever). This
 * is just enough to let one generic page render under any shipping theme
 * via ?theme=<slug>, for visual QA and screenshot automation.
 */
(function () {
  var params = new URLSearchParams(location.search);
  var link = document.getElementById("ftl-theme-link");
  var picker = document.getElementById("ftl-theme-picker");

  // Keeps every .ftl-icon's <use> pointed at the current theme's merged
  // icon sprite (dist/icons/<slug>.svg — generic icons plus that theme's
  // own overrides, see CONTRACT.md "Icon system"). The markup's own
  // assets/icons/icons.svg href is only the pre-JS fallback; this is what
  // actually swaps in a theme's custom icon shapes. Exposed on window so
  // a page that builds .ftl-icon markup after the fact (e.g. a demo that
  // populates an icon-pack grid from a fetch) can re-run it once its own
  // markup exists.
  function applyIcons(slug) {
    var uses = document.querySelectorAll(".ftl-icon use");
    for (var i = 0; i < uses.length; i++) {
      var use = uses[i];
      var href = use.getAttribute("href") || use.getAttribute("xlink:href") || "";
      var hash = href.indexOf("#");
      if (hash < 0) continue;
      var target = "dist/icons/" + slug + ".svg" + href.slice(hash);
      use.setAttribute("href", target);
      if (use.hasAttribute("xlink:href")) use.setAttribute("xlink:href", target);
    }
  }
  window.ftlApplyIconTheme = applyIcons;

  function apply(slug) {
    document.documentElement.dataset.theme = slug;
    link.href = "dist/" + slug + ".css";
    applyIcons(slug);
    try { localStorage.setItem("ftl-example-theme", slug); } catch (e) {}
    if (picker) picker.value = slug;
  }

  fetch("dist/themes.json").then(function (r) { return r.json(); }).then(function (list) {
    var stored;
    try { stored = localStorage.getItem("ftl-example-theme"); } catch (e) {}
    var initial = params.get("theme") || stored || list[0].slug;
    if (picker) {
      picker.innerHTML = list.map(function (t) {
        return '<option value="' + t.slug + '">' + t.label + "</option>";
      }).join("");
      picker.value = initial;
      picker.addEventListener("change", function () { apply(picker.value); });
    }
    apply(initial);
  }).catch(function () {
    apply(params.get("theme") || "aqua");
  });
})();
