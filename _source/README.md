# Site source

GitHub Pages does not publish folders that start with `_`, so this folder is not on the live site.

- `build_pages.py` writes `index.html`, `research.html`, `teaching.html`, `cv.html`. Page text lives in this script.
- `build_food.py` writes `food.html` (and runs `build_pages.py` first). Article data: `hits.json` (URLs, dates, Chinese titles) and `en.py` (role, English title, summary).
- `crawl.py` re-scans rmswzq.com for articles crediting "Ripple".
- `style.css` (in the site root) is edited directly.

Rebuild everything:

    python3 _source/build_food.py
