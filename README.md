# LANsurfer website

Source of the LANsurfer project website, [www.lansurfer.de](https://www.lansurfer.de): a static,
bilingual (English/German) page that explains [LANsurfer](https://github.com/convention-x-treme/lansurfer)
and links to the [demo](https://demo.lansurfer.de), self-hosting docs and GitHub.

Plain HTML and CSS. No build tool, no framework, no JavaScript, no cookies, no analytics, no
external fonts. What is in `site/` is exactly what gets published.

## Layout

```text
site/
├── index.html                     English home        → /
├── imprint/index.html             English imprint     → /imprint/
├── privacy/index.html             English privacy     → /privacy/
├── de/index.html                  German home         → /de/
├── de/impressum/index.html        German imprint      → /de/impressum/
├── de/datenschutz/index.html      German privacy      → /de/datenschutz/
├── 404.html                       served by GitHub Pages for unknown URLs
└── assets/
    ├── site.css                   all styling, dark theme in the LANsurfer colors
    ├── fonts/  licenses/          self-hosted Schibsted Grotesk + JetBrains Mono (OFL-1.1)
    ├── images/                    favicon, touch icon, otter mascot
    └── screenshots/               app screenshots (WebP)
scripts/check.py                   site test (Python 3 standard library only)
.github/workflows/pages.yml        test, build and deploy to GitHub Pages
```

## Preview locally

```sh
python3 -m http.server 8000 --directory site
```

Open <http://localhost:8000/> and <http://localhost:8000/de/>. The site is dark-only, independent of
the visitor's OS or browser theme.

## Test

```sh
python3 scripts/check.py
```

Fails on missing pages, missing `lang`/title/description, wrong canonical URLs, `hreflang`
alternates that do not point at existing, mutually consistent EN/DE pages, broken local links,
images or `#fragments`, any `<script>`, and any stylesheet/image/font loaded from another origin.
CI runs the same command.

## Deployment

`.github/workflows/pages.yml`:

| Event | What runs |
| --- | --- |
| Pull request | test only |
| Push to `main`, manual run | test → upload `site/` as Pages artifact → deploy |

There is no build step beyond packaging `site/` into the Pages artifact.

### One-time repository setup

1. **Settings → Pages → Source: GitHub Actions.**
2. **Settings → Pages → Custom domain:** `www.lansurfer.de`, then enable **Enforce HTTPS** once the
   certificate is issued.
3. DNS: `www` `CNAME` `convention-x-treme.github.io`. Redirect the apex `lansurfer.de` to `www`
   at the DNS provider (or add GitHub's apex `A`/`AAAA` records).

Until the custom domain is active the site is reachable at
`https://convention-x-treme.github.io/lansurfer-website/`. All pages use relative links so they
work there too; only `404.html` uses root-absolute paths (GitHub serves it at any depth) and is
therefore unstyled until the custom domain is live.

## Before going live

Full checklist (GitHub settings, DNS, legal texts, content review, LANsurfer repository
follow-ups): [docs/OPEN_TASKS.md](docs/OPEN_TASKS.md).

The German imprint and privacy texts (Impressum, Datenschutz) are the legally binding versions.

## Editing content

- English and German pages are maintained by hand. Change both language versions together; the
  check catches missing pages and broken `hreflang` pairs, not wording drift.
- Keep links relative (`assets/...`, `../assets/...`), except in `404.html`.
- Colors, fonts, wordmark and mascot usage follow `DESIGN.md` in the
  [LANsurfer repository](https://github.com/convention-x-treme/lansurfer/blob/main/DESIGN.md).
  Show at most one otter per page.
- No `<script>`, no third-party embeds. Adding either changes the privacy text.

### Updating screenshots

The screenshots are captures of a running LANsurfer instance at about 1665 px wide, saved as WebP
under `site/assets/screenshots/`:

| File | View |
| --- | --- |
| `game-requests-dark.webp` | Game Requests list |
| `game-request-dark.webp` | A Game Request detail page with lobby |
| `games-dark.webp` | Game catalog |
| `game-requests-light.webp` | Game Requests list in the app's light theme, shown last as a preview |

Convert a PNG capture with `magick capture.png -quality 82 -define webp:method=6 name.webp`. When a
file's pixel size changes, update the `width`/`height` attributes in both `index.html` files.

## Licenses

LANsurfer's name, logo and otter illustrations: see
[ASSETS-LICENSE.md](https://github.com/convention-x-treme/lansurfer/blob/main/ASSETS-LICENSE.md) in
the LANsurfer repository. Fonts: SIL Open Font License 1.1, texts in `site/assets/licenses/`.
