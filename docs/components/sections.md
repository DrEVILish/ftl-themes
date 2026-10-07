# Page sections: marketing and app UI (v5)

Source: `core/components/sections.css`. Live examples: [`components-sections.html`](../../components-sections.html).

Headings, action panels and media objects for app pages, and the marketing
sections Tailwind Plus and Bootstrap examples are built from: feature grids,
an announcement banner, a bento grid, FAQs, a logo cloud, testimonials, a
newsletter signup, team cards, blog-card bylines, a contact list, a site
footer, and rich items for flyout and mega menus. Builds on core's
`.hero`, `.band`, `.price`, `.feature-list`, `.card.has-media`, `.avatar`,
`.grid`, `.accordion` and `[popover]` dropdowns. Nothing needs JavaScript:
the banner closes with a checkbox and the menus are popovers.

**Recipes (no new class):** a blog grid is `.grid` of `.card.has-media` with
`.post-meta`; a contact section is `.grid` with `.contact-list` beside a
form; a collapsible FAQ is `.accordion`; a hero, pricing table or call to
action is core's `.hero`, `.band`, `.price` and `.feature-list`.

Every look reads the tokens listed under each section, falling back to the
base palette; set them on `html[data-theme="x"]`.


## .page-heading — the title row at the top of a page

```html
<header class="page-heading">
  <div class="page-heading-main">
    <nav class="breadcrumbs">…</nav>
    <h1>Back end developer</h1>
    <p class="page-heading-meta"><span>Full-time</span><span>Remote</span></p>
  </div>
  <div class="page-heading-actions"><button class="btn">Edit</button>…</div>
</header> 
```

Tokens: `--page-heading-border`, `--page-heading-border-width`, `--page-heading-gap`, `--page-heading-pad`, `--section-heading-border`

## .action-panel — a titled box with one decision in it

```html
<section class="action-panel">
  <div><h3>Delete your account</h3><p>Once you delete it, it's gone.</p></div>
  <button class="btn btn-danger">Delete account</button>
</section>
```

The action sits beside the text when there is room, under it when not. .is-danger edges it in the danger colour.

Tokens: `--action-panel-bg`, `--action-panel-border`, `--action-panel-padding`

## .media-object — an image beside a body

```html
<div class="media-object"><img class="avatar" src="…" alt=""><div>…</div></div>
```

.is-center aligns the image to the body's middle, .is-reverse puts it on the far side. Nests for threaded replies.

Tokens: `--media-object-gap`

## .features — a grid of icon, title and text

```html
<ul class="features">
  <li><svg class="icon">…</svg><h3>Push to deploy</h3><p>…</p></li>
</ul>
```

Feature sections and shop incentives (free shipping, returns…). .is-centered centres each item; --features-min sets the column width.

Tokens: `--features-gap`, `--features-icon-bg`, `--features-icon-fg`, `--features-icon-size`, `--features-min`

## .banner — an announcement bar across the top or bottom

```html
<div class="banner" role="region" aria-label="Announcement">
  <p><strong>Conf 2026</strong> is on 12 June. <a href="…">Get tickets</a></p>
  <label class="btn-close"><input type="checkbox" class="banner-dismiss" aria-label="Dismiss"></label>
</div>
```

A checked .banner-dismiss hides the banner with no script (remember the choice server-side, or let the app remove it). Add .sticky-top or .fixed-bottom to pin it. .is-accent fills it with the accent.

Tokens: `--banner-bg`, `--banner-border`, `--banner-fg`, `--banner-padding`

## .bento — a mosaic of cards in a fixed grid

```html
<div class="bento"><article class="card is-wide is-tall">…</article>…</div>
```

Four columns (two on tablets, one on phones); a child spans more with .is-wide / .is-tall or --span-cols / --span-rows.

Tokens: `--bento-cols`, `--bento-gap`, `--bento-row`, `--span-cols`, `--span-rows`

## .faq — questions and answers

```html
<dl class="faq"><div><dt>How do I pay?</dt><dd>By card or invoice.</dd></div>…</dl>
```

Open by default, in two columns when there is room. For a collapsible list use .accordion (core) with the same text.

Tokens: `--faq-gap`, `--faq-min`

## .logo-cloud — a row of partner or customer logos

```html
<ul class="logo-cloud"><li><img src="acme.svg" alt="Acme"></li>…</ul>
```

Logos are muted to one tone so no brand shouts; .is-color keeps their colours. Every logo needs alt text (the company name).

Tokens: `--logo-cloud-gap`, `--logo-cloud-height`, `--logo-cloud-opacity`

## .testimonial — a quote with its author

```html
<figure class="testimonial">
  <blockquote><p>“It changed how we ship.”</p></blockquote>
  <figcaption><img class="avatar" src="…" alt=""><span><strong>Ana Ruiz</strong><span>CTO, Acme</span></span></figcaption>
</figure>
```

.is-featured makes it large and centred (a single hero quote).

Tokens: `--testimonial-bg`, `--testimonial-border`, `--testimonial-featured-padding`, `--testimonial-padding`

## .newsletter — a heading, text and an inline signup form

```html
<section class="newsletter">
  <div><h2>Stay in the loop</h2><p>One email a month.</p></div>
  <form class="newsletter-form"><label class="visually-hidden" for="nl">Email</label>
    <input class="input" id="nl" type="email" required autocomplete="email" placeholder="you@example.com">
    <button class="btn btn-primary">Subscribe</button></form>
</section>
```

Side by side when there is room, stacked when not.

## .person — a team member card

```html
<ul class="people"><li class="person"><img src="…" alt="">
  <h3>Leo Park</h3><p>Designer</p><ul class="person-links">…</ul></li></ul> 
```

Tokens: `--people-gap`, `--people-min`

## .post-meta — the byline under a blog card's title

```html
<p class="post-meta"><time datetime="2026-10-01">1 Oct 2026</time><span>6 min read</span></p> 
```

## .contact-list — ways to get in touch

```html
<dl class="contact-list"><div><dt><svg class="icon">…</svg><span class="visually-hidden">Email</span></dt>
  <dd><a href="mailto:hi@acme.dev">hi@acme.dev</a></dd></div>…</dl> 
```

Tokens: `--contact-icon-fg`

## .site-footer — the page footer with link columns

```html
<footer class="site-footer">
  <div class="site-footer-brand">…</div>
  <nav aria-label="Product"><h2>Product</h2><ul><li><a href="…">Pricing</a></li>…</ul></nav>
  …
  <div class="site-footer-bottom"><p>© 2026 Acme</p><ul class="cluster">…</ul></div>
</footer> 
```

Tokens: `--site-footer-bg`, `--site-footer-border`, `--site-footer-fg`, `--site-footer-heading-fg`, `--site-footer-link`, `--site-footer-min`, `--site-footer-padding`

## .menu-feature and .mega-menu — rich menu items

```html
<div class="dropdown mega-menu" popover id="products">
  <a class="menu-feature" href="…"><svg class="icon">…</svg>
    <span><strong>Analytics</strong><span>See where traffic comes from</span></span></a>
  …
  <div class="mega-menu-footer"><a href="…">Watch demo</a>…</div>
</div> 
```

A flyout is a core [popover] .dropdown whose items are .menu-feature links (icon, title, one line of help). A mega menu is the same popover with .mega-menu: a wide grid of them, plus an optional .mega-menu-footer.

Tokens: `--mega-menu-footer-bg`, `--mega-menu-width`, `--menu-feature-hover`
