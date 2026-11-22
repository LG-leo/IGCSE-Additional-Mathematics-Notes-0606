# Recover the old Pages URL (optional but recommended)

The repository used to be named **`IG0606ADD-with-CAM-coursebook-NOTE`**. GitHub redirects
the old *repository* URL (`github.com/LG-leo/...`) to the new name, **but GitHub Pages does
not redirect** — the old site was served at

    https://lg-leo.github.io/IG0606ADD-with-CAM-coursebook-NOTE/

and every URL under it now returns **404**. Search engines still have those old URLs
indexed and inbound links still point at them, so recreating the old Pages site as a
redirect is the cheapest way to recover that lost authority.

## Steps

1. On GitHub, create a **new public repository** named exactly
   `IG0606ADD-with-CAM-coursebook-NOTE` (the old rename redirect will be dropped once the
   name is reused — that is expected).
2. Add `index.html` and `404.html` from this folder to the repository root (plus a
   `.nojekyll` file, empty, so Pages serves the files as-is).
3. Repository **Settings → Pages**:
   - Source: *Deploy from a branch*
   - Branch: `main` / `(root)`
4. Wait for the Pages build, then verify:

       curl -I https://lg-leo.github.io/IG0606ADD-with-CAM-coursebook-NOTE/
       # 200, and the page redirects to the new site

5. In **Bing Webmaster Tools** (and Google Search Console if used), request re-indexing
   of the old base URL. The redirect will pass visitors (and a “moved” signal) to the new
   site; for the strongest signal, also submit the **new** site's `sitemap.xml`.

> Why this helps: the old Pages URL is what was ranked / linked before the rename. A
> JavaScript/meta-refresh redirect is not a true 301, but combined with a canonical link
> to the new site it recovers most of the human traffic and gives crawlers an explicit
> “this content moved here” signal.
