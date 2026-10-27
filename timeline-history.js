/* Band of major historical events, shared by the course timelines
   (History of Economic Thought and Theories of International Trade, English and Chinese).
   Each entry: [from, to (null for a single year; 2025 for ongoing), kind, English label, English note, Chinese label, Chinese note] */
window.HISTORY = [
  [1347, 1351, 'disaster', 'Black Death', 'Plague kills perhaps a third to a half of Europe’s population. Labor becomes scarce, wages rise, and serfdom weakens in western Europe.', '黑死病', '鼠疫夺去欧洲约三分之一至一半的人口。劳动力变得稀缺，工资上升，西欧的农奴制随之削弱。'],
  [1492, null, 'other', 'Columbus', 'Columbus reaches the Americas, opening the Atlantic economy, the conquest of the Americas, and the exchange of crops, animals, and diseases between hemispheres.', '哥伦布', '哥伦布抵达美洲，开启了大西洋经济、对美洲的征服，以及东西半球之间作物、牲畜和疾病的交换。'],
  [1618, 1648, 'war', 'Thirty Years’ War', 'A devastating war in central Europe. The Peace of Westphalia that ended it is often taken as the start of the modern system of sovereign states.', '三十年战争', '一场席卷中欧的毁灭性战争。结束这场战争的《威斯特伐利亚和约》常被视为现代主权国家体系的起点。'],
  [1688, null, 'revolution', 'Glorious Revolution', 'Parliament deposes James II and limits the English crown, laying foundations for public credit and the Bank of England (1694).', '光荣革命', '议会废黜詹姆斯二世并限制英国王权，为公共信用和英格兰银行（1694年）奠定了基础。'],
  [1756, 1763, 'war', 'Seven Years’ War', 'A global war between Britain and France fought in Europe, North America, and India. Britain emerges as the leading colonial and commercial power.', '七年战争', '英法之间在欧洲、北美和印度展开的全球性战争。英国由此成为首要的殖民和商业强国。'],
  [1775, 1783, 'revolution', 'American Revolution', 'The thirteen colonies win independence from Britain, partly in revolt against British trade restrictions.', '美国革命', '北美十三个殖民地脱离英国而独立，起因之一是反抗英国的贸易限制。'],
  [1789, 1799, 'revolution', 'French Revolution', 'The French Revolution abolishes feudal privileges and spreads ideas of popular sovereignty and equality across Europe.', '法国大革命', '法国大革命废除了封建特权，把人民主权和平等的观念传播到整个欧洲。'],
  [1803, 1815, 'war', 'Napoleonic Wars', 'Napoleon’s wars and the Continental Blockade cut European trade. Peace in 1815 brings Britain’s Corn Law.', '拿破仑战争', '拿破仑战争和大陆封锁切断了欧洲贸易。1815年和平到来后，英国通过了《谷物法》。'],
  [1839, 1842, 'war', 'Opium War', 'Britain defeats Qing China and forces it to open ports to trade and cede Hong Kong, beginning the era of “unequal treaties.”', '鸦片战争', '英国打败清朝，迫使中国开放通商口岸并割让香港，“不平等条约”时代由此开始。'],
  [1845, 1849, 'disaster', 'Irish Famine', 'Potato blight causes the Great Famine in Ireland: about a million die and a million or more emigrate. The crisis hastens repeal of the Corn Laws in 1846.', '爱尔兰大饥荒', '马铃薯枯萎病在爱尔兰引发大饥荒：约一百万人死亡，一百多万人移居海外。这场危机加速了1846年《谷物法》的废除。'],
  [1861, 1865, 'war', 'U.S. Civil War', 'The American Civil War ends slavery in the United States. The victorious North keeps high protective tariffs for decades.', '美国内战', '美国内战终结了美国的奴隶制。获胜的北方在此后几十年里维持了高额保护性关税。'],
  [1884, 1914, 'other', 'Scramble for Africa', 'After the Berlin Conference (1884–85), European powers divide almost all of Africa among themselves.', '瓜分非洲', '柏林会议（1884—1885年）之后，欧洲列强几乎瓜分了整个非洲。'],
  [1914, 1918, 'war', 'World War I', 'The First World War destroys the nineteenth-century world economy and the gold standard; about 20 million people die.', '第一次世界大战', '第一次世界大战摧毁了十九世纪的世界经济和金本位制，约两千万人死亡。'],
  [1917, null, 'revolution', 'Russian Revolution', 'The Bolsheviks take power in Russia, creating the first socialist state and, from 1928, a centrally planned economy.', '俄国革命', '布尔什维克在俄国夺取政权，建立第一个社会主义国家，并从1928年起实行中央计划经济。'],
  [1939, 1945, 'war', 'World War II', 'The Second World War, the deadliest conflict in history with some 70 to 85 million deaths, including the Holocaust. It ends with the United States as the dominant economic power.', '第二次世界大战', '第二次世界大战是历史上死亡人数最多的冲突，约七千万至八千五百万人死亡，其中包括纳粹大屠杀。战后美国成为占主导地位的经济强国。'],
  [1947, 1975, 'other', 'Decolonization', 'From India’s independence (1947) through the “Year of Africa” (1960) to the end of Portugal’s African empire (1975), most colonies become independent states.', '非殖民化', '从印度独立（1947年）、“非洲年”（1960年）到葡萄牙非洲帝国的终结（1975年），大多数殖民地成为独立国家。'],
  [1949, null, 'revolution', 'PRC founded', 'The People’s Republic of China is founded after the Communist victory in the civil war.', '新中国成立', '共产党在内战中获胜后，中华人民共和国成立。'],
  [1973, null, 'other', 'Oil crisis', 'The OPEC oil embargo quadruples oil prices, ending the postwar boom and bringing stagflation.', '石油危机', '欧佩克石油禁运使油价翻了两番，战后繁荣结束，滞胀随之而来。'],
  [1978, null, 'other', 'China’s reform', 'China begins “reform and opening up” under Deng Xiaoping.', '改革开放', '中国在邓小平领导下开始实行改革开放。'],
  [1989, 1991, 'revolution', 'End of Cold War', 'The Berlin Wall falls (1989) and the Soviet Union dissolves (1991). Former socialist economies join the world market.', '冷战结束', '柏林墙倒塌（1989年），苏联解体（1991年）。原社会主义经济体加入世界市场。'],
  [2020, 2023, 'disaster', 'COVID-19', 'The COVID-19 pandemic kills millions, disrupts global supply chains, and causes the sharpest fall in world output since the Second World War.', '新冠疫情', '新冠疫情造成数百万人死亡，扰乱全球供应链，并导致二战以来世界产出最急剧的下降。'],
  [2022, 2025, 'war', 'Russia–Ukraine war', 'Russia’s full-scale invasion of Ukraine (following the annexation of Crimea in 2014) brings sweeping sanctions and a shock to world energy and food prices.', '俄乌战争', '俄罗斯全面入侵乌克兰（此前已于2014年吞并克里米亚），引发大规模制裁，并冲击世界能源和粮食价格。'],
];
window.HISTORY_COLORS = {war:'#9b2c2c', revolution:'#5b4a8b', disaster:'#4a5560', other:'#2f6f6f'};

// Draw the band. o = {svg, el, x, top, height, left, right, lang, tip}
window.drawHistory = function (o) {
  const zh = o.lang === 'zh', g = o.el('g', {class:'hist'}, o.svg), rows = 3, rh = (o.height - 10) / rows;
  const label = o.el('text', {x:o.left - 10, y:o.top + o.height/2 + 4, 'text-anchor':'end', class:'lane-label'}, o.svg);
  label.textContent = zh ? '历史大事' : 'Historical events';
  if (o.evLabelY) { const t = o.el('text', {x:o.left - 10, y:o.evLabelY, 'text-anchor':'end', class:'lane-label'}, o.svg); t.textContent = zh ? '经济思想与事件' : 'Economic milestones'; }
  o.el('rect', {x:o.left, y:o.top + 2, width:o.right - o.left, height:o.height - 4, fill:'#fbf7f4'}, g);
  const ends = Array(rows).fill(-1e9), cw = zh ? 11 : 5.6;
  window.HISTORY.forEach(([a, b, kind, en, enNote, zt, zNote]) => {
    const name = zh ? zt : en, note = zh ? zNote : enNote, c = window.HISTORY_COLORS[kind];
    const xa = o.x(a), xb = b ? o.x(b) : xa, lw = name.length * cw + 4;
    const anchorEnd = xa + 8 + lw > o.right;
    const span = anchorEnd ? [xa - 6 - lw, Math.max(xb, xa) + 4] : [xa - 6, Math.max(xb, xa) + 6 + lw];
    let r = ends.findIndex(e => e < span[0]); if (r < 0) r = ends.indexOf(Math.min(...ends));
    ends[r] = span[1] + 12;
    const cy = o.top + 6 + r * rh + rh/2;
    const yrs = b ? `${a}–${b === 2025 ? (zh ? '至今' : 'present') : b}` : `${a}`;
    const hg = o.el('g', {class:'hev', tabindex:0, 'data-tip':`${name}（${yrs}）：${note}`.replace(/（(.*?)）：/, zh ? '（$1）：' : ' ($1): ')}, g);
    if (b) o.el('rect', {x:xa, y:cy - 4, width:Math.max(4, xb - xa), height:8, rx:2, fill:c}, hg);
    else o.el('path', {d:`M${xa},${cy - 5} L${xa + 5},${cy} L${xa},${cy + 5} L${xa - 5},${cy} Z`, fill:c}, hg);
    const t = o.el('text', anchorEnd ? {x:xa - 7, y:cy + 4, 'text-anchor':'end'} : {x:Math.max(xb, xa) + 6, y:cy + 4}, hg);
    t.textContent = name; t.setAttribute('style', `fill:${c};font-size:10.5px;font-weight:600`);
    const tt = o.el('title', {}, hg); tt.textContent = hg.dataset.tip;
    const show = e => { o.tip.textContent = hg.dataset.tip; o.tip.hidden = false; const rc = hg.getBoundingClientRect(); const px = e && e.clientX ? e.clientX : rc.left + rc.width/2; o.tip.style.left = Math.min(window.innerWidth - 270, Math.max(8, px - 60)) + 'px'; o.tip.style.top = (rc.bottom + 6) + 'px'; };
    hg.addEventListener('mouseenter', show); hg.addEventListener('mousemove', show); hg.addEventListener('focus', show);
    hg.addEventListener('mouseleave', () => o.tip.hidden = true); hg.addEventListener('blur', () => o.tip.hidden = true);
  });
};
