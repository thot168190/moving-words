const fs = require('fs');

function getChapter4(filePath) {
  const s = fs.readFileSync(filePath, 'utf8');
  const st = s.indexOf('const chapterData = ');
  const b = s.indexOf('{', st);
  let d = 0, k;
  for (k = b; k < s.length; k++) {
    if (s[k] === '{') d++;
    else if (s[k] === '}') { d--; if (d === 0) break; }
  }
  const D = JSON.parse(s.slice(b, k + 1));
  return D["4"] || {};
}

const oldCh4 = getChapter4('public/learning/index.html.bak_0827_1500');
const curCh4 = getChapter4('public/learning/index.html');

console.log("=== 챕터 4 과거(bak_0827_1500) vs 현재(0828) 좌표 대조 분석 ===");

for (let i = 0; i < curCh4.works.length; i++) {
  const w = curCh4.works[i];
  const oldW = oldCh4.works && oldCh4.works[i];
  
  const curL1 = curCh4.levelOneWords[i] || [];
  const curL2 = curCh4.levelTwoWords[i] || [];
  const curS1 = curCh4.levelOneSpots[i] || [];
  const curS2 = curCh4.sceneSpots[i] || [];
  
  const oldL1 = oldCh4.levelOneWords ? (oldCh4.levelOneWords[i] || []) : [];
  const oldL2 = oldCh4.levelTwoWords ? (oldCh4.levelTwoWords[i] || []) : [];
  const oldS1 = oldCh4.levelOneSpots ? (oldCh4.levelOneSpots[i] || []) : [];
  const oldS2 = oldCh4.sceneSpots ? (oldCh4.sceneSpots[i] || []) : [];
  
  console.log(`\n[4-${w.n}] ${w.title}`);
  console.log(`  현재 L1 단어: ${JSON.stringify(curL1)}`);
  console.log(`  현재 L1 좌표: ${JSON.stringify(curS1)}`);
  console.log(`  현재 L2 단어: ${JSON.stringify(curL2)}`);
  console.log(`  현재 L2 좌표: ${JSON.stringify(curS2)}`);
  console.log(`  과거 L1 단어: ${JSON.stringify(oldL1)}`);
  console.log(`  과거 L1 좌표: ${JSON.stringify(oldS1)}`);
  console.log(`  과거 L2 단어: ${JSON.stringify(oldL2)}`);
  console.log(`  과거 L2 좌표: ${JSON.stringify(oldS2)}`);
}
