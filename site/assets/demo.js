// output/investment-case.json, written by financial_model.py: fictional allowances, not vendor quotes.
const $ = id => document.getElementById(id);
const d = await (await fetch('assets/investment-case.json')).json();
const eur = v => (v < 0 ? '−€' : '€') + Math.abs(Math.round(v)).toLocaleString('en');
const t = (v, l, c = '') => `<div class="kpi-tile ${c}"><div class="v">${v}</div><div class="l">${l}</div></div>`;
$('cp-tiles').innerHTML = t(eur(d.year_one_net_with_ramp), 'first-year net, with adoption ramp', 'big bad') + t(`month ${d.payback_month_with_ramp}`, 'first non-negative cumulative cash flow') +
  t(Math.round(d.steady_first_year_break_even_adoption * 100) + '%', 'adoption needed to break even in year one') + t(d.baseline.hours_saved_month + ' h', 'hours released per month at 60% adoption');
const cf = d.cash_flow, W = 760, H = 260, L = 56, B = 26, T = 12;
const lo = Math.min(...cf.map(x => x.cumulative)), hi = Math.max(...cf.map(x => x.cumulative));
const x = m => L + (m - 1) / (cf.length - 1) * (W - L - 10), y = v => T + (hi - v) / (hi - lo) * (H - T - B);
let s = `<line x1="${L}" x2="${W - 10}" y1="${y(0)}" y2="${y(0)}" class="zero"/><text x="${L - 6}" y="${y(0) + 4}" class="ax" text-anchor="end">€0</text>`;
[lo, hi].forEach(v => s += `<text x="${L - 6}" y="${y(v) + 4}" class="ax" text-anchor="end">${eur(v)}</text>`);
[1, 12, 24, 36].forEach(m => s += `<text x="${x(m)}" y="${H - 6}" class="ax" text-anchor="middle">m${m}</text>`);
s += `<rect x="${x(1)}" y="${T}" width="${x(12) - x(1)}" height="${H - T - B}" class="y1"/><text x="${x(6.5)}" y="${T + 14}" class="ax" text-anchor="middle">year one</text>`;
s += `<path d="${cf.map((p, i) => `${i ? 'L' : 'M'}${x(p.month).toFixed(1)},${y(p.cumulative).toFixed(1)}`).join('')}" class="line"/>`;
s += cf.map(p => `<circle cx="${x(p.month)}" cy="${y(p.cumulative)}" r="${p.month === d.payback_month_with_ramp ? 6 : 3.5}" class="${p.cumulative >= 0 ? 'pos' : 'neg'}${p.month === d.payback_month_with_ramp ? ' pb' : ''}" data-m="${p.month}"/>`).join('');
$('cp-chart').setAttribute('viewBox', `0 0 ${W} ${H}`); $('cp-chart').innerHTML = s;
$('cp-chart').addEventListener('mouseover', e => { const m = +e.target.dataset?.m; if (!m) return; const p = cf[m - 1];
  $('cp-hover').textContent = `month ${m}: adoption ${Math.round(p.adoption * 100)}%, benefit ${eur(p.benefit)}, cost ${eur(p.operating_cost)}, cumulative ${eur(p.cumulative)}`; });
const ad = [...new Set(d.sensitivity.map(r => r.adoption))], oc = [...new Set(d.sensitivity.map(r => r.monthly_operating_cost))];
$('cp-sens').innerHTML = `<tr><th>adoption \\ cost</th>${oc.map(c => `<th class="num">€${c}/mo</th>`).join('')}</tr>` + ad.map(a => `<tr><td>${a * 100}%</td>${oc.map(c => { const r = d.sensitivity.find(z => z.adoption === a && z.monthly_operating_cost === c); return `<td class="num ${r.first_year_net >= 0 ? 'cp-pos' : 'cp-neg'}">${eur(r.first_year_net)}</td>`; }).join('')}</tr>`).join('');
$('cp-rec').textContent = d.recommendation; $('cp-disc').textContent = d.disclaimer;
