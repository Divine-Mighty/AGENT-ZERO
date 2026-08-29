#!/usr/bin/env python3
"""WATCHERS(R) site build -> watchers-site.html

Single file out, every image base64-inlined. PIECES below is the only product
source of truth; never edit watchers-site.html directly, it is an artifact and
gets overwritten.

    python3 wing2.py   # regenerate wing_frag.svg first, if the wing changed
    python3 build.py

Layout follows the MotionSites "Obsidian" composition: one non-scrolling
fullscreen stage, overlaid nav, headline block top-left, two staggered cards
bottom-right, floating labels, a vertical scroll cue, and a full-screen menu
overlay.
"""

import base64
import hashlib
import html
import math
import os

OUT = "watchers-site.html"
WING = "wing_frag.svg"

# --------------------------------------------------------------------------
# Product data. Sold out is permanent; a new run gets a new slug.
# --------------------------------------------------------------------------

PIECES = [
    dict(
        slug="wraith-hood-01",
        name="Wraith Hood",
        cat="outerwear",
        price=180,
        label="DROP 04",
        blurb="Heavyweight loopback hood, boxed shoulder, raw-cut placket. "
              "Screen print pulled by hand in Darwin.",
        alt="Heavyweight bone-on-black hooded sweatshirt, boxed shoulder, "
            "raw-cut placket.",
        sold_out=False,
        feature=1,
    ),
    dict(
        slug="static-tee-03",
        name="Static Tee",
        cat="tee",
        price=75,
        label="VAULT",
        blurb="240gsm carded cotton. Front lifted from a dead channel, "
              "back panel carries the full lockup.",
        alt="Boxy bone-on-black t-shirt with a broken television static "
            "print across the chest.",
        sold_out=False,
        feature=2,
    ),
    dict(
        slug="nightwatch-cargo",
        name="Nightwatch Cargo",
        cat="outerwear",
        price=210,
        label="DROP 04",
        blurb="Ripstop cargo, articulated knee, bellows pocket. Cut for "
              "standing still for a long time.",
        alt="Black ripstop cargo trousers with bellows pockets and an "
            "articulated knee.",
        sold_out=False,
    ),
    dict(
        slug="no-witness-tee",
        name="No Witness Tee",
        cat="tee",
        price=75,
        label="DROP 03",
        blurb="Sixty made. All sixty gone. Kept here for the record.",
        alt="Boxy black t-shirt with a bone dripping eye print at centre "
            "chest.",
        sold_out=True,
    ),
    dict(
        slug="blind-spot-cap",
        name="Blind Spot Cap",
        cat="headwear",
        price=60,
        label="DROP 04",
        blurb="Unstructured six-panel, bone stitch on black twill, "
              "brass closure.",
        alt="Unstructured black six-panel cap with bone embroidery above "
            "the brim.",
        sold_out=False,
    ),
    dict(
        slug="evidence-tote",
        name="Evidence Tote",
        cat="accessory",
        price=45,
        label="DROP 03",
        blurb="16oz canvas, gusseted base, numbered panel. The number is "
              "yours and is not reissued.",
        alt="Black heavyweight canvas tote bag with a numbered bone print "
            "panel.",
        sold_out=True,
    ),
]

# --------------------------------------------------------------------------
# Generated card art.
#
# Placeholder plates, not photography. They are deterministic per slug so the
# build is reproducible. Swap plate_svg() for real lookbook shots when the
# per-product photography lands.
# --------------------------------------------------------------------------


def seed_of(slug):
    return int(hashlib.sha256(slug.encode()).hexdigest()[:12], 16)


def plate_svg(piece):
    """An abstract print-plate: halftone field, registration marks, grain."""
    s = seed_of(piece["slug"])
    size, grid = 600, 22
    step = size / grid

    ax = 0.4 + ((s >> 3) % 100) / 90.0
    ay = 0.4 + ((s >> 11) % 100) / 90.0
    ph = ((s >> 19) % 628) / 100.0
    cx = 120 + ((s >> 27) % 360)
    cy = 120 + ((s >> 35) % 360)

    dots = []
    for r in range(grid):
        for c in range(grid):
            x = (c + 0.5) * step
            y = (r + 0.5) * step
            # smooth field, pinched toward a seeded focal point
            f = (math.sin(ax * c * 0.42 + ph) * math.cos(ay * r * 0.38 + ph))
            d = math.hypot(x - cx, y - cy) / size
            rad = (0.55 + 0.45 * f) * step * 0.46 * (1.0 - 0.55 * d)
            if rad < 0.35:
                continue
            dots.append(
                '<circle cx="{:.1f}" cy="{:.1f}" r="{:.2f}"/>'.format(
                    x, y, rad))

    scans = "".join(
        '<rect x="0" y="{}" width="{}" height="1"/>'.format(y, size)
        for y in range(0, size, 4))

    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" '
        'width="{size}" height="{size}">'
        '<defs>'
        '<radialGradient id="g" cx="{gx:.3f}" cy="{gy:.3f}" r="0.75">'
        '<stop offset="0" stop-color="#E9DFC8" stop-opacity=".30"/>'
        '<stop offset="1" stop-color="#E9DFC8" stop-opacity="0"/>'
        '</radialGradient>'
        '<filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" '
        'numOctaves="3" seed="{seed}"/>'
        '<feColorMatrix type="saturate" values="0"/></filter>'
        '</defs>'
        '<rect width="{size}" height="{size}" fill="#111112"/>'
        '<rect width="{size}" height="{size}" fill="url(#g)"/>'
        '<g fill="#E9DFC8" opacity=".42">{dots}</g>'
        '<g fill="#060607" opacity=".35">{scans}</g>'
        '<g stroke="#E9DFC8" stroke-width="1" opacity=".55" fill="none">'
        '<path d="M{cx:.0f} {cy0:.0f}V{cy1:.0f}M{cx0:.0f} {cy:.0f}H{cx1:.0f}"/>'
        '<circle cx="{cx:.0f}" cy="{cy:.0f}" r="26"/>'
        '</g>'
        '<rect width="{size}" height="{size}" filter="url(#n)" '
        'opacity=".14"/>'
        '</svg>'
    ).format(size=size, seed=s % 9973, dots="".join(dots), scans=scans,
             gx=cx / size, gy=cy / size, cx=cx, cy=cy,
             cy0=cy - 54, cy1=cy + 54, cx0=cx - 54, cx1=cx + 54)


def data_uri(svg):
    return "data:image/svg+xml;base64," + base64.b64encode(
        svg.encode("utf-8")).decode("ascii")


def load_wing():
    if not os.path.exists(WING):
        raise SystemExit(
            "missing {}: run `python3 wing2.py` first".format(WING))
    with open(WING) as fh:
        return fh.read()


# --------------------------------------------------------------------------
# Mark. PLACEHOLDER: the real blackletter W + WATCHERS lockup with the drip
# has not been supplied to this repo. Drop the supplied asset in and replace
# this function; do not re-letter the wordmark by hand.
# --------------------------------------------------------------------------

MARK = (
    '<svg class="mark" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.4" stroke-linejoin="round" aria-hidden="true" '
    'focusable="false">'
    '<path d="M1.8 11.6C5 7 8.6 4.7 12 4.7s7 2.3 10.2 6.9c-3.2 4.6-6.8 6.9'
    '-10.2 6.9S5 16.2 1.8 11.6Z"/>'
    '<circle cx="12" cy="11.6" r="2.9" fill="currentColor" stroke="none"/>'
    '<path d="M12 18.9c0 0-1.3 2.2-1.3 3.1a1.3 1.3 0 0 0 2.6 0c0-.9-1.3-3.1'
    '-1.3-3.1Z" fill="currentColor" stroke="none"/>'
    '</svg>'
)

NAV_LINKS = [("Drops", "#drops"), ("Vault", "#vault"), ("Contact", "#contact")]


# --------------------------------------------------------------------------
# Page
# --------------------------------------------------------------------------

FONTS = ("https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600"
         "&family=JetBrains+Mono:wght@400;500&family=Pirata+One&display=swap")

ICON = ('<svg class="ico" width="14" height="14" viewBox="0 0 24 24" '
        'fill="none" stroke="currentColor" stroke-width="1.5" '
        'aria-hidden="true"><path d="M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4z'
        'M14 14h6v6h-6z"/></svg>')

CSS = """
:root{
  --void:#0A0A0A; --ink:#060607; --panel:#111112;
  --bone:#E9DFC8; --bone-dim:#8C8676; --bone-faint:#5A564C;
  --alarm:#B3261E; --line:rgba(233,223,200,.10);
  --pad:20px;
}
@media (min-width:640px){ :root{ --pad:24px } }
@media (min-width:768px){ :root{ --pad:48px } }

*,*::before,*::after{ box-sizing:border-box }
html,body{ margin:0; height:100% }
body{
  background:var(--void); color:var(--bone); overflow:hidden;
  font-family:Archivo,system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing:antialiased;
}
a{ color:inherit }
button{ font:inherit; color:inherit; background:none; border:0; cursor:pointer }
:focus-visible{ outline:2px solid var(--bone); outline-offset:3px }

.mono{
  font-family:'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,monospace;
  text-transform:uppercase; font-size:10px; letter-spacing:.18em;
  font-weight:500;
}
.skip{
  position:absolute; left:-9999px; top:0; z-index:100;
  background:var(--panel); padding:12px 18px; border:1px solid var(--line);
}
.skip:focus{ left:12px; top:12px }

/* ---------- stage ---------- */
.stage{
  position:relative; display:flex; flex-direction:column;
  height:100dvh; min-height:540px; width:100%; overflow:hidden;
}
.bg{ position:absolute; inset:0; pointer-events:none }
.wings{
  position:absolute; left:50%; top:48%; width:min(1480px,152vw);
  transform:translate(-50%,-50%); color:var(--bone); opacity:.16;
  animation:breathe 9s ease-in-out infinite;
}
.wings svg{ display:block; width:100%; height:auto }
@keyframes breathe{
  0%,100%{ transform:translate(-50%,-50%) scale(1) }
  50%    { transform:translate(-50%,-50%) scale(1.035) }
}
.scan{
  position:absolute; inset:0; opacity:.5;
  background:repeating-linear-gradient(180deg,
    rgba(233,223,200,.045) 0 1px, transparent 1px 3px);
}
.vig{
  position:absolute; inset:0;
  background:radial-gradient(ellipse at 50% 44%, transparent 28%,
    var(--void) 88%);
}

/* ---------- nav ---------- */
.nav{
  position:relative; z-index:10; display:flex; align-items:center;
  justify-content:space-between; gap:16px; padding:20px var(--pad);
}
@media (min-width:768px){ .nav{ padding:24px var(--pad) } }
.nav-l,.nav-r{ display:flex; align-items:center; gap:28px }
.nav-r{ gap:18px }
.brand{ display:flex; align-items:center; gap:10px; text-decoration:none }
.mark{ width:24px; height:24px; display:block }
.wordmark{ letter-spacing:.28em; font-size:11px }
.nav-links{ display:none; gap:24px }
@media (min-width:768px){ .nav-links{ display:flex } }
.nav-links a{
  text-decoration:none; color:rgba(233,223,200,.7); transition:color .3s;
}
.nav-links a:hover,.nav-links a[aria-current]{ color:var(--bone) }
.enter{ display:none }
@media (min-width:768px){ .enter{ display:inline-flex } }
.burger{ display:flex; padding:6px; margin:-6px }

/* ---------- main ---------- */
.main{ position:relative; flex:1; min-height:0; padding:0 var(--pad) }
.hero{ padding-top:16px; max-width:512px }
@media (min-width:640px){ .hero{ padding-top:32px } }
@media (min-width:768px){ .hero{ padding-top:64px } }
.hero h1{
  margin:0; font-family:'Pirata One',serif; font-weight:400;
  font-size:30px; line-height:.95; letter-spacing:-.005em;
}
@media (min-width:640px){ .hero h1{ font-size:36px } }
@media (min-width:768px){ .hero h1{ font-size:60px } }
@media (min-width:1024px){ .hero h1{ font-size:72px } }
.hero p{
  margin:18px 0 0; max-width:320px; font-size:12px; line-height:1.65;
  color:rgba(233,223,200,.6);
}
@media (min-width:640px){ .hero p{ font-size:14px } }
@media (min-width:768px){ .hero p{ font-size:16px } }
.cta{
  display:inline-flex; align-items:center; gap:10px; margin-top:24px;
  padding:10px 20px; border:1px solid rgba(233,223,200,.3);
  border-radius:999px; transition:background .3s ease-out;
}
@media (min-width:640px){ .cta{ padding:12px 24px } }
.cta:hover{ background:rgba(233,223,200,.1) }

/* ---------- cards ---------- */
.cards{
  position:absolute; right:var(--pad); bottom:24px; display:grid;
  grid-template-columns:repeat(2,auto); gap:12px;
}
@media (min-width:640px){ .cards{ bottom:32px; gap:16px } }
@media (min-width:768px){ .cards{ bottom:48px; gap:20px } }
.card{
  position:relative; width:144px; aspect-ratio:1; border-radius:12px;
  overflow:hidden; display:flex; flex-direction:column;
  justify-content:flex-end; text-align:left; padding:0;
  background:var(--panel); border:1px solid var(--line);
}
@media (max-width:400px){ .card{ width:126px } }
@media (min-width:640px){ .card{ width:176px; border-radius:16px } }
@media (min-width:768px){ .card{ width:208px } }
@media (min-width:1024px){ .card{ width:240px } }
.card-a{ grid-column:1; grid-row:1; align-self:end }
.card-b{ grid-column:2; grid-row:2 }
.card img{
  position:absolute; inset:0; width:100%; height:100%; object-fit:cover;
  filter:grayscale(1); transition:filter .5s, transform .7s ease-out;
}
.card:hover img,.card:focus-visible img{ filter:grayscale(0); transform:scale(1.05) }
.card .veil{
  position:absolute; inset:0;
  background:linear-gradient(to top, rgba(0,0,0,.6), rgba(0,0,0,.2) 55%,
    transparent);
}
.card .body{ position:relative; padding:12px 40px 12px 12px }
.card .lab{ display:block; color:rgba(233,223,200,.6) }
@media (min-width:640px){ .card .lab{ font-size:11px } }
.card .ttl{ display:block; margin:4px 0 0; font-weight:600; font-size:14px;
  line-height:1.2 }
@media (min-width:640px){ .card .ttl{ font-size:16px } }
@media (min-width:768px){ .card-a .ttl{ font-size:18px } }
.card-b .ttl{ font-size:16px }
@media (min-width:640px){ .card-b .ttl{ font-size:20px } }
@media (min-width:768px){ .card-b .ttl{ font-size:24px } }
.card>.ico{ position:absolute; right:12px; bottom:12px; color:rgba(233,223,200,.7) }
.card .out{ color:var(--alarm); margin-top:6px; display:block }

/* ---------- floating labels + cue ---------- */
.floats{ display:none }
@media (min-width:1024px){ .floats{ display:block } }
.float{
  position:absolute; display:flex; align-items:center; gap:8px;
  color:rgba(233,223,200,.5);
}
.float .dot{ width:5px; height:5px; border-radius:50%; background:var(--bone) }
.float .dot.live{ background:var(--alarm); animation:rec 1.6s steps(1) infinite }
@keyframes rec{ 0%,55%{ opacity:1 } 56%,100%{ opacity:.15 } }
.f1{ top:20%; left:43% }
.f2{ top:62%; left:calc(50% - 44px) }
.cue{ position:absolute; left:50%; bottom:32px; transform:translateX(-50%); display:none }
@media (min-width:768px){ .cue{ display:block } }
.cue span{
  writing-mode:vertical-rl; transform:rotate(180deg);
  letter-spacing:.3em; color:rgba(233,223,200,.4);
}

/* ---------- overlays ---------- */
.menu{
  position:fixed; inset:0; z-index:50; background:rgba(6,6,7,.9);
  backdrop-filter:blur(24px); -webkit-backdrop-filter:blur(24px);
  opacity:0; pointer-events:none; transition:opacity .5s;
}
.menu.open{ opacity:1; pointer-events:auto }
.menu-in{
  height:100%; display:flex; flex-direction:column;
  transform:translateY(-32px); transition:transform .5s ease-out;
}
.menu.open .menu-in{ transform:none }
.menu-head{
  display:flex; align-items:center; justify-content:space-between;
  padding:20px var(--pad);
}
@media (min-width:768px){ .menu-head{ padding:24px var(--pad) } }
.menu-nav{ padding:0 var(--pad); flex:1 }
.menu-nav a{
  display:block; padding:18px 0; border-bottom:1px solid var(--line);
  font-family:'Pirata One',serif; font-size:36px; font-weight:400;
  text-decoration:none; opacity:0; transform:translateY(-8px);
  transition:opacity .4s ease-out, transform .4s ease-out;
}
.menu.open .menu-nav a{ opacity:1; transform:none }
.menu-foot{
  padding:24px var(--pad); color:rgba(233,223,200,.4);
  opacity:0; transition:opacity .4s ease-out .45s;
}
.menu.open .menu-foot{ opacity:1 }

.modal{
  position:fixed; inset:0; z-index:60; display:grid; place-items:center;
  padding:20px; background:rgba(6,6,7,.86); backdrop-filter:blur(18px);
  -webkit-backdrop-filter:blur(18px);
  opacity:0; pointer-events:none; transition:opacity .35s;
}
.modal.open{ opacity:1; pointer-events:auto }
.sheet{
  width:min(560px,100%); max-height:calc(100dvh - 40px); overflow:auto;
  background:var(--panel); border:1px solid var(--line); border-radius:16px;
  transform:translateY(12px) scale(.985);
  transition:transform .45s cubic-bezier(.2,.8,.2,1);
}
.modal.open .sheet{ transform:none }
.sheet img{ display:block; width:100%; aspect-ratio:16/10; object-fit:cover }
.sheet .in{ padding:22px }
.sheet h2{
  margin:0; font-family:'Pirata One',serif; font-weight:400; font-size:34px;
  line-height:1;
}
.sheet .meta{ display:flex; gap:16px; margin-top:10px; color:var(--bone-dim) }
.sheet .out{ color:var(--alarm) }
.sheet p{ margin:16px 0 0; color:var(--bone-dim); font-size:14px; line-height:1.7 }
.sheet .act{
  display:flex; gap:10px; margin-top:22px; flex-wrap:wrap;
}
.sheet .act button{
  border:1px solid rgba(233,223,200,.3); border-radius:999px;
  padding:12px 24px; transition:background .3s ease-out;
}
.sheet .act button:hover{ background:rgba(233,223,200,.1) }
.close{ padding:8px; margin:-8px }

@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{
    animation-duration:.001ms !important; animation-iteration-count:1 !important;
    transition-duration:.001ms !important;
  }
  .wings{ animation:none }
  .menu-nav a,.menu-foot{ opacity:1; transform:none }
}
"""


JS = r"""
(function(){
  var PIECES = __DATA__;
  var menu   = document.getElementById('menu');
  var burger = document.getElementById('burger');
  var modal  = document.getElementById('modal');
  var sheet  = {
    img:   document.getElementById('m-img'),
    name:  document.getElementById('m-name'),
    price: document.getElementById('m-price'),
    label: document.getElementById('m-label'),
    state: document.getElementById('m-state'),
    blurb: document.getElementById('m-blurb'),
    buy:   document.getElementById('m-buy')
  };
  var lastFocus = null;

  function setMenu(open){
    menu.classList.toggle('open', open);
    menu.setAttribute('aria-hidden', open ? 'false' : 'true');
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    if(open){ var a = menu.querySelector('.menu-nav a'); if(a) a.focus(); }
    else burger.focus();
  }

  burger.addEventListener('click', function(){
    setMenu(!menu.classList.contains('open'));
  });
  menu.querySelectorAll('[data-close]').forEach(function(el){
    el.addEventListener('click', function(){ setMenu(false); });
  });

  function openPiece(slug, push){
    var p = PIECES[slug];
    if(!p) return;
    lastFocus = document.activeElement;
    sheet.img.src = p.img;
    sheet.img.alt = p.alt;
    sheet.name.textContent  = p.name;
    sheet.price.textContent = 'A$' + p.price;
    sheet.label.textContent = p.label;
    sheet.state.textContent = p.sold_out ? 'Sold out' : 'In stock';
    sheet.state.className   = p.sold_out ? 'mono out' : 'mono';
    sheet.blurb.textContent = p.blurb;
    sheet.buy.textContent   = p.sold_out ? 'Notify me' : 'Add to bag';
    sheet.buy.dataset.slug  = slug;
    modal.classList.add('open');
    modal.setAttribute('aria-hidden','false');
    setMenu(false);
    if(push) history.pushState({piece:slug}, '', '?piece=' + slug);
    sheet.buy.focus();
  }

  function closePiece(push){
    modal.classList.remove('open');
    modal.setAttribute('aria-hidden','true');
    if(push) history.pushState({}, '', location.pathname);
    if(lastFocus) lastFocus.focus();
  }

  document.querySelectorAll('[data-piece]').forEach(function(el){
    el.addEventListener('click', function(){
      openPiece(el.dataset.piece, true);
    });
  });
  modal.addEventListener('click', function(e){
    if(e.target === modal) closePiece(true);   // backdrop
  });
  modal.querySelector('[data-close-btn]').addEventListener('click', function(){
    closePiece(true);
  });

  sheet.buy.addEventListener('click', function(){
    var p = PIECES[sheet.buy.dataset.slug];
    sheet.buy.textContent = p && p.sold_out ? 'On the list' : 'Added';
  });

  document.addEventListener('keydown', function(e){
    if(e.key !== 'Escape') return;
    if(modal.classList.contains('open')) closePiece(true);
    else if(menu.classList.contains('open')) setMenu(false);
  });

  // every piece is addressable at ?piece=<slug>; opening one cold must open
  // the modal on mount, and popstate closes it
  window.addEventListener('popstate', function(){
    if(modal.classList.contains('open')) closePiece(false);
  });
  var slug = new URLSearchParams(location.search).get('piece');
  if(slug) openPiece(slug, false);
})();
"""


def esc(text):
    return html.escape(str(text), quote=True)


def card_html(piece, slot, uri):
    tag = ('<span class="mono out">Sold out</span>' if piece["sold_out"]
           else "")
    return (
        '<button class="card card-{slot}" data-piece="{slug}" '
        'aria-label="{name}, A${price}. Open details.">'
        '<img src="{uri}" alt="{alt}" decoding="async">'
        '<span class="veil"></span>'
        '<span class="body">'
        '<span class="mono lab">{label}</span>'
        '<span class="ttl">{title}</span>{tag}'
        '</span>{icon}</button>'
    ).format(slot=slot, slug=esc(piece["slug"]), name=esc(piece["name"]),
             price=piece["price"], uri=uri, alt=esc(piece["alt"]),
             label=esc(piece["label"]), title=esc(piece["name"]), tag=tag,
             icon=ICON)


def build():
    import json

    uris = {p["slug"]: data_uri(plate_svg(p)) for p in PIECES}
    featured = sorted((p for p in PIECES if p.get("feature")),
                      key=lambda p: p["feature"])[:2]

    data = {p["slug"]: dict(name=p["name"], price=p["price"],
                            label=p["label"], blurb=p["blurb"], alt=p["alt"],
                            cat=p["cat"], sold_out=p["sold_out"],
                            img=uris[p["slug"]])
            for p in PIECES}

    nav = "".join(
        '<a class="mono" href="{}">{}</a>'.format(href, esc(text))
        for text, href in NAV_LINKS)

    menu_links = "".join(
        '<a href="{href}" style="transition-delay:{d}ms" data-close>{t}</a>'
        .format(href=href, t=esc(text), d=150 + 75 * i)
        for i, (text, href) in enumerate(NAV_LINKS + [("Enter", "#drops")]))

    cards = (card_html(featured[0], "a", uris[featured[0]["slug"]])
             + card_html(featured[1], "b", uris[featured[1]["slug"]]))

    page = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>WATCHERS&reg; &mdash; Watch everything. Trust no one.</title>
<meta name="description" content="WATCHERS. Drop-based streetwear. No seasons, no restocks. Ships from Darwin, NT.">
<meta property="og:title" content="WATCHERS&reg;">
<meta property="og:description" content="Watch everything. Trust no one.">
<meta name="theme-color" content="#0A0A0A">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="__FONTS__">
<style>__CSS__</style>
</head>
<body>
<a class="skip mono" href="#main">Skip to content</a>

<div class="stage">
  <div class="bg" aria-hidden="true">
    <div class="wings">__WINGS__</div>
    <div class="scan"></div>
    <div class="vig"></div>
  </div>

  <header class="nav">
    <div class="nav-l">
      <a class="brand" href="/" aria-label="WATCHERS home">
        __MARK__<span class="mono wordmark">Watchers</span>
      </a>
      <nav class="nav-links" aria-label="Primary">__NAV__</nav>
    </div>
    <div class="nav-r">
      <a class="mono enter" href="#drops">Enter</a>
      <button class="burger" id="burger" aria-expanded="false"
              aria-controls="menu" aria-label="Open menu">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
             stroke="currentColor" stroke-width="1.5" aria-hidden="true">
          <path d="M3 7h18M3 12h18M3 17h18"/>
        </svg>
      </button>
    </div>
  </header>

  <main class="main" id="main">
    <div class="hero">
      <h1>Watch everything.<br>Trust no one.</h1>
      <p>Drop-based. No seasons, no restocks. When it is gone it stays gone.</p>
      <button class="cta mono" data-piece="__LEAD__">
        View the drop __ICON__
      </button>
    </div>

    __CARDS__

    <div class="floats" aria-hidden="true">
      <span class="float f1"><span class="dot live"></span>
        <span class="mono">Drop 04 / live</span></span>
      <span class="float f2"><span class="dot"></span>
        <span class="mono">Vault / 67&#37; claimed</span></span>
    </div>

    <div class="cue" aria-hidden="true"><span class="mono">Scroll</span></div>
  </main>
</div>

<div class="menu" id="menu" aria-hidden="true">
  <div class="menu-in">
    <div class="menu-head">
      <a class="brand" href="/" aria-label="WATCHERS home">
        __MARK__<span class="mono wordmark">Watchers</span>
      </a>
      <button class="close" data-close aria-label="Close menu">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
             stroke="currentColor" stroke-width="1.5" aria-hidden="true">
          <path d="M6 6l12 12M18 6L6 18"/>
        </svg>
      </button>
    </div>
    <nav class="menu-nav" aria-label="Menu">__MENU__</nav>
    <p class="menu-foot mono">Ships from Darwin, NT. Est. 2024.</p>
  </div>
</div>

<div class="modal" id="modal" role="dialog" aria-modal="true"
     aria-labelledby="m-name" aria-hidden="true" data-close>
  <div class="sheet">
    <img id="m-img" src="" alt="" loading="lazy" decoding="async">
    <div class="in">
      <h2 id="m-name"></h2>
      <div class="meta">
        <span class="mono" id="m-price"></span>
        <span class="mono" id="m-label"></span>
        <span class="mono" id="m-state"></span>
      </div>
      <p id="m-blurb"></p>
      <div class="act">
        <button class="mono" id="m-buy"></button>
        <button class="mono" data-close-btn>Close</button>
      </div>
    </div>
  </div>
</div>

<script>__JS__</script>
</body>
</html>
"""
    js = JS.replace("__DATA__", json.dumps(data, separators=(",", ":")))
    page = (page
            .replace("__FONTS__", FONTS)
            .replace("__CSS__", CSS)
            .replace("__WINGS__", load_wing())
            .replace("__MARK__", MARK)
            .replace("__NAV__", nav)
            .replace("__MENU__", menu_links)
            .replace("__CARDS__", '<div class="cards">' + cards + "</div>")
            .replace("__LEAD__", featured[0]["slug"])
            .replace("__ICON__", ICON)
            .replace("__JS__", js))
    return page


if __name__ == "__main__":
    out = build()
    with open(OUT, "w") as fh:
        fh.write(out)
    print("{}  {:,} bytes  {} pieces".format(OUT, len(out), len(PIECES)))
