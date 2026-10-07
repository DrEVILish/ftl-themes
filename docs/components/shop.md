# Shop: products, cart, checkout and orders (v5)

Source: `core/components/shop.css`. Live examples: [`components-shop.html`](../../components-shop.html).

Product cards and grids, a category filter rail, a product page with a
gallery, read-only stars and review summaries, choice cards for delivery
and payment, cart lines, an order summary and order history. Builds on
core's `.card`, `.price`, `.badge`, `.badge-button`, `.btn`, `.check`,
`.progress`, `.stretched-link` and `.drawer`, and the forms group's
`.stepper`, `.swatches`, `.rating` and floating labels. Nothing needs
JavaScript; stock, totals, payment and validation are the app's.

**Recipes:** checkout is core `ol.steps` + `.field.is-floating` fields in an
`.is-validated` form + `.choice-cards` + `.order-summary` in a
`.shop-layout.is-summary`; incentives are `.features.is-centered`
(sections.css); on phones put `.filters` in a `.drawer`.

Every look reads the tokens listed under each section, falling back to the
base palette; set them on `html[data-theme="x"]`.


## .product-grid and .product — a product card

```html
<ul class="product-grid">
  <li class="product">
    <img src="…" alt="Basic tee in black">
    <h3><a href="…" class="stretched-link">Basic tee</a></h3>
    <p class="product-meta">Black</p>
    <p class="price is-sm">$35</p>
  </li>
</ul>
```

The image is square (--product-ratio), the whole card is one link via core's .stretched-link, and a .badge in the card sits on the image.

Tokens: `--product-gap`, `--product-image-bg`, `--product-min`, `--product-radius`, `--product-ratio`

## Sale and small prices, on core's `.price`

```html
<p class="price is-sm"><span class="price-sale">$18</span> <span class="price-was">$24</span></p>
```

`.price.is-sm` sizes a plan's big figure down for cards and cart lines; `.price-was` is the struck-through old price, `.price-sale` the new one in the danger colour. Say "was $24" in text for screen readers if the strike-through carries meaning.

## .stars — a read-only star rating

```html
<span class="stars" style="--rating: 4.5" role="img" aria-label="4.5 out of 5 stars"></span>
```

Five glyphs filled to --rating (0–5) in --stars-fg. A theme can swap the glyph with --stars-glyph. For a rating the user sets, use .rating.

Tokens: `--rating`, `--stars-empty`, `--stars-fg`, `--stars-glyph`, `--stars-size`

## .review-summary and .review

```html
<div class="review-summary">
  <p><span class="stars" style="--rating:4.2" role="img" aria-label="4.2 out of 5"></span> Based on 1,624 reviews</p>
  <dl><div><dt>5 stars</dt><dd><progress class="progress" max="100" value="63"></progress> 63%</dd></div>…</dl>
</div>
<article class="review"><header>…avatar, name, stars, date…</header><p>…</p></article> 
```

## .product-detail and .product-gallery

```html
<div class="product-detail">
  <div class="product-gallery">
    <img src="front.jpg" alt="…">
    <div class="product-thumbs" role="radiogroup" aria-label="Images">…radio labels with thumbnails…</div>
  </div>
  <div class="product-info"><h1>…</h1><p class="price">…</p>…options…<button class="btn btn-primary">Add to bag</button></div>
</div>
```

Gallery and info sit side by side from tablet width. The thumbnails are .toggle-btn-style radios; the app (or a CSS :has() rule per image) swaps the main image.

Tokens: `--product-detail-gap`, `--product-image-bg`, `--product-radius`, `--product-ratio`

## .choice-card — a radio or checkbox drawn as a card

```html
<div class="choice-cards" role="radiogroup" aria-label="Delivery">
  <label class="choice-card"><input type="radio" name="d" value="std" checked>
    <span><strong>Standard</strong><span>4–10 business days</span></span><span class="choice-card-aside">$5.00</span></label>
</div> 
```

Delivery methods, payment options, plans.

Tokens: `--choice-card-bg`, `--choice-card-border`, `--choice-card-border-width`, `--choice-card-checked`, `--choice-card-min`, `--choice-card-padding`, `--choice-card-radius`

## .filters — a category filter rail

```html
<form class="filters" aria-label="Filters">
  <details open><summary>Colour</summary>
    <label class="check"><input type="checkbox" name="c" value="white"> White</label>…
  </details>…
</form>
```

Each group collapses; checked filters can repeat above the results as .badge-button chips. On phones put the form in a core .drawer.

## .cart-line — one line in a cart or order

```html
<ul class="cart"><li class="cart-line">
  <img src="…" alt="">
  <div><h3><a href="…">Basic tee</a></h3><p class="product-meta">Black · L</p></div>
  <div class="stepper">…</div>
  <p class="price is-sm">$35</p>
  <button class="btn-close" aria-label="Remove Basic tee"></button>
</li></ul> 
```

Tokens: `--cart-image`, `--product-image-bg`

## .order-summary — line totals with a grand total

```html
<section class="order-summary" aria-labelledby="sum"><h2 id="sum">Order summary</h2>
  <dl><div><dt>Subtotal</dt><dd>$99.00</dd></div>…<div class="is-total"><dt>Total</dt><dd>$112.32</dd></div></dl>
  <button class="btn btn-primary">Checkout</button></section> 
```

Tokens: `--order-summary-bg`, `--order-summary-padding`

## .order — one past order in an order history

```html
<article class="order">
  <header class="order-header">
    <dl><div><dt>Order number</dt><dd>WU88191111</dd></div><div><dt>Date placed</dt><dd><time …>Jan 6, 2026</time></dd></div>…</dl>
    <div class="cluster"><a class="btn btn-sm" href="…">View order</a></div>
  </header>
  <ul class="cart">…cart-lines without steppers…</ul>
</article> 
```

Tokens: `--order-bg`, `--order-border`

## .shop-layout — filters beside results, or a form beside its summary

Two columns from tablet width, one on phones. .is-summary puts a narrower column (an .order-summary) at the end instead of the start.

Tokens: `--shop-layout-gap`
