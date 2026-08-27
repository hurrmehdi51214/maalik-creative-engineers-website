# -*- coding: utf-8 -*-
"""Page builders: home, capabilities, domain template, products, sectors."""
from build import *   # noqa  (core helpers, data, icons)


# =========================================================================== HOME
def build_home():
    d = 0
    stats = [("15", "Years in operation since 2010"),
             ("12", "Capability domains covered"),
             ("20+", "International OEM and technology partners"),
             ("13", "Programme categories delivered")]
    stat_html = "".join(
        '<div class="stat"><div class="fig">%s</div><div class="lbl">%s</div></div>' % s for s in stats)

    pillars = "".join(
        '<div class="card rv"><span class="c-n">%s</span><h3>%s</h3>'
        '<p class="pill-head">%s</p><p>%s</p></div>'
        % (n, name, head, body) for name, head, body, n in PILLARS)

    sectors = "".join(
        '<a class="spanel" href="%s"><img src="%sassets/img/%s.jpg" alt="" loading="lazy">'
        '<div class="spanel-in"><div class="sp-n">SECTOR %02d</div><h3>%s</h3><p>%s</p></div></a>'
        % (url(d, "sectors/" + s["slug"]), rel(d), s["img"], i + 1, s["name"], s["line"])
        for i, s in enumerate(SECTORS))

    rail = "".join(
        '<div class="step"><div class="dot"></div><div class="sn">%s</div><h4>%s</h4><p>%s</p></div>'
        % st for st in DELIVERY)

    featured = [p for p in PARTNERS if p.get("featured")] + [p for p in PARTNERS if not p.get("featured")]
    wall = logo_wall(d, featured[:15])

    insights = "".join(
        '<a class="card rv" href="%s"><span class="c-n">TECHNICAL BRIEF</span><h3>%s</h3>'
        '<p>Written for an evaluator making a selection decision, not for a marketing audience.</p>'
        '<span class="tlink">Read the brief <i class="arw"></i></span></a>'
        % (url(d, "insights"), t) for t in BRIEF_TOPICS[:3])

    body = (
        hero(d, "land-terrain", "Defence and advanced technology solutions",
             "From stated requirement<br>to sustained capability.", DESCRIPTORS["hero_sub"],
             [("Explore Capabilities", url(d, "capabilities"), "btn-primary"),
              ("Submit a Requirement", url(d, "contact/request-for-information"), "btn-ghost")])
        + '<section class="stats"><div class="wrap">%s</div></section>' % stat_html
        + """
<section class="section texture">
  <div class="wrap">
    <div class="sec-head" style="max-width:900px">
      <p class="eyebrow">Capabilities</p>
      <h2 class="rule-h">Twelve domains.<br>One point of accountability.</h2>
      <p class="lede">Most requirements do not stop at a single piece of equipment. They cross
        communications, sensing, analysis and support. We hold all of them under one contract and one
        project manager.</p>
    </div>
    """ + domain_cards(d) + """
    <div class="btn-row"><a class="btn btn-ghost" href="%s">View the full product index <i class="arw"></i></a></div>
  </div>
</section>

<section class="section band texture">
  <img src="%sassets/img/beyond-catalogue.jpg" alt="" loading="lazy">
  <div class="wrap">
    <div style="max-width:830px">
      <p class="eyebrow">Beyond the Catalogue</p>
      <h2 class="rule-h">If it exists in the technology sector, we can structure it, source it and deliver it.</h2>
      <p class="lede">The portfolio on this site is what we supply most often. It is not the limit of what we
        supply. Our value is the ability to take a requirement that does not yet have a catalogue entry,
        identify the right manufacturer anywhere in the world, qualify them technically and commercially,
        and bring the resulting capability into service in Pakistan with full documentation and support.
        If your requirement is not listed here, that is the conversation we most want to have.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="%s">Discuss a non-standard requirement <i class="arw"></i></a>
        <a class="btn btn-ghost" href="%s">Read the method <i class="arw"></i></a>
      </div>
    </div>
  </div>
</section>

<section class="section ink2">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Why we are selected</p>
      <h2 class="rule-h">Four things a customer is actually buying.</h2></div>
    <div class="grid g4 gap-md">%s</div>
  </div>
</section>

<section class="section" style="padding-bottom:0">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Sectors served</p>
      <h2 class="rule-h">The same portfolio, cut the way you think about it.</h2>
      <p class="lede">An officer thinks in terms of their own service and mission, not in terms of a
        supplier taxonomy. These pages re-cut the portfolio by customer.</p></div>
  </div>
  <div>%s</div>
</section>

<section class="section paper">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">The delivery model</p>
      <h2 class="rule-h">From stated requirement to sustained capability.</h2>
      <p class="lede">We think in programme terms, not transactional ones. Every requirement runs through
        the same six stages, with one accountable project manager across all of them.</p></div>
    <div class="rail">%s</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head" style="max-width:880px">
      <p class="eyebrow">Partner network</p>
      <h2 class="rule-h">We do not resell. We represent.</h2>
      <p class="lede">Our manufacturing relationships are direct, current and contractual. Every system we
        offer comes with a named manufacturer, a documented authorisation and a factory-level support
        route.</p>
    </div>
    %s
    <div class="btn-row"><a class="btn btn-ghost" href="%s">View the partner network <i class="arw"></i></a></div>
  </div>
</section>

<section class="section ink2">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Insights</p>
      <h2 class="rule-h">Technical briefs, not press releases.</h2>
      <p class="lede">One brief a month, authored and attributed to a named engineer, written to help an
        evaluator make a decision.</p></div>
    <div class="grid g3 gap-md">%s</div>
    <div class="btn-row"><a class="btn btn-ghost" href="%s">All insights <i class="arw"></i></a></div>
  </div>
</section>
""" % (url(d, "products"), rel(d), url(d, "contact/request-for-information"),
       url(d, "capabilities/beyond-the-catalogue"), pillars, sectors, rail, wall,
       url(d, "partners"), insights, url(d, "insights"))
        + cta_band(d))

    page("index.html", "Maalik Creative Engineers | Defence and Security Technology",
         "Defence, security and advanced technology solutions for the Pakistan Armed Forces. "
         "Supply, integration and through-life support.", body, active="", depth=0)


# =========================================================================== CAPABILITIES INDEX
def build_capabilities_index():
    d = 1
    body = (
        hero(d, "dom-isr", "Capabilities", "Twelve domains.<br>One point of accountability.",
             "Most requirements do not stop at a single piece of equipment. They cross communications, "
             "sensing, analysis and support. We hold all of them under one contract and one project "
             "manager.",
             [("View the product index", url(d, "products"), "btn-primary")], "short",
             crumb(d, [("Home", ""), ("Capabilities", None)]))
        + """
<section class="section">
  <div class="wrap">
    <div class="sec-head" style="max-width:880px">
      <p class="eyebrow">The taxonomy</p>
      <h2 class="rule-h">Every system we supply has one primary home.</h2>
      <p class="lede">Twelve domains, each with its own product families and named systems. Items that
        serve more than one domain are cross-listed rather than duplicated, so a search returns one
        answer rather than four.</p>
    </div>
    """ + domain_cards(d) + """
  </div>
</section>

<section class="section band texture">
  <img src="%sassets/img/beyond-catalogue.jpg" alt="" loading="lazy">
  <div class="wrap"><div style="max-width:790px">
    <p class="eyebrow">Not a numbered domain</p>
    <h2 class="rule-h">Beyond the Catalogue</h2>
    <p class="lede">This is not a category, it is a statement of operating model: the ability to source,
      qualify and deliver technology that does not yet have a supplier in Pakistan. A significant share
      of our work begins there.</p>
    <div class="btn-row"><a class="btn btn-primary" href="%s">Read the method <i class="arw"></i></a></div>
  </div></div>
</section>
""" % (rel(d), url(d, "capabilities/beyond-the-catalogue"))
        + support_block(d, "ink2") + cta_band(d))

    page("capabilities/index.html", "Defence Capabilities | Maalik Creative Engineers",
         "Twelve capability domains from tactical communications and optronics to unmanned systems, "
         "air defence, cyber security and AI.", body, active="capabilities", depth=1)


# =========================================================================== DOMAIN TEMPLATE
def build_domain(dm):
    d = 2
    overview = "".join("<p>%s</p>" % p for p in dm["overview"])
    glance = "".join('<div><span class="gn">%02d</span>%s</div>' % (i + 1, g)
                     for i, g in enumerate(dm["glance"]))

    fimgs = FAMILY_IMAGES.get(dm["slug"], {})
    fam_bits = []
    for i, (name, blurb, place) in enumerate(dm["families"]):
        stem = fimgs.get(i)
        if stem:
            media = ('<div class="icard-img is-shot"><img src="%sassets/img/products/%s.jpg" '
                     'alt="%s" loading="lazy" width="1000" height="750">'
                     '<span class="icard-tag">%s</span></div>' % (rel(d), stem, name, place))
        else:
            media = ('<div class="icard-img is-plate">%s<span class="icard-tag">%s</span></div>'
                     % (plate(dm["slug"] + "|" + name, dm["icon"],
                              "DOMAIN %s / %02d" % (dm["n"], i + 1)), place))
        fam_bits.append(
            '<a class="icard rv" href="%s">%s'
            '<div class="icard-body"><h3>%s</h3><p>%s</p>'
            '<span class="tlink">Enquire about this family <i class="arw"></i></span></div></a>'
            % (url(d, "contact/request-for-information"), media, name, blurb))
    fams = "".join(fam_bits)

    feat = FEATURED.get(dm["slug"], [])
    feat_block = ""
    if feat:
        cells = "".join(
            '<figure class="shot rv"><img src="%sassets/img/products/%s.jpg" alt="%s" '
            'loading="lazy" width="1000" height="750">'
            '<figcaption><span class="mono">%s</span><span>%s</span></figcaption></figure>'
            % (rel(d), stem, cap, desig, cap) for stem, desig, cap in feat)
        feat_block = ('<section class="section tight"><div class="wrap">'
                      '<div class="sec-head"><p class="eyebrow">Featured systems</p>'
                      '<h2 class="rule-h">Manufacturer photography.</h2>'
                      '<p class="lede">Supplied by the manufacturer. Performance parameters are '
                      'released only through a verified datasheet request.</p></div>'
                      '<div class="grid g3 gap-md">%s</div></div></section>' % cells)

    if dm["models"]:
        rows = []
        for i, (desig, cls, place) in enumerate(dm["models"]):
            extra = ' class="extra hide"' if i >= 10 else ""
            badge = ('<span class="badge pp">%s</span>' % place if place == "PP"
                     else '<span class="badge">%s</span>' % place)
            rows.append('<tr%s><td class="desig">%s</td><td>%s</td><td>%s</td></tr>'
                        % (extra, desig, cls, badge))
        more = ""
        if len(dm["models"]) > 10:
            more = ('<div class="btn-row"><button class="btn btn-ghost btn-sm" data-expand="#models" '
                    'data-label="Show all %d systems"><span>Show all %d systems</span> '
                    '<i class="arw"></i></button></div>' % (len(dm["models"]), len(dm["models"])))
        models_block = """
<section class="section ink2">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Named systems and models</p>
      <h2 class="rule-h">What is available in this domain today.</h2>
      <p class="lede">Model designations are the manufacturer's own. Performance parameters are not
        published here; they sit behind a verified datasheet request.</p></div>
    <div class="tbl-wrap" id="models"><table class="spec">
      <thead><tr><th>Designation</th><th>Class and application</th><th>Page type</th></tr></thead>
      <tbody>%s</tbody></table></div>
    %s
    <p class="mono" style="color:var(--text-faint);margin-top:20px">PP = individual product page &nbsp;&middot;&nbsp;
      FP = product family page &nbsp;&middot;&nbsp; CP = listed on this capability page</p>
  </div>
</section>""" % ("".join(rows), more)
    else:
        models_block = """
<section class="section ink2">
  <div class="wrap"><div class="note" style="max-width:840px">
    <h4>Systems in this domain are described by class and role only</h4>
    <p>Copy here is strictly functional. We publish class, role and position within an architecture.
      Engagement envelopes, ranges, altitudes, warhead and guidance data, quantities held and deployment
      locations are not published. All technical detail sits behind the controlled datasheet request
      workflow and is released only to verified enquirers.</p>
  </div></div>
</section>"""

    rel_doms = [dom_by_slug(s) for s in dm["related"] if dom_by_slug(s)]
    rel_cards = domain_cards(d, "g3", rel_doms)
    partners_here = [p for p in PARTNERS if dm["slug"] in p["domains"]]
    pblock = ""
    if partners_here:
        pwall = logo_wall(d, partners_here)
        pblock = """
<section class="section">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Manufacturers in this domain</p>
      <h2 class="rule-h">Named, current and contractual.</h2>
      <p class="lede">Each relationship carries a documented authorisation and a factory-level support
        route. Country of origin is published because it determines the export licensing path.</p></div>
    %s
  </div>
</section>""" % pwall

    restricted = ""
    if dm.get("restricted"):
        restricted = ('<div class="note" style="margin-top:34px;max-width:780px">'
                      '<h4>Export control and end use</h4><p>Systems in this domain are supplied only to '
                      'authorised end users, against end-user documentation where the manufacturer or '
                      'country of origin requires it, and in compliance with the export control regime of '
                      'the country of origin. A lawful, documented route is confirmed before any '
                      'commitment is offered.</p></div>')

    body = (
        hero(d, dm["img"], "Domain %s" % dm["n"], dm["name"], dm["hero"],
             [("Discuss a requirement", url(d, "contact/request-for-information"), "btn-primary"),
              ("Request a capability statement", url(d, "downloads"), "btn-ghost")],
             "short", crumb(d, [("Home", ""), ("Capabilities", "capabilities"), (dm["short"], None)]))
        + """
<section class="section">
  <div class="wrap"><div style="max-width:780px">
    <p class="eyebrow">Domain overview</p>
    <h2 class="rule-h">%s</h2>
    <div class="measure" style="color:var(--text-dim)">%s</div>
    %s
  </div></div>
</section>

<div class="wrap"><div class="glance">%s</div></div>

<section class="section">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Product families</p>
      <h2 class="rule-h">What this domain contains.</h2>
      <p class="lede">%d product families. Where a specific model is offered it is named in the systems
        table below, so that this view stays scannable.</p></div>
    <div class="grid g3 gap-md">%s</div>
  </div>
</section>
%s
%s
<section class="section">
  <div class="wrap"><div class="split" style="border:1px solid var(--line-soft);border-radius:2px">
    <div class="split-body">
      <p class="eyebrow">Integration</p>
      <h2 class="rule-h" style="font-size:1.85rem">This domain does not work alone.</h2>
      <p style="color:var(--text-dim)">%s</p>
      <p style="color:var(--text-dim);font-size:.95rem">Systems here connect most often to %s.
        We design and deliver those connections as part of the same programme.</p>
      <div class="chips" style="margin-top:10px">%s</div>
    </div>
    <div class="split-media"><img src="%sassets/img/dom-c3.jpg" alt="" loading="lazy"></div>
  </div></div>
</section>
""" % (dm["hero"], overview, restricted, glance, len(dm["families"]), fams, feat_block, models_block,
       STANDING["integration"],
       ", ".join(x["short"] for x in rel_doms),
       "".join('<a class="chip" href="%s">%s</a>' % (url(d, "capabilities/" + x["slug"]), x["short"])
               for x in rel_doms),
       rel(d))
        + support_block(d) + pblock
        + """
<section class="section ink2">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Related domains</p>
      <h2 class="rule-h">Where evaluators usually go next.</h2></div>
    %s
  </div>
</section>

<section class="section band texture">
  <img src="%sassets/img/%s.jpg" alt="" loading="lazy">
  <div class="wrap center" style="max-width:740px">
    <p class="eyebrow">Enquiry</p>
    <h2 class="rule-h">Discuss a %s requirement.</h2>
    <p class="lede">Send a specification, a tender reference or a description of the operational problem.
      We acknowledge every enquiry within one working day.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="%s">Submit a Requirement <i class="arw"></i></a>
      <a class="btn btn-ghost" href="%s">Browse the product index <i class="arw"></i></a>
    </div>
  </div>
</section>
""" % (rel_cards, rel(d), dm["img"], strip_tags(dm["short"]).lower(),
       url(d, "contact/request-for-information"), url(d, "products")))

    page("capabilities/%s/index.html" % dm["slug"], dm["meta_title"], dm["meta_desc"],
         body, active="capabilities", depth=2)


# =========================================================================== BEYOND THE CATALOGUE
def build_beyond():
    d = 2
    steps = "".join('<li><h4>%s</h4><p>%s</p></li>' % s for s in METHOD)
    reach = "".join('<div class="chip" style="cursor:default">%s</div>' % s for s in SECTOR_REACH)
    examples = [
        ("A sensing requirement with no local supplier",
         "The operational effect was achievable with a sensor class the customer had not specified. "
         "We identified three candidate manufacturers, qualified two, and delivered against the effect "
         "rather than the assumed equipment."),
        ("An obsolete sub-assembly on an in-service platform",
         "The original manufacturer had exited the line. We identified an adjacent manufacturer able to "
         "produce to the drawing, qualified the output and brought the item back into supply."),
        ("A specialist material for a production programme",
         "The requirement sat outside defence entirely. We located a qualified mill, established the "
         "export licensing position and structured the supply against the production schedule."),
    ]
    ex_html = "".join('<div class="card rv"><span class="c-n">EXAMPLE %02d</span><h3>%s</h3><p>%s</p></div>'
                      % (i + 1, t, b) for i, (t, b) in enumerate(examples))

    body = (
        hero(d, "beyond-catalogue", "Beyond the Catalogue",
             "The requirement that is not<br>in anyone&rsquo;s catalogue.",
             "Sourcing, qualifying and delivering technology that does not yet have a supplier in Pakistan.",
             [("Send us a requirement we have never seen before",
               url(d, "contact/request-for-information"), "btn-primary")], "short",
             crumb(d, [("Home", ""), ("Capabilities", "capabilities"), ("Beyond the Catalogue", None)]))
        + """
<section class="section">
  <div class="wrap"><div style="max-width:800px">
    <p class="eyebrow">The premise</p>
    <h2 class="rule-h">A catalogue describes what a company has already sold.</h2>
    <p class="lede">It says very little about what a company can do. A significant share of our work
      begins with a requirement for which no local supplier exists, no obvious manufacturer is identified,
      and no precedent has been set. That is not an exception to our business. It is the part of it that
      our customers value most.</p>
  </div></div>
</section>

<section class="section paper">
  <div class="wrap">
    <div class="sec-head" style="max-width:800px"><p class="eyebrow">The method</p>
      <h2 class="rule-h">Six steps, applied the same way every time.</h2>
      <p class="lede">This is a described, repeatable process rather than a claim. Each step has an output
        the customer can see before the next one starts.</p></div>
    <ol class="numlist">%s</ol>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">What we have sourced this way</p>
      <h2 class="rule-h">Anonymised, and deliberately so.</h2>
      <p class="lede">Class of requirement and outcome only. No customer identification, no quantities,
        no locations. Further detail is available to qualified enquirers subject to customer clearance.</p></div>
    <div class="grid g3 gap-md">%s</div>
  </div>
</section>

<section class="section ink2">
  <div class="wrap">
    <div class="sec-head" style="max-width:820px"><p class="eyebrow">Sector reach</p>
      <h2 class="rule-h">We operate across the technology sector, not only defence.</h2>
      <p class="lede">The sourcing, qualification and delivery method is the same whether the requirement
        is an optronic sight or an industrial plant. These are areas we work in beyond the core portfolio.</p></div>
    <div class="chips">%s</div>
  </div>
</section>

<section class="section band texture">
  <img src="%sassets/img/band-dark.jpg" alt="" loading="lazy">
  <div class="wrap center" style="max-width:720px">
    <p class="eyebrow">Enquiry</p>
    <h2 class="rule-h">Send us a requirement we have never seen before.</h2>
    <p class="lede">If it is not listed anywhere on this site, that is the conversation we most want to have.</p>
    <div class="btn-row"><a class="btn btn-primary" href="%s">Submit a Requirement <i class="arw"></i></a></div>
  </div>
</section>
""" % (steps, ex_html, reach, rel(d), url(d, "contact/request-for-information")))

    page("capabilities/beyond-the-catalogue/index.html",
         "Beyond the Catalogue | Maalik Creative Engineers",
         "Sourcing, qualifying and delivering technology that does not yet have a supplier in Pakistan. "
         "A described six-step method.", body, active="capabilities", depth=2)


# =========================================================================== PRODUCTS INDEX
PLATFORM_MAP = {
    "command-control-communications": ["Dismounted and man-portable", "Vehicle mounted", "Fixed site and infrastructure"],
    "intelligence-surveillance-reconnaissance": ["Airborne", "Naval and shipborne", "Fixed site and infrastructure"],
    "electro-optics-night-vision": ["Dismounted and man-portable", "Vehicle mounted", "Fixed site and infrastructure"],
    "unmanned-systems-counter-uas": ["Airborne", "Vehicle mounted"],
    "air-defence-systems": ["Vehicle mounted", "Fixed site and infrastructure", "Naval and shipborne"],
    "weapon-systems-munitions": ["Dismounted and man-portable", "Airborne", "Naval and shipborne"],
    "electronic-warfare": ["Airborne", "Vehicle mounted", "Naval and shipborne"],
    "avionics-aerospace": ["Airborne"],
    "platforms-vehicles": ["Naval and shipborne", "Vehicle mounted"],
    "cyber-security-information-assurance": ["Software and platform-independent"],
    "artificial-intelligence-digital-intelligence": ["Software and platform-independent"],
    "safe-city-critical-infrastructure": ["Fixed site and infrastructure", "Software and platform-independent"],
}
ENV_MAP = {
    "command-control-communications": ["Land", "Maritime and coastal", "Air", "Urban"],
    "intelligence-surveillance-reconnaissance": ["Land", "Maritime and coastal", "Air", "Sub-surface"],
    "electro-optics-night-vision": ["Land", "Maritime and coastal", "Urban"],
    "unmanned-systems-counter-uas": ["Land", "Air", "Urban"],
    "air-defence-systems": ["Land", "Air", "Maritime and coastal"],
    "weapon-systems-munitions": ["Land", "Air", "Sub-surface"],
    "electronic-warfare": ["Land", "Air", "Maritime and coastal", "Sub-surface"],
    "avionics-aerospace": ["Air"],
    "platforms-vehicles": ["Land", "Maritime and coastal"],
    "cyber-security-information-assurance": ["Network and cyber"],
    "artificial-intelligence-digital-intelligence": ["Network and cyber", "Urban"],
    "safe-city-critical-infrastructure": ["Urban", "Network and cyber", "Land"],
}
FUNC_MAP = {
    "command-control-communications": ["Communicate", "Command and control"],
    "intelligence-surveillance-reconnaissance": ["Observe and detect", "Analyse"],
    "electro-optics-night-vision": ["Observe and detect"],
    "unmanned-systems-counter-uas": ["Observe and detect", "Engage", "Protect and defend"],
    "air-defence-systems": ["Protect and defend", "Engage"],
    "weapon-systems-munitions": ["Engage"],
    "electronic-warfare": ["Protect and defend", "Engage", "Observe and detect"],
    "avionics-aerospace": ["Command and control", "Observe and detect"],
    "platforms-vehicles": ["Sustain and support", "Protect and defend"],
    "cyber-security-information-assurance": ["Protect and defend", "Analyse"],
    "artificial-intelligence-digital-intelligence": ["Analyse", "Command and control"],
    "safe-city-critical-infrastructure": ["Observe and detect", "Protect and defend", "Command and control"],
}


def all_products():
    """Flatten the taxonomy into index rows."""
    rows = []
    for dm in DOMAINS:
        mans = [p for p in PARTNERS if dm["slug"] in p["domains"]]
        man = mans[0]["name"] if mans else ""
        for desig, cls, place in dm["models"]:
            rows.append({"name": desig, "desc": cls, "domain": dm, "kind": "model",
                         "place": place, "man": man})
        for name, blurb, place in dm["families"]:
            rows.append({"name": name, "desc": blurb, "domain": dm, "kind": "family",
                         "place": place, "man": man})
    return rows


def build_products():
    d = 1
    rows = all_products()
    cards = []
    for r in rows:
        dm = r["domain"]
        attrs = ('data-item data-domain="%s" data-platform="%s" data-environment="%s" '
                 'data-function="%s" data-manufacturer="%s" data-search="%s"'
                 % (dm["slug"], "|".join(PLATFORM_MAP[dm["slug"]]), "|".join(ENV_MAP[dm["slug"]]),
                    "|".join(FUNC_MAP[dm["slug"]]), r["man"],
                    (r["name"] + " " + r["desc"] + " " + strip_tags(dm["name"])).replace('"', "")))
        stem = image_for(r["name"], r["kind"], dm["slug"])
        if stem:
            media = ('<div class="pcard-img"><img src="%sassets/img/products/%s.jpg" alt="%s" '
                     'loading="lazy" width="1000" height="750"></div>' % (rel(d), stem, r["name"]))
        else:
            media = ('<div class="pcard-img is-plate">%s</div>'
                     % plate(dm["slug"] + "|" + r["name"], dm["icon"], "DOMAIN " + dm["n"]))
        desig_cls = ' class="pdesig"' if r["kind"] == "model" else ""
        cards.append(
            '<a class="pcard" %s href="%s">%s<div class="pcard-body">'
            '<span class="c-n">%s &middot; DOMAIN %s</span>'
            '<h3%s>%s</h3><p>%s</p>'
            '<span class="tlink">Request detail <i class="arw"></i></span></div></a>'
            % (attrs, url(d, "capabilities/" + dm["slug"]), media, r["place"], dm["n"],
               desig_cls, r["name"], r["desc"]))

    def facet(key, values, labels=None):
        out = ['<button class="chip" data-facet="%s" data-value="">All</button>' % key]
        for v in values:
            lbl = labels[v] if labels else v
            out.append('<button class="chip" data-facet="%s" data-value="%s">%s</button>' % (key, v, lbl))
        return "".join(out)

    dom_labels = {dm["slug"]: dm["short"] for dm in DOMAINS}
    mans = sorted(set(r["man"] for r in rows if r["man"]))

    filters = """
<div style="display:grid;gap:26px">
  <div><h4 style="margin-bottom:.85rem;color:var(--text-dim);font-size:.8rem;letter-spacing:.22em">Capability domain</h4><div class="chips">%s</div></div>
  <div><h4 style="margin-bottom:.85rem;color:var(--text-dim);font-size:.8rem;letter-spacing:.22em">Platform</h4><div class="chips">%s</div></div>
  <div><h4 style="margin-bottom:.85rem;color:var(--text-dim);font-size:.8rem;letter-spacing:.22em">Environment</h4><div class="chips">%s</div></div>
  <div><h4 style="margin-bottom:.85rem;color:var(--text-dim);font-size:.8rem;letter-spacing:.22em">Function</h4><div class="chips">%s</div></div>
  <div><h4 style="margin-bottom:.85rem;color:var(--text-dim);font-size:.8rem;letter-spacing:.22em">Manufacturer</h4><div class="chips">%s</div></div>
</div>""" % (facet("domain", [dm["slug"] for dm in DOMAINS], dom_labels),
             facet("platform", FACETS["platform"]),
             facet("environment", FACETS["environment"]),
             facet("function", FACETS["function"]),
             facet("manufacturer", mans))

    body = (
        hero(d, "dom-avionics", "Products", "Every system, one index.",
             "A single filterable index of every product family and named system across all twelve "
             "capability domains. Every filter combination produces a shareable URL.",
             None, "mini", crumb(d, [("Home", ""), ("Products", None)]))
        + """
<section class="section tight">
  <div class="wrap">
    <div style="display:flex;gap:20px;flex-wrap:wrap;align-items:flex-end;margin-bottom:36px">
      <div class="field" style="flex:1;min-width:280px">
        <label for="q">Search designation, family or application</label>
        <input id="q" type="search" data-search placeholder="FALCON, TETRA, counter-UAS, thermal&hellip;">
      </div>
      <button class="btn btn-ghost btn-sm" data-reset>Clear all filters <i class="arw"></i></button>
    </div>
    %s
    <p class="mono" style="margin:34px 0 22px;color:var(--text-faint)">
      Showing <span data-count style="color:var(--red-hot)">0</span> of %d entries</p>
    <div class="grid g3 gap-md" data-index>%s</div>
    <div data-empty class="empty hide">
      <h3>Not listed does not mean not available.</h3>
      <p>No published product matches that combination. That does not mean we cannot source it.
        Send us the requirement.</p>
      <a class="btn btn-primary" href="%s">Submit a Requirement <i class="arw"></i></a>
    </div>
  </div>
</section>
""" % (filters, len(rows), "".join(cards), url(d, "contact/request-for-information"))
        + cta_band(d, "insights-band"))

    page("products/index.html", "Product Index | Maalik Creative Engineers",
         "A single filterable index of every product family and named system across twelve capability "
         "domains, with shareable filter URLs.", body, active="products", depth=1)


# =========================================================================== SECTORS
def build_sectors_index():
    d = 1
    panels = "".join(
        '<a class="spanel" href="%s"><img src="%sassets/img/%s.jpg" alt="" loading="lazy">'
        '<div class="spanel-in"><div class="sp-n">SECTOR %02d</div><h3>%s</h3><p>%s</p></div></a>'
        % (url(d, "sectors/" + s["slug"]), rel(d), s["img"], i + 1, s["name"], s["line"])
        for i, s in enumerate(SECTORS))
    body = (
        hero(d, "sector-land", "Sectors", "Cut by customer,<br>not by taxonomy.",
             "An officer thinks in terms of their own service and mission. These six pages re-cut the "
             "same portfolio the way the customer thinks about it.",
             None, "mini", crumb(d, [("Home", ""), ("Sectors", None)]))
        + '<section class="section" style="padding:0"><div>%s</div></section>' % panels
        + support_block(d) + cta_band(d))
    page("sectors/index.html", "Sectors Served | Maalik Creative Engineers",
         "Land forces, naval forces, air and space, strategic organisations, law enforcement and "
         "critical infrastructure.", body, active="sectors", depth=1)


def build_sector(s, idx):
    d = 2
    doms = [dom_by_slug(x) for x in s["domains"] if dom_by_slug(x)]
    cards = domain_cards(d, "g3", doms)
    feat = []
    for dm in doms[:3]:
        pool = dm["models"][:3] if dm["models"] else [(f[0], f[1], f[2]) for f in dm["families"][:3]]
        for name, desc, place in pool:
            feat.append(
                '<a class="card rv" href="%s"><span class="c-n">DOMAIN %s</span><h3>%s</h3><p>%s</p>'
                '<span class="tlink">View domain <i class="arw"></i></span></a>'
                % (url(d, "capabilities/" + dm["slug"]), dm["n"], name, desc))
    body = (
        hero(d, s["img"], "Sector %02d" % idx, s["name"], s["line"],
             [("Discuss a requirement", url(d, "contact/request-for-information"), "btn-primary")],
             "short", crumb(d, [("Home", ""), ("Sectors", "sectors"), (s["name"], None)]))
        + """
<section class="section">
  <div class="wrap"><div style="max-width:780px">
    <p class="eyebrow">Operational context</p>
    <h2 class="rule-h">What shapes procurement in this sector.</h2>
    <p class="measure" style="color:var(--text-dim)">%s</p>
  </div></div>
</section>

<section class="section ink2">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Relevant capability domains</p>
      <h2 class="rule-h">In priority order for this sector.</h2>
      <p class="lede">%s</p></div>
    %s
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Featured systems</p>
      <h2 class="rule-h">Curated across domains for this sector.</h2></div>
    <div class="grid g3 gap-md">%s</div>
    <div class="btn-row"><a class="btn btn-ghost" href="%s">Browse the full index <i class="arw"></i></a></div>
  </div>
</section>

<section class="section paper">
  <div class="wrap"><div style="max-width:800px">
    <p class="eyebrow">Support proposition</p>
    <h2 class="rule-h">How sustainment works here.</h2>
    <p class="lede">%s</p>
    <div class="btn-row"><a class="btn btn-dark" href="%s">View our services <i class="arw"></i></a></div>
  </div></div>
</section>

<section class="section band texture">
  <img src="%sassets/img/%s.jpg" alt="" loading="lazy">
  <div class="wrap center" style="max-width:720px">
    <p class="eyebrow">Enquiry</p>
    <h2 class="rule-h">Discuss a %s requirement.</h2>
    <p class="lede">Your enquiry is tagged to this sector and routed to the team that covers it.</p>
    <div class="btn-row"><a class="btn btn-primary" href="%s">Submit a Requirement <i class="arw"></i></a></div>
  </div>
</section>
""" % (s["context"], s["focus"], cards, "".join(feat[:9]), url(d, "products"),
       s["support"], url(d, "services"), rel(d), s["img"], s["name"].lower(),
       url(d, "contact/request-for-information")))

    page("sectors/%s/index.html" % s["slug"], "%s | Maalik Creative Engineers" % s["name"],
         s["line"], body, active="sectors", depth=2)
