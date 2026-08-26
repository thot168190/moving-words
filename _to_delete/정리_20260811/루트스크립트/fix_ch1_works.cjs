const fs = require('fs');
const path = 'public/learning/index.html';
let content = fs.readFileSync(path, 'utf8');

const correctWorks = `const works=[
      {n:'01',title:'빛을 보내는 등대',sub:'해안에서 보내는 첫 신호',video:'챕터1_완성동영상/scene-ch1-02.mp4',img:'챕터1_완성동영상/scene-ch1-02-poster.jpg',current:true,words:[['tower','탑'],['island','섬'],['shine','빛나다'],['warn','경고하다'],['cliff','절벽'],['shore','물가'],['guide','안내하다'],['flash','번쩍임']]},
      {n:'02',title:'바람을 타는 범선',sub:'수평선을 향해 떠나다',video:'챕터1_완성동영상/scene-ch1-03.mp4',img:'챕터1_완성동영상/scene-ch1-03-poster.jpg',words:[['sail','돛'],['deck','갑판'],['rope','밧줄'],['flag','깃발'],['journey','여정'],['row','노를 젓다'],['port','항구'],['navy','해군']]},
      {n:'03',title:'고래와 깊은 바다',sub:'깊은 바다에서 만난 것',video:'챕터1_완성동영상/scene-ch1-01.mp4',img:'챕터1_완성동영상/scene-ch1-01-poster.jpg',hasHand:true,words:[['whale','고래'],['ocean','대양'],['wave','파도'],['surface','수면'],['rise','솟아오르다'],['dive','잠수하다'],['spray','물보라'],['bubble','거품']]},
      {n:'04',title:'깊은 바다의 산호 협곡',sub:'빛이 닿는 마지막 깊이',video:'챕터1_완성동영상/scene-ch1-08.mp4',img:'챕터1_완성동영상/scene-ch1-08-poster.jpg',words:[['shell','조개껍데기'],['seal','물범'],['tide','조수'],['current','해류'],['stream','물줄기'],['sink','가라앉다'],['cage','케이지'],['shadow','그림자']]}
    ];`;

content = content.replace(/const works=\[[\s\S]*?\];/m, correctWorks);
fs.writeFileSync(path, content, 'utf8');
console.log('Fixed Chapter 1 original works');
