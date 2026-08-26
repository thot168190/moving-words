const fs = require('fs');
const path = 'public/learning/index.html';
let content = fs.readFileSync(path, 'utf8');

// 1. Move shelf.innerHTML into setupWorks
// First, find and remove the global shelf.innerHTML
content = content.replace(
  /const shelf=document\.getElementById\('shelf'\);\s*shelf\.innerHTML=works\.map\(\(w,i\)=>`<button class="work.*?\)\.join\(''\);/,
  "const shelf=document.getElementById('shelf');"
);

// Second, prepend it inside setupWorks()
content = content.replace(
  /function setupWorks\(\) \{ /,
  "function setupWorks() { shelf.innerHTML=works.map((w,i)=>`<button class=\"work ${w.current?'current':''} ${w.locked?'locked':''}\" data-index=\"${i}\"><div class=\"poster\"><span class=\"state\">${w.current?'학습 중':w.locked?'잠김':'학습하기'}</span><video muted loop playsinline preload=\"metadata\" src=\"${w.video}\"></video><img src=\"${w.img}\" alt=\"${w.title} 학습 영상 대표 화면\"></div><div class=\"meta\"><small>LESSON ${w.n} · 8 WORDS</small><h3>${w.title}</h3><p>${w.sub}</p></div></button>`).join(''); "
);

// 3. The user wants up to the WHALE to be open, which is 4 scenes, or 3 scenes?
// In Chapter 1, they are:
// 1: Lighthouse
// 2: Sailboat
// 3: Dolphin (newly inserted, was it 3?)
// 4: Whale
// Wait, the user said "챕터 1에 3개까지 고래까지 인데그거 어디갔어?" (Chapter 1 up to 3 scenes, up to the whale, where did that go?).
// In my latest insert, Dolphin is 03 and Whale is 04!
// Oh no, the original order was:
// 01: Lighthouse
// 02: Sailboat
// 03: Whale
// 04: Dolphin
// Let's check my works array!
// In my `newWorks`, I put Dolphin as 03 and Whale as 04!
// Let me swap 03 and 04 back! And ensure the words/spots are swapped too!

fs.writeFileSync(path, content, 'utf8');
console.log('Fixed shelf.innerHTML');
