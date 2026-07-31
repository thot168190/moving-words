// verify_ch1.mjs — 챕터1 works 배열 검증기 (코다리 실행용)
// 사용법:  node verify_ch1.mjs <html파일경로>
// 파이썬 안 씀. node만 쓴다. 파일을 고치지 않고 읽기만 한다.
import fs from 'fs';

const path = process.argv[2];
if (!path) { console.log('사용법: node verify_ch1.mjs <html파일경로>'); process.exit(2); }
const src = fs.readFileSync(path, 'utf8');

const i = src.indexOf('const works=[');
if (i < 0) { console.log('❌ works 배열 없음 — 이 파일에는 챕터1 데이터가 없다'); process.exit(1); }
let d = 0, j = src.indexOf('[', i), k;
for (k = j; k < src.length; k++) {
  if (src[k] === '[') d++;
  else if (src[k] === ']') { d--; if (d === 0) break; }
}
const arr = src.slice(j, k + 1);

const EXPECT = {
  '01': ['tower','island','shine','warn','cliff','shore','guide','flash'],
  '02': ['sail','deck','rope','flag','journey','row','port','navy'],
  '03': ['dolphin','follow','leap','calm','float','reflect','silver','distance'],
  '04': ['whale','wave','rise','surface','ocean','dive','spray','bubble'],
  '05': ['shell','seal','tide','current','sink','cage','shadow','stream'],
};

// 괄호 짝맞춤으로 자른다 — 정규식으로 `]]`를 쓰면 마지막 단어를 먹는다
function matchBracket(str, from, open, close) {
  let d = 0;
  for (let p = from; p < str.length; p++) {
    if (str[p] === open) d++;
    else if (str[p] === close) { d--; if (d === 0) return p; }
  }
  return -1;
}
const scenes = [];
for (let p = 0; p < arr.length; p++) {
  if (arr[p] !== '{') continue;
  const e = matchBracket(arr, p, '{', '}');
  if (e < 0) break;
  const obj = arr.slice(p, e + 1);
  p = e;
  const wi = obj.indexOf('words:[');
  const ws = wi < 0 ? '' : obj.slice(wi + 6, matchBracket(obj, wi + 6, '[', ']') + 1);
  scenes.push({
    n:     (/n:'(\d+)'/.exec(obj)     || [, '?'])[1],
    title: (/title:'([^']*)'/.exec(obj) || [, '?'])[1],
    sub:   (/sub:'([^']*)'/.exec(obj)   || [, '?'])[1],
    video: (/video:'([^']*)'/.exec(obj) || [, ''])[1],
    img:   (/img:'([^']*)'/.exec(obj)   || [, ''])[1],
    pairs: [...ws.matchAll(/\['([a-zA-Z]+)','([^']*)'\]/g)].map(m => [m[1], m[2]]),
  });
}
let total = 0, bad = 0;

console.log(`파일: ${path}`);
console.log(`장면 수: ${scenes.length}  (5여야 통과)\n`);

for (const s of scenes) {
  total += s.pairs.length;
  const en = s.pairs.map(p => p[0]);
  console.log(`── ${s.n}  ${s.title}  |  ${s.sub}`);
  console.log(`   단어 ${s.pairs.length}개 : ${s.pairs.map(p => `${p[0]}(${p[1]})`).join('  ')}`);
  const exp = EXPECT[s.n];
  if (!exp) { console.log('   ⚠️ 예상 목록에 없는 장면 번호'); bad++; }
  else {
    const miss  = exp.filter(w => !en.includes(w));
    const extra = en.filter(w => !exp.includes(w));
    if (miss.length || extra.length) {
      bad++;
      if (miss.length)  console.log(`   ❌ 빠진 단어 : ${miss.join(' ')}`);
      if (extra.length) console.log(`   ❌ 낯선 단어 : ${extra.join(' ')}`);
    } else console.log(`   ✅ 단어 ${s.pairs.length}개 일치`);
    if (s.pairs.some(p => !/[가-힣]/.test(p[1]))) {
      bad++; console.log(`   ❌ 한글 뜻이 아닌 항목: ${s.pairs.filter(p => !/[가-힣]/.test(p[1])).map(p => p[0]).join(' ')}`);
    }
  }
  console.log(`   영상 ${s.video || '❌없음'}`);
  console.log(`   포스터 ${s.img || '❌없음'}\n`);
}

const uniq = new Set();
for (const s of scenes) for (const p of s.pairs) uniq.add(p[0]);
console.log(`총 단어 ${total}개 (40이어야) / 고유 ${uniq.size}개`);
console.log(`current:true ${(arr.match(/current:true/g) || []).length}개 (1이어야)`);
console.log(`\n판정: ${scenes.length === 5 && total === 40 && bad === 0 ? '✅ PASS' : '❌ FAIL — 위 ❌ 줄을 보고하라'}`);
process.exit(scenes.length === 5 && total === 40 && bad === 0 ? 0 : 1);
