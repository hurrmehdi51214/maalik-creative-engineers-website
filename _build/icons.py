# -*- coding: utf-8 -*-
"""
Custom line icon set. Single weight, 1.5 px stroke, drawn on a 24 px grid,
no fills -- per Section 1.5 and Section 7.2 of the content guide.
"""

_W = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
      'stroke-linecap="square" stroke-linejoin="miter" aria-hidden="true">{}</svg>')

_P = {
    # 01 Command, Control and Communications -- mast radiating
    "c3": '<path d="M12 21V9"/><path d="M9 21h6"/><path d="M12 9l-3.2 6.5M12 9l3.2 6.5"/>'
          '<path d="M8.4 6.2a5 5 0 0 1 7.2 0"/><path d="M6.1 3.6a8.4 8.4 0 0 1 11.8 0"/>'
          '<circle cx="12" cy="8" r="1"/>',
    # 02 ISR -- radar sweep
    "isr": '<path d="M12 12 21 7.5"/><path d="M3.6 16.4a10 10 0 1 1 16.8 0"/>'
           '<path d="M6.9 14.6a6.2 6.2 0 1 1 10.2 0"/><circle cx="12" cy="12" r="1.1"/>'
           '<path d="M3 19.5h18"/>',
    # 03 Electro-optics -- reticle over lens
    "eo": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3.2"/>'
          '<path d="M12 1.6v4.2M12 18.2v4.2M1.6 12h4.2M18.2 12h4.2"/>',
    # 04 Unmanned systems -- quadrotor
    "uas": '<rect x="9.5" y="9.5" width="5" height="5"/><path d="M9.5 9.5 5.6 5.6M14.5 9.5l3.9-3.9'
           'M9.5 14.5l-3.9 3.9M14.5 14.5l3.9 3.9"/><circle cx="4.4" cy="4.4" r="2"/>'
           '<circle cx="19.6" cy="4.4" r="2"/><circle cx="4.4" cy="19.6" r="2"/>'
           '<circle cx="19.6" cy="19.6" r="2"/>',
    # 05 Air defence -- layered engagement arcs
    "airdef": '<path d="M2.5 20h19"/><path d="M12 20V9.5"/><path d="m9.4 12.6 2.6-3.1 2.6 3.1"/>'
              '<path d="M5.2 20a6.8 6.8 0 0 1 13.6 0"/><path d="M2.5 20a9.5 9.5 0 0 1 19 0"/>'
              '<path d="M12 9.5V4"/>',
    # 06 Weapon systems -- guided trajectory to point
    "weapons": '<path d="M3 20.5c5.6 0 9-3.2 11.4-8.2"/><path d="m14.4 12.3 5.6-8.8"/>'
               '<path d="M20 3.5h-4.1M20 3.5v4.1"/><circle cx="20" cy="3.5" r="0"/>'
               '<path d="M3 20.5H1.8M3 20.5v1.2"/><circle cx="14.4" cy="12.3" r="1.6"/>',
    # 07 Electronic warfare -- spectrum
    "ew": '<path d="M2 12h2.4l1.4-6 2.2 12 2-9 2 13 2.1-14 1.6 8 1.1-4H22"/>',
    # 08 Avionics -- HUD horizon
    "avionics": '<rect x="2.5" y="4.5" width="19" height="15"/><path d="M2.5 12h6M15.5 12h6"/>'
                '<path d="m9.4 12 2.6-2.4 2.6 2.4-2.6 2.4z"/><path d="M6 8h1.6M6 16h1.6M16.4 8H18M16.4 16H18"/>',
    # 09 Platforms -- hull and chassis
    "platforms": '<path d="M2.5 15.5h19l-2.4 5H4.9z"/><path d="M5.5 15.5v-4h13v4"/>'
                 '<path d="M8.5 11.5v-3h7v3"/><path d="M12 8.5v-4"/><path d="M12 4.5h4.5"/>',
    # 10 Cyber -- shield with circuit
    "cyber": '<path d="M12 2.6 20 5.4v6.2c0 5-3.4 8.4-8 9.8-4.6-1.4-8-4.8-8-9.8V5.4z"/>'
             '<path d="M12 8v3.2M12 11.2H9.2v3M12 11.2h2.8v3"/>'
             '<circle cx="12" cy="7.2" r="0.9"/><circle cx="9.2" cy="15" r="0.9"/><circle cx="14.8" cy="15" r="0.9"/>',
    # 11 AI -- node graph
    "ai": '<circle cx="12" cy="4.6" r="2"/><circle cx="4.6" cy="12" r="2"/><circle cx="19.4" cy="12" r="2"/>'
          '<circle cx="8" cy="19.4" r="2"/><circle cx="16" cy="19.4" r="2"/>'
          '<path d="M10.6 6.2 6 10.4M13.4 6.2 18 10.4M5.6 13.8 7 17.5M18.4 13.8 17 17.5M10 19.4h4"/>',
    # 12 Safe city -- skyline under watch
    "safecity": '<path d="M2.5 20.5h19"/><path d="M4.5 20.5V11h4v9.5"/><path d="M10.5 20.5V6.5h4v14"/>'
                '<path d="M16.5 20.5V13h3.5v7.5"/><path d="M6 14h1M6 17h1M12 9.5h1M12 13h1M12 16.5h1"/>',
    # Beyond the catalogue
    "beyond": '<path d="M12 2.6v18.8M2.6 12h18.8"/><circle cx="12" cy="12" r="8.4" stroke-dasharray="2.6 2.6"/>'
              '<path d="m8.6 8.6 6.8 6.8M15.4 8.6l-6.8 6.8"/>',
    # services
    "svc-integration": '<rect x="2.5" y="2.5" width="7" height="7"/><rect x="14.5" y="2.5" width="7" height="7"/>'
                       '<rect x="8.5" y="14.5" width="7" height="7"/><path d="M6 9.5v3h12v-3M12 12.5v2"/>',
    "svc-procurement": '<path d="M5 2.5h9l5 5v14H5z"/><path d="M14 2.5v5h5"/><path d="M8 12h8M8 15.5h8M8 19h5"/>',
    "svc-logistics": '<path d="M2.5 7.5 12 3l9.5 4.5v9L12 21l-9.5-4.5z"/><path d="M2.5 7.5 12 12l9.5-4.5M12 12v9"/>',
    "svc-install": '<path d="M14.5 3.5a4 4 0 0 0 5.3 5.3L9.6 19H5v-4.6z"/><path d="M4 20.5h16"/>',
    "svc-mro": '<circle cx="12" cy="12" r="3.2"/><path d="M12 2.5v3.4M12 18.1v3.4M2.5 12h3.4M18.1 12h3.4'
               'M5.2 5.2 7.6 7.6M16.4 16.4l2.4 2.4M18.8 5.2 16.4 7.6M7.6 16.4l-2.4 2.4"/>',
    "svc-tot": '<path d="M3 8.5h12M3 8.5l3.5-3.5M3 8.5 6.5 12"/><path d="M21 15.5H9M21 15.5 17.5 12M21 15.5 17.5 19"/>',
    "svc-software": '<path d="m8 8-4.5 4L8 16"/><path d="m16 8 4.5 4L16 16"/><path d="m13.5 4.5-3 15"/>',
    # generic
    "doc": '<path d="M5.5 2.5h8l5 5v14h-13z"/><path d="M13.5 2.5v5h5"/><path d="M8.5 12h7M8.5 15.5h7M8.5 19h4"/>',
    "shield": '<path d="M12 2.6 20 5.4v6.2c0 5-3.4 8.4-8 9.8-4.6-1.4-8-4.8-8-9.8V5.4z"/>'
              '<path d="m8.4 12 2.6 2.6 4.6-5.2"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/>'
             '<path d="M12 3a14 14 0 0 1 0 18 14 14 0 0 1 0-18z"/>',
    "wrench": '<path d="M20 5.2a4.6 4.6 0 0 1-6 6L6.6 18.6a2.2 2.2 0 1 1-3.1-3.1L11 8.1a4.6 4.6 0 0 1 6-6l-3 3 2.1 2.1z"/>',
    "pin": '<path d="M12 21.5s7-6.4 7-11.5a7 7 0 1 0-14 0c0 5.1 7 11.5 7 11.5z"/><circle cx="12" cy="10" r="2.6"/>',
    "phone": '<path d="M6.5 2.6h4l1.6 4-2.3 1.6a12 12 0 0 0 6 6L17.4 12l4 1.6v4c0 1.1-.9 2-2 2A16.8 16.8 0 0 1 2.6 4.6c0-1.1.9-2 2-2z"/>',
    "mail": '<rect x="2.5" y="4.5" width="19" height="15"/><path d="m2.5 6 9.5 7 9.5-7"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 6.5V12l4 2.4"/>',
    "search": '<circle cx="10.5" cy="10.5" r="7"/><path d="m15.6 15.6 5 5"/>',
}


def icon(name, cls="ico"):
    body = _P.get(name)
    if body is None:
        body = _P["shield"]
    return '<span class="%s">%s</span>' % (cls, _W.format(body))
