# -*- coding: utf-8 -*-
"""Page builders: services, partners, about, insights, careers, contact, downloads, legal, system."""
from build import *   # noqa


# =========================================================================== SERVICES
def build_services_index():
    d = 1
    cards = "".join(
        '<a class="icard rv" href="%s"><div class="icard-img">'
        '<img src="%sassets/img/%s.jpg" alt="" loading="lazy"><span class="icard-tag">%02d</span></div>'
        '<div class="icard-body"><h3>%s</h3><p>%s</p>'
        '<span class="tlink">Read more <i class="arw"></i></span></div></a>'
        % (url(d, "services/" + s["slug"]), rel(d), s["img"], i + 1, s["name"], s["key"])
        for i, s in enumerate(SERVICES))

    sim = "".join('<tr><td class="desig">%s</td><td>%s</td></tr>' % t for t in SIMULATION)
    trade = "".join('<tr><td class="desig">%s</td><td>%s</td></tr>' % t for t in TRADING)

    body = (
        hero(d, "svc-mro", "Services", "The contract ends.<br>The support does not.",
             "Seven services that turn a supply relationship into a programme relationship, from "
             "requirement definition through to life extension of equipment already in service.",
             [("Talk to our support team", url(d, "contact/support"), "btn-primary")], "short",
             crumb(d, [("Home", ""), ("Services", None)]))
        + """
<section class="section">
  <div class="wrap">
    <div class="sec-head" style="max-width:840px"><p class="eyebrow">What we do</p>
      <h2 class="rule-h">Seven services, one accountable programme.</h2>
      <p class="lede">A customer does not want seven suppliers with seven contracts. Each of these is
        delivered by us, under one contract, with one project manager who stays with the programme from
        requirement definition to disposal.</p></div>
    <div class="grid g3 gap-md">%s</div>
  </div>
</section>

<section class="section paper">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">The delivery model</p>
      <h2 class="rule-h">The same six stages, every time.</h2></div>
    <div class="rail">%s</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head" style="max-width:820px"><p class="eyebrow">Cross-domain</p>
      <h2 class="rule-h">Simulation and training systems.</h2>
      <p class="lede">Training capability sits across every domain. It is presented here rather than
        inside a single capability page, with cross-links from the domains it serves.</p></div>
    <div class="tbl-wrap"><table class="spec">
      <thead><tr><th>System</th><th>Application</th></tr></thead><tbody>%s</tbody></table></div>
  </div>
</section>

<section class="section ink2">
  <div class="wrap">
    <div class="sec-head" style="max-width:820px"><p class="eyebrow">Trading and technical services</p>
      <h2 class="rule-h">Inputs to a production programme.</h2>
      <p class="lede">Sourcing that supports manufacture rather than replacing it. Frequently the highest
        value thing we do for a strategic organisation.</p></div>
    <div class="tbl-wrap"><table class="spec">
      <thead><tr><th>Category</th><th>Scope</th></tr></thead><tbody>%s</tbody></table></div>
  </div>
</section>
""" % (cards,
       "".join('<div class="step"><div class="dot"></div><div class="sn">%s</div><h4>%s</h4><p>%s</p></div>'
               % st for st in DELIVERY), sim, trade)
        + cta_band(d))

    page("services/index.html", "Integration, Logistics and Support Services | Maalik",
         "Systems integration, procurement, import and clearance, installation, training, maintenance, "
         "overhaul and technology transfer.", body, active="services", depth=1)


def build_service(s, idx):
    d = 2
    what = "".join("<li>%s</li>" % x for x in s["what"])
    others = [x for x in SERVICES if x["slug"] != s["slug"]][:3]
    rel_cards = "".join(
        '<a class="card rv" href="%s"><span class="c-n">SERVICE</span><h3>%s</h3><p>%s</p>'
        '<span class="tlink">Read more <i class="arw"></i></span></a>'
        % (url(d, "services/" + o["slug"]), o["name"], o["key"]) for o in others)

    body = (
        hero(d, s["img"], "Service %02d" % idx, s["name"], s["key"],
             [("Talk to our support team", url(d, "contact/support"), "btn-primary")], "short",
             crumb(d, [("Home", ""), ("Services", "services"), (s["name"], None)]))
        + """
<section class="section">
  <div class="wrap"><div style="max-width:780px">
    <p class="eyebrow">Why it matters</p>
    <h2 class="rule-h">%s</h2>
    <p class="measure" style="color:var(--text-dim)">%s</p>
  </div></div>
</section>

<section class="section ink2">
  <div class="wrap"><div class="split" style="border:1px solid var(--line-soft);border-radius:2px">
    <div class="split-body">
      <p class="eyebrow">What we do</p>
      <h2 class="rule-h" style="font-size:1.85rem">Scope of the service.</h2>
      <ul>%s</ul>
    </div>
    <div class="split-media"><img src="%sassets/img/%s.jpg" alt="" loading="lazy"></div>
  </div></div>
</section>

<section class="section">
  <div class="wrap"><div class="grid g2 gap-lg">
    <div><p class="eyebrow">How we do it</p><h3 style="margin-bottom:1rem">Method</h3>
      <p style="color:var(--text-dim)">%s</p></div>
    <div><p class="eyebrow">What you receive</p><h3 style="margin-bottom:1rem">Deliverable</h3>
      <p style="color:var(--text-dim)">%s</p></div>
  </div></div>
</section>

<section class="section ink2">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Related services</p>
      <h2 class="rule-h">Usually procured alongside.</h2></div>
    <div class="grid g3 gap-md">%s</div>
  </div>
</section>

<section class="section band texture">
  <img src="%sassets/img/%s.jpg" alt="" loading="lazy">
  <div class="wrap center" style="max-width:720px">
    <p class="eyebrow">Enquiry</p>
    <h2 class="rule-h">Talk to our support team.</h2>
    <p class="lede">For equipment already in service, use the support route so your request reaches the
      service team directly rather than a general inbox.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="%s">Support and service request <i class="arw"></i></a>
      <a class="btn btn-ghost" href="%s">Submit a new requirement <i class="arw"></i></a>
    </div>
  </div>
</section>
""" % (s["key"], s["why"], what, rel(d), s["img"], s["how"], s["receive"], rel_cards,
       rel(d), s["img"], url(d, "contact/support"), url(d, "contact/request-for-information")))

    page("services/%s/index.html" % s["slug"], "%s | Maalik Creative Engineers" % s["name"],
         s["key"], body, active="services", depth=2)


# =========================================================================== PARTNERS
def build_partners_index():
    d = 1
    cards = []
    for p in PARTNERS:
        chips = "".join('<span class="chip" style="cursor:default;font-size:.72rem;padding:4px 9px">%s</span>'
                        % dom_by_slug(x)["short"] for x in p["domains"] if dom_by_slug(x))
        cards.append(
            '<a class="card rv" data-pgroup="%s|%s" href="%s">'
            '<span class="c-n">%s</span><h3>%s</h3>'
            '<p>%s</p><div class="chips" style="margin-bottom:1.2rem">%s</div>'
            '<span class="tlink">View profile <i class="arw"></i></span></a>'
            % (p["group"], p["region"], url(d, "partners/" + p["slug"]), p["country"],
               p["name"], p["supplies"][:190] + ("&hellip;" if len(p["supplies"]) > 190 else ""), chips))

    group_chips = '<button class="chip on" data-lf="">All</button>' + "".join(
        '<button class="chip" data-lf="%s">%s</button>' % (g, g) for g in PARTNER_GROUPS)
    region_chips = "".join('<button class="chip" data-lf="%s">%s</button>' % (r, r) for r in PARTNER_REGIONS)

    body = (
        hero(d, "partners-band", "Partners", "A manufacturing network,<br>not a supplier list.",
             "We represent manufacturers. That means a documented authorisation, a direct technical "
             "channel to the factory, and accountability that does not stop at the point of sale.",
             [("Become a partner", url(d, "partners/become-a-partner"), "btn-primary")], "short",
             crumb(d, [("Home", ""), ("Partners", None)]))
        + """
<section class="section" data-listfilter="pgroup">
  <div class="wrap">
    <div class="sec-head" style="max-width:840px"><p class="eyebrow">Directory</p>
      <h2 class="rule-h">Grouped by capability, then by region.</h2>
      <p class="lede">A visitor is looking for a manufacturer of a specific thing, not for a country.
        Country of origin is published on every entry because it determines the export licensing route.</p></div>
    <div class="chips" style="margin-bottom:14px">%s</div>
    <div class="chips" style="margin-bottom:40px">%s</div>
    <div class="grid g3 gap-md">%s</div>
  </div>
</section>

<section class="section ink2">
  <div class="wrap"><div class="note" style="max-width:860px">
    <h4>Logo and relationship wording is a legal matter, not a design matter</h4>
    <p>No manufacturer logo, trademark or product photograph is published without written permission or
      an existing authorisation that explicitly permits marketing use. Several manufacturers require
      pre-approval of the exact wording used to describe the relationship. Where permission is not yet in
      place, the manufacturer is listed as text only. We never imply exclusivity that has not been
      granted in writing.</p>
  </div></div>
</section>

<section class="section band texture">
  <img src="%sassets/img/partners-band.jpg" alt="" loading="lazy">
  <div class="wrap center" style="max-width:740px">
    <p class="eyebrow">For manufacturers</p>
    <h2 class="rule-h">Bring your technology to Pakistan.</h2>
    <p class="lede">Established institutional relationships, procurement fluency, and a Pakistani
      engineering and support base so that you do not need to build one.</p>
    <div class="btn-row"><a class="btn btn-primary" href="%s">Discuss representation in Pakistan <i class="arw"></i></a></div>
  </div>
</section>
""" % (group_chips, region_chips, "".join(cards), rel(d), url(d, "partners/become-a-partner")))

    page("partners/index.html", "OEM and Technology Partners | Maalik Creative Engineers",
         "Our international manufacturing network across communications, optronics, air defence, "
         "avionics, cyber security and AI.", body, active="partners", depth=1)


def build_partner(p):
    d = 2
    doms = [dom_by_slug(x) for x in p["domains"] if dom_by_slug(x)]
    cards = domain_cards(d, "g3", doms)
    note = ""
    if p.get("note"):
        note = ('<div class="note" style="margin-top:30px;max-width:760px">'
                '<h4>Why this relationship matters</h4><p>%s</p></div>' % p["note"])
    parent = ('<dt>Group</dt><dd>%s</dd>' % p["parent"]) if p.get("parent") else ""
    mark = ""
    if p["slug"] in PARTNER_LOGOS:
        mark = ('<div class="partner-mark"><img src="%sassets/img/partners/%s.png" alt="%s" '
                'width="420" height="200"></div>' % (rel(d), p["slug"], p["name"]))

    body = (
        hero(d, doms[0]["img"] if doms else "partners-band", "Partner profile", p["name"],
             p["supplies"][:170] + ("&hellip;" if len(p["supplies"]) > 170 else ""),
             [("Enquire about this manufacturer", url(d, "contact/request-for-information"), "btn-primary")],
             "short", crumb(d, [("Home", ""), ("Partners", "partners"), (p["name"][:34], None)]))
        + """
<section class="section">
  <div class="wrap"><div class="grid g2 gap-lg">
    <div>
      <p class="eyebrow">Profile</p>
      <h2 class="rule-h" style="font-size:1.85rem">The relationship, stated precisely.</h2>
      <p style="color:var(--text-dim)">%s</p>
      <p style="color:var(--text-dim);font-size:.95rem">The nature of this relationship is described using
        only language the manufacturer has approved. Where a specific designation such as authorised
        representative, authorised distributor, technology partner or integration partner applies, it is
        stated on this page and can be evidenced on request.</p>
      %s
    </div>
    <div>
      %s
      <dl class="kv">
        <dt>Full legal name</dt><dd>%s</dd>
        <dt>Country of origin</dt><dd>%s</dd>
        <dt>Region</dt><dd>%s</dd>
        <dt>Category</dt><dd>%s</dd>
        %s
        <dt>Relationship</dt><dd>[insert approved designation]</dd>
        <dt>Year established</dt><dd>[insert year]</dd>
      </dl>
    </div>
  </div></div>
</section>

<section class="section ink2">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Capability domains covered</p>
      <h2 class="rule-h">What is available through this relationship.</h2></div>
    %s
  </div>
</section>

<section class="section">
  <div class="wrap"><div style="max-width:780px">
    <p class="eyebrow">Support arrangement</p>
    <h2 class="rule-h">What the relationship provides behind the sale.</h2>
    <p class="measure" style="color:var(--text-dim)">%s</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="%s">Enquire about this manufacturer <i class="arw"></i></a>
      <a class="btn btn-ghost" href="%s">Back to the directory <i class="arw"></i></a>
    </div>
  </div></div>
</section>
""" % (p["supplies"], note, mark, p["name"], p["country"], p["region"], p["group"], parent,
       cards, STANDING["support"], url(d, "contact/request-for-information"), url(d, "partners")))

    page("partners/%s/index.html" % p["slug"], "%s | Partner Profile | Maalik" % p["name"][:44],
         p["supplies"][:150], body, active="partners", depth=2)


def build_become_partner():
    d = 2
    offers = [
        ("Institutional access", "Established relationships across the tri-services, strategic "
         "organisations and law enforcement agencies."),
        ("Procurement fluency", "Working knowledge of the Pakistan public procurement framework, PPRA "
         "process and tendering practice."),
        ("An engineering base", "A Pakistani engineering and support base, so you do not need to "
         "establish one to compete."),
        ("Programme management", "Contract and programme management run on your behalf, with qualified "
         "project managers deployed to the programme."),
        ("Local sustainment", "In-country warranty administration, spares holding and maintenance "
         "capability behind every delivery."),
        ("Bid phase support", "Support through technical evaluation and the bid phase, including "
         "documentation and compliance statements."),
    ]
    expect = [
        "Documented authorisation to represent the product in Pakistan",
        "Technical documentation and training access for our engineers",
        "A spares supply commitment consistent with the offered warranty",
        "Export licensing support from the country of origin",
    ]
    ocards = "".join('<div class="card rv"><span class="c-n">%02d</span><h3>%s</h3><p>%s</p></div>'
                     % (i + 1, t, b) for i, (t, b) in enumerate(offers))
    ex = "".join("<li>%s</li>" % x for x in expect)

    body = (
        hero(d, "partners-band", "Become a partner", "Bring your technology<br>to Pakistan.",
             "Written for a manufacturer evaluating whether to appoint a Pakistan representative. "
             "Here is what we provide, and what we ask for in return.",
             [("Submit a partnership enquiry", url(d, "contact/partnership"), "btn-primary")], "short",
             crumb(d, [("Home", ""), ("Partners", "partners"), ("Become a Partner", None)]))
        + """
<section class="section">
  <div class="wrap">
    <div class="sec-head" style="max-width:840px"><p class="eyebrow">What we offer a manufacturer</p>
      <h2 class="rule-h">A route to market that already exists.</h2>
      <p class="lede">Entering the Pakistan market directly means building institutional relationships,
        procurement knowledge and a support base from nothing. We hold all three.</p></div>
    <div class="grid g3 gap-md">%s</div>
  </div>
</section>

<section class="section ink2">
  <div class="wrap"><div class="split" style="border:1px solid var(--line-soft);border-radius:2px">
    <div class="split-body">
      <p class="eyebrow">What we expect of a partner</p>
      <h2 class="rule-h" style="font-size:1.85rem">Four things, stated plainly.</h2>
      <ul>%s</ul>
      <p style="color:var(--text-faint);font-size:.9rem">We do not claim relationships we cannot
        evidence, and we do not inflate a designation. That discipline protects you as much as it
        protects us.</p>
    </div>
    <div class="split-media"><img src="%sassets/img/svc-tot.jpg" alt="" loading="lazy"></div>
  </div></div>
</section>

<section class="section">
  <div class="wrap"><div class="grid g2 gap-lg">
    <div>
      <p class="eyebrow">Partnership enquiry</p>
      <h2 class="rule-h">Start the conversation.</h2>
      <p style="color:var(--text-dim)">This form is routed to a separate business development inbox, not
        to the general enquiry address. We acknowledge every enquiry within one working day.</p>
      <p style="color:var(--text-dim);font-size:.93rem">A one-page company profile written specifically
        for manufacturers, suitable for circulation at exhibitions, is available on the
        <a class="tlink" style="display:inline-flex" href="%s">Downloads page</a>.</p>
    </div>
    <div>%s</div>
  </div></div>
</section>
""" % (ocards, ex, rel(d), url(d, "downloads"), partner_form(d)))

    page("partners/become-a-partner/index.html", "Become a Partner | Maalik Creative Engineers",
         "For manufacturers evaluating representation in Pakistan: institutional access, procurement "
         "fluency, engineering base and local sustainment.", body, active="partners", depth=2)


# =========================================================================== FORMS
def field(label, name, kind="text", required=False, hint="", options=None, ph=""):
    req = ' <span class="req">*</span>' if required else ""
    rq = " required" if required else ""
    if kind == "textarea":
        inp = '<textarea id="%s" name="%s"%s placeholder="%s"></textarea>' % (name, name, rq, ph)
    elif kind == "select":
        opts = "".join('<option value="%s">%s</option>' % (o, o) for o in (options or []))
        inp = '<select id="%s" name="%s"%s><option value="">Select&hellip;</option>%s</select>' % (
            name, name, rq, opts)
    else:
        inp = '<input id="%s" name="%s" type="%s"%s placeholder="%s">' % (name, name, kind, rq, ph)
    h = '<p class="hint">%s</p>' % hint if hint else ""
    return '<div class="field"><label for="%s">%s%s</label>%s%s</div>' % (name, label, req, inp, h)


def form_wrap(inner, note, ok_title, ok_body):
    return ("""<form class="form" data-form novalidate>%s
  <p class="form-note">%s</p>
  <button class="btn btn-primary" type="submit">Send enquiry <i class="arw"></i></button>
</form>
<div class="form-ok"><h4>%s</h4><p>%s</p></div>""" % (inner, note, ok_title, ok_body))


PRIVACY_NOTE = ('Information submitted through this form is used only to respond to your enquiry and is '
                'retained in line with our Privacy Policy. Uploaded files are virus scanned. We do not '
                'share enquiry data with third parties without your consent.')


def general_form(d):
    inner = ('<div class="fr2">%s%s</div><div class="fr2">%s%s</div>%s%s'
             % (field("Name", "name", required=True), field("Organisation", "org", required=True),
                field("Role", "role"), field("Email", "email", "email", required=True),
                field("Telephone", "tel", "tel"),
                field("Message", "message", "textarea", required=True,
                      ph="How can we help?")))
    return form_wrap(inner, PRIVACY_NOTE, "Enquiry received.",
                     "We acknowledge every enquiry within one working day. A member of the team will "
                     "respond to the address you supplied.")


def rfi_form(d):
    doms = [strip_tags(x["name"]) for x in DOMAINS] + ["Not listed / Beyond the Catalogue"]
    inner = ('<div class="fr2">%s%s</div><div class="fr2">%s%s</div><div class="fr2">%s%s</div>'
             '<div class="fr2">%s%s</div>%s%s'
             % (field("Name", "name", required=True), field("Organisation", "org", required=True),
                field("Role", "role", required=True),
                field("Official email", "email", "email", required=True,
                      hint="An official domain speeds up verification for controlled documents."),
                field("Telephone", "tel", "tel"),
                field("Capability domain", "domain", "select", required=True, options=doms),
                field("Product or system of interest", "system"),
                field("Tender or reference number", "ref", hint="If applicable."),
                field("Required delivery timeframe", "timeframe", "select",
                      options=["Within 3 months", "3 to 6 months", "6 to 12 months",
                               "More than 12 months", "Not yet determined"]),
                field("Requirement description", "message", "textarea", required=True,
                      ph="Describe the operational effect required, not only the equipment assumed.")))
    inner += field("Specification or tender document", "upload", "file",
                   hint="PDF, DOC, DOCX or ZIP, up to 25 MB. Files are virus scanned on receipt.")
    return form_wrap(inner, PRIVACY_NOTE,
                     "Requirement received by the bid and technical team.",
                     "We acknowledge every enquiry within one working day and will respond with a "
                     "technical assessment and a route to source it.")


def partner_form(d):
    inner = ('<div class="fr2">%s%s</div><div class="fr2">%s%s</div><div class="fr2">%s%s</div>'
             '<div class="fr2">%s%s</div>%s'
             % (field("Company name", "company", required=True),
                field("Country", "country", required=True),
                field("Website", "website", "url"),
                field("Product category", "category", required=True),
                field("Existing Pakistan presence", "presence", "select",
                      options=["None", "Distributor in place", "Direct office", "Prefer not to say"]),
                field("Export control classification", "ecc", hint="If known."),
                field("Contact name", "name", required=True), field("Role", "role"),
                field("Message", "message", "textarea", required=True,
                      ph="Tell us about the product and what you are looking for in a representative.")))
    return form_wrap(inner, PRIVACY_NOTE, "Partnership enquiry received.",
                     "This enquiry is routed to business development. We acknowledge every enquiry "
                     "within one working day.")


def support_form(d):
    inner = ('<div class="fr2">%s%s</div><div class="fr2">%s%s</div><div class="fr2">%s%s</div>%s'
             % (field("Organisation", "org", required=True),
                field("Contract or order reference", "ref", required=True),
                field("System or model", "system", required=True),
                field("Urgency", "urgency", "select", required=True,
                      options=["Equipment unserviceable", "Degraded but usable",
                               "Scheduled maintenance", "Spares enquiry", "General question"]),
                field("Contact name", "name", required=True),
                field("Telephone", "tel", "tel", required=True),
                field("Nature of the issue", "message", "textarea", required=True,
                      ph="Describe the fault or the support required.")))
    return form_wrap(inner, PRIVACY_NOTE, "Support request received.",
                     "Your request has been routed to the service and support team. We acknowledge every "
                     "request within one working day.")


FORMS = {"": general_form, "request-for-information": rfi_form,
         "partnership": partner_form, "support": support_form}


# =========================================================================== CONTACT
def build_contact(route):
    d = 1 if not route["slug"] else 2
    others = [r for r in CONTACT_ROUTES if r["slug"] != route["slug"]]
    ocards = "".join(
        '<a class="card rv" href="%s"><span class="c-n">%s</span><h3>%s</h3><p>%s</p>'
        '<span class="tlink">Use this route <i class="arw"></i></span></a>'
        % (url(d, "contact/" + r["slug"] if r["slug"] else "contact"), r["eyebrow"], r["name"], r["desc"])
        for r in others)

    trail = [("Home", ""), ("Contact", None)] if not route["slug"] else \
            [("Home", ""), ("Contact", "contact"), (route["short"], None)]

    body = (
        hero(d, "contact-band", route["eyebrow"], route["name"], route["desc"], None, "mini",
             crumb(d, trail))
        + """
<section class="section">
  <div class="wrap"><div class="grid g2 gap-lg">
    <div>
      <p class="eyebrow">%s</p>
      <h2 class="rule-h">Tell us the requirement.</h2>
      <p style="color:var(--text-dim)">This form is routed to <strong style="color:var(--text)">%s</strong>.
        Four routes exist so that your enquiry reaches the people who can answer it, rather than a
        general inbox.</p>
      <dl class="kv" style="margin-top:26px">
        <dt>Head office</dt><dd>%s</dd>
        <dt>Telephone</dt><dd>%s</dd>
        <dt>General</dt><dd><a href="mailto:%s" style="color:var(--red-hot)">%s</a></dd>
        <dt>Tenders and RFI</dt><dd><a href="mailto:%s" style="color:var(--red-hot)">%s</a></dd>
        <dt>Partnership</dt><dd><a href="mailto:%s" style="color:var(--red-hot)">%s</a></dd>
        <dt>Support</dt><dd><a href="mailto:%s" style="color:var(--red-hot)">%s</a></dd>
        <dt>Office hours</dt><dd>%s</dd>
        <dt>Registered name</dt><dd>%s</dd>
        <dt>Registration no.</dt><dd>%s</dd>
      </dl>
      <div class="note" style="margin-top:30px">
        <h4>Response commitment</h4>
        <p>We acknowledge every enquiry within one working day.</p>
      </div>
    </div>
    <div>%s</div>
  </div></div>
</section>

<section class="section ink2">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Other routes</p>
      <h2 class="rule-h">Four visitor types, four inboxes.</h2></div>
    <div class="grid g3 gap-md">%s</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Location</p><h2 class="rule-h">Head office.</h2></div>
    <div class="plate" style="aspect-ratio:21/7">
      <div class="pl-desig">%s<small>Embedded map to be added at launch with the verified head office address</small></div>
    </div>
  </div>
</section>
""" % (route["eyebrow"], route["to"], "<br>".join(COMPANY["address"]),
       tel_html(),
       COMPANY["email_general"], COMPANY["email_general"],
       COMPANY["email_tender"], COMPANY["email_tender"],
       COMPANY["email_partner"], COMPANY["email_partner"],
       COMPANY["email_support"], COMPANY["email_support"],
       COMPANY["hours"], COMPANY["legal"], COMPANY["reg_no"],
       FORMS[route["slug"]](d), ocards, ", ".join(COMPANY["address"])))

    path = "contact/index.html" if not route["slug"] else "contact/%s/index.html" % route["slug"]
    title = ("Contact and Requirement Submission | Maalik" if not route["slug"]
             else "%s | Maalik Creative Engineers" % route["name"])
    page(path, title,
         "Submit a requirement, tender reference or technical specification. Every enquiry acknowledged "
         "within one working day.", body, active="", depth=d)
