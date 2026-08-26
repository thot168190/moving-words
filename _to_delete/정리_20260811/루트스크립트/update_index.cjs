const fs = require('fs');

const path = 'public/learning/index.html';
let content = fs.readFileSync(path, 'utf8');

// The replacement code:
const chapterDataCode = `    let currentChapterId = 1;
    let works = [];
    let levelOneWords = [];
    let levelTwoWords = [];
    let sceneSpots = [];
    let levelOneSpots = [];
    
    const chapterData = {
      1: {
        works: [
          {n:'01',title:'빛을 보내는 등대',sub:'해안에서 보내는 첫 신호',video:'챕터1_완성동영상/scene-ch1-02.mp4',img:'챕터1_완성동영상/scene-ch1-02-poster.jpg',current:true,words:[['tower','탑'],['island','섬'],['shine','빛나다'],['warn','경고하다'],['cliff','절벽'],['shore','물가'],['guide','안내하다'],['flash','번쩍임']]},
          {n:'02',title:'바람을 타는 범선',sub:'수평선을 향해 떠나다',video:'챕터1_완성동영상/scene-ch1-03.mp4',img:'챕터1_완성동영상/scene-ch1-03-poster.jpg',words:[['sail','돛'],['deck','갑판'],['rope','밧줄'],['flag','깃발'],['journey','여정'],['row','노를 젓다'],['port','항구'],['navy','해군']]},
          {n:'03',title:'돌고래가 따라오는 배',sub:'은빛 바다 위 도약',video:'챕터1_완성동영상/scene-ch1-09.mp4',img:'챕터1_완성동영상/scene-ch1-09-poster.jpg',words:[['dolphin','돌고래'],['follow','따라오다'],['leap','도약하다'],['calm','고요한'],['float','떠 있다'],['reflect','비추다'],['silver','은빛'],['distance','먼 거리']]},
          {n:'04',title:'고래와 깊은 바다',sub:'깊은 바다에서 만난 것',video:'챕터1_완성동영상/scene-ch1-09.mp4',img:'챕터1_완성동영상/scene-ch1-09-poster.jpg',words:[['whale','고래'],['ocean','대양'],['wave','파도'],['surface','수면'],['rise','솟아오르다'],['dive','잠수하다'],['spray','물보라'],['bubble','거품']]},
          {n:'05',title:'깊은 바다의 산호 협곡',sub:'빛이 닿는 마지막 깊이',video:'챕터1_완성동영상/scene-ch1-08.mp4',img:'챕터1_완성동영상/scene-ch1-08-poster.jpg',words:[['shell','조개껍데기'],['seal','물범'],['tide','조수'],['current','해류'],['stream','물줄기'],['sink','가라앉다'],['cage','케이지'],['shadow','그림자']]}
        ],
        levelOneWords: [
          [['tower','탑'],['island','섬'],['shine','빛나다'],['shore','물가']],
          [['rope','밧줄'],['flag','깃발'],['journey','여정'],['row','노를 젓다']],
          [['follow','따라오다'],['float','떠 있다'],['reflect','비추다'],['silver','은빛']],
          [['wave','파도']],
          [['shell','조개껍데기'],['sink','가라앉다'],['shadow','그림자']]
        ],
        levelTwoWords: [
          [['warn','경고하다'],['cliff','절벽'],['guide','안내하다'],['flash','번쩍임']],
          [['sail','돛'],['deck','갑판'],['port','항구'],['navy','해군']],
          [['dolphin','돌고래'],['leap','도약하다'],['calm','고요한'],['distance','먼 거리']],
          [['whale','고래'],['ocean','대양'],['surface','수면'],['rise','솟아오르다'],['dive','잠수하다'],['spray','물보라'],['bubble','거품']],
          [['seal','물범'],['tide','조수'],['current','해류'],['stream','물줄기'],['cage','케이지']]
        ],
        sceneSpots: [
          [[67,36],[52,18],[57,66],[17,82]],
          [[51,43],[50,14],[25,77],[82,79]],
          [[50,68],[48,36],[76,55],[50,8]],
          [[53,68],[47,49],[50,29],[72,26]],
          [[40,48],[28,42],[42,77],[72,25]],
          [[49,20],[73,34],[24,79],[76,72]],
          [[50,24],[50,60],[50,72],[76,48]],
          [[52,34],[20,66],[50,68],[50,8]]
        ],
        levelOneSpots: [
          [[65,43],[79,79],[51,12],[15,43]],
          [[55,40],[49,15],[18,27],[19,79]],
          [[49,48],[66,19],[38,29],[76,58]],
          [[48,15],[38,48],[20,78],[76,40]],
          [[42,51],[25,17],[75,22],[84,61]],
          [[45,26],[74,15],[22,66],[74,86]],
          [[50,13],[32,56],[72,56],[73,28]],
          [[62,28],[30,68],[65,58],[65,15]]
        ]
      },
      3: {
        works: [
          {n:'01',title:'놀이공원 대관람차',sub:'빙글빙글 돌아가는 풍경',video:'챕터3_완성동영상/Ferris_wheel_animation_202608061947.mp4',img:'',current:true,words:[['wheel','바퀴'],['ride','타다'],['park','공원'],['spin','돌다'],['high','높은'],['view','전망'],['sky','하늘'],['fun','재미']]},
          {n:'02',title:'물보라 롤러코스터',sub:'아찔한 스피드',video:'챕터3_완성동영상/Rollercoaster_drawing_with_water…_202608061527.mp4',img:'',words:[['track','트랙'],['speed','속도'],['scream','비명'],['drop','떨어지다'],['water','물'],['splash','물보라'],['fast','빠른'],['thrill','스릴']]},
          {n:'03',title:'범퍼카 타는 아이들',sub:'쾅쾅 부딪히는 재미',video:'챕터3_완성동영상/Boy_and_girl_in_bumper_202608062001.mp4',img:'',words:[['car','자동차'],['bump','부딪히다'],['drive','운전하다'],['laugh','웃다'],['seat','좌석'],['steer','조종하다'],['crash','충돌'],['play','놀다']]}
        ],
        levelOneWords: [
          [['wheel','바퀴'],['ride','타다'],['park','공원'],['spin','돌다']],
          [['track','트랙'],['speed','속도'],['scream','비명'],['drop','떨어지다']],
          [['car','자동차'],['bump','부딪히다'],['drive','운전하다'],['laugh','웃다']]
        ],
        levelTwoWords: [
          [['high','높은'],['view','전망'],['sky','하늘'],['fun','재미']],
          [['water','물'],['splash','물보라'],['fast','빠른'],['thrill','스릴']],
          [['seat','좌석'],['steer','조종하다'],['crash','충돌'],['play','놀다']]
        ],
        sceneSpots: [
          [[30,30],[70,30],[30,70],[70,70]],[[30,30],[70,30],[30,70],[70,70]],[[30,30],[70,30],[30,70],[70,70]]
        ],
        levelOneSpots: [
          [[20,20],[80,20],[20,80],[80,80]],[[20,20],[80,20],[20,80],[80,80]],[[20,20],[80,20],[20,80],[80,80]]
        ]
      },
      4: {
        works: [
          {n:'01',title:'자료실의 분류벽 (카드 목록장)',sub:'학교의 모든 기록',video:'챕터4_완성동영상/Pencil_drawing_of_library_cabinet_202608071752.mp4',img:'',current:true,words:[['catalog','목록'],['arrange','정리하다'],['list','명단'],['article','기사'],['chart','도표'],['graph','그래프'],['magazine','잡지'],['clip','클립']]},
          {n:'02',title:'무대 원고 편집실 (타자기)',sub:'이야기가 시작되는 곳',video:'챕터4_완성동영상/Mechanical_typewriter_drawing_on…_202608071752.mp4',img:'',words:[['edit','편집하다'],['text','글자'],['spell','철자'],['language','언어'],['poem','시'],['comedy','희극'],['drama','드라마'],['scene','장면']]},
          {n:'03',title:'여행기록 보존대 (양장본)',sub:'먼 곳의 기억들',video:'챕터4_완성동영상/Archival_sorting_table_drawing_a…_202608071752.mp4',img:'',words:[['diary','일기장'],['document','문서'],['record','기록하다'],['photograph','사진'],['dictionary','사전'],['essay','수필'],['envelope','봉투'],['object','사물']]}
        ],
        levelOneWords: [
          [['catalog','목록'],['arrange','정리하다'],['list','명단'],['article','기사']],
          [['edit','편집하다'],['text','글자'],['spell','철자'],['language','언어']],
          [['diary','일기장'],['document','문서'],['record','기록하다'],['photograph','사진']]
        ],
        levelTwoWords: [
          [['chart','도표'],['graph','그래프'],['magazine','잡지'],['clip','클립']],
          [['poem','시'],['comedy','희극'],['drama','드라마'],['scene','장면']],
          [['dictionary','사전'],['essay','수필'],['envelope','봉투'],['object','사물']]
        ],
        sceneSpots: [
          [[30,30],[70,30],[30,70],[70,70]],[[30,30],[70,30],[30,70],[70,70]],[[30,30],[70,30],[30,70],[70,70]]
        ],
        levelOneSpots: [
          [[20,20],[80,20],[20,80],[80,80]],[[20,20],[80,20],[20,80],[80,80]],[[20,20],[80,20],[20,80],[80,80]]
        ]
      }
    };
    
    function loadChapter(chapterNum) {
      currentChapterId = chapterNum;
      const data = chapterData[chapterNum] || chapterData[1];
      works = data.works;
      levelOneWords = data.levelOneWords;
      levelTwoWords = data.levelTwoWords;
      sceneSpots = data.sceneSpots;
      levelOneSpots = data.levelOneSpots;
      
      const FREE_SCENES=3;
      works.forEach((w,i)=>{const lock=i>=FREE_SCENES;w.locked=lock;w.needsPurchase=lock;});
      
      const shelf=document.getElementById('shelf');
      shelf.innerHTML=works.map((w,i)=>\`<button class="work \${w.current?'current':''} \${w.locked?'locked':''}" data-index="\${i}"><div class="poster"><span class="state">\${w.current?'학습 중':w.locked?'잠김':'학습하기'}</span><video muted loop playsinline preload="metadata" src="\${w.video}"></video><img src="\${w.img}" alt="\${w.title} 학습 영상 대표 화면"></div><div class="meta"><small>LESSON \${w.n} · 8 WORDS</small><h3>\${w.title}</h3><p>\${w.sub}</p></div></button>\`).join('');
      setupWorks();
    }`;

// Replace lines 304 to 312
let worksRegex = /const works=\[[\s\S]*?\];\s*const FREE_SCENES=3;\s*works\.forEach\(\(w,i\)=>\{const lock=i>=FREE_SCENES;w\.locked=lock;w\.needsPurchase=lock;\}\);/m;
content = content.replace(worksRegex, chapterDataCode);

// Replace lines 330 to 331 (shelf rendering) since we moved it into loadChapter
content = content.replace(/const shelf=document\.getElementById\('shelf'\);\s*shelf\.innerHTML=works\.map\([\s\S]*?\.join\(''\);/m, `loadChapter(1);`);

// Replace words/spots definitions (lines 336-349, 413-430) because they are now in chapterData
content = content.replace(/\/\/ LEVEL 1\/2 레벨태그 csv와 지시서 표 기준 매핑\s*const levelOneWords=\[[\s\S]*?\];\s*const levelTwoWords=\[[\s\S]*?\];/m, `// LEVEL 1/2 words are loaded from chapterData`);
content = content.replace(/\/\/ LEVEL 2: 실제 대상 가까이에 네 개의 대표 단어를 배치합니다\.\s*const sceneSpots=\[[\s\S]*?\];\s*\/\/ LEVEL 1은 단어가 가리키는 대상 가까이의 흰 여백을 사용합니다\.\s*\/\/ 특히 고래의 tail은 꼬리 옆, surface는 수면 위에 고정합니다\.\s*const levelOneSpots=\[[\s\S]*?\];/m, `// Spots are loaded from chapterData`);

// Now modify enterChapter
let enterChapterRegex = /document\.querySelectorAll\('\.chapter-card'\)\.forEach\(card=>card\.onclick=\(\)=>\{Number\(card\.dataset\.chapter\)===1\?enterChapter\(\):notify\(`\$\{card\.querySelector\('h3'\)\.textContent\} 챕터는 아직 열쇠가 필요합니다\.`\)\}\);/;
let newEnterChapter = `document.querySelectorAll('.chapter-card').forEach(card=>card.onclick=()=>{
      const ch = Number(card.dataset.chapter);
      if([1,3,4].includes(ch)){
        loadChapter(ch);
        document.getElementById('chapterDetail').querySelector('.header h2').textContent = \`CHAPTER \${String(ch).padStart(2,'0')}\`;
        enterChapter();
      } else {
        notify(\`\${card.querySelector('h3').textContent} 챕터는 아직 준비중입니다.\`);
      }
    });`;
content = content.replace(enterChapterRegex, newEnterChapter);

// Fix setupWorks. Wait, currently setupWorks is inline logic! I need to wrap it in a function so loadChapter can call it!
// The inline logic is around line 542 (document.querySelectorAll('.work').forEach(...))
let workEventsRegex = /document\.querySelectorAll\('\.work'\)\.forEach\(el=>\{[\s\S]*?scrollTo\(\{top:80,behavior:'smooth'\}\)\};\s*\}\);/m;
let workEventsContent = content.match(workEventsRegex)[0];
content = content.replace(workEventsRegex, `function setupWorks() { ${workEventsContent} }`);

fs.writeFileSync(path, content, 'utf8');
console.log('Update successful');
