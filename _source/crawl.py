import re, html, json, time, os, urllib.request
from concurrent.futures import ThreadPoolExecutor
D=os.path.dirname(os.path.abspath(__file__))
UA={'User-Agent':'Mozilla/5.0'}
def get(u):
    for k in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30).read().decode('utf-8','ignore')
        except Exception as e: time.sleep(2)
    return ''
cats=['csjz','hzjj','shms','snyt','stny','swyhj','zhjy']
ids={}
for c in cats:
    p=1; seen_pages=set()
    while True:
        t=get(f'http://rmswzq.com/article/{c}/?page={p}')
        got=tuple(re.findall(r'href="(\d+)\.html"',t))
        new=[i for i in got if i not in ids]
        if not got or got in seen_pages or not new: break
        seen_pages.add(got)
        for i in got: ids.setdefault(i,c)
        p+=1; time.sleep(0.3)
    print(c,'pages',p-1,'total ids',len(ids),flush=True)
json.dump(ids,open(f'{D}/ids.json','w'))
def check(item):
    i,c=item
    t=get(f'http://rmswzq.com/article/{c}/{i}.html'); time.sleep(0.3)
    body=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<(script|style).*?</\1>','',t))))
    if re.search('(?i)ripple',body):
        title=re.search(r'<title>([^<]*)',t).group(1).rsplit('-',2)[0]
        date=(re.search(r'发布时间：([\d-]+)',body) or [None,''])[1]
        src=(re.search(r'来源:\s*(\S+)',body) or [None,''])[1]
        role=[body[m.start()-12:m.end()+3] for m in re.finditer('(?i)ripple',body)]
        open(f'{D}/art_{i}.txt','w').write(body)
        return dict(id=i,cat=c,url=f'http://rmswzq.com/article/{c}/{i}.html',title=title,date=date,source=src,credit=role)
    if not t: return dict(id=i,error=True)
res=[]
with ThreadPoolExecutor(3) as ex:
    for n,r in enumerate(ex.map(check,ids.items())):
        if r: res.append(r)
        if n%100==0: print('checked',n,'hits',sum(1 for x in res if 'title' in x),flush=True)
json.dump(res,open(f'{D}/hits.json','w'),ensure_ascii=False,indent=1)
print('DONE',len(ids),'checked;',sum(1 for x in res if 'title' in x),'hits;',sum(1 for x in res if 'error' in x),'errors')
