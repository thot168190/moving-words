const fs = require('fs');
const path = 'public/learning/index.html';
let content = fs.readFileSync(path, 'utf8');

const chap2Data = `
      2: {
        works: [
          {n:'01',title:'참나무 아래 초원',sub:'생명이 시작되는 곳',video:'챕터2_완성동영상/Oak_tree_in_meadow_202608061427.mp4',img:'',current:true,words:[['tree','나무'],['leaf','나뭇잎'],['grass','풀'],['root','뿌리'],['branch','나뭇가지'],['seed','씨앗'],['soil','흙'],['bark','나무껍질']]},
          {n:'02',title:'평원의 기린과 얼룩말',sub:'더불어 사는 동물들',video:'챕터2_완성동영상/Giraffe_and_zebras_on_plain_202608061431.mp4',img:'',words:[['animal','동물'],['herd','무리'],['tail','꼬리'],['neck','목'],['spot','점'],['stripe','줄무늬'],['plain','평원'],['graze','풀을 뜯다']]},
          {n:'03',title:'진흙 속 개구리',sub:'비 온 뒤의 풍경',video:'챕터2_완성동영상/Frog_leaps_from_mud_bank_202608061507.mp4',img:'',words:[['frog','개구리'],['jump','뛰다'],['mud','진흙'],['bank','둑'],['pond','연못'],['insect','곤충'],['catch','잡다'],['hide','숨다']]}
        ],
        levelOneWords: [
          [['tree','나무'],['leaf','나뭇잎'],['grass','풀'],['root','뿌리']],
          [['animal','동물'],['herd','무리'],['tail','꼬리'],['neck','목']],
          [['frog','개구리'],['jump','뛰다'],['mud','진흙'],['bank','둑']]
        ],
        levelTwoWords: [
          [['branch','나뭇가지'],['seed','씨앗'],['soil','흙'],['bark','나무껍질']],
          [['spot','점'],['stripe','줄무늬'],['plain','평원'],['graze','풀을 뜯다']],
          [['pond','연못'],['insect','곤충'],['catch','잡다'],['hide','숨다']]
        ],
        sceneSpots: [
          [[30,30],[70,30],[30,70],[70,70]],[[30,30],[70,30],[30,70],[70,70]],[[30,30],[70,30],[30,70],[70,70]]
        ],
        levelOneSpots: [
          [[20,20],[80,20],[20,80],[80,80]],[[20,20],[80,20],[20,80],[80,80]],[[20,20],[80,20],[20,80],[80,80]]
        ]
      },`;

// Inject chap2Data into chapterData { 
content = content.replace(/const chapterData = \{\s*1: \{/m, 'const chapterData = {' + chap2Data + '\n      1: {');

// Update UI locks
content = content.replace(/class="chapter-card \$\{\[0,2,3\]\.includes\(i\)\?'open':'locked-chapter'\}"/g, 'class="chapter-card ${[0,1,2,3].includes(i)?\'open\':\'locked-chapter\'}"');
content = content.replace(/\$\{\[0,2,3\]\.includes\(i\)\?\'\':\'<i class="key" aria-hidden="true"><\/i>\'\}/g, '${[0,1,2,3].includes(i)?\'\':\'<i class="key" aria-hidden="true"></i>\'}');

// Update click handler array
content = content.replace(/if\(\[1,3,4\]\.includes\(ch\)\)\{/g, 'if([1,2,3,4].includes(ch)){');

fs.writeFileSync(path, content, 'utf8');
console.log('Chapter 2 added successfully');
