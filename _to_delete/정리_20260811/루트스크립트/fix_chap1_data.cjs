const fs = require('fs');
const path = 'public/learning/index.html';
let content = fs.readFileSync(path, 'utf8');

const correctChap1 = `1: {
        works: [
          {n:'01',title:'빛을 보내는 등대',sub:'해안에서 보내는 첫 신호',video:'챕터1_완성동영상/scene-ch1-02.mp4',img:'챕터1_완성동영상/scene-ch1-02-poster.jpg',current:true,words:[['tower','탑'],['island','섬'],['shine','빛나다'],['warn','경고하다'],['cliff','절벽'],['shore','물가'],['guide','안내하다'],['flash','번쩍임']]},
          {n:'02',title:'바람을 타는 범선',sub:'수평선을 향해 떠나다',video:'챕터1_완성동영상/scene-ch1-03.mp4',img:'챕터1_완성동영상/scene-ch1-03-poster.jpg',words:[['sail','돛'],['deck','갑판'],['rope','밧줄'],['flag','깃발'],['journey','여정'],['row','노를 젓다'],['port','항구'],['navy','해군']]},
          {n:'03',title:'고래와 깊은 바다',sub:'깊은 바다에서 만난 것',video:'챕터1_완성동영상/scene-ch1-01.mp4',img:'챕터1_완성동영상/scene-ch1-01-poster.jpg',hasHand:true,words:[['whale','고래'],['ocean','대양'],['wave','파도'],['surface','수면'],['rise','솟아오르다'],['dive','잠수하다'],['spray','물보라'],['bubble','거품']]},
          {n:'04',title:'깊은 바다의 산호 협곡',sub:'빛이 닿는 마지막 깊이',video:'챕터1_완성동영상/scene-ch1-08.mp4',img:'챕터1_완성동영상/scene-ch1-08-poster.jpg',words:[['dolphin','돌고래'],['shell','조개껍데기'],['seal','물범'],['tide','조수'],['current','해류'],['stream','물줄기'],['sink','가라앉다'],['cage','케이지'],['shadow','그림자']]}
        ],
        levelOneWords: [
          [['tower','탑'],['island','섬'],['shine','빛나다'],['shore','물가']],
          [['rope','밧줄'],['flag','깃발'],['journey','여정'],['row','노를 젓다']],
          [['wave','파도']],
          [['shell','조개껍데기'],['sink','가라앉다'],['shadow','그림자']]
        ],
        levelTwoWords: [
          [['warn','경고하다'],['cliff','절벽'],['guide','안내하다'],['flash','번쩍임']],
          [['sail','돛'],['deck','갑판'],['port','항구'],['navy','해군']],
          [['whale','고래'],['ocean','대양'],['surface','수면'],['rise','솟아오르다'],['dive','잠수하다'],['spray','물보라'],['bubble','거품']],
          [['seal','물범'],['tide','조수'],['current','해류'],['stream','물줄기'],['cage','케이지']]
        ],
        sceneSpots: [
          [[67,36],[52,18],[57,66],[17,82]],
          [[51,43],[50,14],[25,77],[82,79]],
          [[53,68],[47,49],[50,29],[72,26]],
          [[40,48],[28,42],[42,77],[72,25]]
        ],
        levelOneSpots: [
          [[65,43],[79,79],[51,12],[15,43]],
          [[55,40],[49,15],[18,27],[19,79]],
          [[48,15],[38,48],[20,78],[76,40]],
          [[42,51],[25,17],[75,22],[84,61]]
        ]
      },`;

content = content.replace(/1: \{[\s\S]*?3: \{/m, correctChap1 + '\n      3: {');
fs.writeFileSync(path, content, 'utf8');
console.log('Fixed chapterData[1]');
