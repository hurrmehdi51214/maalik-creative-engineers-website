# -*- coding: utf-8 -*-
"""Build the whole site.  Run from the project root:  python _build/run.py"""
import os, sys, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build as core
from build import PAGES, ROOT, DOMAINS, SECTORS, SERVICES, PARTNERS, CONTACT_ROUTES  # noqa
import pages, pages2, pages3


def sitemap(base="https://www.maalikcreative.com"):
    urls = []
    for p in sorted(set(PAGES)):
        if p.endswith("404.html"):
            continue
        loc = p.replace("index.html", "").replace("\\", "/")
        prio = "1.0" if loc == "" else ("0.9" if loc.count("/") <= 1 else "0.7")
        urls.append("  <url><loc>%s/%s</loc><changefreq>monthly</changefreq>"
                    "<priority>%s</priority></url>" % (base.rstrip("/"), loc, prio))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n'
           % "\n".join(urls))
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % base.rstrip("/"))


def main():
    pages.build_home()
    pages.build_capabilities_index()
    for dm in DOMAINS:
        pages.build_domain(dm)
    pages.build_beyond()
    pages.build_products()
    pages.build_sectors_index()
    for i, s in enumerate(SECTORS):
        pages.build_sector(s, i + 1)

    pages2.build_services_index()
    for i, s in enumerate(SERVICES):
        pages2.build_service(s, i + 1)
    pages2.build_partners_index()
    for p in PARTNERS:
        pages2.build_partner(p)
    pages2.build_become_partner()
    for r in CONTACT_ROUTES:
        pages2.build_contact(r)

    pages3.build_about()
    pages3.build_leadership()
    pages3.build_programmes()
    pages3.build_quality()
    pages3.build_facilities()
    pages3.build_insights()
    pages3.build_careers()
    pages3.build_downloads()
    for slug in pages3.LEGAL:
        pages3.build_legal(slug)
    pages3.build_search()
    pages3.build_404()

    sitemap()
    print("Built %d pages  (%s)" % (len(set(PAGES)), datetime.date.today()))
    for p in sorted(set(PAGES)):
        print("  ", p.replace("\\", "/"))


if __name__ == "__main__":
    main()
