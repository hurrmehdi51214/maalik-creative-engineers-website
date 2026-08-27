# -*- coding: utf-8 -*-
"""Page builders: about set, insights, careers, downloads, legal, system pages."""
from build import *   # noqa


ABOUT_NAV = [("Company", "about"), ("Leadership", "about/leadership"),
             ("Programs and Track Record", "about/programs"),
             ("Compliance", "about/quality"), ("Facilities", "about/facilities")]


def about_subnav(d, current):
    items = "".join(
        '<a class="chip%s" href="%s">%s</a>' % (" on" if h == current else "", url(d, h), t)
        for t, h in ABOUT_NAV)
    return ('<section class="section tight" style="padding:34px 0;border-bottom:1px solid var(--line)">'
            '<div class="wrap"><div class="chips">%s</div></div></section>' % items)


# =========================================================================== ABOUT / COMPANY
def build_about():
    d = 1
    pillars = "".join(
        '<div class="card rv"><span class="c-n">%s</span><h3>%s</h3>'
        '<p class="pill-head">%s</p><p>%s</p></div>'
        % (n, name, head, body) for name, head, body, n in PILLARS)

    objectives = [
        "Identify requirements early and assess them technically and operationally.",
        "Support manufacturers fully through the preparation phase.",
        "Leverage expertise in public procurement law and produce error-free submissions.",
        "Assist in accurate project costing.",
        "Identify the most suitable technical and commercial local partners.",
        "Provide complete support through bid evaluation.",
        "Deploy qualified project managers capable of running a program on a manufacturer's behalf.",
        "Provide warranty and post-warranty support without exception.",
    ]
    obj = "".join("<li>%s</li>" % o for o in objectives)

    timeline = [
        ("2010", "Incorporation", "Maalik Creative Engineers (Private) Limited is established and "
         "registered in Pakistan."),
        ("2012", "Communications and optronics", "Tactical communications and electro-optic sighting "
         "enter the portfolio, with the first manufacturer authorisations in place."),
        ("2013", "Simulation and training", "Simulation and training system delivery begins across "
         "service branches."),
        ("2015", "Air defence and avionics", "Air defence, avionics and airborne mission system work "
         "enters the portfolio, together with depot facility establishment."),
        ("2017", "Unmanned systems and counter-UAS", "Unmanned platforms, payloads and counter-drone "
         "capability are added, including co-production arrangements."),
        ("2019", "Cyber security and AI", "Cyber security delivery and applied artificial intelligence "
         "platforms are added through partner relationships."),
        ("2026", "Consolidation", "Five separate web properties are consolidated into a single portfolio "
         "under one brand and one taxonomy."),
    ]
    tl = "".join('<li><h4>%s &mdash; %s</h4><p>%s</p></li>' % t for t in timeline)

    body = (
        hero(d, "about-facility", "About", "Engineering that<br>has to work.",
             BOILERPLATE["short"],
             [("Download the corporate profile", url(d, "downloads"), "btn-primary")], "short",
             crumb(d, [("Home", ""), ("About", None)]))
        + about_subnav(d, "about")
        + """
<section class="section">
  <div class="wrap"><div style="max-width:820px">
    <p class="eyebrow">Who we are</p>
    <h2 class="rule-h">A Pakistani defence and technology solutions house.</h2>
    <p class="lede">%s</p>
  </div></div>
</section>

<section class="section ink2">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Value pillars</p>
      <h2 class="rule-h">Four things a customer is actually buying.</h2></div>
    <div class="grid g4 gap-md">%s</div>
  </div>
</section>

<section class="section">
  <div class="wrap"><div class="split" style="border:1px solid var(--line-soft);border-radius:2px">
    <div class="split-body">
      <p class="eyebrow">Mission and objectives</p>
      <h2 class="rule-h" style="font-size:1.85rem">How we operate.</h2>
      <ul>%s</ul>
    </div>
    <div class="split-media"><img src="%sassets/img/svc-integration.jpg" alt="" loading="lazy"></div>
  </div></div>
</section>

<section class="section paper">
  <div class="wrap"><div style="max-width:820px">
    <p class="eyebrow">The business model</p>
    <h2 class="rule-h">Three legs, none of which works without the other two.</h2>
  </div>
  <div class="grid g3 gap-md" style="margin-top:44px">
    <div class="card"><span class="c-n">01</span><h3>Systems integration and supply</h3>
      <p>Sourcing, supplying, integrating and commissioning military grade hardware and software against
        the stated requirements and tenders of the Pakistan Armed Forces, strategic organisations and
        law enforcement agencies.</p></div>
    <div class="card"><span class="c-n">02</span><h3>OEM representation and partnership</h3>
      <p>Acting as the authorised in-country partner and technical interface for a global network of
        manufacturers across communications, optronics, unmanned systems, air defence, avionics, cyber
        security and artificial intelligence.</p></div>
    <div class="card"><span class="c-n">03</span><h3>Engineering and through-life support</h3>
      <p>Contract management, import and clearance, installation, training, spares provisioning, warranty
        and post-warranty service, depot maintenance, overhaul, life extension, and transfer of technology
        and local co-production where a program calls for it.</p></div>
  </div>
  </div>
</section>

<section class="section">
  <div class="wrap"><div class="grid g2 gap-lg">
    <div>
      <p class="eyebrow">Development</p>
      <h2 class="rule-h">How the portfolio was built.</h2>
    </div>
    <ul class="timeline">%s</ul>
  </div></div>
</section>

<section class="section ink2">
  <div class="wrap"><div class="note" style="max-width:880px">
    <h4>Heritage and continuity</h4>
    <p>Maalik Creative Engineers (Private) Limited was established in 2010. Where the company is the
      successor to, or has absorbed, an existing legal entity, that relationship is stated plainly with
      the year the earlier entity was established. Continuity of registration, personnel and program
      experience is a genuine asset and is straightforward to state honestly. We do not present the
      history, contract values or delivery record of a separate company as though it were our own. Before
      any figure or program appears on this site we confirm which legal entity holds it and describe the
      relationship accurately.</p>
  </div></div>
</section>
""" % (BOILERPLATE["long"], pillars, obj, rel(d), tl)
        + cta_band(d))

    page("about/index.html", "About Maalik Creative Engineers",
         "Established 2010. A Pakistani defence and technology solutions house delivering and sustaining "
         "mission critical capability.", body, active="about", depth=1)


# =========================================================================== LEADERSHIP
def build_leadership():
    d = 2
    people = [
        ("Ali Asad", "Chief Executive Officer",
         "Ali Asad leads the company and holds the manufacturer relationships that underpin the "
         "portfolio. He sets the commercial structure of each program, from first technical "
         "assessment through to contract closure, and represents the company at principal level "
         "with the manufacturers we are authorised to act for. He has overseen the consolidation "
         "of the company's activity into the twelve capability domains published on this site."),
        ("Hurr Mehdi", "Director and Chief Operating Officer",
         "Hurr Mehdi is responsible for delivery. He heads programs and procurement and contracts, "
         "which means every requirement that enters the company passes through his function twice: "
         "once as a bid to be built and once as a program to be run. He works directly with "
         "customers' technical staff on requirement definition, and owns documentation discipline "
         "and compliance across submissions."),
        ("Saeed Ul Haq", "Head of Support and Sustainment",
         "Saeed Ul Haq is accountable for what happens after delivery: spares provisioning, "
         "warranty administration, scheduled and unscheduled maintenance, depot repair and life "
         "extension of systems already in service. He sizes initial provisioning against real "
         "usage rather than assumption, and manages the in-country service capability that keeps "
         "delivered equipment available."),
        ("Hassan Zaheer", "Head of Software Engineering",
         "Hassan Zaheer leads bespoke software and systems development, covering mission and "
         "enterprise software, embedded and IoT engineering, and the integration layer that makes "
         "multi-vendor equipment behave as one system. He is responsible for architecture, "
         "interface definition and the handover of source, documentation and build environment "
         "as part of every deliverable."),
        ("Shahroz Ahmed", "Head of Communications Systems",
         "Shahroz Ahmed covers the communications portfolio end to end: narrowband tactical radio, "
         "trunked networks, private broadband and satellite, together with the dispatch and "
         "command layer above them. He works on coverage and interoperability problems at "
         "formation scale, and runs commissioning and operator training for delivered networks."),
        ("Numan Fiaz", "Head of Cyber and Digital",
         "Numan Fiaz leads the cyber security practice and the applied artificial intelligence "
         "portfolio. His remit spans security assessment, managed security operations, incident "
         "response and governance work, alongside the data fusion and analytics platforms supplied "
         "to mandated agencies. He is responsible for ensuring governance and audit controls are "
         "treated as product requirements rather than options."),
    ]
    cards = "".join(
        '<div class="person rv"><div class="pf"><span>Portrait<br>to follow</span></div>'
        '<div class="pb"><h4>%s</h4><div class="role">%s</div><p>%s</p></div></div>'
        % (n, r, b) for n, r, b in people)

    body = (
        hero(d, "careers-team", "About", "Leadership",
             "The people who will actually run your program, not only the people who sign the "
             "contract.",
             None, "mini", crumb(d, [("Home", ""), ("About", "about"), ("Leadership", None)]))
        + about_subnav(d, "about/leadership")
        + """
<section class="section">
  <div class="wrap">
    <div class="sec-head" style="max-width:820px"><p class="eyebrow">Leadership team</p>
      <h2 class="rule-h">Engineering and program leadership, not only commercial leadership.</h2>
      <p class="lede">An evaluator wants to know who will run the program. The engineering,
        support and program management leadership is listed here alongside the commercial
        leadership, with the discipline each is accountable for.</p></div>
    <div class="people">%s</div>
  </div>
</section>

<section class="section ink2">
  <div class="wrap"><div class="note" style="max-width:860px">
    <h4>Portraits to follow</h4>
    <p>Photography is scheduled. All six portraits will be shot in a single session with identical
      background, lighting and crop, at 1200 &times; 1500. Mismatched portraits are the fastest way
      for an institutional site to look small, which is why the placeholders stay until the full
      set exists.</p>
  </div></div>
</section>
""" % cards
        + cta_band(d))

    page("about/leadership/index.html", "Leadership | Maalik Creative Engineers",
         "Commercial, engineering and program management leadership, with the discipline each is "
         "accountable for.", body, active="about", depth=2)


# =========================================================================== PROGRAMMES
def build_programmes():
    d = 2
    rows = "".join('<tr><td class="desig">%s</td><td>%s</td>'
                   '<td class="mono">%s</td></tr>' % (n, d_, per)
                   for n, d_, per in PROGRAMMES)
    body = (
        hero(d, "dom-platforms", "About", "Programs and track record",
             "Presented as capability categories delivered over time rather than as a year-by-year list "
             "of contract values. That is more useful to a technical reader and carries far less risk.",
             None, "short", crumb(d, [("Home", ""), ("About", "about"), ("Programs", None)]))
        + about_subnav(d, "about/programs")
        + """
<section class="section">
  <div class="wrap">
    <div class="sec-head" style="max-width:840px"><p class="eyebrow">Capability categories delivered</p>
      <h2 class="rule-h">What we have delivered, by category.</h2>
      <p class="lede">Each category states the nature of the work. We do not publish contract values
        against named customers, quantities, delivery dates, unit locations or formation names. Every
        entry is confirmed against company records before publication.</p></div>
    <div class="tbl-wrap"><table class="spec">
      <thead><tr><th>Capability category</th><th>Nature of the work</th><th>Period</th></tr></thead>
      <tbody>%s</tbody></table></div>
  </div>
</section>

<section class="section ink2">
  <div class="wrap"><div class="grid g2 gap-lg">
    <div>
      <p class="eyebrow">Transfer of technology</p>
      <h2 class="rule-h" style="font-size:1.85rem">Capability that stays in the country.</h2>
      <p style="color:var(--text-dim)">Technology transfer and co-production outcomes are the
        differentiator that matters most to strategic organisations, because they convert a purchase into
        a national capability. Our transfer work has covered thermal imaging and optronics co-production,
        unmanned aerial system co-production, and the establishment of in-country depot maintenance
        facilities for air defence and artillery systems.</p>
      <a class="tlink" href="%s">Transfer of technology and co-production <i class="arw"></i></a>
    </div>
    <div class="note">
      <h4>Confidentiality</h4>
      <p>%s</p>
    </div>
  </div></div>
</section>

<section class="section">
  <div class="wrap"><div class="note" style="max-width:880px">
    <h4>Verification before publication, mandatory</h4>
    <p>In defence procurement, an unsupportable credential claim discovered during due diligence is not a
      marketing setback, it is a disqualification. Before any figure or program appears here we confirm
      which legal entity holds it and describe the relationship accurately, for example
      &ldquo;delivered by our predecessor entity&rdquo; or &ldquo;delivered by our group&rdquo;.</p>
  </div></div>
</section>
""" % (rows, url(d, "services/transfer-of-technology-co-production"), STANDING["confidentiality"])
        + cta_band(d))

    page("about/programs/index.html", "Programs and Track Record | Maalik",
         "Capability categories delivered over time across simulation, optronics, unmanned systems, air "
         "defence, avionics, naval craft and space.", body, active="about", depth=2)


# =========================================================================== QUALITY
def build_quality():
    d = 2
    statements = [
        ("Export control and end use",
         "We supply only to authorised end users, comply with the export control regimes of the "
         "countries of origin of the equipment we supply, and require end-user documentation where "
         "the manufacturer or origin country requires it. Where a lawful, documented route to "
         "Pakistan cannot be established, we do not offer the item."),
        ("Data protection and confidentiality",
         "Customer information, specifications and tender material are held in confidence and used "
         "only for the purpose for which they were supplied. Access is limited to the personnel "
         "working on the enquiry. Retention periods and the route for data requests are set out in "
         "our Privacy Policy."),
        ("Anti-corruption and business conduct",
         "We do not offer, promise, give or accept any improper payment or advantage to obtain or "
         "retain business. This applies to our own personnel, to agents acting on our behalf, and "
         "to any local partner or sub-contractor engaged on a program. The position is unconditional."),
        ("Accuracy of published information",
         "We describe each manufacturer relationship using only the designation that manufacturer "
         "has approved, and we do not claim authorisations, approvals or partnership tiers that "
         "cannot be evidenced on request."),
    ]
    st = "".join('<div class="card rv"><span class="c-n">%02d</span><h3>%s</h3><p>%s</p></div>'
                 % (i + 1, t, b) for i, (t, b) in enumerate(statements))

    body = (
        hero(d, "dom-cyber", "About", "Compliance",
             "The positions we hold on export control, data protection, business conduct and the "
             "accuracy of what we publish.",
             None, "short", crumb(d, [("Home", ""), ("About", "about"), ("Compliance", None)]))
        + about_subnav(d, "about/quality")
        + """
<section class="section">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Compliance statements</p>
      <h2 class="rule-h">Positions we hold without exception.</h2>
      <p class="lede">Each of these is a commitment we can evidence. None of them is conditional on
        the size or urgency of the opportunity.</p></div>
    <div class="grid g2 gap-md">%s</div>
  </div>
</section>

<section class="section ink2">
  <div class="wrap"><div class="note" style="max-width:880px">
    <h4>Operational security in published content</h4>
    <p>We do not publish performance parameters, integration details, deployment locations, unit
      quantities, customer formation names or serial data for any delivered system. We do not
      publish images of any specific installation, of identifiable serving personnel, or of customer
      equipment markings, unit insignia, tail numbers or hull numbers. Detailed technical
      information is released only through a verified datasheet request, subject to customer
      clearance where it applies.</p>
  </div></div>
</section>
""" % st
        + cta_band(d))

    page("about/quality/index.html", "Compliance | Maalik Creative Engineers",
         "Our export control, data protection, anti-corruption and publishing accuracy positions.",
         body, active="about", depth=2)


# =========================================================================== FACILITIES
def build_facilities():
    d = 2
    facs = [
        ("Head office", "Corporate, commercial, procurement and contracts functions.", "about-facility"),
        ("Engineering and integration space", "System architecture, multi-vendor integration and "
         "acceptance testing.", "svc-integration"),
        ("Workshop and test capability", "Bench work, calibration, fault diagnosis and acceptance test "
         "against specification.", "svc-mro"),
        ("Secure storage", "Controlled storage for equipment awaiting inspection, clearance or "
         "hand-over.", "svc-logistics"),
        ("Depot and maintenance facility", "Depot level repair, overhaul and life extension for supported "
         "platforms.", "svc-tot"),
        ("Training delivery", "Operator, maintainer and train-the-trainer delivery, in English.",
         "svc-install"),
    ]
    cards = "".join(
        '<div class="icard rv"><div class="icard-img"><img src="%sassets/img/%s.jpg" alt="" loading="lazy">'
        '<span class="icard-tag">%02d</span></div><div class="icard-body"><h3>%s</h3><p>%s</p></div></div>'
        % (rel(d), img, i + 1, t, b) for i, (t, b, img) in enumerate(facs))

    body = (
        hero(d, "about-facility", "About", "Facilities",
             "Photograph the real facilities. Two credible in-house photographs beat twelve polished "
             "stock images, and this audience knows the difference.",
             None, "short", crumb(d, [("Home", ""), ("About", "about"), ("Facilities", None)]))
        + about_subnav(d, "about/facilities")
        + """
<section class="section">
  <div class="wrap">
    <div class="sec-head" style="max-width:820px"><p class="eyebrow">What we hold</p>
      <h2 class="rule-h">Where the work actually happens.</h2>
      <p class="lede">Where a facility is sensitive we describe its function and capability without
        publishing images or a precise location.</p></div>
    <div class="grid g3 gap-md">%s</div>
  </div>
</section>

<section class="section ink2">
  <div class="wrap"><div class="note" style="max-width:880px">
    <h4>Photography brief for this page</h4>
    <p>Shoot in available light with fill rather than key flash. Include hands: on equipment, on a
      keyboard, on a test instrument. Shoot at working eye level or slightly below. Capture the
      unglamorous, a spares rack, a cable loom, a torque wrench, a calibration certificate on a clipboard.
      Clear every frame before use: remove or blur customer markings, serial and part numbers, network
      diagrams, screens showing live data, whiteboards, documents and identifiable personnel. Apply one
      consistent grade across the whole library.</p>
  </div></div>
</section>
""" % cards
        + cta_band(d))

    page("about/facilities/index.html", "Facilities | Maalik Creative Engineers",
         "Head office, engineering and integration space, workshop and test capability, secure storage "
         "and depot maintenance.", body, active="about", depth=2)


# =========================================================================== INSIGHTS
ARTICLES = [
    ("Technical Brief", "eo-cooled",
     "Cooled against uncooled thermal imaging: choosing by mission profile",
     "A cooled detector buys you range and thermal sensitivity, and costs you cool-down time, "
     "power, acoustic signature and a finite compressor life. An uncooled detector starts "
     "instantly and runs for years. Neither is better; they answer different questions. This "
     "brief sets out the four mission characteristics that decide which one belongs in your "
     "requirement."),
    ("Technical Brief", "c3-tetra",
     "DMR, TETRA and broadband push-to-talk: selecting a formation architecture",
     "Three bearers, three cost structures, three failure modes. The decision is rarely about "
     "audio quality and almost always about coverage geometry, subscriber count, data "
     "requirement and what happens when the network is contested. We work through the "
     "selection in the order a formation communications officer would."),
    ("Technical Brief", "anti-uav",
     "Counter-UAS: why detection, identification and defeat are three procurements",
     "A system that detects but cannot positively identify will generate engagements against "
     "friendly and civil traffic. A system that can defeat but not identify is worse. Treating "
     "counter-UAS as one line item is the most common specification error we see, and the "
     "easiest to correct at requirement stage."),
    ("Technical Brief", "eo-border",
     "Specifying a border surveillance system: sensor mix, coverage geometry and sustainment",
     "Coverage is a geometry problem before it is a sensor problem. Mast height, terrain "
     "masking, overlap and the revisit interval you can tolerate set the sensor count; the "
     "sensor class then follows. Sustainment at a remote fixed site decides whether the system "
     "is still working in year three."),
    ("Technical Brief", "cy-architecture",
     "Building a managed security operations capability: in-house against managed service",
     "The question is not tooling. It is whether you can staff three shifts of trained analysts "
     "indefinitely, and what your detection coverage looks like at 0300 on a public holiday. We "
     "set out the staffing arithmetic that usually decides this, and the hybrid models that work "
     "when neither pure option fits."),
    ("Technical Brief", "ind-plant",
     "Transfer of technology: what genuinely transfers and what does not",
     "A transfer arrangement that is not specified in detail before signature does not happen "
     "after it. Documentation, tooling, test equipment, process knowledge and the right to "
     "modify are separate items and are negotiated separately. This brief lists what to write "
     "into the arrangement, item by item."),
    ("Newsroom", "eo-uncooled",
     "Shibli optronics portfolio added to the published catalogue",
     "The FALCON, SKUA, GUARDIAN, TARSIER, ORCA, ERMINE and TERRIER families, together with the "
     "Nightrider driver sight and See King marine system, are now published with full "
     "manufacturer photography. Shibli manufactures in Islamabad, which shortens support lines "
     "and removes the export licensing step entirely."),
    ("Newsroom", "c3-dmr-professional",
     "Hytera mission critical and business radio portfolio published in full",
     "Thirty-seven Hytera models across DMR, TETRA, push-to-talk over cellular and dual-mode "
     "are now listed individually, from the HP78X professional portable through to the PT890Ex "
     "intrinsically safe TETRA radio and the DS-6250S trunking base station."),
    ("Newsroom", "sc-bodycam",
     "Safe city and secure document capability extended",
     "SUNMI, ASY Anti-forgery, Genuine Printing, Everbridge and REDtone Digital Services join "
     "the partner network, extending the portfolio across business IoT terminals, "
     "anti-counterfeiting, high-security printing, critical event management and managed "
     "connectivity."),
    ("Events", "isr-radar-panel",
     "IDEAS, Karachi",
     "The International Defence Exhibition and Seminar is the principal defence exhibition in "
     "Pakistan and the point in the year where most manufacturer conversations start. We attend "
     "with our optronics and communications principals. Stand number and dates are published "
     "ahead of each edition."),
    ("Events", "av-combat-aircraft",
     "DSA, Kuala Lumpur",
     "Defence Services Asia is where we meet manufacturers looking for a route into Pakistan "
     "without establishing their own presence. If you are evaluating representation, this is "
     "the most efficient place to have that conversation in person."),
    ("Events", "c3-command-centre",
     "Regional critical communications forum",
     "Mission critical communications events are where the DMR, TETRA and broadband roadmap "
     "questions get answered directly by the people building the infrastructure. We attend with "
     "our communications principals."),
]


def build_insights():
    d = 1
    cards = "".join(
        '<a class="icard rv" data-cat="%s" href="%s"><div class="icard-img is-shot">'
        '<img src="%sassets/img/products/%s.jpg" alt="" loading="lazy" width="1000" height="750">'
        '<span class="icard-tag">%s</span></div>'
        '<div class="icard-body"><h3>%s</h3><p>%s</p>'
        '<span class="tlink">Request this brief <i class="arw"></i></span></div></a>'
        % (cat, url(d, "contact"), rel(d), img, cat.upper(), title, body)
        for cat, img, title, body in ARTICLES)

    body = (
        hero(d, "insights-band", "Insights", "Technical briefs,<br>not press releases.",
             "Three content types under one index: technical briefs written to help an evaluator "
             "make a decision, company announcements, and the exhibitions where we can be found.",
             None, "mini", crumb(d, [("Home", ""), ("Insights", None)]))
        + """
<section class="section" data-listfilter="cat">
  <div class="wrap">
    <div class="chips" style="margin-bottom:40px">
      <button class="chip on" data-lf="">All</button>
      <button class="chip" data-lf="Technical Brief">Technical Briefs</button>
      <button class="chip" data-lf="Newsroom">Newsroom</button>
      <button class="chip" data-lf="Events">Events and Exhibitions</button>
    </div>
    <div class="grid g3 gap-md">%s</div>
    <div class="note" style="margin-top:48px;max-width:860px">
      <h4>Full briefs on request</h4>
      <p>Each technical brief runs to 700 to 1,200 words and is authored and attributed to a named
        engineer. Ask for any of them by title and we will send the full text; there is no form and
        no registration.</p>
    </div>
  </div>
</section>
""" % cards
        + cta_band(d))

    page("insights/index.html", "Insights | Maalik Creative Engineers",
         "Technical briefs, company announcements and exhibition presence from Maalik Creative "
         "Engineers.", body, active="", depth=1)


# =========================================================================== CAREERS
def build_careers():
    d = 1
    disc = "".join('<div class="chip" style="cursor:default">%s</div>' % x for x in DISCIPLINES)

    body = (
        hero(d, "careers-team", "Careers", "Engineering that<br>has to work.",
             "The systems we deliver are used by people whose safety depends on them working. That "
             "is the standard the work is held to, and it is the reason the work is worth doing.",
             None, "short", crumb(d, [("Home", ""), ("Careers", None)]))
        + """
<section class="section">
  <div class="wrap"><div class="grid g2 gap-lg">
    <div>
      <p class="eyebrow">The work</p>
      <h2 class="rule-h">What you would actually be doing.</h2>
      <p style="color:var(--text-dim)">Translating an operational requirement into a specification,
        then into a system that is commissioned, integrated and supported. Not building
        demonstrators. Building things that go into service and stay there.</p>
      <p style="color:var(--text-dim)">You will work directly with manufacturers abroad, with the
        customer's technical staff, and with equipment on a bench. Professional development includes
        manufacturer training at the factory.</p>
    </div>
    <div>
      <p class="eyebrow">Disciplines</p>
      <div class="chips">%s</div>
    </div>
  </div></div>
</section>

<section class="section ink2">
  <div class="wrap">
    <div class="sec-head" style="max-width:780px"><p class="eyebrow">Open positions</p>
      <h2 class="rule-h">No vacancies at present.</h2>
      <p class="lede">We are not recruiting for a specific role right now. We do read speculative
        applications, and we keep them on file against the disciplines above &mdash; when a program
        creates a role, that file is where we look first.</p></div>
    <div class="btn-row">
      <a class="btn btn-primary" href="%s">Send a speculative application <i class="arw"></i></a>
    </div>
  </div>
</section>
""" % (disc, url(d, "contact"))
        + cta_band(d, "careers-team"))

    page("careers/index.html", "Careers | Maalik Creative Engineers",
         "Systems, RF, optronics, software, AI and cyber security engineering at a Pakistani "
         "defence and technology solutions house.", body, active="", depth=1)


# =========================================================================== DOWNLOADS
def build_downloads():
    d = 1
    ungated = [
        ("Corporate profile", "Company overview, capability summary and contact routes.", "PDF", "v1.0"),
        ("Capability overview", "The twelve capability domains in summary form.", "PDF", "v1.0"),
        ("Partner-facing company profile", "One page, written for manufacturers, suitable for "
         "circulation at exhibitions.", "PDF", "v1.0"),
    ]
    gated = [
        ("Domain capability statements", "One per capability domain, with family and system detail."),
        ("Product datasheets", "Full technical specification for a named system."),
        ("Technical specifications", "Interface, integration and configuration detail."),
    ]
    ug = "".join(
        '<div class="card rv">%s<span class="c-n">%s &middot; %s</span><h3>%s</h3><p>%s</p>'
        '<a class="tlink" href="#">Download <i class="arw"></i></a></div>'
        % (icon("doc"), fmt, ver, t, b) for t, b, fmt, ver in ungated)
    g = "".join('<div class="card rv">%s<span class="c-n">VERIFIED RELEASE</span><h3>%s</h3><p>%s</p>'
                '<a class="tlink" href="%s">Request access <i class="arw"></i></a></div>'
                % (icon("shield"), t, b, url(d, "contact/request-for-information")) for t, b in gated)

    body = (
        hero(d, "svc-procurement", "Downloads", "Documents, versioned<br>and dated.",
             "Corporate documents are open. Technical detail is released through a verified request. "
             "Every document carries a version number and a date.",
             None, "mini", crumb(d, [("Home", ""), ("Downloads", None)]))
        + """
<section class="section">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Open</p>
      <h2 class="rule-h">Available without a form.</h2>
      <p class="lede">Gating a corporate profile costs more than it earns. These are open.</p></div>
    <div class="grid g3 gap-md">%s</div>
  </div>
</section>

<section class="section ink2">
  <div class="wrap">
    <div class="sec-head" style="max-width:840px"><p class="eyebrow">Controlled release</p>
      <h2 class="rule-h">Released to verified enquirers.</h2>
      <p class="lede">Detection, recognition and identification ranges, sensor pitch and resolution,
        encryption details, frequency coverage, endurance and payload capacity, and any performance
        parameter for a weapon or air defence system sit behind this workflow. This is standard practice
        for reputable defence suppliers and is expected by our customers.</p></div>
    <div class="grid g3 gap-md">%s</div>
    <div class="note" style="margin-top:44px;max-width:860px">
      <h4>What the request captures</h4>
      <p>Organisation, role, official email domain and intended use. Requests are released manually after
        verification. We do not publish this material openly because doing so would damage credibility
        rather than build it.</p>
    </div>
  </div>
</section>
""" % (ug, g)
        + cta_band(d))

    page("downloads/index.html", "Downloads | Maalik Creative Engineers",
         "Corporate profile, capability overview and partner-facing profile, plus controlled release of "
         "datasheets and capability statements.", body, active="", depth=1)


# =========================================================================== LEGAL
LEGAL = {
    "privacy": ("Privacy Policy", "How we handle enquiry data, analytics and cookies.", [
        ("What we collect", "Information you submit through an enquiry form: name, organisation, role, "
         "email address, telephone number, the content of your message and any file you attach. We also "
         "collect standard technical information such as browser type and pages visited."),
        ("Why we hold it", "To respond to your enquiry, to prepare an offer where one is requested, and "
         "to administer a contract where one is awarded. We do not use enquiry data for marketing without "
         "your consent."),
        ("Retention", "Enquiry records are retained for 24 months and contract records for the "
         "period required by Pakistani law and by the terms of the contract, after which they are "
         "securely destroyed."),
        ("Cookies and analytics", "We use a privacy-respecting analytics configuration with IP "
         "anonymisation. No advertising or cross-site tracking cookies are set. A cookie preference "
         "control is presented on first visit."),
        ("Sharing", "We do not sell or share enquiry data. Where responding to your enquiry requires us "
         "to approach a manufacturer, we share only what is necessary and only with your knowledge."),
        ("Your rights and contact", "To request a copy of the data we hold about you, to correct it, or "
         "to ask for its deletion, contact us at the address on the Contact page."),
    ]),
    "terms": ("Terms of Use", "The basis on which this site is published.", [
        ("Purpose of this site", "This site describes capability. It is not an offer, and nothing on it "
         "constitutes a contractual commitment."),
        ("Product information is indicative", "Product descriptions, families and system designations are "
         "indicative. Specifications are subject to change without notice by the manufacturer. Binding "
         "specification is established only in a written offer or contract."),
        ("Third party marks", "Manufacturer names, trademarks and product designations remain the "
         "property of their owners and are used to identify the products described."),
        ("No warranty on availability", "Availability of any system depends on manufacturer supply, "
         "export licensing and end-use authorisation at the time of enquiry."),
        ("Governing law", "These terms are governed by the laws of the Islamic Republic of Pakistan."),
    ]),
    "export-control": ("Export Control and Compliance Statement",
                       "End use, end-user documentation and origin-country regimes.", [
        ("Authorised end users only", "We supply defence and security equipment only to authorised end "
         "users: the Pakistan Armed Forces, strategic organisations, law enforcement and civil armed "
         "forces, and other bodies lawfully mandated to hold the equipment concerned."),
        ("Origin country regimes", "We comply with the export control regimes of the countries of origin "
         "of the equipment we supply. Where an export licence is required from the country of origin, the "
         "licensing position is established before any commitment is offered."),
        ("End-user documentation", "Where the manufacturer or the country of origin requires end-user "
         "certification or a non-re-export undertaking, we require and obtain that documentation before "
         "shipment."),
        ("No re-export or diversion", "We do not participate in any arrangement intended to divert "
         "controlled equipment from its declared end user or declared end use."),
        ("Refusal", "Where a lawful, documented route cannot be established, we decline the requirement. "
         "That position is not negotiable."),
    ]),
    "accessibility": ("Accessibility Statement", "Our commitment and how to report a problem.", [
        ("Standard", "This site is built to meet WCAG 2.2 Level AA. That covers colour contrast, keyboard "
         "operability, focus visibility, text alternatives for images, and structure that works with a "
         "screen reader."),
        ("Known limitations", "Embedded third-party content such as a map may not fully meet the "
         "standard. Where that is the case, the same information is available in text form on the same "
         "page."),
        ("Reduced motion", "Animation is limited and respects the operating system reduced-motion "
         "preference."),
        ("Reporting a problem", "If you encounter an accessibility barrier on this site, contact us "
         "through the Contact page and we will respond within one working day and correct the issue."),
    ]),
}


def build_legal(slug):
    d = 2
    title, sub, blocks = LEGAL[slug]
    secs = "".join('<div style="margin-bottom:40px"><h3 style="margin-bottom:.9rem">%s</h3>'
                   '<p class="measure" style="color:var(--text-dim)">%s</p></div>' % b for b in blocks)
    body = (
        hero(d, "dom-avionics", "Legal", title, sub, None, "mini",
             crumb(d, [("Home", ""), ("Legal", None), (title, None)]))
        + """
<section class="section">
  <div class="wrap wrap-narrow">
    <p class="mono" style="color:var(--text-faint);margin-bottom:40px">
      Version 1.0 &nbsp;&middot;&nbsp; Last updated 28 August 2026 &nbsp;&middot;&nbsp; %s</p>
    %s
    <div class="note"><h4>Questions about this document</h4>
      <p>Contact us through the <a class="tlink" style="display:inline-flex" href="%s">Contact page</a>.
        We acknowledge every enquiry within one working day.</p></div>
  </div>
</section>
""" % (COMPANY["legal"], secs, url(d, "contact")))
    page("legal/%s/index.html" % slug, "%s | Maalik Creative Engineers" % title, sub,
         body, active="", depth=2)


# =========================================================================== SYSTEM PAGES
def build_search():
    d = 1
    body = (
        hero(d, "dom-ai", "Search", "Search the portfolio.",
             "Search runs across product designations, family names, capability domains and application "
             "tags. The product index carries the full facet set.",
             None, "mini", crumb(d, [("Home", ""), ("Search", None)]))
        + """
<section class="section">
  <div class="wrap wrap-narrow">
    <form class="form" action="%s" method="get">
      <div class="field">
        <label for="q">Search designation, family, domain or application</label>
        <input id="q" name="q" type="search" placeholder="FALCON, TETRA, counter-UAS, managed SOC&hellip;">
        <p class="hint">Your search runs against the full product index and produces a shareable URL.</p>
      </div>
      <button class="btn btn-primary" type="submit">Search the index <i class="arw"></i></button>
    </form>
    <div style="margin-top:56px">
      <p class="eyebrow">Common destinations</p>
      <div class="chips">%s</div>
    </div>
  </div>
</section>
""" % (url(d, "products"),
       "".join('<a class="chip" href="%s">%s</a>' % (url(d, "capabilities/" + x["slug"]), x["short"])
               for x in DOMAINS)))
    page("search/index.html", "Search | Maalik Creative Engineers",
         "Search across product designations, family names, capability domains and application tags.",
         body, active="", depth=1)


def build_404():
    d = 0
    body = (
        hero(d, "band-dark", "404", "That page is not where<br>you expected it to be.",
             "The link may be out of date, or the page may have moved during the consolidation of our "
             "previous sites.",
             [("Capabilities", url(d, "capabilities"), "btn-primary"),
              ("Product index", url(d, "products"), "btn-ghost"),
              ("Contact", url(d, "contact"), "btn-ghost")], "short")
        + """
<section class="section">
  <div class="wrap">
    <div class="sec-head"><p class="eyebrow">Capability domains</p>
      <h2 class="rule-h">Try one of these.</h2></div>
    """ + domain_cards(d) + """
  </div>
</section>
""")
    page("404.html", "Page not found | Maalik Creative Engineers",
         "The page you requested could not be found.", body, active="", depth=0)
