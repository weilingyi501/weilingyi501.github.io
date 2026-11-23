/* Small interactive models for Introduction to Economics, Part I. */
(function () {
const zh = document.documentElement.lang.startsWith('zh'), L = (e, c) => zh ? c : e, f = (x, d = 0) => x.toFixed(d);
const line = (fn, a, b, n = 80) => Array.from({length: n + 1}, (_, i) => { const x = a + (b - a) * i / n; return [x, fn(x)]; });
const S = {
 surplus: {t: L('How many people can leave food production?', '有多少人可以离开粮食生产？'), n: L('One hundred people each need one unit of food a year. Those who do not grow food can become specialists, soldiers, or rulers.', '一百个人每人每年需要一单位粮食。不种粮食的人可以成为工匠、士兵或统治者。'),
  s: [['p', L('Food grown per farmer', '每个农民的产量'), 1, 3, .05, 1.2]], x: [1, 3], y: [0, 70], xl: L('food grown per farmer', '每个农民的产量'), yl: '%',
  d: v => ({lines: [[line(x => 100 - 100 / x, 1, 3), '#023e8a', L('share free for other work', '可从事其他工作的比例')]], dot: [v.p, 100 - 100 / v.p],
   o: L(`Each farmer feeds ${f(v.p, 2)} people, so <b>${f(100 / v.p)}</b> people farm and <b>${f(100 - 100 / v.p)}</b> are free for other work. With output of 1.00 no one is.`, `每个农民养活${f(v.p, 2)}人，因此<b>${f(100 / v.p)}</b>人务农，<b>${f(100 - 100 / v.p)}</b>人可以从事其他工作。产量为1.00时，没有人能脱离农业。`)})},
 lease: {t: L('Rent and the market', '地租与市场'), n: L('A tenant family grows 100 bushels on a plot. A money rent must be paid by selling grain at the market price.', '一个佃农家庭在一块地上收获100蒲式耳粮食。货币地租必须靠按市价出售粮食来支付。'),
  s: [['r', L('Money rent (shillings)', '货币地租（先令）'), 0, 60, 1, 30], ['p', L('Price per bushel (shillings)', '每蒲式耳价格（先令）'), .5, 2, .05, 1]], x: [.5, 2], y: [0, 120], xl: L('price per bushel', '每蒲式耳价格'), yl: '',
  d: v => {const k = v.r / v.p; return {lines: [[line(x => Math.min(120, v.r / x), .5, 2), '#023e8a', L('bushels sold to pay the rent', '为缴租出售的蒲式耳数')], [[[.5, 100], [2, 100]], '#c47a2c', L('harvest', '收成')]], dot: [v.p, Math.min(120, k)],
   o: k > 100 ? L(`The rent takes ${f(k)} bushels, more than the harvest. The family must raise output or lose the lease.`, `地租相当于${f(k)}蒲式耳，超过全部收成。这家人必须提高产量，否则将失去租约。`) : L(`The family must sell <b>${f(k)}</b> of 100 bushels, and a fall in price raises the share. A customary labor service would not change with the price.`, `这家人必须出售100蒲式耳中的<b>${f(k)}</b>蒲式耳，价格下跌会使比例上升。传统的劳役不会随价格变化。`)}}},
 malthus: {t: L('Malthus’s two series', '马尔萨斯的两个级数'), n: L('Population and food both start at 1 and are measured in generations of 25 years. Food grows by a fixed amount, population by a fixed ratio.', '人口和食物都从1开始，以25年为一代。食物每代增加固定数量，人口每代按固定比例增长。'),
  s: [['g', L('Population multiplies each generation by', '人口每代增长倍数'), 1, 2, .05, 2], ['a', L('Food added each generation', '每代增加的食物'), .2, 3, .1, 1]], x: [0, 6], y: [0, 20], xl: L('generations', '世代'), yl: '',
  d: v => {let c = null; for (let x = .05; x <= 6; x += .05) if (Math.pow(v.g, x) > 1 + v.a * x + 1e-6) { c = x; break; } return {lines: [[line(x => Math.min(20, Math.pow(v.g, x)), 0, 6), '#b03a2e', L('population', '人口')], [line(x => Math.min(20, 1 + v.a * x), 0, 6), '#2e7d32', L('food', '食物')]],
   o: c === null ? L('Food keeps ahead of population for all six generations shown.', '在所示的六代之内，食物始终领先于人口。') : c < .1 ? L('Population outruns food from the start.', '人口从一开始就超过食物。') : L(`Population overtakes food after about <b>${f(c, 1)}</b> generations (${f(c * 25)} years). Slower births or faster farm progress put the date off.`, `大约<b>${f(c, 1)}</b>代（${f(c * 25)}年）之后，人口超过食物。出生率下降或农业进步加快会推迟这一时间。`)}}},
 workday: {t: L('Dividing the working day', '工作日的划分'), n: L('In Marx’s theory the working day has two parts: the time needed to produce the value of wages, and the time left over.', '在马克思的理论中，工作日分为两部分：生产工资价值所需的时间，以及其余的时间。'),
  s: [['d', L('Length of the working day (hours)', '工作日长度（小时）'), 6, 14, .5, 8], ['n', L('Hours needed to produce the value of wages', '生产工资价值所需小时数'), 2, 8, .5, 6]], bar: 1,
  d: v => {const n = Math.min(v.n, v.d), s = v.d - n; return {seg: [[n, '#023e8a', L('necessary', '必要')], [s, '#c47a2c', L('surplus', '剩余')]], tot: 14,
   o: L(`Necessary labor <b>${f(n, 1)}</b> hours, surplus labor <b>${f(s, 1)}</b> hours. The rate of surplus value is <b>${f(100 * s / n)}%</b>. It rises with a longer day, or when the goods workers buy take less labor to make.`, `必要劳动<b>${f(n, 1)}</b>小时，剩余劳动<b>${f(s, 1)}</b>小时。剩余价值率为<b>${f(100 * s / n)}%</b>。工作日延长，或工人购买的商品所需劳动减少，都会使它上升。`)}}},
 utility: {t: L('Spending the last dollar', '最后一美元怎么花'), n: L('You have $20 for two goods at $1 a unit. Extra utility falls with each unit: 24 − a for the a-th unit of A, and 20 − b for the b-th unit of B.', '你有20美元，购买两种单价1美元的商品。额外效用逐单位递减：A的第a单位为24 − a，B的第b单位为20 − b。'),
  s: [['a', L('Dollars spent on A', '花在A上的美元'), 0, 20, 1, 5]], x: [0, 20], y: [0, 26], xl: L('dollars spent on A', '花在A上的美元'), yl: '',
  d: v => {const ma = 24 - v.a, mb = 20 - (20 - v.a); return {lines: [[line(x => 24 - x, 0, 20), '#023e8a', L('extra utility of A', 'A的额外效用')], [line(x => x, 0, 20), '#c47a2c', L('extra utility of B', 'B的额外效用')]], dot: [v.a, ma],
   o: Math.abs(ma - mb) < .5 ? L(`The last dollar brings <b>${ma}</b> from each good, so no switch can help. This is the best choice.`, `花在两种商品上的最后一美元都带来<b>${ma}</b>的额外效用，任何调整都无益。这是最佳选择。`) : L(`The last dollar on A brings ${ma}, and on B ${mb}. Move money toward <b>${ma > mb ? 'A' : 'B'}</b>.`, `花在A上的最后一美元带来${ma}，花在B上的带来${mb}。应把钱移向<b>${ma > mb ? 'A' : 'B'}</b>。`)}}},
 sabotage: {t: L('Holding back output', '限制产量'), n: L('A firm sells at the price 100 − Q and has a cost of $20 a unit. It chooses the output that gives the most profit, up to its capacity.', '一家企业按价格 100 − Q 出售，每单位成本20美元。它在产能之内选择利润最大的产量。'),
  s: [['c', L('Capacity (units)', '产能（单位）'), 20, 80, 1, 70]], x: [0, 80], y: [0, 1700], xl: L('output', '产量'), yl: '',
  d: v => {const q = Math.min(40, v.c); return {lines: [[line(x => (80 - x) * x, 0, 80), '#023e8a', L('profit', '利润')], [[[v.c, 0], [v.c, 1700]], '#c47a2c', L('capacity', '产能')]], dot: [q, (80 - q) * q],
   o: v.c <= 40 ? L(`The firm uses all of its capacity of <b>${v.c}</b>.`, `企业用尽了<b>${v.c}</b>的产能。`) : L(`Profit is highest at 40 units, so <b>${f(100 * (v.c - 40) / v.c)}%</b> of capacity stands idle. More capacity does not raise output.`, `产量为40时利润最大，因此<b>${f(100 * (v.c - 40) / v.c)}%</b>的产能闲置。增加产能不会提高产量。`)}}},
 cross: {t: L('A simple Keynesian economy', '一个简单的凯恩斯经济'), n: L('Consumption is 50 + MPC × income, and full-employment output is 500. Government and foreign trade are left out.', '消费等于 50 + MPC × 收入，充分就业产出为500。不考虑政府和对外贸易。'),
  s: [['m', L('Marginal propensity to consume', '边际消费倾向'), .5, .85, .01, .75], ['i', L('Investment', '投资'), 0, 120, 1, 75]], x: [0, 800], y: [0, 800], xl: L('income', '收入'), yl: '',
  d: v => {const y = (50 + v.i) / (1 - v.m), k = 500 * (1 - v.m) - 50; return {lines: [[line(x => x, 0, 800), '#8a929b', L('spending = income', '支出 = 收入')], [line(x => Math.min(800, 50 + v.i + v.m * x), 0, 800), '#023e8a', L('planned spending', '计划支出')], [[[500, 0], [500, 800]], '#c47a2c', L('full employment', '充分就业')]], dot: y <= 800 ? [y, y] : null,
   o: (Math.abs(y - 500) < 2 ? L('Income settles at about full employment.', '收入大致稳定在充分就业水平。') : y < 500 ? L(`Income settles at <b>${f(y)}</b>, which is ${f(500 - y)} short of full employment.`, `收入稳定在<b>${f(y)}</b>，比充分就业低${f(500 - y)}。`) : L(`Spending would support an income of ${f(y)}, more than the economy can produce, so prices tend to rise.`, `支出对应的收入为${f(y)}，超出经济的生产能力，物价趋于上涨。`)) + (k < 0 ? '' : L(` Full employment would need investment of <b>${f(k)}</b>.`, `充分就业需要的投资为<b>${f(k)}</b>。`))}}},
 growth: {t: L('What one percentage point does', '一个百分点的作用'), n: L('Output starts at 100. Compare two growth rates over time. The starting values are the text’s rates for the two periods.', '产出从100开始，比较两种增长率。初始值是教材给出的两个时期的增长率。'),
  s: [['a', L('First growth rate (% a year)', '第一种增长率（每年%）'), 0, 6, .1, 3.7], ['b', L('Second growth rate (% a year)', '第二种增长率（每年%）'), 0, 6, .1, 2.5]], x: [0, 40], y: [0, 500], xl: L('years', '年'), yl: '',
  d: v => {const A = x => 100 * Math.pow(1 + v.a / 100, x), B = x => 100 * Math.pow(1 + v.b / 100, x), dbl = r => r > 0 ? f(Math.log(2) / Math.log(1 + r / 100)) : '∞'; return {lines: [[line(x => Math.min(500, A(x)), 0, 40), '#023e8a', L('first', '第一种')], [line(x => Math.min(500, B(x)), 0, 40), '#c47a2c', L('second', '第二种')]],
   o: L(`After 40 years output is <b>${f(A(40))}</b> against <b>${f(B(40))}</b>. Doubling takes ${dbl(v.a)} years against ${dbl(v.b)}.`, `40年后产出分别为<b>${f(A(40))}</b>和<b>${f(B(40))}</b>。翻一番分别需要${dbl(v.a)}年和${dbl(v.b)}年。`)}}}
};
document.querySelectorAll('[data-sim]').forEach(box => {
  const m = S[box.dataset.sim], v = {};
  box.className = 'box';
  box.innerHTML = `<h3>${m.t}</h3><p class="note">${m.n}</p><div class="grid2">` + m.s.map(s => `<div><label for="in-${s[0]}">${s[1]}: <b data-v="${s[0]}"></b></label><input id="in-${s[0]}" type="range" min="${s[2]}" max="${s[3]}" step="${s[4]}" value="${s[5]}" data-k="${s[0]}"></div>`).join('') + `</div><svg viewBox="0 0 640 ${m.bar ? 70 : 280}" width="100%" role="img" aria-label="${m.t}"></svg><div class="out"></div>`;
  const svg = box.querySelector('svg');
  function draw() {
    m.s.forEach(s => { v[s[0]] = +box.querySelector(`[data-k=${s[0]}]`).value; box.querySelector(`[data-v=${s[0]}]`).textContent = +v[s[0]].toFixed(2); });
    const r = m.d(v); let c = '';
    if (m.bar) { let x = 0; r.seg.forEach(g => { const w = 640 * g[0] / r.tot; if (w > 0) c += `<rect x="${x}" y="14" width="${w}" height="40" fill="${g[1]}"/>` + (w > 70 ? `<text x="${x + w / 2}" y="39" text-anchor="middle" style="fill:#fff;font-weight:600">${g[2]} ${f(g[0], 1)}</text>` : ''); x += w; }); }
    else {
      const W = 640, H = 280, l = 46, R = 12, T = 14, B = 36, X = x => l + (x - m.x[0]) / (m.x[1] - m.x[0]) * (W - l - R), Y = y => H - B - (y - m.y[0]) / (m.y[1] - m.y[0]) * (H - T - B);
      for (let i = 0; i <= 4; i++) { const y = m.y[0] + (m.y[1] - m.y[0]) * i / 4, x = m.x[0] + (m.x[1] - m.x[0]) * i / 4; c += `<line x1="${l}" x2="${W - R}" y1="${Y(y)}" y2="${Y(y)}" stroke="#eef0f3"/><text x="${l - 6}" y="${Y(y) + 4}" text-anchor="end">${+y.toFixed(1)}${m.yl}</text><text x="${X(x)}" y="${H - B + 16}" text-anchor="middle">${+x.toFixed(2)}</text>`; }
      c += `<text x="${(l + W - R) / 2}" y="${H - 4}" text-anchor="middle">${m.xl}</text>`;
      r.lines.forEach((g, i) => { c += `<path d="${g[0].map((p, j) => (j ? 'L' : 'M') + X(p[0]).toFixed(1) + ',' + Y(p[1]).toFixed(1)).join('')}" fill="none" stroke="${g[1]}" stroke-width="2.4"/><text x="${l + 10}" y="${T + 12 + 16 * i}" style="fill:${g[1]};font-weight:600">${g[2]}</text>`; });
      if (r.dot) c += `<circle cx="${X(r.dot[0])}" cy="${Y(r.dot[1])}" r="6" fill="#b03a2e"/>`;
    }
    svg.innerHTML = c; box.querySelector('.out').innerHTML = r.o;
  }
  box.addEventListener('input', draw); draw();
});
})();
