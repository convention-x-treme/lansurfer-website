#!/usr/bin/env python3
"""Check the static site in site/ before it is published.

Fails on: missing pages, missing lang/title/description, canonical or hreflang
links that do not match a page, broken local links/images/fragments, any
<script>, and any resource (stylesheet, image, font) loaded from another origin.
Standard library only.
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag, urlsplit

SITE = Path(__file__).resolve().parent.parent / "site"
ORIGIN = "https://www.lansurfer.de/"
PAGES = [
    "index.html", "imprint/index.html", "privacy/index.html",
    "de/index.html", "de/impressum/index.html", "de/datenschutz/index.html",
    "404.html",
]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = self.title = self.description = self.canonical = None
        self.alternates = {}
        self.refs = []  # (attribute, value) pairs that load or link something
        self.ids = set()
        self.scripts = 0
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "title":
            self._in_title = True
        elif tag == "script":
            self.scripts += 1
        elif tag == "meta" and a.get("name") == "description":
            self.description = a.get("content")
        elif tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        elif tag == "link" and a.get("rel") == "alternate" and "hreflang" in a:
            self.alternates[a["hreflang"]] = a.get("href")
        elif tag in ("a", "link") and "href" in a:
            self.refs.append(("href", a["href"]))
        for key in ("src", "srcset"):
            if key in a:
                self.refs += [(key, part.split()[0]) for part in a[key].split(",")]

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title = (self.title or "") + data


def target(page_path, ref):
    """Map a local reference to the file it serves, or None if it is missing."""
    ref = urlsplit(ref).path
    base = SITE if ref.startswith("/") else page_path.parent
    path = (base / ref.lstrip("/")).resolve()
    if ref.endswith("/") or path.is_dir():
        path = path / "index.html"
    return path if path.is_file() and path.is_relative_to(SITE) else None


def canonical_file(url):
    return SITE / urlsplit(url).path.lstrip("/") / "index.html" if url.endswith("/") else None


def check():
    errors = []
    parsed = {}
    for rel in PAGES:
        path = SITE / rel
        if not path.is_file():
            errors.append(f"{rel}: missing")
            continue
        page = Page()
        page.feed(path.read_text(encoding="utf-8"))
        parsed[rel] = page

    for rel, page in parsed.items():
        path = SITE / rel
        err = lambda msg: errors.append(f"{rel}: {msg}")
        if page.lang not in ("en", "de"):
            err(f"html lang is {page.lang!r}")
        if not (page.title or "").strip():
            err("empty <title>")
        if not page.description:
            err("missing meta description")
        if page.scripts:
            err("contains <script>")

        if rel != "404.html":
            expected = ORIGIN + rel.removesuffix("index.html")
            if page.canonical != expected:
                err(f"canonical {page.canonical!r}, want {expected!r}")
            if set(page.alternates) != {"en", "de", "x-default"}:
                err(f"hreflang set {sorted(page.alternates)}")
            if page.alternates.get(page.lang) != page.canonical:
                err("hreflang for own language does not point at the canonical URL")
            if page.alternates.get("x-default") != page.alternates.get("en"):
                err("x-default must point at the English page")
            for lang, url in page.alternates.items():
                file = canonical_file(url or "")
                if not (url or "").startswith(ORIGIN) or file is None or not file.is_file():
                    err(f"hreflang {lang} -> {url} has no page")
                    continue
                other = parsed.get(str(file.relative_to(SITE)))
                if lang != "x-default" and other and other.alternates != page.alternates:
                    err(f"hreflang alternates differ from {file.relative_to(SITE)}")

        for key, ref in page.refs:
            scheme = urlsplit(ref).scheme
            if scheme in ("http", "https", "mailto"):
                if key != "href" or ref.startswith("http:"):
                    err(f"external or insecure {key}: {ref}")
                continue
            if scheme:
                err(f"unexpected URL scheme: {ref}")
                continue
            ref_path, fragment = urldefrag(ref)
            file = target(path, ref_path) if ref_path else path
            if file is None:
                err(f"broken {key}: {ref}")
            elif fragment:
                linked = parsed.get(str(file.relative_to(SITE)))
                if linked is None or fragment not in linked.ids:
                    err(f"broken fragment: {ref}")

    css = (SITE / "assets/site.css").read_text(encoding="utf-8")
    for url in re.findall(r"url\([\"']?([^\"')]+)", css):
        if urlsplit(url).scheme or not (SITE / "assets" / url).is_file():
            errors.append(f"assets/site.css: bad url({url})")

    return errors


if __name__ == "__main__":
    problems = check()
    for problem in problems:
        print(problem, file=sys.stderr)
    print(f"{len(PAGES)} pages checked, {len(problems)} problem(s)")
    sys.exit(1 if problems else 0)
