"""Builds Website/food.html from hits.json (crawler output) + en.py (English titles/roles/summaries)."""
import json, re, html, os, datetime
from collections import OrderedDict
from en import D
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(HERE, '..')
hits = {h['id']: h for h in json.load(open(os.path.join(HERE, 'hits.json'))) if 'title' in h}
DATE_FIX = {'6864': '2025-08-04'}   # 2015 article reissued (and edited) in 2025
from build_pages import bar  # shared top bar (also rebuilds index/research/teaching on import)

items = []
for i, (role, en, summ) in D.items():
    h = hits[i]
    items.append(dict(id=i, role=role, en=en, summ=summ, zh=h['title'].strip(),
                      date=DATE_FIX.get(i, h['date']), url=h['url']))
items.sort(key=lambda x: x['date'], reverse=True)

def group(role):
    if role.startswith('Translat'): return 'translation'
    if role.startswith('Proofreader') or role == 'Subtitle Proofreader': return 'translation'
    if role in ('Moderator', 'Transcription'): return 'talks'
    if role == 'Editor': return 'editing'
    if role in ('Author', 'Co-author'): return 'writing'
    return 'other'

counts = {g: sum(group(x['role']) == g for x in items) for g in ('writing', 'translation', 'editing', 'talks')}
by_year = OrderedDict()
for x in items: by_year.setdefault(x['date'][:4], []).append(x)

e = html.escape
rows = []
for y, xs in by_year.items():
    rows.append(f'<h3 class="year" data-year>{y}</h3>')
    for x in xs:
        rows.append(f'''<div class="paper" data-g="{group(x['role'])}">
  <div class="title"><a href="{e(x['url'])}" target="_blank" rel="noopener">{e(x['en'])}</a></div>
  <div class="zh">{e(x['zh'])}</div>
  <div class="meta"><span class="tag">{e(x['role'])}</span> {datetime.date.fromisoformat(x['date']).strftime('%b %Y')}</div>
  <p class="summ">{e(x['summ'])}</p>
</div>''')

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Political Economy of Food | Lingyi Wei</title>
  <meta name="description" content="Translation and editorial work by Lingyi Wei for the People's Food Sovereignty Network (人民食物主权).">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@300;400;500;600&family=Noto+Serif+SC:wght@400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <style>
    .intro {{ padding: 0 0 8px; }}
    .intro h1 {{ font-size: 36px; font-weight: 600; margin: 0 0 10px; }}
    .intro p {{ color: var(--muted); }}
    .intro .story {{ margin: 0 0 22px; padding-bottom: 18px; border-bottom: 1px solid var(--rule); }}
    .intro .story p {{ color: var(--text); font-size: 18px; line-height: 1.7; }}
    .intro p {{ text-align: justify; text-justify: inter-word; hyphens: auto; -webkit-hyphens: auto; }}
    .intro .cjk {{ }}
    @media (max-width: 560px) {{ .intro p {{ text-align: left; }} }}
    .zh {{ font-family: 'Noto Serif SC', serif; font-size: 15px; color: var(--muted); margin-top: 2px; }}
    .tag {{ font-size: 13px; font-weight: 600; color: var(--bar); background: var(--blue-soft); padding: 1px 9px; border-radius: 999px; margin-right: 8px; }}
    .paper {{ margin-bottom: 34px; }}
    .paper .meta {{ font-size: 14px; margin: 8px 0 6px; }}
    .summ {{ font-size: 16px; color: var(--muted); margin: 0; line-height: 1.65; }}
    .filters {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 24px 0 0; font-size: 15px; }}
    .filters button {{ font: inherit; background: none; color: var(--muted); border: 1px solid var(--rule); border-radius: 999px; padding: 5px 14px; cursor: pointer; }}
    .filters button[aria-pressed="true"] {{ background: var(--bar); border-color: var(--bar); color: #fff; }}
    h3.year {{ font-size: 22px; font-weight: 600; margin: 48px 0 20px; padding-bottom: 6px; border-bottom: 2px solid var(--blue-soft); color: var(--text); }}
    .hidden {{ display: none; }}
  </style>
</head>
<body>
{bar('Food')}
<main class="page">
  <section class="intro">
    <h1>Political Economy of Food</h1>
    <div class="story">
      <p>Food is what led me to economics, and to political economy more broadly. As an undergraduate I studied food science: the technologies that keep food fresh, preserve its color, and extend its shelf life. I interned in a chemical testing lab and at a coffee roasting business, then worked full time in meat procurement in Hong Kong. We bought frozen and chilled meat from packing plants in the United States, South America, and Europe, and distributed it to local supermarkets and restaurants. In that world food is a commodity, and the supply chain that delivers it cuts consumers off from the people who produce it and the places it comes from. So much is hidden: we do not see how food is produced, or how it depends on soil, water, air, microorganisms, and other plants and animals.</p>
      <p>When the pandemic hit in 2020, the procurement business seemed to run as usual. Beneath the surface, meatpacking workers were suffering, and I wrote about the labor relations behind it in <span class="cjk">“<a href="https://www.thepaper.cn/newsDetail_forward_10286277" target="_blank" rel="noopener">疫情为何在美国肉类加工厂中肆虐？</a>”</span> [Why Has COVID-19 Spread So Widely in U.S. Meatpacking Plants?], published in <em>The Paper</em> <span class="cjk">(澎湃新闻)</span>, a prestigious Chinese news outlet. That was when I decided to leave the industry and look for answers in academia. I wanted to understand how the world works, how it shapes ordinary people’s lives, and what we can do given those conditions.</p>
      <p>Raj Patel’s essay “<a href="https://www.scientificamerican.com/article/agroecology-is-the-solution-to-world-hunger/" target="_blank" rel="noopener">Agroecology Is the Solution to World Hunger</a>” puts the puzzle plainly: food production has outstripped demand, yet more food has come with more hunger. As Patel writes, people are deprived of food “not because it is scarce but because they lack the power to access it.” Hunger has never been simply a technical problem; it is a problem of political economy. So is food more broadly: what we eat, how it is produced, how farming shapes and depends on the environment, and who gets to decide, which is the question at the heart of food sovereignty. That is why I remain passionate about food and the political economy around it, and why I hope to build a course on the subject someday.</p>
    </div>
    <p>Since 2018 I have volunteered as an editor and translator for the <a href="http://rmswzq.com/" target="_blank" rel="noopener">People’s Food Sovereignty Network</a> <span class="cjk">(人民食物主权)</span>. Below are the {len(items)} pieces I have worked on. Each title links to the original article, in Chinese.</p>
    <div class="filters" role="group" aria-label="Filter by role">
      <button aria-pressed="true" data-f="all">All ({len(items)})</button>
      <button aria-pressed="false" data-f="writing">Writing ({counts['writing']})</button>
      <button aria-pressed="false" data-f="translation">Translation &amp; proofreading ({counts['translation']})</button>
      <button aria-pressed="false" data-f="editing">Editing ({counts['editing']})</button>
      <button aria-pressed="false" data-f="talks">Lectures &amp; discussions ({counts['talks']})</button>
    </div>
  </section>
  <section style="padding-top:0">
{chr(10).join(rows)}
  </section>
</main>
<footer>Articles are hosted on rmswzq.com, in Chinese. English titles and summaries are my own. · <a href="index.html">Back to main page</a></footer>
<script>
  document.querySelectorAll('.filters button').forEach(b => b.addEventListener('click', () => {{
    document.querySelectorAll('.filters button').forEach(o => o.setAttribute('aria-pressed', o === b));
    const f = b.dataset.f;
    document.querySelectorAll('.paper').forEach(p => p.classList.toggle('hidden', f !== 'all' && p.dataset.g !== f));
    document.querySelectorAll('h3.year').forEach(h => {{
      let n = h.nextElementSibling, any = false;
      while (n && !n.matches('h3.year')) {{ if (!n.classList.contains('hidden')) any = true; n = n.nextElementSibling; }}
      h.classList.toggle('hidden', !any);
    }});
  }}));
</script>
</body>
</html>
'''
open(os.path.join(SITE, 'food.html'), 'w').write(page)
print('wrote', len(items), 'items', counts)
