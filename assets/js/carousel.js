/* ftl-themes: carousel navigation without the page jump — a reference
 * snippet, not part of the library contract (like window.js).
 *
 * .carousel-nav links are plain #slide fragment links, so the carousel works
 * with no JS. But following a fragment scrolls every ancestor to bring the
 * slide to the top of the screen, so clicking a dot also yanks the page.
 * This scrolls only the carousel, sideways: dots go to their slide,
 * .carousel-prev/.carousel-next step one slide from wherever it is, and the
 * dot for the slide in view gets aria-current="true". */
(function () {
  function carouselFor(nav) {
    var c = nav.previousElementSibling;
    return c && c.matches(".carousel") ? c : nav.parentElement.querySelector(".carousel");
  }
  function current(c) { return Math.round(c.scrollLeft / c.clientWidth); }
  function mark(c, nav) {
    var slide = c.children[current(c)];
    nav.querySelectorAll("a:not(.carousel-prev):not(.carousel-next)").forEach(function (a) {
      if (a.hash.slice(1) === (slide && slide.id)) a.setAttribute("aria-current", "true");
      else a.removeAttribute("aria-current");
    });
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest(".carousel-nav a[href^='#']");
    if (!a) return;
    var nav = a.closest(".carousel-nav"), c = carouselFor(nav);
    if (!c) return;
    e.preventDefault();
    var step = a.matches(".carousel-prev") ? -1 : a.matches(".carousel-next") ? 1 : 0;
    var n = c.children.length, i = step ? (current(c) + step + n) % n
      : Array.prototype.indexOf.call(c.children, document.getElementById(a.hash.slice(1)));
    if (i < 0) return;
    c.scrollTo({ left: c.scrollLeft + c.children[i].getBoundingClientRect().left - c.getBoundingClientRect().left });
  });
  document.querySelectorAll(".carousel-nav").forEach(function (nav) {
    var c = carouselFor(nav);
    if (!c) return;
    var t;
    c.addEventListener("scroll", function () { clearTimeout(t); t = setTimeout(function () { mark(c, nav); }, 80); });
    mark(c, nav);
  });
})();
