/* ftl-themes: shared theme-loader for the demo pages.
 *
 * Not part of the library contract — a real app wires this however it
 * wants (server-rendered data-theme attribute, a cookie, whatever). This
 * is just enough to let one generic page render under any shipping theme
 * via ?theme=<slug>, for visual QA and screenshot automation.
 */
(function () {
  var params = new URLSearchParams(location.search);
  var link = document.getElementById("theme-link");
  var picker = document.getElementById("theme-picker");
  var known = null; // slugs from dist/themes.json; null until it loads
  var entries = {}; // slug -> themes.json entry

  // Keeps every .icon's <use> pointed at the current theme's merged
  // icon sprite (dist/icons/<slug>.svg — generic icons plus that theme's
  // own overrides, see CONTRACT.md "Icon system"). The markup's own
  // assets/icons/icons.svg href is only the pre-JS fallback; this is what
  // actually swaps in a theme's custom icon shapes. Exposed on window so
  // a page that builds .icon markup after the fact (e.g. a demo that
  // populates an icon-pack grid from a fetch) can re-run it once its own
  // markup exists.
  function applyIcons(slug) {
    var uses = document.querySelectorAll(".icon use");
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
  window.applyIconTheme = applyIcons;

  // The tab icon and home-screen icon follow the theme
  // (dist/favicons/<slug>.svg and -180.png, built by build_favicons.py).
  function setIcon(rel, href, type) {
    var l = document.querySelector('link[rel="' + rel + '"]');
    if (!l) { l = document.createElement("link"); l.rel = rel; document.head.appendChild(l); }
    if (type) l.type = type;
    l.href = href;
  }

  // A slug is only ever spliced into a path, so accept nothing but a
  // known theme name: ?theme=../x or a stale localStorage value must not
  // become a stylesheet URL.
  function valid(slug) {
    if (typeof slug !== "string" || !/^[a-z0-9]+(-[a-z0-9]+)*$/.test(slug)) return false;
    return known === null || known.indexOf(slug) !== -1;
  }

  // `persist` is true only for a choice the user made in the picker. A
  // theme that came from ?theme= (the gallery's iframes, screenshot
  // automation) must not overwrite the stored preference.
  // A picker value is "slug" or "slug:variant" (CONTRACT.md "Palette
  // variants"); the variant only ever lands in a data attribute, but is
  // held to the same charset as a slug anyway.
  function apply(value, persist) {
    var before = document.documentElement.dataset.theme + ":" + (document.documentElement.dataset.variant || "");
    var parts = String(value).split(":");
    var slug = parts[0], variant = parts[1];
    document.documentElement.dataset.theme = slug;
    if (variant && /^[a-z0-9-]+$/.test(variant)) document.documentElement.dataset.variant = variant;
    else delete document.documentElement.dataset.variant;
    // Resolves once the new stylesheet has loaded (so a view transition
    // captures the finished theme), then announces it for prefs.js.
    var href = "dist/" + slug + ".css";
    var ready = new Promise(function (done) {
      if (!link || link.getAttribute("href") === href) return done();
      link.addEventListener("load", done, { once: true });
      link.addEventListener("error", done, { once: true });
      setTimeout(done, 3000);
      link.href = href;
    }).then(function () { document.dispatchEvent(new CustomEvent("themechange")); });
    applyIcons(slug);
    setIcon("icon", "dist/favicons/" + slug + ".svg", "image/svg+xml");
    setIcon("apple-touch-icon", "dist/favicons/" + slug + "-180.png");
    // Links between the demo pages carry the theme along, so a theme that
    // arrived via ?theme= (not persisted) survives the click.
    var query = "?theme=" + slug + (document.documentElement.dataset.variant ? "&variant=" + variant : "");
    var demoLinks = document.querySelectorAll("a[data-demo-link]");
    for (var i = 0; i < demoLinks.length; i++) {
      demoLinks[i].href = demoLinks[i].getAttribute("href").split("?")[0] + query;
    }
    if (persist) {
      try { localStorage.setItem("example-theme", value); } catch (e) {}
    }
    if (picker) picker.value = value;
    // Theme tint (CONTRACT.md "Theme tint"): a user-picked sub-theme
    // replaces any custom colour; a load from storage/URL keeps it.
    if (window.themeTint) window.themeTint(picker, entries[slug], persist && before !== slug + ":" + (variant || ""));
    return ready;
  }

  // A user's switch cross-fades through a view transition (PLAN.md §11);
  // a theme styles its entrance with ::view-transition-new(root). Instant
  // without the API, or under reduced motion (OS or data-motion), unless
  // the user chose data-motion="full".
  function switchTheme(value) {
    var motion = document.documentElement.dataset.motion;
    var still = !document.startViewTransition || motion === "reduced" || motion === "none" ||
      (motion !== "full" && matchMedia("(prefers-reduced-motion: reduce)").matches);
    if (still) return apply(value, true);
    document.startViewTransition(function () { return apply(value, true); });
  }

  fetch("dist/themes.json").then(function (r) {
    if (!r.ok) throw new Error("themes.json " + r.status);
    return r.json();
  }).then(function (list) {
    if (!list.length) throw new Error("themes.json is empty");
    known = list.map(function (t) { entries[t.slug] = t; return t.slug; });
    var stored;
    try { stored = localStorage.getItem("example-theme"); } catch (e) {}
    var wanted = params.get("theme") && params.get("variant") ? params.get("theme") + ":" + params.get("variant") : params.get("theme");
    // Page default (its own data-theme) before the first theme alphabetically.
    var initial = [wanted, stored, document.documentElement.dataset.theme, known[0]].filter(function (v) { return v && valid(String(v).split(":")[0]); })[0];
    if (picker) {
      picker.textContent = "";
      list.forEach(function (t) {
        var o = document.createElement("option");
        o.value = t.slug;
        o.textContent = t.label;
        picker.appendChild(o);
        (t.variants || []).forEach(function (v) {
          var vo = document.createElement("option");
          vo.value = t.slug + ":" + v.id;
          vo.textContent = t.label + " — " + v.label;
          picker.appendChild(vo);
        });
      });
      picker.addEventListener("change", function () { switchTheme(picker.value); });
    }
    apply(initial, false);
  }).catch(function () {
    var wanted = params.get("theme");
    apply(valid(wanted) ? wanted : "aqua", false);
  });
})();
