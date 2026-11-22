# Recover the old Pages URL (optional but recommended)

The repository used to be named **`IG0606ADD-with-CAM-coursebook-NOTE`**. GitHub redirects
the old *repository* URL (`github.com/LG-leo/...`) to the new name, **but GitHub Pages does
not redirect** — the old site was served at

    https://lg-leo.github.io/IG0606ADD-with-CAM-coursebook-NOTE/

and every URL under it now returns **404**. Search engines still have those old URLs
indexed and inbound links still point at them, so recreating the old Pages site as a
redirect is the cheapest way to recover that lost authority.

## Files in this folder (upload all five to the new repo root)

| File | Purpose |
|---|---|
| `index.html` | Old site root → redirects to the new site (`meta refresh` + `location.replace`) |
| `404.html` | Every other old URL → GitHub Pages serves this; JS maps old chapter files to the matching new chapter page |
| `robots.txt` | Allows crawling and points to the new site's sitemap |
| `.nojekyll` | Empty marker so Pages serves the files as-is (no Jekyll processing) |
| `README.md` | Shown on the old repository page so visitors see "this repo has moved" |

The `404.html` map is explicit on purpose: the old file numbers do **not** match the
chapter numbers (e.g. the old `…ch4.md` file contains **chapter 5**), so every file is
mapped by content, not by name.

## Steps

1. On GitHub, create a **new public repository** named exactly
   `IG0606ADD-with-CAM-coursebook-NOTE` (https://github.com/new).
   Note: reusing the old name drops the automatic `github.com` rename redirect — that is
   the expected trade-off; the `README.md` banner covers visitors who arrive at the repo
   page instead of the website.

2. Upload **all five files** from this folder to the repository root, using either:
   - **Web UI**: repository page → *Add file → Upload files* → drag
     `index.html`, `404.html`, `robots.txt`, `README.md`, `.nojekyll` → *Commit changes*.
     (In Finder, press `Cmd + Shift + .` to show the hidden `.nojekyll`.)
   - **GitHub Desktop**: *File → New repository*, create it in an empty local folder, copy
     the five files in, commit, then *Publish repository* with the exact name.

3. Repository **Settings → Pages**:
   - Source: *Deploy from a branch*
   - Branch: **`main`** / **`(root)`**
   - Save

4. Wait ~1 minute for the Pages build, then verify:

       curl -I  https://lg-leo.github.io/IG0606ADD-with-CAM-coursebook-NOTE/
       # expect 200

       curl -s https://lg-leo.github.io/IG0606ADD-with-CAM-coursebook-NOTE/ | grep -o 'https://lg-leo.github.io/IGCSE[^"]*'
       # expect the new site URL

       curl -I "https://lg-leo.github.io/IG0606ADD-with-CAM-coursebook-NOTE/IG0606%20CompletelyNotes2_ch4.md"
       # expect 404 + our 404.html, which then redirects to .../cn/ch05/

5. In **Bing Webmaster Tools** (and Google Search Console if used), submit the **new**
   site's sitemap and request re-indexing of the old base URL. The redirect passes visitors
   (and a "moved" signal) to the new site.

> Why this helps: the old Pages URL is what was ranked / linked before the rename. A
> JavaScript/meta-refresh redirect is not a true 301, but combined with a canonical link
> to the new site it recovers most of the human traffic and gives crawlers an explicit
> "this content moved here" signal.
