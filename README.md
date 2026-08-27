# Maalik Creative Engineers — corporate website

A complete static website built from the *Master Website Content and Architecture Guide*,
using the visual system of redcat.red adapted to the Maalik Creative Engineers brand mark.

**73 pages. No build step required to view or deploy. No server-side dependency.**

---

## Running it

Open `index.html` directly, or serve the folder (recommended, so that clean URLs work):

```bash
python -m http.server 8181
```

Then visit <http://127.0.0.1:8181/>.

## Deploying it

Upload the whole folder to any static host — Netlify, Cloudflare Pages, GitHub Pages,
Vercel, or ordinary shared hosting. Nothing needs to be compiled.

Exclude `_build/` from the upload; it is the generator, not part of the site.

Before going live, set the real domain in `_build/run.py` (`sitemap(base=...)`) and rebuild,
so `sitemap.xml` and `robots.txt` carry the correct hostname.

---

## What is here

| Section | Pages |
|---|---|
| Home | 1 |
| Capabilities | index, 12 capability domains, Beyond the Catalogue |
| Products | filterable index of 197 families and named systems |
| Sectors | index + 6 sector pages |
| Services | index + 7 service pages |
| Partners | directory, 22 partner profiles, Become a Partner |
| About | Company, Leadership, Programmes, Quality, Facilities |
| Insights, Careers, Downloads, Search | 4 |
| Contact | 4 routes, 4 separate forms |
| Legal | Privacy, Terms, Export Control, Accessibility |
| System | 404 |

### Implemented behaviour

- Sticky header that compresses on scroll, with a full-width Capabilities mega menu
  (hover on pointer devices, tap on touch devices).
- Full-screen mobile navigation with accordion sections and a permanently visible
  Contact action pinned to the viewport.
- Product index with five filter facets, type-ahead search, live result count, and
  **shareable filter URLs** — every filter state is written to the query string and
  restored on load, exactly as Section 4.5 requires.
- Empty-state copy that converts a dead end into an enquiry
  ("Not listed does not mean not available").
- Four contact routes with four distinct forms and four distinct confirmation states.
  Forms validate client-side and show a response-time commitment; **they are not wired
  to a back end** — see *Before launch* below.
- Partner directory filtering by capability group and by region.
- Expandable model tables (the C3 domain lists 41 systems, collapsed to 10).
- Reveal-on-scroll, respecting `prefers-reduced-motion`.

---

## Design system

Derived from redcat.red — near-black canvas, wide letter-spaced condensed uppercase
display type, light body text, a single accent colour, full-bleed image bands alternating
with contained content, and one light "paper" band per page for rhythm.

The accent red is sampled directly from your logo: `#E11414`, with `#8F0000` deep and
`#FF2A1F` hot.

Typography follows Section 1.5 of the guide: **Barlow Semi Condensed** for display and
headings, **Barlow Condensed** for navigation and labels, **Inter** for body, and
**IBM Plex Mono** for model designations and specification tables.

Component rules from Section 1.5 are respected throughout: 2 px corner radius everywhere,
no drop shadows, a 2 px left border that turns red on card hover, a 3 px accent rule under
every section heading, and single-weight 1.5 px line icons drawn on a 24 px grid.

### One deliberate departure from the guide

Section 1.5 specifies a deep-navy and antique-brass palette. You asked for the redcat.red
scheme, and your logo is red, so the site is built dark with the brand red as accent.
Everything else in Section 1.5 — the typographic scale, grid, spacing rhythm, component
treatment and icon rules — is followed as written. If you would rather have the navy
system, it is a change to the colour variables at the top of `assets/css/site.css` and
nothing else.

---

## Editing the content

All copy and structure live in **`_build/data.py`**. Change it there and rebuild:

```bash
python _build/run.py
```

That regenerates all 73 pages. The twelve capability domains, six sectors and seven
services are each driven by a single template, so a thirteenth domain is a content entry,
not a development sprint — as Section 4.2 insists.

| File | Purpose |
|---|---|
| `_build/data.py` | All content: domains, families, models, sectors, services, partners, copy bank |
| `_build/build.py` | Page shell, header, mega menu, footer, shared blocks |
| `_build/pages.py` | Home, capabilities, domain template, products, sectors |
| `_build/pages2.py` | Services, partners, forms, contact routes |
| `_build/pages3.py` | About set, insights, careers, downloads, legal, system pages |
| `_build/icons.py` | The custom line icon set |
| `_build/plates.py` | Generated technical plates used where product photography does not yet exist |
| `_build/run.py` | Builds everything, writes `sitemap.xml` and `robots.txt` |

---

## Before launch

### 1. Replace every bracketed placeholder

Search the built site for `[insert` — each one is a fact that must be verified before
publication, per the reading conventions in Section 0:

- Company registration number and National Tax Number
- Head office address, direct telephone, and the four monitored email addresses
- Leadership names, roles and biographies
- Certification names, certifying bodies, certificate scopes and numbers
- Timeline years on the About page
- Indicative periods in the Programmes table

The four statistics on the homepage (15 years, 12 domains, 20+ partners, 13 programme
categories) are derived from the guide and must be confirmed before publication.

### 2. Wire up the forms

The four forms validate and confirm client-side but do not send. Point each at your own
handler or a form service, keeping the four separate inboxes:

| Form | Routes to |
|---|---|
| `/contact/` | General inbox |
| `/contact/request-for-information/` | Bid and technical team |
| `/contact/partnership/` | Business development |
| `/contact/support/` | Service and support team |

Add server-side validation, virus scanning on the 25 MB upload, and a CAPTCHA that does
not obstruct legitimate users. Then honour the published commitment: every enquiry
acknowledged within one working day.

### 3. Commission the photography

This is the highest-return item in the whole project, and Section 7.1 is right about it.
The images currently in `assets/img/` are licence-free environmental, industrial and
technical photography, colour-graded into one consistent library. They are deliberately
**environment-led, never equipment-led**, because Section 7.4 rules out AI-generated
imagery of equipment, foreign military stock, and anything showing identifiable personnel
or installations. They are placeholders with a defensible licence position, not a
substitute for your own facility shoot.

Replace them with:

- One professional photography day covering the workshop, integration bench, secure
  storage, training delivery and the team at work.
- Leadership portraits from that same session — same background, lighting and crop.
- Manufacturer-supplied product photography, cleared in writing for marketing use.

Keep the same filenames and everything picks the new images up automatically.

Where product photography does not exist yet, family cards carry a **generated technical
plate** rather than a repeated photograph or an invented product render. Each plate is
deterministic and unique to its family. Swap them for real product shots as the asset
library fills.

### 4. Clear the partner directory

Section 6 and Section 10.2 are unambiguous and this is a legal matter, not a design one.
For every one of the 22 partner entries, confirm in writing: that a current relationship
exists, what the manufacturer permits you to call it, whether logo and product imagery use
is authorised, and whether they require pre-approval of the page copy. Hold back any entry
where that is unresolved.

The directory currently uses **text-only entries with no manufacturer logos**, which is the
safe default. Add logos only where written permission is held. Every profile carries a
`[insert approved designation]` field for the relationship wording — fill it with the
manufacturer's approved language and nothing more.

### 5. Build the controlled datasheet workflow

The Downloads page publishes the corporate documents openly and gates technical detail
behind a verified request, as Section 4.3 requires. The request form needs a back end that
captures organisation, role, official email domain and intended use, and releases
manually after verification.

---

## Accuracy and compliance notes carried into the build

- No performance parameters are published anywhere on open pages. Air Defence and Weapon
  Systems pages carry a standing note explaining why, and describe systems by class and
  role only.
- Domain 11 copy consistently frames AI and digital intelligence platforms as lawful,
  authorised use by mandated agencies, with governance and audit presented as product
  features.
- The Programmes page presents capability categories rather than contract values, and
  closes with the confidentiality statement from Section 8.4.
- The About page carries the heritage and continuity note verbatim in substance, because
  an unsupportable credential claim found during due diligence is a disqualification.
- The banned-words list in Section 8.6 was applied to every line of copy written here.

---

## Technical

- Semantic HTML, one `<h1>` per page, breadcrumbs below level one.
- WCAG 2.2 AA intent: skip link, visible focus rings, descriptive alt text, no colour-only
  meaning, reduced-motion support.
- Meta title and description per page, taken from Section 8.5 where specified.
- `sitemap.xml` and `robots.txt` generated at build time.
- Total site weight 8.1 MB, of which 4.7 MB is imagery. Images are lazy-loaded below the
  fold. Before launch, convert to AVIF with WebP and JPEG fallbacks at the five responsive
  widths listed in Section 7.5.
- No external JavaScript, no tracking, no cookies set by the site itself. Fonts load from
  Google Fonts; self-host them if you would rather not make that request.
