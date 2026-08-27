# -*- coding: utf-8 -*-
"""
Generated technical plates.

Product photography must come from the manufacturer's asset library or an own
studio shoot (Section 7.2). Until that library exists, a family card carries a
drawn technical plate rather than a repeated photograph or an invented product
render -- Section 7.4 prohibits AI-generated imagery of equipment.

Each plate is deterministic: the same family name always produces the same
drawing, so the site does not shuffle between builds.
"""
import hashlib
import math

from icons import _P, _W


def _rng(seed):
    """Small deterministic PRNG seeded from a string."""
    h = hashlib.sha256(seed.encode("utf-8")).digest()
    state = [b for b in h]
    i = [0]

    def nxt():
        i[0] = (i[0] + 1) % len(state)
        state[i[0]] = (state[i[0]] * 33 + 17 + i[0]) % 251
        return state[i[0]] / 251.0
    return nxt


W, H = 400, 250
RED = "#e11414"


def _grid(step=20):
    out = []
    x = 0
    while x <= W:
        out.append('<line x1="%d" y1="0" x2="%d" y2="%d"/>' % (x, x, H))
        x += step
    y = 0
    while y <= H:
        out.append('<line x1="0" y1="%d" x2="%d" y2="%d"/>' % (y, W, y))
        y += step
    return '<g stroke="#ffffff" stroke-width=".5" opacity=".055">%s</g>' % "".join(out)


def _arcs(r):
    """Concentric detection arcs with a sweep."""
    cx, cy = 62 + r() * 40, H - 26
    out = []
    for i in range(6):
        rad = 34 + i * 34
        out.append('<path d="M %.1f %.1f A %.1f %.1f 0 0 1 %.1f %.1f" fill="none" '
                   'stroke="%s" stroke-width="1" opacity="%.2f"/>'
                   % (cx - rad, cy, rad, rad, cx + rad, cy, RED, 0.42 - i * 0.055))
    ang = 34 + r() * 26
    out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.2" '
               'opacity=".55"/>' % (cx, cy, cx + 250 * math.cos(math.radians(-ang)),
                                    cy + 250 * math.sin(math.radians(-ang)), RED))
    for i in range(4):
        out.append('<circle cx="%.1f" cy="%.1f" r="2" fill="#fff" opacity=".5"/>'
                   % (cx + 40 + r() * 250, 34 + r() * 130))
    return "".join(out)


def _wave(r):
    """Spectrum trace."""
    pts, x = [], 0
    base = H * 0.62
    while x <= W:
        v = (math.sin(x / (16 + r() * 8)) * (10 + r() * 26)
             + math.sin(x / 47.0) * 20)
        pts.append("%.1f,%.1f" % (x, base - v))
        x += 8
    bars = "".join('<rect x="%.1f" y="%.1f" width="2" height="%.1f" fill="#fff" opacity=".13"/>'
                   % (i * 15 + 6, base + 12, 6 + r() * 44) for i in range(26))
    return ('%s<polyline points="%s" fill="none" stroke="%s" stroke-width="1.4" opacity=".72"/>'
            '<line x1="0" y1="%.1f" x2="%d" y2="%.1f" stroke="#fff" stroke-width=".6" opacity=".18"/>'
            % (bars, " ".join(pts), RED, base + 10, W, base + 10))


def _mesh(r):
    """Node graph."""
    nodes = [(30 + r() * (W - 60), 26 + r() * (H - 52)) for _ in range(11)]
    lines = []
    for i, a in enumerate(nodes):
        for b in nodes[i + 1:]:
            d = math.hypot(a[0] - b[0], a[1] - b[1])
            if d < 118:
                lines.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#fff" '
                             'stroke-width=".7" opacity="%.2f"/>' % (a[0], a[1], b[0], b[1],
                                                                     0.30 - d / 620.0))
    dots = "".join('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" opacity=".8"/>'
                   % (n[0], n[1], 2.2 + (i % 3), RED if i % 3 == 0 else "#ffffff")
                   for i, n in enumerate(nodes))
    return "".join(lines) + dots


def _contour(r):
    """Topographic contour set."""
    out = []
    for i in range(9):
        amp = 12 + r() * 16
        ph = r() * 6
        y0 = 24 + i * 26
        pts = []
        x = -10
        while x <= W + 10:
            pts.append("%.1f,%.1f" % (x, y0 + math.sin(x / 58.0 + ph) * amp))
            x += 14
        out.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1" opacity="%.2f"/>'
                   % (" ".join(pts), RED if i % 4 == 0 else "#ffffff",
                      0.30 if i % 4 == 0 else 0.13))
    return "".join(out)


def _reticle(r):
    """Sighting reticle with scale ticks."""
    cx, cy = W * (0.36 + r() * 0.2), H * 0.48
    out = ['<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" stroke-width="1" opacity=".55"/>'
           % (cx, cy, 46, RED),
           '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="#fff" stroke-width=".7" opacity=".22"/>'
           % (cx, cy, 78)]
    for a in range(0, 360, 15):
        rad = math.radians(a)
        ln = 8 if a % 45 else 15
        out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#fff" stroke-width=".8" '
                   'opacity=".30"/>' % (cx + 46 * math.cos(rad), cy + 46 * math.sin(rad),
                                        cx + (46 + ln) * math.cos(rad), cy + (46 + ln) * math.sin(rad)))
    out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width=".9" opacity=".6"/>'
               % (cx - 66, cy, cx + 66, cy, RED))
    out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width=".9" opacity=".6"/>'
               % (cx, cy - 66, cx, cy + 66, RED))
    return "".join(out)


def _iso(r):
    """Orthographic module stack."""
    out = []
    ox, oy = 96 + r() * 60, 60 + r() * 30
    for i in range(4):
        w, h2 = 84, 22
        y = oy + i * 30
        out.append('<path d="M %.1f %.1f l %d -%d l %d %d l -%d %d z" fill="none" stroke="%s" '
                   'stroke-width="1" opacity="%.2f"/>'
                   % (ox, y, w, h2, w, h2, w, h2, RED if i == 1 else "#ffffff", 0.5 if i == 1 else 0.2))
    for i in range(3):
        out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#fff" stroke-width=".6" '
                   'opacity=".18"/>' % (30, 40 + i * 62, W - 30, 40 + i * 62))
    return "".join(out)


_MOTIFS = [_arcs, _wave, _mesh, _contour, _reticle, _iso]


def plate(seed, icon_name, tag=""):
    """Return an inline SVG technical plate, deterministic for `seed`."""
    r = _rng(seed)
    motif = _MOTIFS[int(hashlib.sha256(seed.encode("utf-8")).hexdigest(), 16) % len(_MOTIFS)]
    watermark = ""
    body = _P.get(icon_name)
    if body:
        watermark = ('<g transform="translate(%d,%d) scale(%.2f)" opacity=".07" stroke="#ffffff" '
                     'stroke-width="1.5" fill="none">%s</g>'
                     % (W - 150, H - 150, 5.6, body))
    label = ""
    if tag:
        label = ('<text x="16" y="%d" fill="#ffffff" opacity=".30" '
                 'font-family="IBM Plex Mono, monospace" font-size="9" '
                 'letter-spacing="2">%s</text>' % (H - 14, tag))
    gid = hashlib.sha256(seed.encode("utf-8")).hexdigest()[:8]
    return (
        '<svg class="plate-svg" viewBox="0 0 %d %d" preserveAspectRatio="xMidYMid slice" '
        'role="img" aria-hidden="true">'
        '<defs><linearGradient id="g%s" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#14151a"/><stop offset="1" stop-color="#08080a"/>'
        '</linearGradient></defs>'
        '<rect width="%d" height="%d" fill="url(#g%s)"/>%s%s%s%s'
        '<rect x=".5" y=".5" width="%d" height="%d" fill="none" stroke="#ffffff" opacity=".07"/>'
        '</svg>'
        % (W, H, gid, W, H, gid,
           _grid(), watermark, motif(r), label, W - 1, H - 1))
