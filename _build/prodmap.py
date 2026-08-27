# -*- coding: utf-8 -*-
"""
Which image illustrates which catalogue entry.

Named models resolve to the manufacturer photograph of that exact model.
Product families, which are categories rather than single items, resolve to a
representative image. Anything with neither falls back to the generated
technical plate, so no card is ever left bare.
"""

# --- named models -> the manufacturer shot of that exact model ---------------
MODEL_IMAGES = {
    # Hytera, Domain 01
    "HP78X": "hp78x", "HP78X UL913": "hp78x", "HP70X": "hp70x", "HP70X UL913": "hp70x",
    "HP68X": "hp68x", "HP60X": "hp60x", "HP56X": "hp56x", "HP56X UL913": "hp56x",
    "HP50X": "hp50x", "HP50X UL913": "hp50x",
    "HP79XEx IIC": "hp79xex", "HP79XEx IIA": "hp79xex",
    "HP71XEx IIC": "hp71xexiic", "HP71XEx IIA": "hp71xexiia",
    "HM78X": "hm78x", "HM68X": "hm68x", "HM65X": "hm65x",
    "S1 Pro / S1 Pro LF": "s1",
    "BP56X": "bp56x", "BP51X": "bp51x", "BP36X": "bp36x",
    "PD40X": "pd40x", "PD41X": "pd41x", "PD48X": "pd48x", "PD36X": "pd36x",
    "BD50X": "bd50x", "BD55X": "bd55x", "BD61X": "bd61x",
    "MD61X": "md61x", "MD62X": "md62x",
    "DS-6250S": "ds-6250s",
    "PT590": "pt590", "PT580H Plus": "pt580h", "PT580H Plus UL913": "pt580h",
    "PT560H": "pt560h", "PT890Ex": "pt890ex", "MT680 Plus": "mt680-plus",
    "PTC680": "ptc680", "PDC680": "c3-dual-mode",
    "P5 series": "p50", "P60": "p60", "PNC660": "pnc660",
    # Shibli, Domain 03
    "FALCON": "falcon",
    "SKUA MP PRO 640": "eo-cooled", "SKUA MP PRO 1280": "eo-uncooled",
    "SKUA-LR": "eo-observation", "SKUA MINI": "eo-mini50",
    "C2 / SKUA MP PRO": "eo-c2", "C2 / SKUA LR": "eo-c2",
    "GUARDIAN PRO": "guardian-pro",
    "GUARDIAN 100mm 640": "eo-border", "GUARDIAN 25-150 1280": "guardian-sys",
    "GUARDIAN 150 1280": "eo-border",
    "TARSIER MINI 50": "eo-mini50", "TARSIER MINI 50 LRF": "eo-mini50",
    "TARSIER LR 80": "eo-tarsier-lr", "TARSIER LRF 80": "eo-tarsier-lr",
    "TARSIER clip-on": "eo-combat",
    "ORCA-NV": "eo-nightvision", "ERMINE-NV": "ermine-nv", "TERRIER NV": "terrier-nv",
    "Head mount display": "eo-accessories",
    "Nightrider": "eo-vehicle-marine", "See King": "eo-vehicle-marine",
    # Shibli, Domain 04
    "SKYSTRYX Loitering UAV": "uas-fixed-wing", "SKYSTRYX ISR UAV": "uas-family",
    "SkyGuard-M1": "skyguard-m1", "SkyGuard-MIS": "skyguard-mis",
    "Counter-UAS detection radar": "isr-ground-radar",
    "Radar and EO counter-UAS system": "anti-uav",
    "Counter-UAS jamming equipment": "ew-spectrum",
    # Domain 02
    "Multi-mission multi-function radar": "isr-radar-panel",
    "Radar and electro-optical integrated system": "isr-naval-eo",
    "Artillery and counter-battery radar": "isr-ground-radar",
    "Airborne early warning and control": "av-aew",
    # Domains 08 and 12
    "Avionics spares and components": "av-displays",
    "Body worn cameras": "sc-bodycam",
    "Docking and data stations": "c3-radio-unit",
    "Digital evidence management": "cy-architecture",
    # Domain 11, platform entries
    "Open source intelligence platform": "cy-architecture",
    "Intelligence fusion platform": "c3-command-centre",
    "Image intelligence": "isr-naval-eo",
    "Audio and voice intelligence": "c3-radio-unit",
    "Structured data intelligence": "c3-rugged-computing",
    "Digital identity investigation": "cy-architecture",
    "Secure offline data platform": "c3-rugged-c2",
    "Agentic AI platform": "c3-rugged-computing",
    "Mixed and virtual reality environments": "av-hud",
}

# --- product families -> a representative image ------------------------------
FAMILY_IMAGES_BY_NAME = {
    # 01 Command, Control and Communications
    "Command and control systems": "c3-rugged-c2",
    "Integrated command, control and dispatch": "c3-command-centre",
    "DMR professional and mission critical radios": "c3-dmr-professional",
    "DMR business and commercial radios": "c3-dmr-business",
    "DMR infrastructure": "ds-6250s",
    "TETRA radios and systems": "c3-tetra",
    "Broadband, PoC and multi-band radio": "c3-poc",
    "4G and 5G broadband infrastructure": "c3-comms-shelter",
    "Satellite communications": "isr-satellite-dish",
    "Antennas, RF conditioning and site infrastructure": "c3-rf-unit",
    "Communication vehicles and rapid deployment": "plt-light-vehicles",
    "Radio accessories and ancillaries": "c3-radio-unit",
    # 02 ISR
    "Unmanned aerial systems for ISR": "uas-fixed-wing",
    "Airborne radars": "av-isr-aircraft",
    "Reconnaissance pods": "av-combat-aircraft",
    "Air defence radars": "ad-radar-vehicle",
    "Ground surveillance radars": "isr-ground-radar",
    "Maritime radars": "isr-naval-mast",
    "Sonar systems": "isr-sonar-buoy",
    "Underwater surveillance systems": "isr-sonar-buoy",
    # 03 Electro-optics
    "Handheld surveillance and forward observation, cooled": "eo-cooled",
    "Handheld surveillance and forward observation, uncooled": "eo-uncooled",
    "Portable command and control units": "eo-c2",
    "Border, coastal and base surveillance": "eo-border",
    "Combat optronics": "eo-combat",
    "Image intensified night vision": "eo-nightvision",
    "Vehicle and marine optronics": "eo-vehicle-marine",
    "Observation, aiming and general optronics": "eo-observation",
    "Optronic accessories and ancillaries": "eo-accessories",
    # 04 Unmanned
    "Unmanned aerial systems, general": "uas-family",
    "UAV payloads": "isr-naval-eo",
    "Aerial target drones": "uas-targets",
    "Integrated anti-UAV defence system": "anti-uav",
    # 05 Air defence
    "High to medium altitude air defence systems": "ad-layered",
    "Low to medium altitude air defence systems": "ad-launcher-vehicle",
    "Pedestal mounted air defence systems": "ad-vehicle-system",
    "Man portable air defence systems": "ad-manpads",
    "Shipborne air defence missile systems": "isr-ciws",
    "Air defence maintenance and depot facilities": "mro-engine-shop",
    "Missile life extension programmes": "wpn-missile-rack",
    # 06 Weapons
    "Surface-to-surface missiles and rockets": "wpn-guided-munition",
    "Air-to-ground rockets": "wpn-air-torpedo",
    "GPS guided air-to-surface bombs": "wpn-guided-bomb",
    "Lightweight torpedoes": "wpn-bomb",
    "Heavyweight torpedoes": "wpn-missile-rack",
    "Hand guns and service pistols": "wpn-service-pistol",
    "Assault rifles": "wpn-assault-rifle",
    "Sub-machine guns": "wpn-smg",
    "Sniper and designated marksman rifles": "wpn-sniper",
    "Grenade launchers": "wpn-rifles",
    "Ammunition": "wpn-ammunition",
    "Weapon optics and accessories": "wpn-pistol-range",
    # 07 Electronic warfare
    "Airborne electronic warfare systems": "ew-air-ground",
    "Land based electronic warfare": "ew-networked",
    "Ship-borne electronic warfare systems": "isr-naval-mast",
    "Underwater decoys and acoustic countermeasures": "isr-sonar-buoy",
    "Monitoring, jamming and direction finding": "ew-spectrum",
    "Interception and jamming for security applications": "c3-rf-unit",
    # 08 Avionics
    "Mission computers": "av-displays",
    "Flight control computers": "c3-rugged-computing",
    "Digital map computers": "av-hud",
    "Data recorders": "c3-rugged-c2",
    "Radar altimeters": "av-isr-aircraft",
    "Multi-function displays": "av-cockpit",
    "Head-up displays": "av-hud",
    "Airborne communication systems": "av-transport",
    "Communication control systems": "c3-radio-unit",
    "Airborne early warning and control systems": "av-aew",
    "Airborne radars and avionics suites": "av-combat-aircraft",
    "Satellites and space systems": "isr-satellite-dish",
    # 09 Platforms
    "Naval vessels": "plt-naval-vessels",
    "Fast attack craft": "plt-naval-vessels",
    "Tug boats and harbour craft": "plt-naval-vessels",
    "Armoured vehicles": "plt-armour",
    "Special purpose military trucks": "plt-light-vehicles",
    "Auxiliary power units": "c3-comms-shelter",
    "Armoured vehicle spares and assemblies": "mro-engine-shop",
    # 10 Cyber security
    "Assessment methodologies": "cy-architecture",
    "Application security assessment": "c3-rugged-computing",
    "Network infrastructure security assessment": "c3-comms-shelter",
    "Database security assessment": "cy-architecture",
    "Managed security operations centre": "c3-command-centre",
    "Security monitoring service": "c3-command-centre",
    "Digital forensics and incident response": "c3-rugged-computing",
    "Red team services": "cy-architecture",
    "Security risk assessment": "cy-architecture",
    "Secure configuration review": "c3-rugged-computing",
    "Compliance assessment": "cy-architecture",
    "Email phishing simulation service": "cy-architecture",
    "Security awareness portfolio": "c3-command-centre",
    "Security information and event management": "c3-rugged-computing",
    "Deception platform": "cy-architecture",
    "Threat intelligence platform": "c3-command-centre",
    # 11 AI and digital intelligence
    "Reputation and information environment monitoring": "cy-architecture",
    "Computer vision": "isr-naval-eo",
    "Big data analytics": "c3-rugged-computing",
    "National security picture and intelligence fusion": "c3-command-centre",
    "Event, incident and information flow management": "c3-command-centre",
    # 12 Safe city and infrastructure
    "Safe city surveillance and operational visibility": "sc-bodycam",
    "Integrated command environments": "c3-command-centre",
    "Emergency response communication solutions": "c3-dmr-professional",
    "Perimeter and site protection": "eo-border",
    "Ballistic protection": "wpn-ammo-cases",
    "Telecom network design, integration and optimisation": "c3-comms-shelter",
    "Revenue assurance and fraud analytics": "c3-rugged-computing",
    "Call detail record analysis and mediation": "cy-architecture",
    "Energy efficient power and infrastructure systems": "ind-plant",
    "Climate monitoring and environmental data intelligence": "tst-instrument",
    "Waste and resource management frameworks": "ind-plant",
    "Smart municipal and urban optimisation systems": "c3-command-centre",
    # cross-domain
    "Specialised raw materials and alloys": "ind-plant",
    "Industrial plants and equipment": "ind-plant",
    "Test and measurement equipment": "tst-instrument",
}


def image_for(name, kind, domain_slug=None):
    """Return an image stem for a catalogue entry, or None."""
    if kind == "model":
        hit = MODEL_IMAGES.get(name)
        if hit:
            return hit
    return FAMILY_IMAGES_BY_NAME.get(name)
