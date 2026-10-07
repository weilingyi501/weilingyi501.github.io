"""Builds index.html, research.html, teaching.html (shared header/footer, style.css)."""
import os
SITE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
LEAF = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 19c0-8 5-13 14-14-1 9-6 14-14 14z"/><path d="M5 19l7-7"/></svg>'
NAV = [('/', 'Home'), ('research.html', 'Research'), ('teaching.html', 'Teaching'), ('food.html', 'Food'), ('cv.html', 'CV')]

def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
</head>
<body>
'''

def bar(on):
    lis = []
    for h, l in NAV:
        cls = ' class="on"' if l == on else ''
        lis.append(f'      <li><a href="{h}"{cls}>{l}</a></li>')
    return ('<header class="bar">\n  <div class="inner">\n'
            f'    <a class="brand" href="/">Lingyi Wei</a>\n    <ul>\n'
            + '\n'.join(lis) + '\n    </ul>\n  </div>\n</header>\n')

FOOT = '<footer>Lingyi Wei · Department of Economics, University of Utah · Last updated October 2026</footer>\n</body>\n</html>\n'
MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>'
DOC = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/></svg>'
CAP = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/></svg>'

PHOTO = os.path.join(SITE, 'photo.jpg')
photo_html = ('<img class="photo" src="photo.jpg" alt="Lingyi Wei">' if os.path.exists(PHOTO)
              else '<div class="photo" aria-hidden="true">LW</div>')

JMP_TITLE = 'All Labors Are Equal, But Some Labor Is More “Equal” Than Others: Labor Terms of Trade and the Capitalist World-System'

home = head('Lingyi Wei', 'Lingyi Wei, Ph.D. candidate in Economics at the University of Utah. Economic development, international economics, political economy, and the Chinese economy. On the 2026–27 job market.') + bar('Home') + f'''
<main class="home">
  <aside class="side"><div class="inner">
    {photo_html}
    <h1>Lingyi Wei</h1>
    <p class="role">Ph.D. Candidate in Economics<br>University of Utah</p>
    <div class="badge">On the job market 2026–27</div>
    <div class="icons">
      <a href="mailto:lingyi.wei@utah.edu">{MAIL}Email</a>
      <a href="cv.html">{DOC}CV</a>
      <a href="https://scholar.google.com/citations?hl=en&user=QQPJ5xoAAAAJ">{CAP}Scholar</a>
      <span class="icon-break" aria-hidden="true"></span>
      <a href="https://www.researchgate.net/profile/Lingyi-Wei-2"><img src="https://cdn.simpleicons.org/researchgate/023e8a" alt="" width="18" height="18">ResearchGate</a>
    </div>
  </div></aside>

  <div class="main">
    <p>I am a Ph.D. candidate in Economics at the <a href="https://economics.utah.edu/">University of Utah</a>. I am on the 2026–27 academic job market.</p>
    <p>My research focuses on <strong>economic development</strong>, <strong>international economics</strong>, <strong>political economy</strong>, and the <strong>Chinese economy</strong>. My dissertation, <em>Understanding the Structure of the Capitalist World-System</em>, measures global economic hierarchy using cross-country income distributions and labor terms of trade for more than 170 countries. I find that the hierarchy has remained stable since 1950, but that lower-income countries moved up in labor terms of trade after the 2008 financial crisis.</p>
    <p>I am the 2026–27 Dissertation Fellow of the Union for Radical Political Economics (URPE).</p>

    <div class="jmp">
      <div class="label">Job Market Paper</div>
      <div class="title">{JMP_TITLE}</div>
      <p>The first systematic worldwide estimates of labor terms of trade, for more than 170 countries over 1990–2017. <a href="research.html">More on my research →</a></p>
    </div>

    <h2>Education</h2>
    <ul class="plain">
      <li>Ph.D. in Economics, University of Utah, expected 2027</li>
      <li>M.S. in Economics, University of Utah, 2023</li>
      <li>B.Sc., Hong Kong Polytechnic University, 2018</li>
    </ul>

  </div>
</main>
''' + FOOT

research = head('Research | Lingyi Wei', 'Research by Lingyi Wei: labor terms of trade, the global income hierarchy, and the Chinese political economy.') + bar('Research') + f'''
<main class="page">
  <h1>Research</h1>
  <p class="lead">Economic development · International economics · Political economy · Chinese economy</p>

  <h2>Job Market Paper</h2>
  <div class="jmp">
    <div class="title">{JMP_TITLE}</div>
    <p>I compute labor terms of trade for more than 170 countries over 1990–2017 using multi-regional input–output tables, providing the first systematic worldwide estimates. The global distribution has three or four distinct layers. Countries mostly stayed in place through the early 2000s, but after the global financial crisis the bottom and lower-middle layers moved up markedly.</p>
  </div>

  <h2>Publications</h2>
  <div class="paper">
    <div class="title"><a href="https://doi.org/10.1177/04866134261447586">Gradualism and Structural Adjustment in the Chinese Political Economy</a></div>
    <div class="meta">with Zhun Xu · <em>Review of Radical Political Economics</em>, 2026</div>
    <details><summary></summary><div class="abs">China’s reforms combined an overwhelmingly gradual transition with geographically concentrated episodes of shock-style restructuring. The severity of adjustment reflected pre-reform industrialization and class relations, and provinces exposed to more concentrated restructuring did not subsequently grow faster.</div></details>
  </div>
  <div class="paper">
    <div class="title"><a href="https://doi.org/10.1080/10971475.2024.2335577">Breaking the Curse of “the Last Generation”: Employment Structure and China’s Population Crisis</a></div>
    <div class="meta">with Han Cheng · <em>The Chinese Economy</em>, 2024</div>
    <details><summary></summary><div class="abs">Using provincial panel data from 1990 to 2021, we link China’s fertility decline to the organization of social reproduction. Formal-sector employment is positively and robustly associated with birth rates.</div></details>
  </div>
  <div class="paper">
    <div class="title"><a href="https://monthlyreview.org/articles/surplus-absorption-secular-stagnation-and-the-transition-to-socialism-contradictions-of-the-u-s-and-the-chinese-economies-since-2000/">Surplus Absorption, Secular Stagnation, and the Transition to Socialism: Contradictions of the U.S. and the Chinese Economies since 2000</a></div>
    <div class="meta">with Minqi Li · <em>Monthly Review</em>, 2024</div>
    <details><summary></summary><div class="abs">We compare surplus absorption in the United States and China since 2000. The U.S. has increasingly relied on government deficits, which may prove unsustainable, while China has relied heavily on investment.</div></details>
  </div>
  <div class="paper">
    <div class="title"><a href="https://www.taylorfrancis.com/chapters/edit/10.4324/9781003327448-17/us-sanctions-chinese-political-economy-zhun-xu-lingyi-wei">The US Sanctions and the Chinese Political Economy</a></div>
    <div class="meta">with Zhun Xu · <em>Routledge Handbook of the Political Economy of Sanctions</em>, 2023</div>
    <details><summary></summary><div class="abs">Renewed U.S. sanctions have drawn mixed reactions in China: liberals defend the U.S.-led order, nationalists rally behind Chinese firms, and leftists call for delinking from neoliberal globalization. Beijing has pushed back but has not fundamentally changed U.S.–China economic ties.</div></details>
  </div>

  <h2>Revise &amp; Resubmit</h2>
  <div class="paper">
    <div class="title">Counting the Zones of the Capitalist World-System: New Evidence on the Global Income Hierarchy, 1950–2023</div>
    <div class="meta"><em>Journal of World-Systems Research</em></div>
  </div>

  <h2>Work in Progress</h2>
  <div class="paper">
    <div class="title">Measuring the Hierarchy of Global Capitalism</div>
    <details><summary></summary><div class="abs">Using an index benchmarked to the income of four classical imperial powers, I find the world hierarchy has been strikingly stable since 1950: only twelve economies reached the top layer in six decades.</div></details>
  </div>
  <div class="paper">
    <div class="title">Can China Overcome the Semi-Peripheral Trap?</div>
  </div>

  <p class="note">I also translate and edit for the People’s Food Sovereignty Network. See <a href="food.html">Political Economy of Food</a>.</p>
</main>
''' + FOOT

teaching = head('Teaching | Lingyi Wei', 'Teaching by Lingyi Wei at the University of Utah.') + bar('Teaching') + '''
<main class="page">
  <h1>Teaching</h1>
  <p class="lead">University of Utah</p>

  <h2>Instructor of Record</h2>
  <div class="courses">
    <div class="course">
      <div class="course-row"><span class="name">International Economics</span><span class="when">Fall 2026</span></div>
    </div>
    <div class="course">
      <div class="course-row"><span class="name">Money and Banking</span><button type="button" class="fb-toggle" aria-expanded="false">Student feedback</button><span class="when">Summer 2026</span></div>
      <div class="fb-body" hidden>
        <p class="stat">Instructor recommendation: <strong>4.93 / 5</strong> (ECON average 4.48) · 15 responses</p>
        <blockquote>Professor Wei was very engaged with the course and students. She was very warm, supportive and passionate. What I like most about her class was that she always updated us with current news, let us discuss and connect class materials with real-life events.</blockquote>
        <blockquote>Promptly replies to emails and patiently answers any questions. Delivers lectures with clear logic and at a moderate pace. Teaches in a step-by-step manner.</blockquote>
        <blockquote>The syllabus was clear and the professor nicely laid out objectives at the beginnings of lectures.</blockquote>
        <blockquote>Thank you for teaching! I found this class to be one of the few online classes that I liked the structure of and I thoroughly have learned more about this topic.</blockquote>
      </div>
    </div>
    <div class="course">
      <div class="course-row"><span class="name">Principles of Macroeconomics</span><button type="button" class="fb-toggle" aria-expanded="false">Student feedback</button><span class="when">Summer 2025</span></div>
      <div class="fb-body" hidden>
        <p class="stat">Instructor recommendation: <strong>4.91 / 5</strong> (ECON average 4.48) · 11 responses</p>
        <blockquote>Made everything so ridiculously organized it was almost impossible not to succeed.</blockquote>
        <blockquote>I was able to learn a lot in the class and my professor was extremely helpful and responsive for the shortened course timeline</blockquote>
        <blockquote>The professor explains everything clearly in the instruction videos and also follows up with announcements. The professor also includes reminders and encouragement in announcements.</blockquote>
        <blockquote>I never felt judged by my professor</blockquote>
      </div>
    </div>
    <div class="course">
      <div class="course-row"><span class="name">Principles of Microeconomics</span><button type="button" class="fb-toggle" aria-expanded="false">Student feedback</button><span class="when">Summer 2024</span></div>
      <div class="fb-body" hidden>
        <p class="stat">Instructor recommendation: <strong>4.70 / 5</strong> (ECON average 4.48) · 10 responses</p>
        <blockquote>The professor explains concepts very clearly. I&#x27;m glad this was an in-person class and not an online class.</blockquote>
        <blockquote>The instructor helped answer questions and break up misunderstanding. The instructor also planned fun activities to learn from.</blockquote>
        <blockquote>She has us help teach and give presentations</blockquote>
        <blockquote>Thank you for the semester. I truly appreciate your teaching and the time you&#x27;ve dedicated to our class.</blockquote>
      </div>
    </div>
  </div>

  <h2>Mentoring &amp; Assisting</h2>
  <div class="courses">
    <div class="course">
      <div class="course-row"><span class="name">Honors Graduate Teaching Assistant</span><button type="button" class="fb-toggle" aria-expanded="false">Impact</button><span class="when">2024–2026</span></div>
      <div class="fb-body" hidden>
        <div class="stats">
          <div><b>63</b> <span>Honors students supported</span></div>
          <div><b>22</b> <span>students mentored one-on-one</span></div>
          <div><b>2 or 3 → 10</b> <span>Honors graduates per year</span></div>
        </div>
        <blockquote>Thank you for the reminders, they helped a lot with keeping on track. I almost didn’t write an honors thesis, and my meeting with you at the beginning of the semester helped me realize it wasn’t too late and it was still possible.</blockquote>
        <blockquote>Thank you for all your help this semester as well. It really helped keep me on track!</blockquote>
      </div>
    </div>
    <div class="course">
      <div class="course-row"><span class="name">Teaching Assistant, Principles of Microeconomics</span><span class="when">2022–2023</span></div>
    </div>
  </div>

  <h2>Pedagogical Training</h2>
  <ul class="list">
    <li><span>Graduate Fellow, Martha Bradley Evans Center for Teaching Excellence</span><span class="when">2023–2024</span></li>
    <li><span>Research Mentoring Certificate</span><span class="when">2024</span></li>
    <li><span>Graduate Teaching Institute</span><span class="when">2023, 2024</span></li>
    <li><span>Annual Teaching Symposium, Martha Bradley Evans Center for Teaching Excellence</span><span class="when">2022, 2026</span></li>
  </ul>
</main>
<script>
  document.querySelectorAll('.fb-toggle').forEach(b => b.addEventListener('click', () => {
    const body = b.closest('.course').querySelector('.fb-body');
    const open = b.getAttribute('aria-expanded') === 'true';
    b.setAttribute('aria-expanded', String(!open));
    body.hidden = open;
  }));
</script>
''' + FOOT

cv = head('CV | Lingyi Wei', 'Curriculum vitae of Lingyi Wei.') + bar('CV') + '''
<main class="page cv">
  <div class="cv-head">
    <h1>Curriculum Vitae</h1>
    <a href="Wei_CV.pdf" download>Download PDF</a>
  </div>
  <iframe class="cv-frame" src="Wei_CV.pdf#navpanes=0&view=FitH" title="Lingyi Wei CV"></iframe>
</main>
''' + FOOT

for name, html in [('index.html', home), ('research.html', research), ('teaching.html', teaching), ('cv.html', cv)]:
    open(os.path.join(SITE, name), 'w').write(html)
print('wrote index, research, teaching; photo:', os.path.exists(PHOTO))
