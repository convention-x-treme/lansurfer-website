# Open tasks

Remaining work around www.lansurfer.de. Each section is tracked as a GitHub issue; the issues are
the source of truth. Delete this file once they are all closed.

Status checked on 2026-10-30: www.lansurfer.de is live (GitHub Pages, HTTPS enforced, certificate
for `www.lansurfer.de` and `lansurfer.de`).

## 1. Repository ([#1](https://github.com/convention-x-treme/lansurfer-website/issues/1), open)

- [x] Commit the initial site and push `main` (0d61e50).
- [ ] Optional: protect `main` so pull requests must pass the `build` job (it runs
      `python3 scripts/check.py`). `main` has no branch protection and no ruleset yet.

## 2. GitHub settings ([#2](https://github.com/convention-x-treme/lansurfer-website/issues/2), closed)

- [x] Repository is public, so Actions and Pages run without a paid plan.
- [x] **Settings → Pages → Source:** GitHub Actions.
- [x] **Settings → Environments → github-pages:** deployments allowed from `main`.
- [x] **Settings → Pages → Custom domain:** `www.lansurfer.de`.
- [x] **Settings → Pages → Enforce HTTPS:** enabled.
- [x] Workflow runs and deploys on every push to `main`.
- [ ] Optional, not done: **Organization settings → Pages → Verified domains:** verify
      `lansurfer.de` so no other repository can claim the domain (needs the `TXT` record
      `_github-pages-challenge-convention-x-treme.lansurfer.de`).

## 3. DNS ([#3](https://github.com/convention-x-treme/lansurfer-website/issues/3), open)

- [x] `www.lansurfer.de` `CNAME` `convention-x-treme.github.io.`
- [x] Apex `lansurfer.de`: GitHub's `A`/`AAAA` records; GitHub redirects it to
      `https://www.lansurfer.de/`.
- [ ] `demo.lansurfer.de` has no DNS record yet; the "Try the demo" buttons link to it. Point it at
      the demo instance and confirm `https://demo.lansurfer.de` loads.

## 4. Legal texts ([#4](https://github.com/convention-x-treme/lansurfer-website/issues/4), open)

Files: `site/imprint/index.html`, `site/privacy/index.html`, `site/de/impressum/index.html`,
`site/de/datenschutz/index.html`.

- [x] Operator details filled in: association, address, contact email, person responsible for
      content (§ 18 Abs. 2 MStV), supervisory authority (LfDI Baden-Württemberg).
- [x] Draft notices removed from all four pages.
- [ ] Legal review of imprint and privacy text (German version is declared binding). Check the
      GitHub Pages hosting paragraph (server logs, USA transfer, Data Privacy Framework) against
      GitHub's current terms.

## 5. Content review ([#5](https://github.com/convention-x-treme/lansurfer-website/issues/5), open)

- [ ] Review English and German copy on `site/index.html` and `site/de/index.html` (drafted from
      the LANsurfer README).
- [x] Screenshots replaced with captures of a real instance (Game Requests, Game Request detail,
      game catalog, light theme preview). Recapture whenever the UI changes noticeably.
- [x] Outbound links resolve: `docs/SELF_HOSTING.md`, `CONTRIBUTING.md`, `LICENSE`, releases and
      issues of the LANsurfer repository, convention-x-treme.de.

## 6. Follow-ups in the LANsurfer repository ([#6](https://github.com/convention-x-treme/lansurfer-website/issues/6), open)

None done yet.

- [ ] Delete the superseded working docs on branch `docs/site-and-demo-plans`:
      `docs/superpowers/plans/2026-10-24-project-website-plan.md` and
      `docs/superpowers/specs/2026-10-24-project-website-design.md` (both still exist).
- [ ] `README.md`: link the project website (www.lansurfer.de) and the demo.
- [ ] `docs/TERMINOLOGY.md`: add "Project website" (www.lansurfer.de, this repository) as distinct
      from the in-app "Landing page" (logged-out `GET /`).
- [ ] `docs/ARCHITECTURE.md` §20 Release and distribution: one line that the project website is a
      separate repository deployed by GitHub Pages and is not part of release artifacts.
- [ ] Update convention-x-treme/lansurfer#226 with this repository and close it; the site is live.

## 7. After launch ([#7](https://github.com/convention-x-treme/lansurfer-website/issues/7), closed)

- [x] `/`, `/de/`, `/imprint/`, `/privacy/`, `/de/impressum/`, `/de/datenschutz/` and an unknown URL
      (styled 404) load on desktop and phone: dark theme, self-hosted fonts, no broken images, no
      horizontal overflow.
- [x] `http://` and `https://lansurfer.de` and `http://www.lansurfer.de` redirect to
      `https://www.lansurfer.de/`.
