# -*- coding: utf-8 -*-
"""
Content model for the Maalik Creative Engineers website.
Every string here traces back to the Master Website Content and Architecture Guide.
Section references are given in comments so copy can be audited against the source.
"""

COMPANY = {
    "name": "Maalik Creative Engineers",
    "legal": "Maalik Creative Engineers (Private) Limited",
    "established": "2010",
    "reg_line": "Maalik Creative Engineers (Private) Limited. Established 2010. Registered in Pakistan.",
    "strn": "32277876222068",
    "ntn": "3395905-6",
    "address": ["Office 4-10, 3rd Floor, Al Babar Center",
                "F-8 Markaz",
                "Islamabad, Pakistan"],
    "tel": "+92-51-2204040",
    "mobile": "+92 300 8612572",
    "email": "info@maaliksoft.com",
    "hours": "Monday to Friday, 0900 to 1730 Pakistan Standard Time (UTC+5)",
    "linkedin": "#",
    "maps_q": "Al Babar Center, F-8 Markaz, Islamabad, Pakistan",
}


# Section 1.2 -- approved descriptors
DESCRIPTORS = {
    "hero_sub": "Maalik Creative Engineers supplies, integrates and supports mission critical technology "
                "for the Pakistan Armed Forces, strategic organisations and law enforcement agencies, "
                "backed by a vetted international manufacturing network.",
    "meta": "Maalik Creative Engineers supplies, integrates and supports mission critical defence and "
            "security technology in Pakistan, from tactical communications and optronics to cyber "
            "security, unmanned systems and AI.",
    "footer": "A Pakistani defence and technology solutions house working with an international "
              "manufacturing network to deliver, integrate and sustain mission critical capability.",
}

# Section 8.1 -- boilerplate
BOILERPLATE = {
    "short": "Established in 2010, Maalik Creative Engineers supplies, integrates and sustains mission "
             "critical defence and security technology for the Pakistan Armed Forces, strategic "
             "organisations and law enforcement agencies.",
    "medium": "Maalik Creative Engineers (Private) Limited was established in 2010 as a Pakistani defence, "
              "security and advanced technology solutions house. We source, integrate and sustain mission "
              "critical systems across communications, electro-optics, unmanned systems, air defence, "
              "avionics, cyber security and applied artificial intelligence. Working with a vetted "
              "international manufacturing network and our own engineering base in Pakistan, we deliver "
              "capability that arrives complete and stays supported.",
    "long": "Maalik Creative Engineers (Private) Limited, established in 2010, is a Pakistani defence, "
            "security and advanced technology solutions house serving the Pakistan Armed Forces, strategic "
            "organisations and law enforcement agencies. We operate across twelve capability domains, from "
            "tactical communications and electro-optic sighting to unmanned systems, air defence, avionics, "
            "cyber security and applied artificial intelligence. Our model combines direct relationships "
            "with manufacturers across Asia, Europe and North America with engineering, procurement, "
            "logistics and support capability inside Pakistan. That means a customer receives not a shipment "
            "but a working capability, commissioned, integrated, with trained operators and a sustainment "
            "plan behind it. Where a requirement has no existing supplier, we identify, qualify and bring in "
            "a manufacturer to meet it.",
}

# Section 8.4 -- reusable standing blocks
STANDING = {
    "support": "Every system we supply comes with a support arrangement, not an assumption of one. That "
               "means initial spares provisioning, in-country service capability, operator and maintainer "
               "training delivered in English, warranty administration, structured post-warranty support, "
               "and access to depot level repair, overhaul and life extension where the platform requires it.",
    "integration": "A sensor that does not report into a command system is an observation, not a capability. "
                   "We design and deliver the connections as deliberately as we deliver the equipment.",
    "procurement": "We prepare offers that are complete, compliant and easy to evaluate. That means correct "
                   "documentation, accurate costing, clear technical compliance statements and a submission "
                   "that will not be set aside on a technicality.",
    "confidentiality": "Details of individual programs, including scope, quantities and customer identity, "
                       "are held in confidence. Further information is available to qualified enquirers on "
                       "request, subject to customer clearance.",
}

# Section 1.3 -- value proposition pillars
PILLARS = [
    ("Access", "A vetted global manufacturing base",
     "Named OEM relationships across Asia, Europe and North America. Direct factory access rather than "
     "layered brokerage, with principal-to-principal engagement and factory acceptance testing arranged "
     "where a program requires it.", "01"),
    ("Integration", "Systems, not shipments",
     "In-house engineering that integrates sensors, communications, command and control and analytics from "
     "multiple manufacturers into one working chain, with system architecture and design held in-house.", "02"),
    ("Sustainment", "Supported for the whole life of the equipment",
     "Spares provisioning, local maintenance and overhaul, depot level facilities, warranty and post-warranty "
     "service, operator and maintainer training, and life extension of in-service systems.", "03"),
    ("Procurement fluency", "Fluent in how you buy",
     "Working knowledge of Pakistan public procurement rules and PPRA process, bid preparation and "
     "documentation discipline, technical and commercial evaluation support, and contract management from "
     "award to closure.", "04"),
]

# Section 4.1 Block 6 -- the delivery model
DELIVERY = [
    ("01", "Requirement definition",
     "We work with your technical staff to translate an operational need into a precise, procurable specification."),
    ("02", "Source qualification",
     "We identify and technically qualify manufacturers against the specification, then arrange principal-level engagement."),
    ("03", "Commercial and contractual structuring",
     "Costing, offer preparation and documentation aligned to public procurement rules and your tender conditions."),
    ("04", "Delivery, inspection and clearance",
     "Pre-shipment inspection, freight, port clearance, inland transport and hand-over."),
    ("05", "Installation, integration and training",
     "Commissioning, integration into existing systems, and operator and maintainer training."),
    ("06", "Through-life support",
     "Spares, warranty and post-warranty service, depot maintenance, overhaul and life extension."),
]

# Section 4.4 -- Beyond the Catalogue, the six step method
METHOD = [
    ("Requirement interrogation",
     "We work with your technical staff to separate the operational effect required from the equipment "
     "assumed. Very often the assumed equipment is not the only route to the effect, and identifying that "
     "early widens the sourcing field considerably."),
    ("Global source identification",
     "We survey the international manufacturing base for candidates, including manufacturers with no "
     "existing presence in Pakistan and manufacturers whose products are adjacent to the requirement and "
     "can be adapted."),
    ("Technical qualification",
     "We assess candidates against the specification, request evidence, arrange technical exchange, and "
     "where necessary arrange factory or third-party testing."),
    ("Commercial and compliance qualification",
     "We verify the manufacturer commercially, establish the export licensing position in the country of "
     "origin, and confirm that a lawful, documented route to Pakistan exists before any commitment is offered."),
    ("Structuring and offer",
     "We build the offer to align with the applicable public procurement framework and your tender "
     "conditions, including documentation, warranties, delivery terms and support commitments."),
    ("Delivery and sustainment",
     "From that point the requirement is handled exactly as any catalogue item: inspection, clearance, "
     "installation, training, spares and through-life support."),
]

SECTOR_REACH = [
    "Enterprise software and custom development", "Mobile applications", "Blockchain",
    "E-commerce platforms", "Game and simulation development", "IoT and embedded systems",
    "Industrial plant and equipment", "Specialised raw materials and alloys",
    "Test and measurement instrumentation", "Energy efficiency and environmental monitoring",
    "Specialist technical staffing",
]

# ---------------------------------------------------------------------------
# Section 3.2 / Section 5 -- the twelve capability domains
# families: (name, blurb, placement) ; models: (designation, class, placement)
# ---------------------------------------------------------------------------
DOMAINS = [
    {
        "n": "01", "slug": "command-control-communications",
        "name": "Command, Control and Communications", "short": "Command, Control &amp; Communications",
        "nav": "C3 and Communications",
        "def": "Tactical and strategic communications, command and control systems, and the networks that carry them.",
        "hero": "Keeping the chain of command intact when everything else is contested.",
        "img": "dom-c3", "icon": "c3",
        "meta_title": "Tactical Communications and C4 Systems | Maalik",
        "meta_desc": "DMR and TETRA radios, trunked systems, private broadband, satellite communications and integrated command and control.",
        "overview": [
            "This domain covers everything that carries a decision from the commander to the executing "
            "element and everything that carries the picture back. It spans narrowband tactical radio, "
            "wide-area trunked networks, private broadband, satellite links, and the command and control "
            "software that sits above them.",
            "The operational problems it addresses are coverage, interoperability and survivability. "
            "Formations rarely fail for want of a radio. They fail because two agencies cannot talk to one "
            "another, because coverage does not reach the ground being held, or because a single bearer "
            "carries the whole plan.",
            "We supply the radios, the infrastructure and the dispatch layer, and we take responsibility for "
            "making them work together as one network rather than as a set of procurements.",
        ],
        "glance": ["Narrowband tactical", "Trunked wide-area", "Broadband and satellite", "Command and dispatch"],
        "families": [
            ("Command and control systems", "Network centric warfare solutions, combat management systems, tactical data links and deployable command posts.", "FP"),
            ("Integrated command, control and dispatch", "Control room platforms unifying radio, telephony, video, sensors and dispatch into a single operator position.", "FP"),
            ("DMR professional and mission critical radios", "Seventeen professional and intrinsically safe DMR portables and mobiles for mission critical formation use.", "FP"),
            ("DMR business and commercial radios", "Thirteen business-class DMR portables and mobiles for site, estate and commercial security use.", "FP"),
            ("DMR infrastructure", "Tier II conventional repeaters, multi-site repeater networks and Tier III trunking systems.", "FP"),
            ("TETRA radios and systems", "Mission critical and intrinsically safe TETRA portables and mobiles, plus base stations, switching and dispatch.", "FP"),
            ("Broadband, PoC and multi-band radio", "Software-defined multi-band tactical radios, push-to-talk over cellular families and dual-mode rugged terminals.", "FP"),
            ("4G and 5G broadband infrastructure", "Packet core, macro and one-box base stations, and unified network management for private broadband.", "FP"),
            ("Satellite communications", "Fixed, transportable and on-the-move terminals, RF components and end-to-end satellite network design.", "FP"),
            ("Antennas, RF conditioning and site infrastructure", "Base station antennas, transmitter combiners, duplexers, cavity filters, isolators and preselectors.", "FP"),
            ("Communication vehicles and rapid deployment", "Light, medium and large communication vehicles, mobile command centres and rapidly deployable kits.", "FP"),
            ("Radio accessories and ancillaries", "Batteries, charging, audio accessories, covert kits, car-kits, cases, cables and antennas as a filterable range.", "FP"),
        ],
        "models": [
            ("HP78X", "Professional DMR portable", "PP"), ("HP78X UL913", "Intrinsically safe DMR portable", "PP"),
            ("HP70X", "Professional DMR portable", "PP"), ("HP70X UL913", "Intrinsically safe DMR portable", "PP"),
            ("HP68X", "Professional DMR portable", "PP"), ("HP60X", "Professional DMR portable", "PP"),
            ("HP56X", "Professional DMR portable", "PP"), ("HP56X UL913", "Intrinsically safe DMR portable", "PP"),
            ("HP50X", "Professional DMR portable", "PP"), ("HP50X UL913", "Intrinsically safe DMR portable", "PP"),
            ("HP79XEx IIC", "Intrinsically safe DMR portable, gas group IIC", "PP"),
            ("HP79XEx IIA", "Intrinsically safe DMR portable, gas group IIA", "PP"),
            ("HP71XEx IIC", "Intrinsically safe DMR portable, gas group IIC", "PP"),
            ("HP71XEx IIA", "Intrinsically safe DMR portable, gas group IIA", "PP"),
            ("HM78X", "Professional DMR mobile", "PP"), ("HM68X", "Professional DMR mobile", "PP"),
            ("HM65X", "Professional DMR mobile", "PP"),
            ("S1 Pro / S1 Pro LF", "S series business two-way radio", "PP"),
            ("BP56X", "Business DMR portable", "CP"), ("BP51X", "Business DMR portable", "CP"),
            ("BP36X", "Ultralight business DMR portable", "CP"), ("PD40X", "Business DMR portable", "CP"),
            ("PD41X", "Business DMR portable", "CP"), ("PD48X", "Business DMR portable", "CP"),
            ("PD36X", "Business DMR portable", "CP"), ("BD50X", "Business DMR portable", "CP"),
            ("BD55X", "Business DMR portable", "CP"), ("BD61X", "Business DMR portable", "CP"),
            ("MD61X", "Business DMR mobile", "CP"), ("MD62X", "Business DMR mobile", "CP"),
            ("DS-6250S", "Compact DMR trunking base station", "PP"),
            ("PT590", "Mission critical TETRA portable radio", "PP"),
            ("PT580H Plus", "Mission critical TETRA portable radio", "PP"),
            ("PT580H Plus UL913", "Intrinsically safe TETRA portable radio", "PP"),
            ("PT560H", "Mission critical TETRA portable radio", "PP"),
            ("PT890Ex", "Intrinsically safe TETRA portable radio", "PP"),
            ("MT680 Plus", "Mission critical TETRA mobile radio", "PP"),
            ("PTC680", "Dual-mode TETRA and broadband rugged radio", "PP"),
            ("P5 series", "Push-to-talk over cellular radio family", "PP"),
            ("P60", "Push-to-talk over cellular radio", "PP"),
            ("PNC660", "Push-to-talk over cellular smart radio", "PP"),
            ("PDC680", "Dual-mode rugged radio and smartphone", "PP"),
        ],
        "related": ["intelligence-surveillance-reconnaissance", "electronic-warfare", "safe-city-critical-infrastructure"],
    },
    {
        "n": "02", "slug": "intelligence-surveillance-reconnaissance",
        "name": "Intelligence, Surveillance and Reconnaissance", "short": "ISR",
        "nav": "ISR",
        "def": "Sensors, radars, unmanned platforms and the systems that turn observation into a picture.",
        "hero": "Seeing further, earlier, and in conditions that defeat the unaided eye.",
        "img": "dom-isr", "icon": "isr",
        "meta_title": "ISR Systems and Radar | Maalik Creative Engineers",
        "meta_desc": "Airborne, ground, maritime and underwater surveillance radar, reconnaissance systems and sensor integration.",
        "overview": [
            "ISR is not a category of equipment. It is the process of converting dispersed observation into "
            "a single picture that a commander can act on. This domain covers the sensors that observe and "
            "the architecture that fuses them.",
            "We supply airborne, ground, maritime and sub-surface sensing, from podded reconnaissance "
            "systems and multi-mode airborne radar to man-portable ground surveillance radar, coastal "
            "surface search sets, hull-mounted and towed sonar, and fixed underwater surveillance for "
            "harbours and approaches.",
            "The work that matters is rarely the sensor alone. It is cueing one sensor from another and "
            "delivering the result into a command system in a form that can be used.",
        ],
        "glance": ["Airborne", "Ground", "Maritime", "Underwater"],
        "families": [
            ("Unmanned aerial systems for ISR", "Airborne reconnaissance platforms and their sensor payloads. Cross-listed with Unmanned Systems.", "FP"),
            ("Airborne radars", "Fire control, surveillance and multi-mode radars for fixed and rotary wing platforms.", "FP"),
            ("Reconnaissance pods", "Podded electro-optical and multi-sensor reconnaissance systems for aircraft.", "FP"),
            ("Air defence radars", "Surveillance and target acquisition radars supporting air defence engagement.", "FP"),
            ("Ground surveillance radars", "Man-portable, tripod and vehicle-mounted radars for ground movement detection.", "FP"),
            ("Maritime radars", "Surface search, navigation and coastal surveillance radars.", "FP"),
            ("Sonar systems", "Hull-mounted, towed and portable sonar for sub-surface detection.", "FP"),
            ("Underwater surveillance systems", "Fixed and deployable underwater detection and monitoring for harbours and approaches.", "FP"),
        ],
        "models": [
            ("Multi-mission multi-function radar", "Modular radar for simultaneous ground, coastal and low-altitude air surveillance", "PP"),
            ("Radar and electro-optical integrated system", "Vehicle-mounted radar cued to a stabilised EO sensor for detection, classification and tracking", "PP"),
            ("Artillery and counter-battery radar", "Weapon locating radar supporting counter-battery and fire correction", "CP"),
            ("Airborne early warning and control", "AEW&amp;C aircraft mission systems and support", "CP"),
        ],
        "related": ["electro-optics-night-vision", "unmanned-systems-counter-uas", "command-control-communications"],
    },
    {
        "n": "03", "slug": "electro-optics-night-vision",
        "name": "Electro-Optics and Night Vision", "short": "Electro-Optics &amp; Night Vision",
        "nav": "Electro-Optics and Night Vision",
        "def": "Thermal, image intensified and multispectral sighting, observation and surveillance systems.",
        "hero": "Operational effectiveness through darkness, dust, haze and smoke.",
        "img": "dom-eo", "icon": "eo",
        "meta_title": "Thermal Imaging and Night Vision Systems | Maalik",
        "meta_desc": "Cooled and uncooled thermal sights, night vision, border surveillance and combat optronics for land, naval and air use.",
        "overview": [
            "Electro-optics decide what a force can do between last light and first light, and what it can "
            "do through the dust, haze and smoke that defeat the unaided eye for much of the rest of the day.",
            "This domain covers cooled and uncooled thermal imaging, image intensified night vision, and the "
            "multispectral sighting and observation systems built on them. It runs from a compact clip-on "
            "module ahead of an existing day optic to a continuously scanning border surveillance mast.",
            "It is also the domain where Pakistani manufacturing is strongest. A significant part of this "
            "portfolio is produced domestically, which shortens support lines and removes the export "
            "licensing step entirely.",
        ],
        "glance": ["Cooled thermal", "Uncooled thermal", "Image intensified", "Fixed surveillance"],
        "families": [
            ("Handheld surveillance and forward observation, cooled", "Cooled multifunction thermal binoculars for long range handheld surveillance and forward artillery observation.", "FP"),
            ("Handheld surveillance and forward observation, uncooled", "Uncooled multipurpose thermal binoculars in 640 and 1280 detector classes, long range and compact variants.", "FP"),
            ("Portable command and control units", "Rugged portable C2 boxes with integrated display and charging for multipurpose and long range thermal sights.", "FP"),
            ("Border, coastal and base surveillance", "Cooled and uncooled electro-optical surveillance systems with continuous 360 degree coverage.", "FP"),
            ("Combat optronics", "Thermal weapon and observation sights, laser rangefinder variants and clip-on modules.", "FP"),
            ("Image intensified night vision", "Night vision goggles, monoculars and head-mounted displays.", "FP"),
            ("Vehicle and marine optronics", "Driver night sights for vehicle mobility and marine thermal systems for navigation and surface surveillance.", "FP"),
            ("Observation, aiming and general optronics", "Multi-purpose observation devices, laser aiming modules, day sights, mounts and rangefinding optics.", "FP"),
            ("Optronic accessories and ancillaries", "Tripod interfaces, system cables, power, recording, display, carriage and cleaning ancillaries.", "FP"),
        ],
        "models": [
            ("FALCON", "Cooled multifunction thermal binocular, long range surveillance and forward artillery observation", "PP"),
            ("SKUA MP PRO 640", "Uncooled multipurpose thermal binocular, 640 class detector", "PP"),
            ("SKUA MP PRO 1280", "Uncooled multipurpose thermal binocular, 1280 class detector", "PP"),
            ("SKUA-LR", "Long range handheld thermal binocular", "PP"),
            ("SKUA MINI", "Short range compact handheld thermal binocular", "PP"),
            ("C2 / SKUA MP PRO", "Rugged portable C2 unit with integrated display and charging", "PP"),
            ("C2 / SKUA LR", "Rugged portable C2 unit without display, for long range binoculars", "PP"),
            ("GUARDIAN PRO", "Cooled EO surveillance system, 360 degree continuous coverage", "PP"),
            ("GUARDIAN 100mm 640", "Uncooled border surveillance system, 100 mm optic, 640 class", "PP"),
            ("GUARDIAN 25-150 1280", "Uncooled border surveillance system, 25 to 150 mm continuous zoom, 1280 class", "PP"),
            ("GUARDIAN 150 1280", "Uncooled border surveillance system, 150 mm optic, 1280 class", "PP"),
            ("TARSIER MINI 50", "Compact thermal monocular and weapon sight", "PP"),
            ("TARSIER MINI 50 LRF", "Compact thermal monocular with integrated laser rangefinder", "PP"),
            ("TARSIER LR 80", "Long range thermal scope and sight", "PP"),
            ("TARSIER LRF 80", "Long range thermal scope with integrated laser rangefinder", "PP"),
            ("TARSIER clip-on", "Clip-on thermal module for use forward of an existing day optic", "PP"),
            ("ORCA-NV", "Image intensified night vision goggles", "PP"),
            ("ERMINE-NV", "Image intensified night vision goggles", "PP"),
            ("TERRIER NV", "Image intensified night vision monocular", "PP"),
            ("Head mount display", "Hands-free head-mounted display for thermal and night vision output", "PP"),
            ("Nightrider", "Driver night sight for vehicle mobility in total darkness", "PP"),
            ("See King", "Marine thermal imaging for shipborne navigation, watchkeeping and surface surveillance", "PP"),
        ],
        "related": ["intelligence-surveillance-reconnaissance", "weapon-systems-munitions", "unmanned-systems-counter-uas"],
    },
    {
        "n": "04", "slug": "unmanned-systems-counter-uas",
        "name": "Unmanned Systems and Counter-UAS", "short": "Unmanned Systems &amp; C-UAS",
        "nav": "Unmanned Systems and C-UAS",
        "def": "Unmanned aerial platforms, their payloads, and the systems that detect and defeat hostile drones.",
        "hero": "Extending reach without extending exposure, and denying the same advantage to an adversary.",
        "img": "dom-uas", "icon": "uas",
        "meta_title": "Unmanned Systems and Counter-UAS | Maalik",
        "meta_desc": "ISR, loitering and FPV unmanned aerial systems, payloads, and counter-drone detection, identification and defeat.",
        "overview": [
            "Unmanned systems have changed the arithmetic of reconnaissance and of precision effect. They "
            "have also handed the same advantage to every adversary, which is why this domain is written as "
            "two halves that must be procured together.",
            "On the platform side we supply loitering and ISR fixed-wing systems, compact VTOL "
            "reconnaissance quadcopters, tactical FPV platforms, and the electro-optical, infrared, radar "
            "and communications payloads they carry, including arrangements for technology transfer and "
            "local co-production.",
            "On the counter side, detection, identification and defeat are three separate procurement "
            "problems. A system that detects but cannot positively identify will generate engagements "
            "against friendly and civil traffic. We supply and integrate all three.",
        ],
        "glance": ["Loitering and strike", "ISR platforms", "Payloads", "Detect, identify, defeat"],
        "families": [
            ("Unmanned aerial systems, general", "Tactical, medium altitude and mission-specific systems sourced to requirement, including transfer of technology and local co-production.", "FP"),
            ("UAV payloads", "Electro-optical, infrared, radar and communications payloads for unmanned platforms.", "FP"),
            ("Aerial target drones", "Aerial target systems for live-fire training and system qualification.", "FP"),
            ("Integrated anti-UAV defence system", "Vehicle-mounted architecture combining detection, identification and defeat into a single deployable system.", "FP"),
        ],
        "models": [
            ("SKYSTRYX Loitering UAV", "Autonomous loitering precision strike unmanned aerial vehicle", "PP"),
            ("SKYSTRYX ISR UAV", "Long endurance fixed-wing ISR unmanned aerial vehicle", "PP"),
            ("SkyGuard-M1", "Compact vertical take-off and landing reconnaissance quadcopter", "PP"),
            ("SkyGuard-MIS", "Tactical first-person-view strike quadcopter", "PP"),
            ("Counter-UAS detection radar", "Radar optimised for small, slow, low-altitude aerial targets", "PP"),
            ("Radar and EO counter-UAS system", "Radar-cued electro-optical identification and tracking for positive classification", "PP"),
            ("Counter-UAS jamming equipment", "Vehicle-mounted and fixed-site RF countermeasure equipment", "PP"),
        ],
        "related": ["intelligence-surveillance-reconnaissance", "air-defence-systems", "electronic-warfare"],
    },
    {
        "n": "05", "slug": "air-defence-systems",
        "name": "Air Defence Systems", "short": "Air Defence",
        "nav": "Air Defence Systems",
        "def": "Layered ground based and shipborne air defence, from man-portable to medium altitude.",
        "hero": "Layered protection from the shoulder-launched engagement to medium altitude area defence.",
        "img": "dom-airdef", "icon": "airdef", "restricted": True,
        "meta_title": "Layered Air Defence Systems | Maalik",
        "meta_desc": "Ground based and shipborne air defence from man-portable to medium altitude, with radar integration and depot support.",
        "overview": [
            "Air defence is procured as an architecture, not as a set of launchers. Each tier exists to cover "
            "the gap the tier above it cannot close, and the surveillance and target acquisition chain that "
            "cues them is as much a part of the capability as the effector.",
            "We supply across the layers: high to medium altitude area systems, low to medium altitude point "
            "and area systems, pedestal mounted short range systems for vehicle and static use, "
            "shoulder-launched very short range systems, and shipborne point and area defence.",
            "We also establish the depot maintenance facilities and life extension programs that keep an "
            "air defence inventory available rather than nominally held.",
        ],
        "glance": ["Very short range", "Short to medium range", "Medium altitude area", "Shipborne"],
        "families": [
            ("High to medium altitude air defence systems", "Area air defence systems for the upper tier of a layered architecture.", "FP"),
            ("Low to medium altitude air defence systems", "Medium range point and area defence systems.", "FP"),
            ("Pedestal mounted air defence systems", "Vehicle and static pedestal mounted short range air defence.", "FP"),
            ("Man portable air defence systems", "Shoulder-launched very short range air defence systems.", "FP"),
            ("Shipborne air defence missile systems", "Naval point and area air defence systems.", "FP"),
            ("Air defence maintenance and depot facilities", "Establishment of in-country maintenance centres for air defence systems.", "FP"),
            ("Missile life extension programs", "Inspection, refurbishment, component replacement and service life extension of in-service missiles.", "FP"),
        ],
        "models": [],
        "related": ["intelligence-surveillance-reconnaissance", "unmanned-systems-counter-uas", "weapon-systems-munitions"],
    },
    {
        "n": "06", "slug": "weapon-systems-munitions",
        "name": "Weapon Systems and Munitions", "short": "Weapon Systems &amp; Munitions",
        "nav": "Weapon Systems and Munitions",
        "def": "Precision guided munitions, underwater weapons, small arms, armament and ammunition.",
        "hero": "Precision effect, delivered from land, air and sub-surface platforms.",
        "img": "dom-weapons", "icon": "weapons", "restricted": True,
        "meta_title": "Weapon Systems and Munitions | Maalik",
        "meta_desc": "Precision guided munitions, underwater weapons, service small arms, armament and ammunition with full documentation and support.",
        "overview": [
            "This domain is described functionally and neutrally. We list class, role and platform "
            "compatibility. Performance parameters are not published on open pages.",
            "The portfolio covers precision guided munitions for surface-to-surface and air-to-ground "
            "delivery including satellite guided bombs and guidance kits, lightweight and heavyweight "
            "torpedo systems, and the service small arms, support weapons and ammunition used by armed "
            "forces and law enforcement.",
            "Every item in this domain is supplied against end-user documentation and the export control "
            "regime of the country of origin, with the compliance route confirmed before any commitment is offered.",
        ],
        "glance": ["Precision guided", "Underwater", "Small arms", "Ammunition"],
        "families": [
            ("Surface-to-surface missiles and rockets", "Guided surface-to-surface missile and rocket systems.", "FP"),
            ("Air-to-ground rockets", "Guided air-to-ground rocket systems for fixed and rotary wing platforms.", "FP"),
            ("GPS guided air-to-surface bombs", "Satellite guided air-delivered munitions and guidance kits.", "FP"),
            ("Lightweight torpedoes", "Anti-submarine lightweight torpedo systems.", "FP"),
            ("Heavyweight torpedoes", "Submarine and surface launched heavyweight torpedo systems.", "FP"),
            ("Hand guns and service pistols", "Full size, compact and sub-compact service pistols for armed forces and law enforcement.", "FP"),
            ("Assault rifles", "Standard issue assault rifles in service calibres.", "FP"),
            ("Sniper and designated marksman rifles", "Precision rifles and associated sighting systems.", "FP"),
            ("Grenade launchers", "Under-barrel and standalone grenade launcher systems.", "FP"),
            ("Ammunition", "Small arms and support weapon ammunition in service calibres.", "FP"),
            ("Weapon optics and accessories", "Sighting systems, laser aiming modules, mounts and furniture.", "FP"),
        ],
        "models": [],
        "related": ["electro-optics-night-vision", "air-defence-systems", "platforms-vehicles"],
    },
    {
        "n": "07", "slug": "electronic-warfare",
        "name": "Electronic Warfare", "short": "Electronic Warfare",
        "nav": "Electronic Warfare",
        "def": "Airborne, land, naval and underwater electronic support, attack and protection.",
        "hero": "Control of the electromagnetic spectrum across air, land, sea and sub-surface.",
        "img": "dom-ew", "icon": "ew", "restricted": True,
        "meta_title": "Electronic Warfare Systems | Maalik Creative Engineers",
        "meta_desc": "Airborne, land, naval and underwater electronic support, attack and protection, plus monitoring, direction finding and jamming.",
        "overview": [
            "Every other capability on this site depends on the electromagnetic spectrum, which makes the "
            "spectrum itself contested ground. Electronic warfare is how that ground is held.",
            "We supply self-protection, electronic support and electronic attack systems for airborne "
            "platforms, deployable and static systems for land formations, naval electronic support "
            "measures and countermeasures, and torpedo countermeasures, acoustic decoys and expendable "
            "underwater countermeasures.",
            "We also supply spectrum monitoring, direction finding and jamming systems for force protection "
            "and security applications, including convoy and site protection equipment.",
        ],
        "glance": ["Airborne", "Land", "Naval", "Underwater"],
        "families": [
            ("Airborne electronic warfare systems", "Self-protection, electronic support and electronic attack systems for airborne platforms.", "FP"),
            ("Land based electronic warfare", "Deployable and static electronic support and electronic attack systems for land formations.", "FP"),
            ("Ship-borne electronic warfare systems", "Naval electronic support measures and countermeasures.", "FP"),
            ("Underwater decoys and acoustic countermeasures", "Torpedo countermeasures, acoustic decoys and expendable underwater countermeasures.", "FP"),
            ("Monitoring, jamming and direction finding", "Spectrum monitoring, direction finding and jamming for security and force protection applications.", "FP"),
            ("Interception and jamming for security applications", "Convoy and site protection jamming and interception equipment.", "FP"),
        ],
        "models": [],
        "related": ["command-control-communications", "unmanned-systems-counter-uas", "intelligence-surveillance-reconnaissance"],
    },
    {
        "n": "08", "slug": "avionics-aerospace",
        "name": "Avionics and Aerospace", "short": "Avionics &amp; Aerospace",
        "nav": "Avionics and Aerospace",
        "def": "Airborne mission systems, displays, computers, and space and satellite programs.",
        "hero": "The mission systems, displays and computing that make an airframe a capability.",
        "img": "dom-avionics", "icon": "avionics",
        "meta_title": "Avionics, Mission Systems and Space | Maalik",
        "meta_desc": "Mission computers, cockpit displays, airborne communications, early warning systems and satellite and space programs.",
        "overview": [
            "An airframe is a platform. What makes it a capability is the mission system inside it, and what "
            "keeps it a capability is the spares and component support behind that system.",
            "This domain covers mission and flight control computing, digital map computers, data recorders "
            "and radar altimeters; cockpit multi-function and head-up displays; airborne radio, intercom and "
            "data communication suites and their control systems.",
            "It also covers airborne early warning and control mission systems, integrated radar and "
            "avionics suites for combat aircraft with spares provisioning, line replaceable unit support, "
            "and satellite systems with their associated ground segment, including support to national "
            "space programs.",
        ],
        "glance": ["Mission computing", "Cockpit displays", "Airborne comms", "Space and ground segment"],
        "families": [
            ("Mission computers", "Central mission computing for combat and support aircraft.", "FP"),
            ("Flight control computers", "Digital flight control computing.", "FP"),
            ("Digital map computers", "Digital moving map generation and terrain awareness.", "FP"),
            ("Data recorders", "Flight and mission data recording systems.", "FP"),
            ("Radar altimeters", "Low-level radar altimetry.", "FP"),
            ("Multi-function displays", "Cockpit multi-function display units.", "FP"),
            ("Head-up displays", "Head-up display systems.", "FP"),
            ("Airborne communication systems", "Airborne radio, intercom and data communication suites.", "FP"),
            ("Communication control systems", "Airborne communication control and management units.", "FP"),
            ("Airborne early warning and control systems", "AEW&amp;C mission systems and associated support.", "FP"),
            ("Airborne radars and avionics suites", "Integrated radar and avionics suites for combat aircraft, with support and spares provisioning.", "FP"),
            ("Satellites and space systems", "Satellite systems and ground segment, including support to national space programs.", "FP"),
        ],
        "models": [("Avionics spares and components", "Line replaceable units, components and spares support for in-service avionics", "CP")],
        "related": ["intelligence-surveillance-reconnaissance", "electronic-warfare", "platforms-vehicles"],
    },
    {
        "n": "09", "slug": "platforms-vehicles",
        "name": "Platforms and Vehicles", "short": "Platforms &amp; Vehicles",
        "nav": "Platforms and Vehicles",
        "def": "Naval vessels, armoured and specialist vehicles, and the platforms that carry mission systems.",
        "hero": "The hulls, chassis and airframes that carry the mission and the crews that operate them.",
        "img": "dom-platforms", "icon": "platforms",
        "meta_title": "Naval Vessels and Armoured Platforms | Maalik",
        "meta_desc": "Surface combatants, patrol and fast attack craft, harbour vessels, armoured vehicles, specialist trucks and platform spares.",
        "overview": [
            "Platforms are procured for a service life measured in decades, which makes the spares, "
            "assemblies and refit route as important at the point of selection as the platform itself.",
            "We source surface combatants and patrol vessels to customer specification, high speed patrol "
            "and attack craft, and harbour and coastal support vessels. On land we supply armoured personnel "
            "carriers, protected patrol vehicles, specialist armoured platforms and mission-configured "
            "military trucks.",
            "We also supply the unglamorous items that decide availability: auxiliary power units that "
            "enable silent watch and reduce main engine hours, and spares, assemblies and sub-systems for "
            "vehicles already in service.",
        ],
        "glance": ["Naval vessels", "Fast attack craft", "Armoured vehicles", "Specialist trucks"],
        "families": [
            ("Naval vessels", "Surface combatants and patrol vessels sourced to customer specification.", "FP"),
            ("Fast attack craft", "High speed patrol and attack craft.", "FP"),
            ("Tug boats and harbour craft", "Harbour and coastal support vessels.", "FP"),
            ("Armoured vehicles", "Armoured personnel carriers, protected patrol vehicles and specialist armoured platforms.", "FP"),
            ("Special purpose military trucks", "Specialist logistic and mission-configured military trucks.", "FP"),
            ("Auxiliary power units", "APUs for armoured personnel carriers enabling silent watch and reduced main engine hours.", "FP"),
            ("Armoured vehicle spares and assemblies", "Spares, assemblies and sub-systems for in-service armoured vehicles.", "FP"),
        ],
        "models": [],
        "related": ["weapon-systems-munitions", "avionics-aerospace", "command-control-communications"],
    },
    {
        "n": "10", "slug": "cyber-security-information-assurance",
        "name": "Cyber Security and Information Assurance", "short": "Cyber Security",
        "nav": "Cyber Security",
        "def": "Assessment, monitoring, response, governance and the platforms that underpin them.",
        "hero": "Assessing, monitoring, defending and recovering national and institutional networks.",
        "img": "dom-cyber", "icon": "cyber",
        "meta_title": "Cyber Security and Managed SOC Services | Maalik",
        "meta_desc": "Security assessment, managed security operations, red teaming, GRC, digital forensics and incident response.",
        "overview": [
            "Assume the network is already contested. That is the position every serious information "
            "assurance program starts from, and it changes what you buy: less perimeter, more detection, "
            "response and recovery.",
            "This is a services-led domain. We deliver black-box, grey-box and white-box assessment across "
            "applications, network infrastructure and databases; managed security operations from an "
            "accredited facility; round-the-clock monitoring and incident response; red team engagements; "
            "and the governance, risk and compliance work that makes the result auditable.",
            "The platforms we supply, from SIEM to deception and threat intelligence, are selected to serve "
            "that delivery model rather than the other way round.",
        ],
        "glance": ["Assess", "Detect and respond", "Govern and comply", "Human layer"],
        "families": [
            ("Assessment methodologies", "Black-box assessment emulating an external attacker, grey-box emulating a legitimate user, and white-box with full system access.", "FP"),
            ("Application security assessment", "Web, Android, iOS, desktop and legacy application assessment.", "FP"),
            ("Network infrastructure security assessment", "External and internal assessment of network devices, plus security configuration audit.", "FP"),
            ("Database security assessment", "Configuration audit, injection testing, insecure storage, password policy and permissions evaluation.", "FP"),
            ("Managed security operations centre", "Fully managed security operations from an accredited facility, providing tools, analysts and process.", "FP"),
            ("Security monitoring service", "Incident triage, SIEM advisory and health check reporting, incident reporting and IR platform integration.", "FP"),
            ("Digital forensics and incident response", "Preparation, detection and analysis, containment, eradication and recovery, with evidence handling throughout.", "FP"),
            ("Red team services", "Full-scope simulated adversary engagement testing people, process and technology under realistic conditions.", "FP"),
            ("Security risk assessment", "Control assessment and gap analysis, security audit, risk mitigation strategy and policy documentation.", "FP"),
            ("Secure configuration review", "Configuration review of network devices, databases and operating systems, plus architecture review.", "FP"),
            ("Compliance assessment", "Compliance audits and reporting against ISO 27001, PCI DSS and NIST frameworks.", "FP"),
            ("Email phishing simulation service", "Simulated phishing campaigns measuring and improving workforce response to malicious email.", "FP"),
            ("Security awareness portfolio", "Structured program for building organisational security culture, with curricula and campaign material.", "FP"),
            ("Security information and event management", "Enterprise-wide monitoring platform enabling detection and response across the full infrastructure.", "FP"),
            ("Deception platform", "Decoy deployment and monitoring, breach identification and full forensic capture of adversary TTPs.", "FP"),
            ("Threat intelligence platform", "Aggregation and integration of multiple threat feeds to support intelligence-driven decisions.", "FP"),
        ],
        "models": [],
        "related": ["artificial-intelligence-digital-intelligence", "command-control-communications", "safe-city-critical-infrastructure"],
    },
    {
        "n": "11", "slug": "artificial-intelligence-digital-intelligence",
        "name": "Artificial Intelligence and Digital Intelligence", "short": "AI &amp; Digital Intelligence",
        "nav": "AI and Digital Intelligence",
        "def": "Open source intelligence, image and audio intelligence, data fusion and analytics.",
        "hero": "Turning open, closed and multi-format data into a decision-ready picture.",
        "img": "dom-ai", "icon": "ai",
        "meta_title": "AI and Digital Intelligence Platforms | Maalik",
        "meta_desc": "Open source intelligence, image and audio intelligence, data fusion and analytics for authorised government use.",
        "overview": [
            "These platforms are supplied to mandated agencies for lawful, authorised use. Governance, audit "
            "logging and role-based access control are treated as product requirements, not as options.",
            "The portfolio covers open source intelligence collection and real-time monitoring, intelligence "
            "fusion across multiple databases and formats, image intelligence, audio and voice intelligence "
            "with transcription and translation, and the conversion of unstructured data into structured, "
            "queryable form.",
            "It extends to secure offline data platforms, high-throughput agentic analysis workflows, mixed "
            "and virtual reality environments for planning and briefing, and consolidated national-level "
            "operational pictures assembled from multiple institutional sources.",
        ],
        "glance": ["Collect", "Fuse", "Analyse", "Decide"],
        "families": [
            ("Reputation and information environment monitoring", "AI-assisted monitoring and management of an organisation's public information environment.", "FP"),
            ("Computer vision", "Applied computer vision for detection, classification and tracking across imagery and video.", "FP"),
            ("Big data analytics", "Large-scale data engineering and analytics for national and institutional programs.", "FP"),
            ("National security picture and intelligence fusion", "Consolidated national-level operational picture assembled from multiple institutional data sources.", "FP"),
            ("Event, incident and information flow management", "Workflow platform for managing incidents and the flow of information between agencies.", "FP"),
        ],
        "models": [
            ("Open source intelligence platform", "End-to-end OSINT collection and real-time monitoring with AI-driven analysis", "PP"),
            ("Intelligence fusion platform", "Gathering, exchange and analysis across multiple databases and formats", "PP"),
            ("Image intelligence", "AI-driven image analysis turning visual material into structured, searchable intelligence", "PP"),
            ("Audio and voice intelligence", "Transcription, translation, speaker and content analysis of recorded audio and video", "PP"),
            ("Structured data intelligence", "Conversion of unstructured and semi-structured data into structured, queryable intelligence", "PP"),
            ("Digital identity investigation", "Investigative tooling for resolving and analysing digital identity across sources", "PP"),
            ("Secure offline data platform", "Secure access to data offline with full integrity and confidentiality controls", "PP"),
            ("Agentic AI platform", "High-throughput agentic artificial intelligence for automated analysis workflows", "PP"),
            ("Mixed and virtual reality environments", "Immersive environments for decision support, planning, briefing and training", "PP"),
        ],
        "related": ["cyber-security-information-assurance", "intelligence-surveillance-reconnaissance", "safe-city-critical-infrastructure"],
    },
    {
        "n": "12", "slug": "safe-city-critical-infrastructure",
        "name": "Safe City, Critical Infrastructure and Sustainable Systems", "short": "Safe City &amp; Infrastructure",
        "nav": "Safe City and Infrastructure",
        "def": "Urban security, public safety, telecom integrity, and energy and environmental infrastructure.",
        "hero": "Protecting the population, the network and the infrastructure that both depend on.",
        "img": "dom-safecity", "icon": "safecity",
        "meta_title": "Safe City and Critical Infrastructure | Maalik",
        "meta_desc": "City-scale surveillance, integrated command centres, digital evidence management, telecom integrity and sustainable infrastructure.",
        "overview": [
            "This domain covers the systems that protect a population and the infrastructure that population "
            "depends on. It sits between defence and civil administration and is procured by both.",
            "It runs from city-scale surveillance and integrated command environments to body-worn camera "
            "systems, docking and automated evidence offload, and the digital evidence management platform "
            "that carries material from capture through chain of custody, redaction and retention to "
            "disclosure in court.",
            "It also covers perimeter and site protection for bases and critical facilities, ballistic "
            "protection, telecom network integrity and fraud analytics, and the energy efficiency, climate "
            "monitoring and resource optimisation work that increasingly forms part of an institutional estate.",
        ],
        "glance": ["Safe city", "Physical security", "Network integrity", "Sustainable systems"],
        "families": [
            ("Safe city surveillance and operational visibility", "City-scale surveillance, monitoring and operational awareness systems.", "FP"),
            ("Integrated command environments", "Command centres coordinating city and field response across agencies.", "FP"),
            ("Emergency response communication solutions", "Communications architecture for emergency services and disaster response.", "FP"),
            ("Perimeter and site protection", "Perimeter intrusion detection and site security systems for bases and critical facilities.", "FP"),
            ("Ballistic protection", "Body armour, ballistic plates, helmets and protective equipment.", "FP"),
            ("Telecom network design, integration and optimisation", "End-to-end telecom network engineering for operators and institutions.", "FP"),
            ("Revenue assurance and fraud analytics", "Detection and prevention of revenue leakage and telecom fraud.", "FP"),
            ("Call detail record analysis and mediation", "Mediation, normalisation and analysis of network records for operational and assurance purposes.", "FP"),
            ("Energy efficient power and infrastructure systems", "Energy efficiency engineering for installations, bases and municipal infrastructure.", "FP"),
            ("Climate monitoring and environmental data intelligence", "Environmental sensing networks and the analytics built on them.", "FP"),
            ("Waste and resource management frameworks", "Resource optimisation and waste management for institutional and municipal estates.", "FP"),
            ("Smart municipal and urban optimisation systems", "Integrated systems for utilities, traffic and municipal service optimisation.", "FP"),
        ],
        "models": [
            ("Body worn cameras", "Smart body-worn camera systems for law enforcement and security personnel, including 5G connected models", "PP"),
            ("Docking and data stations", "Multi-bay docking, charging and automated evidence offload stations", "PP"),
            ("Digital evidence management", "Ingest, chain of custody, redaction, retention and disclosure of digital evidence", "PP"),
        ],
        "related": ["command-control-communications", "cyber-security-information-assurance", "artificial-intelligence-digital-intelligence"],
    },
]

# --------------------------------------------------------------------------- Section 4.6
SECTORS = [
    {"slug": "land-forces", "name": "Land Forces", "img": "sector-land",
     "line": "Dismounted optronics, formation communications and short range air defence for the manoeuvre force.",
     "context": "Land formations operate dispersed, across terrain that defeats line-of-sight communications and "
                "in conditions that defeat the unaided eye for much of the day. The recurring procurement "
                "problems are coverage across a formation frontage, positive identification before "
                "engagement, and keeping optronics and radios serviceable at reach from a depot. Equipment "
                "that performs on a range and fails at the third week of an exercise is not a capability.",
     "domains": ["electro-optics-night-vision", "command-control-communications", "air-defence-systems",
                 "unmanned-systems-counter-uas", "weapon-systems-munitions"],
     "focus": "Dismounted optronics, forward observation, formation communications, short-range air defence, "
              "tactical unmanned systems, and armoured and specialist vehicles.",
     "support": "Land systems are supported through forward-held spares packs sized to the formation, "
                "in-country repair for optronics and radios, and maintainer training that lets a unit "
                "resolve first and second line faults without returning equipment to a depot."},
    {"slug": "naval-forces", "name": "Naval Forces", "img": "sector-naval",
     "line": "Maritime sensing, shipborne defence and underwater surveillance for the surface and sub-surface fight.",
     "context": "Naval requirements are shaped by the platform refit cycle and by an environment that is "
                "corrosive to everything installed in it. Sensing must work across surface search, coastal "
                "surveillance and sub-surface detection simultaneously, and the electronic support picture "
                "must be current. Maintenance windows are fixed by the dockyard program, not by the "
                "equipment, which makes availability planning a design consideration.",
     "domains": ["intelligence-surveillance-reconnaissance", "electronic-warfare", "weapon-systems-munitions",
                 "platforms-vehicles", "command-control-communications"],
     "focus": "Maritime radar, sonar and underwater surveillance, shipborne air defence, marine thermal "
              "systems, underwater countermeasures, and vessels and craft.",
     "support": "Shipborne systems are supported on dockyard-compatible maintenance cycles, with spares "
                "provisioning aligned to the refit program and repair capability held where the platform "
                "is based rather than where the manufacturer sits."},
    {"slug": "air-and-space", "name": "Air and Space", "img": "sector-air",
     "line": "Mission systems, airborne sensing and space segment for the air and space domain.",
     "context": "Air and space requirements are dominated by certification, integration and obsolescence. A "
                "mission computer or display is selected once and supported for decades, so line replaceable "
                "unit availability and component obsolescence management matter more at selection than "
                "headline specification. Reconnaissance and early warning capability is only as good as the "
                "downlink and the ground exploitation behind it.",
     "domains": ["avionics-aerospace", "intelligence-surveillance-reconnaissance", "electronic-warfare",
                 "unmanned-systems-counter-uas"],
     "focus": "Airborne radar, mission computers and displays, reconnaissance pods, airborne early warning, "
              "airborne electronic warfare, and satellite and space programs.",
     "support": "Airborne systems are supported through line replaceable unit pools, obsolescence management "
                "for long-life avionics, and manufacturer-backed repair routes with documented turnaround "
                "commitments."},
    {"slug": "strategic-organisations", "name": "Strategic Organisations", "img": "sector-strategic",
     "line": "Secure communications, information assurance and technology transfer for national institutions.",
     "context": "Strategic organisations buy capability that must be sovereign, auditable and sustainable "
                "without external dependency. The determining questions are whether the technology can be "
                "transferred, whether it can be maintained in country, and whether the data it handles stays "
                "inside the institution. Specialised industrial equipment, test and measurement "
                "instrumentation and co-production arrangements often matter more than the end system.",
     "domains": ["cyber-security-information-assurance", "artificial-intelligence-digital-intelligence",
                 "command-control-communications", "avionics-aerospace"],
     "focus": "Secure communications, information assurance, data fusion, specialised industrial equipment, "
              "test and measurement, and transfer of technology and co-production.",
     "support": "Support for this sector is built around independence: documentation transfer, personnel "
                "training at the manufacturer, and establishment of in-country maintenance and depot "
                "facilities so that sustainment does not depend on a foreign visit."},
    {"slug": "law-enforcement-civil-armed-forces", "name": "Law Enforcement and Civil Armed Forces", "img": "sector-law",
     "line": "Trunked communications, evidence management and observation capability for the policing mission.",
     "context": "Law enforcement operates in the same urban space as the public it protects, which puts "
                "evidential integrity and interoperability ahead of raw performance. Communications must "
                "work across agencies that procured separately. Captured material must survive challenge in "
                "court, which makes chain of custody, redaction and retention a procurement requirement "
                "rather than a software feature.",
     "domains": ["command-control-communications", "electro-optics-night-vision",
                 "cyber-security-information-assurance", "artificial-intelligence-digital-intelligence",
                 "safe-city-critical-infrastructure"],
     "focus": "Digital trunked radio, body-worn systems and digital evidence management, observation devices, "
              "digital forensics, open source intelligence, and small arms and protective equipment.",
     "support": "Policing equipment is supported on a high-availability model: pooled spares, rapid swap-out "
                "for body-worn and portable devices, and training delivered in-region to keep officers on "
                "duty rather than in a classroom."},
    {"slug": "critical-infrastructure-safe-city", "name": "Critical Infrastructure and Safe City", "img": "sector-infra",
     "line": "Perimeter surveillance, integrated command and network integrity for the national estate.",
     "context": "Critical infrastructure is defended across a long perimeter with finite manpower, which "
                "makes sensor coverage geometry and automated cueing the central design problem. Sites are "
                "increasingly exposed to small unmanned aircraft, and the network layer that carries the "
                "security system is itself a target. Energy and environmental monitoring is now part of the "
                "same estate management conversation.",
     "domains": ["safe-city-critical-infrastructure", "intelligence-surveillance-reconnaissance",
                 "cyber-security-information-assurance", "command-control-communications"],
     "focus": "Perimeter and border surveillance, integrated command centres, counter-UAS for sensitive "
              "sites, network integrity, and energy and environmental monitoring.",
     "support": "Fixed-site systems are supported with scheduled preventive maintenance, remote health "
                "monitoring where the network permits, and a defined response commitment for a site that "
                "cannot be left unwatched."},
]

# --------------------------------------------------------------------------- Section 4.7
SERVICES = [
    {"slug": "systems-integration", "name": "Systems Integration", "img": "svc-integration",
     "key": "Most capability gaps are not equipment gaps. They are integration gaps.",
     "why": "Institutions rarely start from nothing. They hold an estate of systems bought at different "
            "times, from different manufacturers, under different standards. A new procurement that cannot "
            "talk to that estate does not add capability, it adds an island.",
     "what": ["Requirements analysis and translation into a procurable specification",
              "System architecture and design", "Multi-vendor integration across sensing, communications, "
              "command and control and analytics", "Interface definition and control documentation",
              "Acceptance testing against the agreed specification",
              "Integration of new systems into existing legacy estates"],
     "how": "We start from the operational effect and work backwards to the interfaces. Every integration "
            "carries an interface control document, a test plan written before build, and an acceptance "
            "procedure the customer's technical staff run themselves.",
     "receive": "A working chain rather than a set of boxes, with the architecture documented, the "
                "interfaces specified, and the acceptance evidence in your hands."},
    {"slug": "procurement-contract-management", "name": "Procurement and Contract Management", "img": "svc-procurement",
     "key": "A submission that is complete, compliant and easy to evaluate.",
     "why": "A technically superior offer that is set aside on a documentation technicality has cost the "
            "customer the capability and the manufacturer the program. Procurement fluency is not "
            "administration, it is the mechanism by which good engineering reaches the user.",
     "what": ["Technical and operational assessment of a requirement against manufacturer capability",
              "Cost build-up and assistance with project costing",
              "Identification of suitable local partners and sub-contractors",
              "Complete support through the bid evaluation phase",
              "Contract administration from award to closure",
              "Deployment of qualified project managers to run a program on the manufacturer's behalf"],
     "how": "We work to the applicable public procurement framework and to your tender conditions, with "
            "documentation discipline applied as a process rather than as a final check.",
     "receive": "Error-free submissions, accurate costing, clear technical compliance statements, and a "
                "single accountable contact from award through to closure."},
    {"slug": "logistics-import-clearance", "name": "Logistics, Import and Clearance", "img": "svc-logistics",
     "key": "The elapsed time between contract award and equipment in the user's hands is a capability issue.",
     "why": "Equipment sitting at a port is not a capability. Delay between award and hand-over is routinely "
            "treated as an administrative matter when it is in fact the difference between a requirement "
            "met and a requirement outstanding.",
     "what": ["Pre-shipment inspection", "Freight forwarding", "Port clearance", "Inland transportation",
              "Secure storage", "Hand-over to the user"],
     "how": "Clearance documentation is prepared in parallel with manufacture rather than on arrival, and "
            "the movement plan is agreed before the shipment leaves the factory.",
     "receive": "Equipment delivered to the nominated location, inspected, documented and handed over, with "
                "the movement traceable at every stage."},
    {"slug": "installation-commissioning-training", "name": "Installation, Commissioning and Training", "img": "svc-install",
     "key": "Equipment that is not correctly commissioned, and whose operators are not correctly trained, is not a capability.",
     "why": "The gap between installed and operational is where most delivered capability is lost. It is "
            "closed by commissioning done properly and by training that reaches the people who will actually "
            "use and maintain the system.",
     "what": ["Site survey", "Installation", "Commissioning", "Integration testing", "Operator training",
              "Maintainer training", "Train-the-trainer programs",
              "Documentation packages in English"],
     "how": "Training is delivered against the tasks the operator will actually perform, and maintainer "
            "training is scoped to the fault levels the unit is expected to resolve itself.",
     "receive": "A commissioned system, a trained operator and maintainer cadre, a train-the-trainer "
                "capability, and a documentation set your staff can work from."},
    {"slug": "maintenance-repair-overhaul", "name": "Maintenance, Repair and Overhaul", "img": "svc-mro",
     "key": "Availability is decided after delivery, not before it.",
     "why": "The whole-life cost and availability of a system is determined by its support arrangement, not "
            "by its purchase price. A cheaper system with no spares route is the more expensive procurement.",
     "what": ["Warranty service", "Post-warranty service contracts",
              "Scheduled and unscheduled maintenance", "Spares provisioning and management",
              "Depot level repair facilities", "Overhaul programs", "Obsolescence management",
              "Life extension of in-service systems"],
     "how": "Support is structured before delivery, not after the first failure. Initial provisioning is "
            "sized against the expected usage profile and reviewed against actual consumption.",
     "receive": "A defined availability position, a spares holding sized to it, and a repair route with "
                "stated turnaround rather than an assumption of manufacturer goodwill."},
    {"slug": "transfer-of-technology-co-production", "name": "Transfer of Technology and Co-Production", "img": "svc-tot",
     "key": "Capability that stays in the country.",
     "why": "For strategic organisations this is the highest-value service we offer, because it converts a "
            "purchase into a national capability. It directly supports self-reliance objectives and removes "
            "the dependency that makes a foreign supply chain a strategic risk.",
     "what": ["Structuring transfer of technology arrangements with manufacturers",
              "Establishing local assembly, production and maintenance capability",
              "Technical documentation transfer", "Personnel training at the manufacturer",
              "Establishing in-country maintenance and depot facilities"],
     "how": "We establish at the outset what genuinely transfers and what does not, and we write that into "
            "the arrangement. A transfer that is not specified in detail before signature does not happen "
            "after it.",
     "receive": "A documented transfer scope, trained personnel, an established local facility, and a "
                "production or maintenance capability that continues without the original supplier."},
    {"slug": "custom-engineering-software", "name": "Custom Engineering and Software Development", "img": "svc-software",
     "key": "Where no product exists, we can build it.",
     "why": "A significant share of requirements have no catalogue answer. Sometimes the right response is "
            "not to source a product but to engineer one, or to build the software layer that makes existing "
            "equipment behave as a system.",
     "what": ["Bespoke enterprise and mission software", "Mobile application development",
              "Embedded firmware, sensor integration and IoT platforms",
              "Blockchain applications for provenance, identity and assurance",
              "E-commerce and transactional platforms",
              "Real-time 3D environments for training, visualisation and simulation",
              "Systems architecture, requirement mapping and solution design",
              "Specialist technical resourcing and dedicated remote engineering teams"],
     "how": "Work is delivered by named engineers against a written specification, with source, documentation "
            "and build environment handed over as part of the deliverable.",
     "receive": "Working software, its source and documentation, and a team that can continue to develop it "
                "or hand it to yours."},
]

# --------------------------------------------------------------------------- Section 5.13.1
SIMULATION = [
    ("Full mission simulators", "High fidelity full mission simulators for aircrew and platform crew training."),
    ("Main battle tank simulators", "Crew, gunnery and driver training simulators for armoured platforms."),
    ("Artillery gun simulators", "Gun crew drill and firing simulators."),
    ("Artillery observer simulators", "Forward observer training simulators for target acquisition and fire correction."),
    ("Aerial target systems", "Aerial targets and target drones for live-fire training and system qualification."),
    ("Underwater target systems", "Underwater targets for anti-submarine and torpedo training."),
    ("Security professional training", "Structured training and certification programs for security and technical personnel."),
]

TRADING = [
    ("Specialised raw materials and alloys", "Sourcing of specialist metals, alloys and materials for defence production."),
    ("Industrial plants and equipment", "Turnkey industrial plant, production machinery and process equipment."),
    ("Test and measurement equipment", "Laboratory and production test, measurement and calibration instrumentation."),
]

# --------------------------------------------------------------------------- Section 6
PARTNERS = [
    {"slug": "aerospace-long-march", "name": "Aerospace Long-March International Trade Co. Ltd.",
     "country": "China", "region": "China", "group": "Defence systems and platforms",
     "domains": ["air-defence-systems", "weapon-systems-munitions", "avionics-aerospace"],
     "supplies": "Air defence systems, precision guided munitions and aerospace systems."},
    {"slug": "cgwic", "name": "China Great Wall Industry Corporation (CGWIC)",
     "country": "China", "region": "China", "group": "Defence systems and platforms",
     "domains": ["avionics-aerospace"],
     "supplies": "Satellites, space systems and launch services, and the associated ground segment."},
    {"slug": "cetc-international", "name": "CETC International Co., Ltd.",
     "country": "China", "region": "China", "group": "Defence systems and platforms",
     "domains": ["intelligence-surveillance-reconnaissance", "command-control-communications", "electronic-warfare"],
     "supplies": "Radar and sensing, electronic systems, command and control, and communications."},
    {"slug": "star-vision", "name": "STAR Vision", "country": "China", "region": "China",
     "group": "Defence systems and platforms", "domains": ["electro-optics-night-vision"],
     "supplies": "Optronic and vision systems."},
    {"slug": "aviaexport", "name": "Aviaexport", "country": "Russian Federation", "region": "Russia and Central Asia",
     "group": "Defence systems and platforms", "domains": ["avionics-aerospace", "platforms-vehicles"],
     "supplies": "Aviation systems, fixed and rotary wing support, and aviation spares."},
    {"slug": "samkwang", "name": "Samkwang Shipbuilding and Engineering Co., Ltd.",
     "country": "South Korea", "region": "East Asia", "group": "Defence systems and platforms",
     "domains": ["platforms-vehicles"],
     "supplies": "Naval vessels, fast attack craft, tug boats and harbour craft."},
    {"slug": "unique-alpine", "name": "Unique-Alpine", "country": "Germany", "region": "Europe",
     "group": "Defence systems and platforms", "domains": ["weapon-systems-munitions"],
     "supplies": "Precision and sniper rifle systems."},
    {"slug": "beretta", "name": "Beretta", "country": "Italy", "region": "Europe",
     "group": "Defence systems and platforms", "domains": ["weapon-systems-munitions"],
     "supplies": "Service pistols and small arms."},
    {"slug": "steiner-eoptics", "name": "Steiner eOptics", "country": "United States", "region": "North America",
     "group": "Defence systems and platforms", "domains": ["electro-optics-night-vision", "weapon-systems-munitions"],
     "supplies": "Laser aiming devices, weapon-mounted optronics and observation optics."},
    {"slug": "newcon-optik", "name": "Newcon Optik", "country": "Canada", "region": "North America",
     "group": "Defence systems and platforms", "domains": ["electro-optics-night-vision"],
     "supplies": "Night vision, laser rangefinding and observation devices."},
    {"slug": "hytera", "name": "Hytera Communications Corporation Limited", "country": "China", "region": "China",
     "group": "Communications and critical communications", "featured": True,
     "domains": ["command-control-communications", "safe-city-critical-infrastructure"],
     "supplies": "DMR and TETRA radios and infrastructure, push-to-talk over cellular, mission critical "
                 "services, body-worn camera systems and digital evidence management, integrated command, "
                 "control and dispatch, 4G and 5G private broadband, rapid deployment communications, "
                 "communication vehicles and radio accessories."},
    {"slug": "norsat", "name": "Norsat International", "country": "Canada", "region": "North America",
     "group": "Communications and critical communications", "parent": "Part of the Hytera group",
     "domains": ["command-control-communications"],
     "supplies": "Satellite terminals, satellite components and satellite network solutions."},
    {"slug": "sinctech", "name": "SINCTech (Sinclair Technologies)", "country": "Canada", "region": "North America",
     "group": "Communications and critical communications", "parent": "Part of the Hytera group",
     "domains": ["command-control-communications"],
     "supplies": "Base station antennas, transmitter combiners and RF signal conditioning."},
    {"slug": "hmf-smart-solutions", "name": "HMF Smart Solutions", "country": "Germany", "region": "Europe",
     "group": "Communications and critical communications", "parent": "Part of the Hytera group",
     "domains": ["command-control-communications"],
     "supplies": "Smart communication solutions."},
    {"slug": "optronics-manufacturer-islamabad", "name": "Shibli Electronics",
     "country": "Pakistan", "region": "Pakistan", "group": "Optronics and thermal imaging", "featured": True,
     "domains": ["electro-optics-night-vision", "unmanned-systems-counter-uas",
                 "intelligence-surveillance-reconnaissance"],
     "supplies": "Cooled and uncooled thermal binoculars and monoculars, long range thermal sights and "
                 "clip-on modules, image intensified night vision, border, coastal and base surveillance "
                 "systems, radar and integrated radar-electro-optical systems, counter-UAS systems "
                 "including jamming, vehicle driver night sights, marine thermal systems, portable command "
                 "and control units, unmanned aerial systems including loitering, ISR and FPV platforms, "
                 "and optronic accessories.",
     "note": "Shibli is the source of the FALCON, SKUA, GUARDIAN, TARSIER, ORCA, ERMINE, "
             "TERRIER, Nightrider, See King, SkyGuard and SKYSTRYX product families. Because it is a "
             "Pakistani manufacturer, the relationship shortens support lines and removes the export "
             "licensing step. Manufacturing facility on Fateh Jang Road with a corporate office in Islamabad."},
    {"slug": "cyber-delivery-partner", "name": "Established Pakistani cyber security systems house",
     "country": "Pakistan", "region": "Pakistan", "group": "Cyber security", "featured": True,
     "domains": ["cyber-security-information-assurance"],
     "supplies": "Managed security operations, security assessment, red teaming, governance risk and "
                 "compliance, digital forensics and incident response, and security awareness.",
     "note": "Operating since 2005. Regional offices in Rawalpindi, Lahore and Karachi, with Gulf presence "
             "in Riyadh and Doha and a Canadian headquarters. Holds ISO 27001 accredited operating "
             "facilities. Serves financial institutions, telecom operators and industrial sectors."},
    {"slug": "kaspersky", "name": "Kaspersky", "country": "Vendor", "region": "Europe", "group": "Cyber security",
     "domains": ["cyber-security-information-assurance"],
     "supplies": "Endpoint security, threat intelligence and industrial control system security."},
    {"slug": "cisco", "name": "Cisco", "country": "United States", "region": "North America", "group": "Cyber security",
     "domains": ["cyber-security-information-assurance", "command-control-communications"],
     "supplies": "Network security, segmentation and secure infrastructure."},
    {"slug": "ibm-security", "name": "IBM Security", "country": "United States", "region": "North America",
     "group": "Cyber security", "domains": ["cyber-security-information-assurance"],
     "supplies": "Security information and event management, identity and threat management."},
    {"slug": "forcepoint", "name": "Forcepoint", "country": "United States", "region": "North America",
     "group": "Cyber security", "domains": ["cyber-security-information-assurance"],
     "supplies": "Data loss prevention, cross-domain solutions and user behaviour analytics."},
    {"slug": "ai-digital-intelligence-group", "name": "Pakistan-based AI and digital intelligence group",
     "country": "Pakistan", "region": "Pakistan", "group": "AI and digital intelligence", "featured": True,
     "domains": ["artificial-intelligence-digital-intelligence", "safe-city-critical-infrastructure"],
     "supplies": "Open source intelligence, image and audio intelligence, data fusion, secure data "
                 "platforms, agentic AI, mixed and virtual reality, and safe city systems.",
     "note": "Operates specialist units covering AI intelligence products, secure communications research "
             "and development, public safety and safe city solutions, and climate and energy technology. "
             "Holds ISO 9001 and ISO 14001 certifications and a capability maturity model assessment."},
    {"slug": "sunmi", "name": "SUNMI Technology Co., Ltd.", "country": "China", "region": "China",
     "group": "Safe city, identity and commercial systems",
     "domains": ["safe-city-critical-infrastructure", "artificial-intelligence-digital-intelligence"],
     "supplies": "Business IoT terminals: rugged Android handhelds, point-of-sale and self-service "
                 "terminals, printers and connected devices for retail, logistics and public service "
                 "deployments."},
    {"slug": "asy-anti-forgery", "name": "Shenzhen ASY Anti-forgery Technology Development Co., Ltd.",
     "country": "China", "region": "China", "group": "Safe city, identity and commercial systems",
     "domains": ["safe-city-critical-infrastructure"],
     "supplies": "Integrated anti-counterfeiting solutions: security labels and seals, track and trace "
                 "systems, and authentication technology for documents, credentials and controlled goods."},
    {"slug": "genuine-printing", "name": "Genuine Printing", "country": "China", "region": "China",
     "group": "Safe city, identity and commercial systems",
     "domains": ["safe-city-critical-infrastructure"],
     "supplies": "High-security paper, holographic solutions and smart card components. Operating since "
                 "2005, supplying end-to-end secure document and credential manufacturing."},
    {"slug": "rds", "name": "REDtone Digital Services (Private) Limited", "country": "Pakistan", "region": "Pakistan",
     "group": "Communications and critical communications",
     "domains": ["command-control-communications", "safe-city-critical-infrastructure"],
     "supplies": "Managed connectivity and ICT services: enterprise internet, secure network design and "
                 "integration, data centre and managed service delivery across Pakistan.",
     "note": "Offices in Islamabad, Lahore and Karachi."},
    {"slug": "everbridge", "name": "Everbridge, Inc.", "country": "United States",
     "region": "North America", "group": "Safe city, identity and commercial systems",
     "domains": ["safe-city-critical-infrastructure", "command-control-communications"],
     "supplies": "Critical event management and mass notification: public warning, emergency "
                 "communication and business continuity platforms for government and enterprise."},
    ]

# Logos held on file. A manufacturer with no entry here is listed as text only,
# which is the safe default under Section 10.2 until written permission exists.

# Manufacturer product photography, mapped to the family it illustrates.
# domain slug -> {family index: image stem in assets/img/products}
FAMILY_IMAGES = {
    "electro-optics-night-vision": {
        0: "eo-cooled", 1: "eo-uncooled", 2: "eo-c2", 3: "eo-border",
        4: "eo-combat", 5: "eo-nightvision", 6: "eo-vehicle-marine",
        7: "eo-observation", 8: "eo-accessories",
    },
    "command-control-communications": {
        2: "c3-dmr-professional", 3: "c3-dmr-business", 5: "c3-tetra", 6: "c3-poc",
    },
    "safe-city-critical-infrastructure": {0: "sc-bodycam"},
}

# A short strip of named systems shown above the model table.
FEATURED = {
    "electro-optics-night-vision": [
        ("eo-tarsier-lr", "TARSIER LR 80", "Long range thermal scope and sight"),
        ("eo-mini50", "TARSIER MINI 50", "Compact thermal monocular and weapon sight"),
        ("eo-tripod", "Picatinny 1913 interface", "Tripod interface for handheld optronics"),
    ],
    "command-control-communications": [
        ("c3-dmr-mobile", "HM78X", "Professional DMR mobile"),
        ("c3-s1", "S1 Pro", "S series business two-way radio"),
        ("c3-dual-mode", "PDC680", "Dual-mode rugged radio and smartphone"),
    ],
}

# Section 6: the exact designation each manufacturer permits.
AUTHORISED_REPRESENTATIVE = {
    "sunmi", "asy-anti-forgery", "everbridge", "genuine-printing",
    "optronics-manufacturer-islamabad", "rds",
}


def designation(slug):
    """What we are permitted to call the relationship."""
    if slug in AUTHORISED_REPRESENTATIVE:
        return "Authorised representative"
    return "Authorised distributor and technology partner"


PARTNER_GROUPS = ["Defence systems and platforms", "Communications and critical communications",
                  "Optronics and thermal imaging", "Cyber security", "AI and digital intelligence",
                  "Safe city, identity and commercial systems"]
PARTNER_REGIONS = ["China", "Europe", "North America", "Russia and Central Asia", "East Asia", "Pakistan"]

# --------------------------------------------------------------------------- Section 4.9.3
PROGRAMMES = [
    ("Simulation and training systems", "2012 to date", "Delivery and support of full mission, platform crew and gunnery "
     "simulation across service branches, including artillery gun and forward observer trainers."),
    ("Thermal imaging and optronics", "2013 to date", "Supply of handheld, weapon-mounted and fixed surveillance optronics, "
     "including transfer of technology arrangements supporting local co-production."),
    ("Unmanned aerial systems", "2017 to date", "Supply of tactical and reconnaissance unmanned systems and their payloads, "
     "including co-production arrangements."),
    ("Airborne early warning and control", "2014 to 2021", "Mission system supply and associated through-life support."),
    ("Artillery and counter-battery radar", "2013 to 2019", "Weapon locating radar supply supporting counter-battery and "
     "fire correction capability."),
    ("Airborne radar and avionics suites", "2015 to date", "Integrated radar and avionics suite supply for combat aircraft, "
     "with spares provisioning and component support."),
    ("Layered air defence", "2011 to date", "Supply across the air defence architecture, from man-portable systems to "
     "medium altitude area defence."),
    ("Naval craft and support vessels", "2016 to 2022", "Supply of patrol, attack and harbour support craft to customer "
     "specification."),
    ("Small arms and personal weapons", "2011 to date", "Service pistols, rifles and support weapons for armed forces and "
     "law enforcement, with ammunition and accessory provisioning."),
    ("Laser aiming and observation devices", "2012 to date", "Weapon-mounted aiming modules and handheld observation "
     "equipment across service branches."),
    ("Maintenance and depot facilities", "2018 to date", "Establishment of in-country maintenance and depot facilities for "
     "air defence and artillery systems."),
    ("Missile life extension", "2019 to date", "Inspection, refurbishment, component replacement and service life extension "
     "of in-service missile inventory."),
    ("Space and satellite programs", "2015 to date", "Satellite system and ground segment supply, including support to "
     "national space program establishment."),
]


# --------------------------------------------------------------------------- Section 4.10
BRIEF_TOPICS = [
    "Cooled against uncooled thermal imaging: choosing by mission profile rather than by budget",
    "DMR, TETRA and broadband push-to-talk: selecting a formation communications architecture",
    "What a layered air defence architecture actually requires, from man-portable to medium altitude",
    "Counter-UAS: why detection, identification and defeat are three separate procurement problems",
    "Specifying a border surveillance system: sensor mix, coverage geometry and sustainment",
    "Building a managed security operations capability: in-house against managed service",
    "Open source intelligence for national security: capability, workflow and governance",
    "Transfer of technology arrangements: what genuinely transfers and what does not",
    "Writing a technical specification that does not accidentally exclude the best supplier",
    "Through-life support planning: the spares and obsolescence questions to ask before award",
    "Digital evidence management for law enforcement: from body-worn capture to court",
    "Integrating multi-vendor sensors into a single command and control picture",
]

DISCIPLINES = [
    "Systems engineering", "RF and communications engineering", "Optronics",
    "Software and AI engineering", "Cyber security", "Project and program management",
    "Field service engineering", "Procurement and contracts", "Logistics",
]

# Section 4.5 -- product index filter facets
FACETS = {
    "platform": ["Dismounted and man-portable", "Vehicle mounted", "Naval and shipborne", "Airborne",
                 "Fixed site and infrastructure", "Software and platform-independent"],
    "environment": ["Land", "Maritime and coastal", "Air", "Sub-surface", "Urban", "Network and cyber"],
    "function": ["Observe and detect", "Communicate", "Command and control", "Analyse",
                 "Protect and defend", "Engage", "Train and simulate", "Sustain and support"],
}

# Section 4.12 -- contact routes
CONTACT_ROUTES = [
    {"slug": "", "name": "General enquiry", "short": "General",
     "desc": "Company information, capability questions and anything that does not fit the routes below.",
     "to": "General inbox", "eyebrow": "ROUTE 01"},
    {"slug": "request-for-information", "name": "Request for Information and tender response", "short": "RFI and tender",
     "desc": "Submit a specification, a tender reference or a description of the operational problem. "
             "Reaches the bid and technical team directly.",
     "to": "Bid and technical team", "eyebrow": "ROUTE 02"},
    {"slug": "partnership", "name": "Partnership enquiry", "short": "Partnership",
     "desc": "For manufacturers evaluating representation in Pakistan, and for local partners and "
             "sub-contractors.", "to": "Business development", "eyebrow": "ROUTE 03"},
    {"slug": "support", "name": "Support and service request", "short": "Support",
     "desc": "For customers with equipment in service. Warranty, spares, faults and scheduled maintenance.",
     "to": "Service and support team", "eyebrow": "ROUTE 04"},
]
