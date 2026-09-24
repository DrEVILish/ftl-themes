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

  function apply(slug) {
    document.documentElement.dataset.theme = slug;
    link.href = "dist/" + slug + ".css";
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
