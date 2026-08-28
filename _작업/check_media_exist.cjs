const fs = require('fs');
const path = require('path');

const s = fs.readFileSync('public/learning/index.html', 'utf8');
const st = s.indexOf('const chapterData = ');
const b = s.indexOf('{', st);
let d = 0, k;
for (k = b; k < s.length; k++) {
  if (s[k] === '{') d++;
  else if (s[k] === '}') { d--; if (d === 0) break; }
}
const D = JSON.parse(s.slice(b, k + 1));

let missingVideos = [];
let missingPosters = [];
let totalWorks = 0;

for (const cn of Object.keys(D)) {
  const ch = D[cn];
  for (let i = 0; i < ch.works.length; i++) {
    totalWorks++;
    const w = ch.works[i];
    const vidPath = path.join('public/learning', w.video || w.src || '');
    const imgPath = path.join('public/learning', w.img || '');
    
    if (!fs.existsSync(vidPath)) {
      missingVideos.push({ ch: cn, n: w.n, title: w.title, path: vidPath });
    }
    if (!fs.existsSync(imgPath)) {
      missingPosters.push({ ch: cn, n: w.n, title: w.title, path: imgPath });
    }
  }
}

console.log(`=== 171편 전체 미디어 파일 실존 전수 검사 ===`);
console.log(`총 씬 수: ${totalWorks}편`);
console.log(`누락된 영상 파일: ${missingVideos.length}개`);
if (missingVideos.length > 0) console.log(missingVideos);
console.log(`누락된 포스터 파일: ${missingPosters.length}개`);
if (missingPosters.length > 0) console.log(missingPosters);
