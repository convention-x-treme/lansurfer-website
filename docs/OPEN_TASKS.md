# Open tasks

Everything still needed before www.lansurfer.de is live. Tick items off or delete this file once
done; it is a checklist, not documentation.

## 1. Repository

- [ ] Commit the initial site and push `main`. The repository has no commits yet; the first push
      to `main` runs `.github/workflows/pages.yml` and deploys, so finish the GitHub settings in
      section 2 first, or expect the first deploy to fail.
- [ ] Optional: protect `main` so pull requests must pass the `build` job (it runs
      `python3 scripts/check.py`).

## 2. GitHub settings (convention-x-treme/lansurfer-website)

- [ ] **Settings → Pages → Build and deployment → Source:** `GitHub Actions`.
- [ ] **Settings → Environments → github-pages:** confirm it allows deployments from `main`
      (GitHub creates it on the first Pages run; the default branch rule is `main`).
- [ ] **Settings → Pages → Custom domain:** `www.lansurfer.de`, save, wait for the DNS check.
- [ ] **Settings → Pages → Enforce HTTPS:** enable once the certificate is issued.
- [ ] Optional: **Organization settings → Pages → Verified domains:** verify `lansurfer.de` so no
      other repository can claim the domain.
- [ ] Run the workflow once (**Actions → Pages → Run workflow**) and open the deployed URL.

## 3. DNS (at the lansurfer.de provider)

- [ ] `www.lansurfer.de` `CNAME` `convention-x-treme.github.io.`
- [ ] Apex `lansurfer.de`: either a redirect to `https://www.lansurfer.de/` at the provider, or
      GitHub's apex records (`A` 185.199.108.153, 185.199.109.153, 185.199.110.153,
      185.199.111.153; `AAAA` 2606:50c0:8000::153, 2606:50c0:8001::153, 2606:50c0:8002::153,
      2606:50c0:8003::153) so GitHub redirects apex to `www`.
- [ ] If domain verification (section 2) is used: the `TXT` record GitHub shows for
      `_github-pages-challenge-convention-x-treme.lansurfer.de`.
- [ ] Confirm `https://demo.lansurfer.de` is live; the "Try the demo" buttons link to it.

## 4. Legal texts

Files: `site/imprint/index.html`, `site/privacy/index.html`, `site/de/impressum/index.html`,
`site/de/datenschutz/index.html`.

- [ ] Replace every `[bracketed placeholder]`: operator/association name, address, contact email,
      person responsible for content (§ 18 Abs. 2 MStV), competent data-protection supervisory
      authority.
- [ ] Legal review of imprint and privacy text (German version is declared binding). Check the
      GitHub Pages hosting paragraph (server logs, USA transfer, Data Privacy Framework) against
      GitHub's current terms.
- [ ] Remove the `<p class="notice">` "Draft"/"Entwurf" block from all four pages.

## 5. Content review

- [ ] Review English and German copy on `site/index.html` and `site/de/index.html` (drafted from
      the LANsurfer README).
- [ ] Recapture the screenshots before launch and whenever the UI changes noticeably (procedure in
      the README). The current `lobby-light.png` lists "Warcraft III" twice under "Recently viewed"
      because of fixture state from the capture run.
- [ ] Check the self-hosting links still point to the right places once the website goes live:
      `docs/SELF_HOSTING.md` and `CONTRIBUTING.md` on `main` of the LANsurfer repository.

## 6. Follow-ups in the LANsurfer repository

- [ ] Delete the superseded working docs on branch `docs/site-and-demo-plans`:
      `docs/superpowers/plans/2026-10-24-project-website-plan.md` and
      `docs/superpowers/specs/2026-10-24-project-website-design.md` (the website now lives in this
      repository; no `cmd/lansurfer-site`, `site:*` tasks or `site.yml` workflow are needed there).
- [ ] `README.md`: link the project website (www.lansurfer.de) and the demo.
- [ ] `docs/TERMINOLOGY.md`: add "Project website" (www.lansurfer.de, this repository) as distinct
      from the in-app "Landing page" (logged-out `GET /`).
- [ ] `docs/ARCHITECTURE.md` §20 Release and distribution: one line that the project website is a
      separate repository deployed by GitHub Pages and is not part of release artifacts.
- [ ] Update issue #226 with this repository, the remaining operator steps above, and close it
      once the site is live.

## 7. After launch

- [ ] Open `https://www.lansurfer.de/`, `/de/`, `/imprint/`, `/privacy/`, `/de/impressum/`,
      `/de/datenschutz/` and an unknown URL (styled 404) in dark and light mode, desktop and phone.
- [ ] Confirm `http://` and `https://lansurfer.de` redirect to `https://www.lansurfer.de/`.
