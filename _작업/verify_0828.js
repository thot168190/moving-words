const fs = require('fs');
const s = fs.readFileSync('public/learning/index.html', 'utf8');
const st = s.indexOf('const chapterData = ');
const b = s.indexOf('{', st);
let d = 0, k;
for (k = b; k < s.length; k++) {
  if (s[k] === '{') d++;
  else if (s[k] === '}') { d--; if (d === 0) break; }
}
const D = JSON.parse(s.slice(b, k + 1));

let slots = 0, nulls = 0, mism = 0;
for (const cn of Object.keys(D).sort((a, z) => a - z)) {
  const ch = D[cn];
  const n = ch.works.length;
  for (const key of ['levelOneWords','levelTwoWords','levelOneSpots','sceneSpots']) {
    if (ch[key].length !== n) console.log(`❌ ch${cn} ${key} 길이 ${ch[key].length} != works ${n}`);
  }
  let t = 0;
  for (let i = 0; i < n; i++) {
    const w = ch.works[i];
    const a = ch.levelOneWords[i].length, c = ch.levelTwoWords[i].length;
    t += a + c; slots += a + c;
    if (a !== ch.levelOneSpots[i].length) { console.log(`❌ ${cn}-${w.n} L1 단어${a} 좌표${ch.levelOneSpots[i].length}`); mism++; }
    if (c !== ch.sceneSpots[i].length)    { console.log(`❌ ${cn}-${w.n} L2 단어${c} 좌표${ch.sceneSpots[i].length}`); mism++; }
    for (const sp of [...ch.levelOneSpots[i], ...ch.sceneSpots[i]])
      if (sp === null || !Array.isArray(sp) || sp.length !== 2) { console.log(`❌ ${cn}-${w.n} 좌표이상 ${JSON.stringify(sp)}`); nulls++; }
    const wl = (w.words || []).length;
    if (wl !== a + c) console.log(`❌ ${cn}-${w.n} words${wl} != L1+L2 ${a + c}`);
  }
  console.log(`ch${cn}  ${n}편  ${t}단어`);
}
console.log(`총 슬롯 ${slots} / 좌표이상 ${nulls} / 단어·좌표 불일치 ${mism}`);
