# -*- coding: utf-8 -*-
"""
Static site generator for the Maalik Creative Engineers website.
Run:  python _build/build.py     (from the project root)

One template drives all twelve capability domains, six sectors and seven service
pages, per the "do not build twelve bespoke pages" instruction in Section 4.2.
"""
import os, sys, shutil, re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import *          # noqa
from icons import icon      # noqa
from plates import plate    # noqa

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = []


# --------------------------------------------------------------------------- helpers
def rel(depth):
    return "../" * depth if depth else ""


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    PAGES.append(path)


def url(depth, target):
    """target '' -> home, 'about/leadership' -> ../about/leadership/"""
    if not target:
        return rel(depth) or "./"
    return rel(depth) + target + "/"


def tel_html(cls=""):
    """A bracketed placeholder must never become a live tel: link."""
    t = COMPANY["tel"]
    if "[" in t:
        return '<span%s>%s</span>' % (' class="%s"' % cls if cls else "", t)
    return '<a%s href="tel:%s">%s</a>' % (' class="%s"' % cls if cls else "",
                                          t.replace(" ", ""), t)


def dom_by_slug(slug):
    for d in DOMAINS:
        if d["slug"] == slug:
            return d
    return None


# --------------------------------------------------------------------------- chrome
def mega_menu(depth):
    cols = [DOMAINS[0:3], DOMAINS[3:6], DOMAINS[6:9], DOMAINS[9:12]]
    out = ['<div class="mega"><div class="wrap"><div class="mega-inner">']
    for col in cols:
        out.append('<div class="mega-col">')
        for d in col:
            out.append(
                '<a class="mega-item" href="%s"><span class="mi-top">'
                '<span class="mi-n">%s</span><span class="mi-name">%s</span></span>'
                '<span class="mi-def">%s</span></a>'
                % (url(depth, "capabilities/" + d["slug"]), d["n"], d["short"], d["def"])
            )
        out.append("</div>")
    out.append(
        '<div class="mega-col"><div class="mega-utility">%s'
        '<h4>Beyond the Catalogue</h4>'
        '<p>The portfolio here is what we supply most often. It is not the limit of what we supply.</p>'
        '<a class="tlink" href="%s">Read the method <i class="arw"></i></a></div>'
        '<div style="margin-top:22px">'
        '<a class="mega-item" href="%s"><span class="mi-top"><span class="mi-name">Full product index</span></span>'
        '<span class="mi-def">Every system across all twelve domains, filterable.</span></a>'
        '<a class="mega-item" href="%s"><span class="mi-top"><span class="mi-name">Downloads</span></span>'
        '<span class="mi-def">Corporate profile, capability statements and datasheets.</span></a>'
        '</div></div>'
        % (icon("beyond"), url(depth, "capabilities/beyond-the-catalogue"),
           url(depth, "products"), url(depth, "downloads"))
    )
    out.append("</div></div></div>")
    return "".join(out)


NAV = [
    ("capabilities", "Capabilities", True),
    ("products", "Products", False),
    ("sectors", "Sectors", False),
    ("services", "Services", False),
    ("partners", "Partners", False),
    ("about", "About", False),
]


def header(depth, active):
    r = rel(depth)
    items = []
    for slug, label, has_mega in NAV:
        cls = "nav-link active" if active == slug else "nav-link"
        chev = '<i class="chev"></i>' if has_mega else ""
        li_cls = ' class="has-mega"' if has_mega else ""
        mega = mega_menu(depth) if has_mega else ""
        items.append('<li%s><a class="%s" href="%s">%s%s</a>%s</li>'
                     % (li_cls, cls, url(depth, slug), label, chev, mega))
    return """
<div class="utility"><div class="wrap">
  <span class="u-left">%s</span>
  <a href="%s">Downloads</a><a href="%s">Careers</a><a href="%s">Insights</a><a href="%s">Search</a>
</div></div>
<header class="site-head"><div class="wrap">
  <a class="brand" href="%s" aria-label="Maalik Creative Engineers, home">
    <img src="%sassets/logo/lockup.png" alt="Maalik Creative Engineers" width="1200" height="271">
  </a>
  <nav aria-label="Primary"><ul class="nav">%s</ul></nav>
  <a class="btn-contact" href="%s">Contact</a>
  <button class="burger" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
</div></header>
""" % (COMPANY["reg_line"], url(depth, "downloads"), url(depth, "careers"),
       url(depth, "insights"), url(depth, "search"),
       url(depth, ""), r, "".join(items), url(depth, "contact"))


def mobile_nav(depth):
    r = rel(depth)
    acc = []

    def block(title, links):
        ls = "".join('<a href="%s">%s</a>' % (h, t) for t, h in links)
        return ('<div class="acc"><button class="acc-h">%s<span>+</span></button>'
                '<div class="acc-b">%s</div></div>' % (title, ls))

    acc.append(block("Capabilities",
                     [(d["short"], url(depth, "capabilities/" + d["slug"])) for d in DOMAINS]
                     + [("Beyond the Catalogue", url(depth, "capabilities/beyond-the-catalogue"))]))
    acc.append(block("Products", [("Full product index", url(depth, "products"))]
                     + [(d["short"], url(depth, "products") + "?domain=" + d["slug"]) for d in DOMAINS[:6]]))
    acc.append(block("Sectors", [(s["name"], url(depth, "sectors/" + s["slug"])) for s in SECTORS]))
    acc.append(block("Services", [(s["name"], url(depth, "services/" + s["slug"])) for s in SERVICES]))
    acc.append(block("Partners", [("Partner directory", url(depth, "partners")),
                                  ("Become a Partner", url(depth, "partners/become-a-partner"))]))
    acc.append(block("About", [("Company", url(depth, "about")),
                               ("Leadership", url(depth, "about/leadership")),
                               ("Programmes and Track Record", url(depth, "about/programmes")),
                               ("Quality and Compliance", url(depth, "about/quality")),
                               ("Facilities", url(depth, "about/facilities"))]))
    acc.append(block("More", [("Insights", url(depth, "insights")), ("Careers", url(depth, "careers")),
                              ("Downloads", url(depth, "downloads")), ("Search", url(depth, "search"))]))
    return """
<div class="mobile-nav" role="dialog" aria-label="Menu">
  <div class="mn-head">
    <img src="%sassets/logo/lockup.png" alt="Maalik Creative Engineers">
    <button class="mn-close" aria-label="Close menu">&times;</button>
  </div>
  %s
  <div style="margin-top:28px"><a class="btn btn-primary" href="%s">Submit a Requirement <i class="arw"></i></a></div>
</div>
<div class="mobile-cta"><a class="btn btn-primary" style="width:100%%;justify-content:center" href="%s">Contact <i class="arw"></i></a></div>
""" % (r, "".join(acc), url(depth, "contact/request-for-information"), url(depth, "contact"))


def footer(depth):
    r = rel(depth)
    caps = "".join('<li><a href="%s">%s</a></li>' % (url(depth, "capabilities/" + d["slug"]), d["short"])
                   for d in DOMAINS)
    caps += '<li><a href="%s">Beyond the Catalogue</a></li>' % url(depth, "capabilities/beyond-the-catalogue")
    company = [("About", "about"), ("Leadership", "about/leadership"),
               ("Programmes and Track Record", "about/programmes"),
               ("Quality and Compliance", "about/quality"), ("Facilities", "about/facilities"),
               ("Insights", "insights"), ("Careers", "careers")]
    engage = [("General Enquiry", "contact"), ("Request for Information", "contact/request-for-information"),
              ("Partnership Enquiry", "contact/partnership"), ("Support Request", "contact/support"),
              ("Downloads", "downloads")]
    co = "".join('<li><a href="%s">%s</a></li>' % (url(depth, h), t) for t, h in company)
    en = "".join('<li><a href="%s">%s</a></li>' % (url(depth, h), t) for t, h in engage)
    legal = [("Privacy Policy", "legal/privacy"), ("Terms of Use", "legal/terms"),
             ("Export Control and Compliance", "legal/export-control"),
             ("Accessibility Statement", "legal/accessibility")]
    lg = "".join('<a href="%s">%s</a>' % (url(depth, h), t) for t, h in legal)
    return """
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="%sassets/logo/stacked.png" alt="Maalik Creative Engineers">
        <p>%s</p>
        <div class="foot-reg">%s<br>Registration number: %s<br>NTN: %s</div>
      </div>
      <div class="foot-col"><h4>Capabilities</h4><ul>%s</ul></div>
      <div class="foot-col"><h4>Company</h4><ul>%s</ul></div>
      <div class="foot-col"><h4>Engage</h4><ul>%s</ul></div>
      <div class="foot-col foot-contact">
        <h4>Contact</h4>
        <p>%s</p>
        <p>%s<br>
           <a href="mailto:%s">%s</a><br>
           Tenders and RFI: <a href="mailto:%s">%s</a></p>
        <p>%s</p>
        <p><a href="%s" rel="noopener">LinkedIn</a></p>
      </div>
    </div>
  </div>
  <div class="foot-bottom"><div class="wrap">
    <span class="fb-copy">&copy; <span data-year></span> %s</span>%s
  </div></div>
</footer>
""" % (r, DESCRIPTORS["footer"], COMPANY["legal"], COMPANY["reg_no"], COMPANY["ntn"],
       caps, co, en, "<br>".join(COMPANY["address"]),
       tel_html(),
       COMPANY["email_general"], COMPANY["email_general"],
       COMPANY["email_tender"], COMPANY["email_tender"],
       COMPANY["hours"], COMPANY["linkedin"], COMPANY["legal"], lg)


def page(path, title, desc, body, active="", depth=None):
    if depth is None:
        depth = path.count("/") if path.endswith("index.html") else 0
        depth = max(0, path.count("/"))
    r = rel(depth)
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<meta name="robots" content="index,follow">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:type" content="website">
<meta property="og:image" content="%sassets/img/hero-main.jpg">
<meta name="theme-color" content="#060607">
<link rel="icon" href="%sassets/logo/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="%sassets/logo/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="%sassets/css/site.css">
</head>
<body class="has-mcta">
<a class="skip" href="#main">Skip to content</a>
%s
<main id="main" tabindex="-1">
%s
</main>
%s
%s
<script src="%sassets/js/site.js" defer></script>
</body>
</html>
""" % (title, desc, title, desc, r, r, r, r,
       header(depth, active), body, footer(depth), mobile_nav(depth), r)
    write(path, html)


# --------------------------------------------------------------------------- fragments
def hero(depth, img, eyebrow, h1, sub, ctas=None, klass="", crumb_html=""):
    cta = ""
    if ctas:
        cta = '<div class="btn-row">' + "".join(
            '<a class="btn %s" href="%s">%s <i class="arw"></i></a>' % (c[2], c[1], c[0]) for c in ctas
        ) + "</div>"
    return """
<section class="hero %s">
  <div class="hero-bg"><img src="%sassets/img/%s.jpg" alt="" fetchpriority="high"></div>
  <div class="hero-grid"></div>
  <div class="hero-inner"><div class="wrap">
    %s
    <p class="eyebrow">%s</p>
    <h1>%s</h1>
    <p class="lede">%s</p>
    %s
  </div></div>
  <div class="hero-scan"></div>
</section>""" % (klass, rel(depth), img, crumb_html, eyebrow, h1, sub, cta)


def crumb(depth, trail):
    parts = []
    for i, (label, target) in enumerate(trail):
        if target is None:
            parts.append(label)
        else:
            parts.append('<a href="%s">%s</a>' % (url(depth, target), label))
    return '<nav class="crumb" aria-label="Breadcrumb">%s</nav>' % '<span>/</span>'.join(parts)


def support_block(depth, klass=""):
    return """
<section class="section tight %s">
  <div class="wrap">
    <div class="split" style="gap:0;border:1px solid var(--line-soft);border-radius:2px">
      <div class="split-body" style="padding:48px 44px">
        <p class="eyebrow">Support and sustainment</p>
        <h2 class="rule-h" style="font-size:1.9rem">Availability is decided after delivery, not before it.</h2>
        <p class="measure" style="color:var(--text-dim);font-size:.98rem">%s</p>
        <a class="tlink" href="%s">View our services <i class="arw"></i></a>
      </div>
      <div class="split-media" style="min-height:0"><img src="%sassets/img/svc-mro.jpg" alt="Maintenance and overhaul work in progress"></div>
    </div>
  </div>
</section>""" % (klass, STANDING["support"], url(depth, "services"), rel(depth))


def cta_band(depth, img="contact-band"):
    return """
<section class="section band texture">
  <img src="%sassets/img/%s.jpg" alt="">
  <div class="wrap center" style="max-width:760px">
    <p class="eyebrow">Contact</p>
    <h2 class="rule-h">Tell us the requirement.</h2>
    <p class="lede">Send us a specification, a tender reference or a description of the operational
      problem. We will respond with a technical assessment and a route to source it.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="%s">Submit a Requirement <i class="arw"></i></a>
      <a class="btn btn-ghost" href="%s">Download Corporate Profile <i class="arw"></i></a>
    </div>
  </div>
</section>""" % (rel(depth), img, url(depth, "contact/request-for-information"), url(depth, "downloads"))


def domain_cards(depth, klass="g4", subset=None, paper=False):
    items = subset if subset else DOMAINS
    out = []
    for d in items:
        out.append(
            '<a class="card rv" href="%s">%s<span class="c-n">DOMAIN %s</span>'
            '<h3>%s</h3><p>%s</p><span class="tlink">View domain <i class="arw"></i></span></a>'
            % (url(depth, "capabilities/" + d["slug"]), icon(d["icon"]), d["n"], d["short"], d["def"])
        )
    return '<div class="grid %s gap-md">%s</div>' % (klass, "".join(out))
