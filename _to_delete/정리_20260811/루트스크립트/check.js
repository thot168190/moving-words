    // 정적 학습장 주소를 직접 열어 로그인 확인을 우회하지 못하도록 앱의 학습 진입점으로 보냅니다.
    if(window===window.top)window.location.replace('/#learn');
  </script>
  <script>
    let isPaid = false;
    let currentChapterId = 1;
    let works = [];
    let levelOneWords = [];
    let levelTwoWords = [];
    let sceneSpots = [];
    let levelOneSpots = [];
    
    const chapterData = {
      2: {
        works: [
          {n:'01',title:'참나무 아래 초원',sub:'생명이 시작되는 곳',video:'챕터2_완성동영상/scene-ch2-02.mp4',img:'챕터2_완성동영상/scene-ch2-02-poster.jpg',current:true,words:[['tree','나무'],['leaf','나뭇잎'],['grass','풀'],['root','뿌리'],['branch','나뭇가지'],['seed','씨앗'],['soil','흙'],['bark','나무껍질']]},
          {n:'02',title:'평원의 기린과 얼룩말',sub:'더불어 사는 동물들',video:'챕터2_완성동영상/scene-ch2-03.mp4',img:'챕터2_완성동영상/scene-ch2-03-poster.jpg',words:[['animal','동물'],['herd','무리'],['tail','꼬리'],['neck','목'],['spot','점'],['stripe','줄무늬'],['plain','평원'],['graze','풀을 뜯다']]},
          {n:'03',title:'진흙 속 개구리',sub:'비 온 뒤의 풍경',video:'챕터2_완성동영상/scene-ch2-05.mp4',img:'챕터2_완성동영상/scene-ch2-05-poster.jpg',words:[['frog','개구리'],['jump','뛰다'],['mud','진흙'],['bank','둑'],['pond','연못'],['insect','곤충'],['catch','잡다'],['hide','숨다']]}
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
      },
      1: {
        works: [
          {n:'01',title:'빛을 보내는 등대',sub:'해안에서 보내는 첫 신호',video:'챕터1_완성동영상/scene-ch1-02.mp4',img:'챕터1_완성동영상/scene-ch1-02-poster.jpg',current:true,words:[['tower','탑'],['island','섬'],['shine','빛나다'],['warn','경고하다'],['cliff','절벽'],['shore','물가'],['guide','안내하다'],['flash','번쩍임']]},
          {n:'02',title:'바람을 타는 범선',sub:'수평선을 향해 떠나다',video:'챕터1_완성동영상/scene-ch1-03.mp4',img:'챕터1_완성동영상/scene-ch1-03-poster.jpg',words:[['sail','돛'],['deck','갑판'],['rope','밧줄'],['flag','깃발'],['journey','여정'],['row','노를 젓다'],['port','항구'],['navy','해군']]},
          {n:'03',title:'돌고래가 따라오는 배',sub:'은빛 바다 위 도약',video:'챕터1_완성동영상/scene-ch1-09.mp4',img:'챕터1_완성동영상/scene-ch1-09-poster.jpg',words:[['dolphin','돌고래'],['follow','따라오다'],['leap','도약하다'],['calm','고요한'],['float','떠 있다'],['reflect','비추다'],['silver','은빛'],['distance','먼 거리']]},
          {n:'04',title:'고래와 깊은 바다',sub:'깊은 바다에서 만난 것',video:'챕터1_완성동영상/scene-ch1-01.mp4',img:'챕터1_완성동영상/scene-ch1-01-poster.jpg',hasHand:true,words:[['whale','고래'],['ocean','대양'],['wave','파도'],['surface','수면'],['rise','솟아오르다'],['dive','잠수하다'],['spray','물보라'],['bubble','거품']]},
          {n:'05',title:'깊은 바다의 산호 협곡',sub:'빛이 닿는 마지막 깊이',video:'챕터1_완성동영상/scene-ch1-08.mp4',img:'챕터1_완성동영상/scene-ch1-08-poster.jpg',words:[['dolphin','돌고래'],['shell','조개껍데기'],['seal','물범'],['tide','조수'],['current','해류'],['stream','물줄기'],['sink','가라앉다'],['cage','케이지'],['shadow','그림자']]},
          {n:'06',title:'곶을 돌아 열리는 만',sub:'미지의 풍경',video:'챕터1_완성동영상/scene-ch1-10.mp4?v=4',img:'챕터1_완성동영상/scene-ch1-10-poster.jpg?v=4',words:[['adventure','모험'],['bay','만'],['cape','곶'],['channel','물길'],['coast','해안'],['flood','밀려들다'],['flow','흐르다'],['pool','웅덩이']]}
        ],
        levelOneWords: [
          [['tower','탑'],['island','섬'],['shine','빛나다'],['shore','물가']],
          [['rope','밧줄'],['flag','깃발'],['journey','여정'],['row','노를 젓다']],
          [['follow','따라오다'],['float','떠 있다'],['reflect','비추다'],['silver','은빛']],
          [['wave','파도']],
          [['shell','조개껍데기'],['sink','가라앉다'],['shadow','그림자']],
          [['bay','만'],['coast','해안'],['flow','흐르다'],['pool','웅덩이']]
        ],
        levelTwoWords: [
          [['warn','경고하다'],['cliff','절벽'],['guide','안내하다'],['flash','번쩍임']],
          [['sail','돛'],['deck','갑판'],['port','항구'],['navy','해군']],
          [['dolphin','돌고래'],['leap','도약하다'],['calm','고요한'],['distance','먼 거리']],
          [['whale','고래'],['ocean','대양'],['surface','수면'],['rise','솟아오르다'],['dive','잠수하다'],['spray','물보라'],['bubble','거품']],
          [['seal','물범'],['tide','조수'],['current','해류'],['stream','물줄기'],['cage','케이지']],
          [['adventure','모험'],['cape','곶'],['channel','물길'],['flood','밀려들다']]
        ],
        sceneSpots: [
          [[67,36],[52,18],[57,66],[17,82]],
          [[51,43],[50,14],[25,77],[82,79]],
          [[50,68],[48,36],[76,55],[50,8]],
          [[53,68],[47,49],[50,29],[72,26]],
          [[40,48],[28,42],[42,77],[72,25]],
          [[30,30],[70,30],[30,70],[70,70]]
        ],
        levelOneSpots: [
          [[65,43],[79,79],[51,12],[15,43]],
          [[55,40],[49,15],[18,27],[19,79]],
          [[49,48],[66,19],[38,29],[76,58]],
          [[48,15],[38,48],[20,78],[76,40]],
          [[42,51],[25,17],[75,22],[84,61]],
          [[20,20],[80,20],[20,80],[80,80]]
        ]
      },
      3: {
        works: [
          {n:'01',title:'놀이공원 대관람차',sub:'빙글빙글 돌아가는 풍경',video:'챕터3_완성동영상/scene-ch3-01.mp4',img:'챕터3_완성동영상/scene-ch3-01-poster.jpg',current:true,words:[['wheel','바퀴'],['ride','타다'],['park','공원'],['spin','돌다'],['high','높은'],['view','전망'],['sky','하늘'],['fun','재미']]},
          {n:'02',title:'물보라 롤러코스터',sub:'아찔한 스피드',video:'챕터3_완성동영상/scene-ch3-02.mp4',img:'챕터3_완성동영상/scene-ch3-02-poster.jpg',words:[['track','트랙'],['speed','속도'],['scream','비명'],['drop','떨어지다'],['water','물'],['splash','물보라'],['fast','빠른'],['thrill','스릴']]},
          {n:'03',title:'범퍼카 타는 아이들',sub:'쾅쾅 부딪히는 재미',video:'챕터3_완성동영상/scene-ch3-03.mp4',img:'챕터3_완성동영상/scene-ch3-03-poster.jpg',words:[['car','자동차'],['bump','부딪히다'],['drive','운전하다'],['laugh','웃다'],['seat','좌석'],['steer','조종하다'],['crash','충돌'],['play','놀다']]}
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
      works.forEach((w,i)=>{
        let lock = false;
        if (!isPaid) {
          if (currentChapterId === 1) lock = i >= FREE_SCENES;
          else lock = true;
        }
        w.locked=lock;
        w.needsPurchase=lock;
      });
      
      setupWorks();
      activeWork = works[0];
      if(activeWork) {
        document.querySelectorAll('.work').forEach(x=>x.classList.remove('current'));
        const firstWork = document.querySelector('.work');
        if(firstWork) firstWork.classList.add('current');
        mainVideo.src=activeWork.video;
        mainVideo.load();
        mainPoster.src=activeWork.img;
        document.getElementById('nowLabel').textContent=`LEARNING · ${activeWork.n}`;
        document.getElementById('mainTitle').textContent=activeWork.title;
        renderWords(activeWork);
      }
    }
    const chapters=[
      '세상을 발견하는 순간','숲과 생명','우리 집','학교생활','도시와 교통','음식과 건강',
      '몸과 감정','운동과 도전','여행과 세계','지구와 날씨','우주와 과학','밤과 꿈'
    ];
    const chapterLatin=[
      'INVENTIO','VITA','DOMUS','SCHOLA','URBS','SALUS',
      'SENSUS','MOTUS','MUNDUS','TERRA','COSMOS','SOMNIUM'
    ];
    const chapterGuide=[
      '인벤티오 · 세상을 발견해요','비타 · 숲과 생명','도무스 · 우리 집','스콜라 · 학교생활','우르브스 · 도시와 교통','살루스 · 음식과 건강',
      '센수스 · 몸과 감정','모투스 · 운동과 도전','문두스 · 여행과 세계','테라 · 지구와 날씨','코스모스 · 우주와 과학','솜니움 · 밤과 꿈'
    ];
    // 가로형 모험 지도의 세 섬에 네 개씩 놓인 원형 학습 지점과 맞춥니다.
    const chapterSpots=[[24.3,25.4],[13.4,44.7],[31.2,44.4],[26.1,70.3],[48.4,22.6],[45.3,41.7],[59.8,48.3],[52.4,70.6],[77.8,20.9],[73.6,38.2],[86.8,50.3],[78.6,70.4]];
    const chapterGrid=document.getElementById('chapterGrid');
    chapterGrid.innerHTML=chapters.map((name,i)=>`<button class="chapter-card ${[0].includes(i)?'open':'locked-chapter'}" style="--x:${chapterSpots[i][0]}%;--y:${chapterSpots[i][1]}%" data-chapter="${i+1}" aria-label="챕터 ${i+1}, ${chapterLatin[i]}, ${chapterGuide[i].replace(' · ', ', ')}${i===0?', 학습 가능':', 잠김'}"><small>CHAPTER ${String(i+1).padStart(2,'0')}</small>${[0].includes(i)?'':'<i class="key" aria-hidden="true"></i>'}<h3><span class="label-latin" lang="la">${chapterLatin[i]}</span><span class="label-guide" lang="ko">${chapterGuide[i]}</span></h3></button>`).join('');
    const shelf=document.getElementById('shelf');


    const viewer=document.getElementById('viewer'),mainVideo=document.getElementById('mainVideo'),mainPoster=document.getElementById('mainPoster'),playBtn=document.getElementById('playBtn'),speedBtn=document.getElementById('speedBtn'),resumeBtn=document.getElementById('resumeBtn'),soundBtn=document.getElementById('soundBtn'),fill=document.getElementById('timelineFill'),timeText=document.getElementById('timeText'),wordList=document.getElementById('wordList'),wordOverlay=document.getElementById('wordOverlay');
    // LEVEL 1/2 words are loaded from chapterData
    // 사용자가 직접 만든 카드는 브라우저에 보관합니다. 시연 단계에서는 서버 비용 없이
    // 계정당 최대 10장 흐름을 확인하고, 추후 로그인 DB 저장으로 교체할 수 있습니다.
    // 같은 기기에서 계정을 바꿔도 서로의 카드가 섞이지 않도록 로그인 계정별로 분리합니다.
    let currentAccountKey='guest';
    const customCardKey=()=>`inkword-custom-cards-v2:${currentAccountKey}`;
    const CUSTOM_CARD_LIMIT=10;
    let currentGeneratedCard=null;
    function readCustomCards(){
      try{return JSON.parse(localStorage.getItem(customCardKey())||'[]')}catch{return []}
    }
    function writeCustomCards(cards){localStorage.setItem(customCardKey(),JSON.stringify(cards))}
    function escapeHtml(value=''){return String(value).replace(/[&<>"]/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[char]))}
    function findKnownWord(rawWord){
      const query=rawWord.trim().toLowerCase();
      for(let i=0;i<works.length;i+=1){
        const match=[...(levelOneWords[i]||[]),...(levelTwoWords[i]||[])].find(([word])=>word.toLowerCase()===query);
        if(match)return{work:works[i],word:match[0].toLowerCase(),meaning:match[1]};
      }
      return null;
    }
    function extractGeneratedImage(result){
      const item=result?.data?.[0];
      let path = '';
      if(typeof item==='string') path = item;
      else path = item?.url||item?.path||item?.image?.url||'';

      if(path && !path.startsWith('http')){
        const spaceHost = `https://${config.space.replace('/', '-').toLowerCase()}.hf.space`;
        if(path.startsWith('/file=')){
          path = `${spaceHost}${path}`;
        } else if(path.startsWith('/')){
          path = `${spaceHost}/file=${path}`;
        } else {
          path = `${spaceHost}/file=/${path}`;
        }
      }
      return path;
    }
    // 랜딩에서 소개하는 대표 수채화 카드를 박물관의 상설 전시로도 보여줍니다.
    const featuredMuseumCards=[
      {word:'sailing',meaning:'항해',image:'/feature-cards/sailing.webp'},
      {word:'treasure',meaning:'보물',image:'/feature-cards/treasure.webp'},
      {word:'fishing',meaning:'낚시',image:'/feature-cards/fishing.webp'},
      {word:'storm',meaning:'폭풍',image:'/feature-cards/storm.webp'}
    ];
    function renderMuseumContent(){
      const customCards=readCustomCards();
      const featuredSection=`<section class="featured-museum"><div class="custom-museum-head"><h2>특별 전시 그림 카드</h2><span>${featuredMuseumCards.length}장</span></div><div class="museum-grid">${featuredMuseumCards.map(card=>`<article class="museum-card"><img src="${card.image}" alt="${card.word} 그림 카드"><h3>${card.word}</h3><p>${card.meaning}</p></article>`).join('')}</div></section>`;
      const customSection=customCards.length
        ?`<section class="custom-museum"><div class="custom-museum-head"><h2>내가 만든 그림 카드</h2><span>${customCards.length} / ${CUSTOM_CARD_LIMIT}</span></div><div class="museum-grid">${customCards.map(card=>`<article class="museum-card custom-card"><img src="${escapeHtml(card.image)}" alt="${escapeHtml(card.word)} 학습 카드"><h3>${escapeHtml(card.word)}</h3><p>${escapeHtml(card.meaning||card.style)}</p><button class="delete-card" type="button" data-card-id="${escapeHtml(card.id)}">삭제</button></article>`).join('')}</div></section>`
        :`<section class="custom-museum empty"><div class="custom-museum-head"><h2>내가 만든 그림 카드</h2><span>0 / ${CUSTOM_CARD_LIMIT}</span></div><p>단어를 직접 만들어 저장하면 이곳에 전시됩니다.</p></section>`;
      const learnedCards=works.map((work,index)=>index<completedSceneCount
        ?`<article class="museum-card"><img src="${work.img}" alt="${work.title}"><h3>${work.title}</h3><p>${work.sub}</p></article>`
        :`<article class="museum-card back" aria-label="아직 수집하지 않은 ${index+1}번 카드"><div class="museum-seal"><b>${['I','II','III','IV','V','VI','VII','VIII'][index]}</b></div><p>학습하면 열리는 카드</p></article>`).join('');
      return `<div class="feature-intro"><h1>나의 박물관</h1><p>장면으로 익힌 단어 카드를 한 장씩 모아요.</p></div>${featuredSection}<section class="learned-museum"><div class="custom-museum-head"><h2>챕터 1 학습 카드</h2><span>${completedSceneCount} / 8</span></div><div class="museum-grid">${learnedCards}</div></section>${customSection}`;
    }
    function setupMuseum(){
      document.querySelectorAll('.delete-card').forEach(button=>button.onclick=()=>{
        writeCustomCards(readCustomCards().filter(card=>card.id!==button.dataset.cardId));
        featureContent.innerHTML=renderMuseumContent();setupMuseum();notify('카드를 박물관에서 꺼냈습니다.');
      });
    }
    // Spots are loaded from chapterData
    // 랜딩의 콜로세움 단어와 동일한 음성 규칙입니다.
    // 브라우저 내장 음성을 사용하므로 별도 TTS API 비용은 들지 않습니다.
    const isIOS=/iPad|iPhone|iPod/.test(navigator.userAgent)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);
    let speechUnlocked=false,lastSpokenWord='',lastSpokenAt=0;
    function unlockTTS(){
      if(speechUnlocked||!('speechSynthesis' in window))return;
      speechSynthesis.speak(new SpeechSynthesisUtterance(''));
      speechUnlocked=true;
      window.removeEventListener('pointerdown',unlockTTS);
      window.removeEventListener('touchstart',unlockTTS);
    }
    window.addEventListener('pointerdown',unlockTTS,{passive:true});
    window.addEventListener('touchstart',unlockTTS,{passive:true});
    if('speechSynthesis' in window){
      speechSynthesis.getVoices();
      speechSynthesis.onvoiceschanged=()=>speechSynthesis.getVoices();
    }
    function getBestVoice(){
      const voices=speechSynthesis.getVoices();
      return voices.find(v=>v.name.includes('Samantha'))
        ||voices.find(v=>v.name.includes('Google US English'))
        ||voices.find(v=>v.name.includes('Aria'))
        ||voices.find(v=>v.lang==='en-US')
        ||voices.find(v=>v.lang.startsWith('en'))
        ||null;
    }
    let currentSpeakTimer=null;
    function speakWord(word,button){
      if(!('speechSynthesis' in window)){notify('이 브라우저에서는 음성 재생을 지원하지 않습니다.');return}
      if(currentSpeakTimer){clearTimeout(currentSpeakTimer);currentSpeakTimer=null;}
      speechSynthesis.cancel();
      document.querySelectorAll('.scene-word,.word').forEach(x=>x.classList.remove('speaking'));
      if(button){button.classList.add('speaking');}
      const utterance=new SpeechSynthesisUtterance(word);
      utterance.lang='en-US';utterance.rate=1;utterance.pitch=1.05;utterance.voice=getBestVoice();
      utterance.onend=utterance.onerror=()=>{if(button)button.classList.remove('speaking');};
      currentSpeakTimer=setTimeout(()=>{
        speechSynthesis.speak(utterance);
      },30);
    }
    function speakAllWords(){
      if(!('speechSynthesis' in window)){notify('이 브라우저에서는 음성 재생을 지원하지 않습니다.');return}
      const buttons=[...wordList.querySelectorAll('.word')];
      if(!buttons.length)return;
      speechSynthesis.cancel();
      let index=0;
      const playNext=()=>{
        document.querySelectorAll('.scene-word,.word').forEach(x=>x.classList.remove('speaking'));
        if(index>=buttons.length){soundBtn.textContent='🔊 전체 단어 듣기';return}
        const button=buttons[index++],utterance=new SpeechSynthesisUtterance(button.dataset.word);
        utterance.lang='en-US';utterance.rate=.92;utterance.pitch=1.05;utterance.voice=getBestVoice();
        button.classList.add('speaking');soundBtn.textContent=`🔊 ${index} / ${buttons.length}`;
        utterance.onend=()=>{button.classList.remove('speaking');setTimeout(playNext,140)};
        utterance.onerror=()=>{button.classList.remove('speaking');playNext()};
        speechSynthesis.speak(utterance);
      };
      playNext();
    }
    let wordLevel=1;
    function currentWords(work){const i=works.indexOf(work);return wordLevel===1?(levelOneWords[i]||[]):(levelTwoWords[i]||[])}
    function renderWords(work){
      const sceneIndex=works.indexOf(work),allWords=currentWords(work);
      const spots=wordLevel===1?levelOneSpots[sceneIndex]:sceneSpots[sceneIndex];
      const count=Math.min(allWords.length, (spots||[]).length);
      const indexes=Array.from({length:count},(_,k)=>k);
      wordOverlay.innerHTML=indexes.map((wordIndex,i)=>{
        const [en,ko]=allWords[wordIndex];
        const lengthClass=en.length>=12?'very-long-word':en.length>=9?'long-word':'';
        return `<button class="scene-word visible ${lengthClass}" type="button" data-word="${en}" data-reveal="${i}" style="left:${spots[i][0]}%;top:${spots[i][1]}%" aria-label="${en}, ${ko}, 발음 듣기">${en}<span>${ko}</span></button>`
      }).join('');
      wordOverlay.querySelectorAll('.scene-word').forEach(button=>{
        button.onclick=()=>speakWord(button.dataset.word,button);
      });
      wordList.innerHTML=allWords.map(([en,ko])=>`<button class="word" type="button" data-word="${en}" aria-label="${en}, ${ko}, 발음 듣기"><strong>${en}</strong><em>${ko}</em></button>`).join('');
      wordList.querySelectorAll('.word').forEach(button=>{button.onclick=()=>speakWord(button.dataset.word,button)});
    }
    let activeWork; loadChapter(1);
    const playbackRates=[1,1.5,2];let playbackRateIndex=0;
    speedBtn.onclick=()=>{
      playbackRateIndex=(playbackRateIndex+1)%playbackRates.length;
      const rate=playbackRates[playbackRateIndex];
      mainVideo.playbackRate=rate;
      speedBtn.textContent=`${rate}×`;
      speedBtn.setAttribute('aria-label',`재생 속도 ${rate}배`);
      notify(`재생 속도를 ${rate}배로 바꿨습니다.`);
    };
    document.querySelectorAll('.level-switch button').forEach(button=>button.onclick=()=>{
      wordLevel=Number(button.dataset.level);
      document.querySelectorAll('.level-switch button').forEach(x=>x.classList.toggle('active',x===button));
      document.getElementById('mainSub').textContent=wordLevel===1?'장면을 바로 읽는 핵심 단어부터 시작합니다.':'같은 장면에서 한 단계 깊은 어휘로 확장합니다.';
      renderWords(activeWork);
    });
    function playMain(){viewer.classList.add('playing');wordOverlay.querySelectorAll('.scene-word').forEach(x=>x.classList.remove('visible'));mainVideo.play();playBtn.textContent='Ⅱ';resumeBtn.textContent='잠시 멈추기'}
    function pauseMain(){mainVideo.pause();playBtn.textContent='▶';resumeBtn.textContent='학습 시작'}
    function toggleMain(){mainVideo.paused?playMain():pauseMain()}
    playBtn.onclick=toggleMain;resumeBtn.onclick=toggleMain;mainVideo.onclick=toggleMain;
    mainVideo.ontimeupdate=()=>{const d=mainVideo.duration||1,p=mainVideo.currentTime/d*100;fill.style.width=p+'%';const s=Math.floor(mainVideo.currentTime);timeText.textContent='00:'+String(s).padStart(2,'0');const reveal=Math.max(0,Math.min(4,Math.floor((p-48)/11)+1));wordOverlay.querySelectorAll('.scene-word').forEach((x,i)=>x.classList.toggle('visible',i<reveal))};
    mainVideo.onended=()=>{
      viewer.classList.remove('playing');
      wordOverlay.querySelectorAll('.scene-word').forEach(x=>x.classList.add('visible'));
      pauseMain();
      // 실제 로그인 계정에 장면 완료와 현재 단계 단어를 기록합니다.
      const sceneId=`ch1-${String(activeWork.n).padStart(2,'0')}`;
      const wordIds=currentWords(activeWork).map(([word])=>`${sceneId}-${word.toLowerCase()}`);
      window.parent.postMessage({type:'inkword:scene-complete',sceneId,wordIds},location.origin);
    };
    soundBtn.onclick=speakAllWords;

    let previews=true;
    // 로그인 계정에서 불러온 챕터 1 완료 장면 수입니다.
    let completedSceneCount=0;
    function setupWorks() { shelf.innerHTML=works.map((w,i)=>`<button class="work ${w.current?'current':''} ${w.locked?'locked':''}" data-index="${i}"><div class="poster"><span class="state">${w.current?'학습 중':w.locked?'잠김':'학습하기'}</span><video muted loop playsinline preload="metadata" src="${w.video}"></video><img src="${w.img}" alt="${w.title} 학습 영상 대표 화면"></div><div class="meta"><small>LESSON ${w.n} · 8 WORDS</small><h3>${w.title}</h3><p>${w.sub}</p></div></button>`).join(''); document.querySelectorAll('.work').forEach(el=>{
      const w=works[Number(el.dataset.index)],pv=el.querySelector('video');
      el.addEventListener('mouseenter',()=>{if(previews&&!w.locked&&matchMedia('(hover:hover)').matches)pv.play().catch(()=>{})});
      el.onmouseleave=()=>{pv.pause();pv.currentTime=0};
      el.onclick=()=>{if(w.locked){if(w.needsPurchase){openGate()}else{notify('앞 챕터를 완주하면 학습할 수 있습니다.')}return}document.querySelectorAll('.work').forEach(x=>x.classList.remove('current'));el.classList.add('current');activeWork=w;mainVideo.pause();mainVideo.src=w.video;mainVideo.load();mainVideo.playbackRate=playbackRates[playbackRateIndex];mainPoster.src=w.img;mainPoster.alt=`${w.title} 학습 영상 대표 화면`;document.getElementById('nowLabel').textContent=`LEARNING · ${w.n}`;document.getElementById('mainTitle').textContent=w.title;document.getElementById('mainSub').textContent=wordLevel===1?'장면을 바로 읽는 핵심 단어부터 시작합니다.':'같은 장면에서 한 단계 깊은 어휘로 확장합니다.';renderWords(w);viewer.classList.remove('playing');pauseMain();scrollTo({top:80,behavior:'smooth'})};
    }); }
    document.getElementById('previewToggle').onclick=e=>{previews=!previews;e.currentTarget.classList.toggle('off',!previews);e.currentTarget.setAttribute('aria-label',`미리보기 자동재생 ${previews?'켜짐':'꺼짐'}`);notify(`미리보기 자동재생을 ${previews?'켰습니다.':'껐습니다.'}`)};
    const homeView=document.getElementById('homeView'),chapterDetail=document.getElementById('chapterDetail');
    const welcomeEl=document.querySelector('.welcome'),viewerLayout=document.querySelector('.viewer-layout'),homePlayerAnchor=document.getElementById('homePlayerAnchor');
    const navButtons=[...document.querySelectorAll('.nav button')];
    function activateNav(id){navButtons.forEach(button=>button.classList.toggle('active',button.id===id))}
    function showLearningHome(){
      featureView.classList.remove('active');
      if(chapterDetail.classList.contains('active'))leaveChapter();
      homeView.classList.remove('hidden');activateNav('learnNav');scrollTo({top:0,behavior:'smooth'});
    }
    function enterChapter(){activateNav('learnNav');homeView.classList.add('hidden');chapterDetail.classList.add('active');chapterDetail.insertBefore(viewerLayout,chapterDetail.children[1]);chapterDetail.insertBefore(welcomeEl,viewerLayout);scrollTo({top:0,behavior:'smooth'})}
    function leaveChapter(){homePlayerAnchor.after(welcomeEl,viewerLayout);chapterDetail.classList.remove('active');homeView.classList.remove('hidden');setTimeout(()=>document.getElementById('chapterMap').scrollIntoView({behavior:'smooth'}),20)}
    document.querySelectorAll('.chapter-card').forEach(card=>card.onclick=()=>{
      const ch = Number(card.dataset.chapter);
      if([1,2,3].includes(ch)){
        if (!isPaid && ch !== 1) {
          openGate();
          return;
        }
        loadChapter(ch);
        const chapterTitle = chapters[ch-1]; document.getElementById('chapterDetail').querySelector('.section-head h2').textContent = `챕터 ${ch} · ${chapterTitle}`;
        enterChapter();
      } else {
        notify(`${card.querySelector('h3').textContent} 챕터는 아직 준비중입니다.`);
      }
    });
    document.getElementById('dashboardContinue').onclick=enterChapter;
    document.getElementById('progressEnter').onclick=enterChapter;
    document.getElementById('backBtn').onclick=leaveChapter;
    document.getElementById('learnNav').onclick=showLearningHome;
    document.getElementById('learningBrand').onclick=showLearningHome;
    document.getElementById('mapNav').onclick=()=>{featureView.classList.remove('active');if(chapterDetail.classList.contains('active'))leaveChapter();homeView.classList.remove('hidden');activateNav('mapNav');setTimeout(()=>document.getElementById('chapterMap').scrollIntoView({behavior:'smooth'}),20)};
    const accountButton=document.getElementById('accountButton'),accountMenu=document.getElementById('accountMenu');
    function closeAccountMenu(){accountMenu.classList.remove('open');accountButton.setAttribute('aria-expanded','false')}
    accountButton.onclick=event=>{event.stopPropagation();const open=accountMenu.classList.toggle('open');accountButton.setAttribute('aria-expanded',String(open))};
    document.getElementById('accountLearningHome').onclick=()=>{closeAccountMenu();showLearningHome()};
    document.getElementById('accountLogout').onclick=()=>{closeAccountMenu();window.parent.postMessage({type:'inkword:logout'},location.origin)};
    document.addEventListener('click',event=>{if(!event.target.closest('.account'))closeAccountMenu()});
    document.addEventListener('keydown',event=>{if(event.key==='Escape')closeAccountMenu()});
    const featureView=document.getElementById('featureView'),featureContent=document.getElementById('featureContent');
    function openFeature(type){
      if(chapterDetail.classList.contains('active'))leaveChapter();
      homeView.classList.add('hidden');featureView.classList.add('active');
      activateNav(type==='museum'?'museumNav':type==='studio'?'studioNav':'playNav');
      if(type==='museum')featureContent.innerHTML=renderMuseumContent();
      if(type==='studio')featureContent.innerHTML=`<div class="feature-intro"><h1>내가 만드는 그림 카드</h1><p>제가 하나씩 물어볼게요. 대답만 하면 카드가 완성돼요.</p></div><div class="studio-layout"><div class="generate-preview" id="generatePreview"><div class="generate-empty"><strong>함께 그림 카드를 만들어볼까요?</strong>어려운 설명은 필요 없어요.<br>떠오르는 대로 짧게 알려주세요.</div></div><aside class="studio-side"><div class="mentor-head"><div class="mentor-avatar">✦</div><div><strong>그림 카드 멘토</strong><span>제가 한 단계씩 도와드릴게요.</span></div></div><div class="mentor-roadmap" id="mentorRoadmap"><span class="active">1 단어</span><span>2 뜻</span><span>3 장면</span><span>4 스타일</span></div><div class="mentor-step" data-step="1"><label for="generateWord">어떤 단어를 카드로 만들까요?</label><small>배우고 싶은 영어 단어 하나만 적어주세요.</small><input class="word-input" id="generateWord" value="" placeholder="예: cat"></div><div class="mentor-step waiting" id="meaningStep" data-step="2"><label for="generateMeaning">이 단어는 우리말로 무엇인가요?</label><small>아는 단어는 제가 먼저 뜻을 채워드려요.</small><input class="word-input meaning-input" id="generateMeaning" value="" placeholder="예: 고양이"></div><div class="mentor-step waiting" id="sceneStep" data-step="3"><label for="generateScene">어떤 모습으로 기억하고 싶나요?</label><small>한 문장만 적어도 충분해요.</small><textarea class="word-input" id="generateScene" rows="4" placeholder="예: 구름 위를 날아가는 고양이"></textarea></div><div class="mentor-finish" id="mentorFinish"><div class="studio-creator unlocked" id="studioCreator"><label class="style-label">마지막으로, 그림 느낌을 골라주세요.</label><div class="style-options"><button class="style-option selected">세밀 수채화</button><button class="style-option">잉크 드로잉</button><button class="style-option">빈티지 도감</button><button class="style-option">밝은 파스텔</button><button class="style-option">귀여운 3D 점토</button><button class="style-option">따뜻한 그림책</button></div><p class="mentor-ready" id="mentorReady">단어를 적으면 다음 질문을 이어갈게요.</p><p class="studio-quota" id="studioQuota"></p><p class="studio-connection" id="studioConnection"></p><div class="studio-actions"><button class="primary" id="generateBtn">이 장면으로 카드 만들기</button></div><button class="save-generated" id="saveGenerated" disabled>나의 박물관에 저장</button><p class="studio-status" id="studioStatus" aria-live="polite"></p><p class="studio-note">같은 단어도 장면 설명에 따라 전혀 다른 카드가 만들어집니다.</p></div></div></aside></div>`;
      if(type==='play')featureContent.innerHTML=`<div class="feature-intro"><h1>거꾸로 퀴즈</h1><p>챕터 1의 여덟 장면에서 사라진 단어를 되찾아보세요.</p></div><div class="quiz-scenes" id="quizScenes">${works.map((work,index)=>`<button class="quiz-scene ${index===0?'active':''}" type="button" data-quiz-scene="${index}">${work.n} · ${work.title}</button>`).join('')}</div><div class="memory-layout"><div class="memory-stage" id="memoryStage"></div><aside class="memory-side"><div class="now-label" id="memoryRound">0 / 4</div><h2 id="memoryTitle"></h2><p>단어를 하나 누른 뒤 그림 속 알맞은 물음표를 누르세요.</p><div class="memory-choices" id="memoryChoices"></div><div class="memory-actions"><button class="memory-retry" id="memoryRetry" type="button">다시 풀기</button><button class="memory-next" id="memoryNext" type="button">다음 장면</button></div></aside></div>`;
      if(type==='studio')featureContent.querySelector('h1').textContent='내가 만드는 그림 카드';
      featureContent.querySelector('.feature-intro')?.classList.add(`${type}-intro`);
      scrollTo({top:0,behavior:'smooth'});if(type==='museum')setupMuseum();if(type==='studio')setupGenerator();if(type==='play')setupQuiz();
    }
    function closeFeature(){featureView.classList.remove('active');homeView.classList.remove('hidden');activateNav('learnNav');scrollTo({top:document.getElementById('worlds').offsetTop-80,behavior:'smooth'})}
    function setupQuiz(sceneIndex=0){
      const work=works[sceneIndex];
      const targets=levelOneWords[sceneIndex].slice(0,4).map(([word,ko],index)=>({word,ko,answer:levelOneSpots[sceneIndex][index]}));
      const stage=document.getElementById('memoryStage'),choiceBox=document.getElementById('memoryChoices'),roundText=document.getElementById('memoryRound'),title=document.getElementById('memoryTitle'),reset=document.getElementById('memoryRetry'),next=document.getElementById('memoryNext');let completed=0,selectedButton=null;
      document.querySelectorAll('.quiz-scene').forEach(button=>{button.classList.toggle('active',Number(button.dataset.quizScene)===sceneIndex);button.onclick=()=>setupQuiz(Number(button.dataset.quizScene))});
      title.textContent=`${work.n} · ${work.title}`;roundText.textContent='0 / 4';reset.classList.remove('show');next.classList.remove('show');
      stage.innerHTML=`<img src="${work.img}" alt="${work.title} 거꾸로 퀴즈">${targets.map((target,i)=>`<div class="memory-hole" data-target="${target.word}" id="memoryHole${i}" aria-label="${target.ko} 단어를 놓는 자리" style="left:${target.answer[0]-7}%;top:${target.answer[1]-8}%;width:14%;height:16%">?</div><div class="memory-answer" id="memoryAnswer${i}" style="left:${target.answer[0]}%;top:${target.answer[1]}%">${target.word}</div>`).join('')}`;
      choiceBox.innerHTML=targets.map(target=>`<button class="memory-choice" type="button" draggable="true" data-word="${target.word}">${target.word.toLowerCase()}</button>`).join('');
      const holes=[...stage.querySelectorAll('.memory-hole')],buttons=[...choiceBox.querySelectorAll('.memory-choice')];
      function placeWord(button,hole){
        if(!button||!hole||button.disabled)return;
        if(button.dataset.word!==hole.dataset.target){button.classList.add('wrong');setTimeout(()=>button.classList.remove('wrong'),600);notify('다른 자리예요. 그림을 다시 살펴보세요.');return}
        const index=targets.findIndex(target=>target.word===button.dataset.word);button.disabled=true;button.classList.remove('selected');button.classList.add('correct');hole.classList.add('restored');document.getElementById(`memoryAnswer${index}`).classList.add('show');completed+=1;roundText.textContent=`${completed} / ${targets.length}`;speakWord(button.dataset.word,button);notify(`${button.dataset.word}을 제자리에 돌려놓았어요.`);selectedButton=null;
        if(completed===targets.length){reset.classList.add('show');if(sceneIndex<works.length-1)next.classList.add('show');notify(`${work.title}의 네 단어를 모두 되찾았습니다!`)}
      }
      holes.forEach(hole=>{
        hole.ondragover=e=>{e.preventDefault();hole.classList.add('drop-ready')};hole.ondragleave=()=>hole.classList.remove('drop-ready');
        hole.ondrop=e=>{e.preventDefault();hole.classList.remove('drop-ready');placeWord(choiceBox.querySelector(`[data-word="${e.dataTransfer.getData('text/plain')}"]`),hole)};
        hole.onclick=()=>{if(selectedButton)placeWord(selectedButton,hole);else notify('먼저 오른쪽에서 단어를 하나 선택해주세요.')};
      });
      buttons.forEach(button=>{
        button.onclick=()=>{selectedButton=button;buttons.forEach(x=>x.classList.toggle('selected',x===button));notify('이제 그림 속 물음표를 눌러보세요.')};
        button.ondragstart=e=>{e.dataTransfer.setData('text/plain',button.dataset.word);button.classList.add('dragging')};button.ondragend=()=>{button.classList.remove('dragging');holes.forEach(hole=>hole.classList.remove('drop-ready'))};
      });
      reset.onclick=()=>setupQuiz(sceneIndex);
      next.onclick=()=>setupQuiz(Math.min(sceneIndex+1,works.length-1));
    }
    function setupGenerator(){
      let style='세밀 수채화';currentGeneratedCard=null;
      const preview=document.getElementById('generatePreview'),generateButton=document.getElementById('generateBtn'),saveButton=document.getElementById('saveGenerated'),wordInput=document.getElementById('generateWord'),meaningInput=document.getElementById('generateMeaning'),sceneInput=document.getElementById('generateScene'),status=document.getElementById('studioStatus'),quota=document.getElementById('studioQuota'),connection=document.getElementById('studioConnection'),meaningStep=document.getElementById('meaningStep'),sceneStep=document.getElementById('sceneStep'),mentorFinish=document.getElementById('mentorFinish'),mentorReady=document.getElementById('mentorReady'),roadmapSteps=[...document.querySelectorAll('#mentorRoadmap span')];
      const config=window.INKWORD_IMAGE_LAB||{};
      const monthKey=new Date().toISOString().slice(0,7),usageKey=`inkword.imageLab.${currentAccountKey}.${monthKey}`;
      const readUsage=()=>Number(localStorage.getItem(usageKey)||0);
      const updateQuota=()=>{quota.textContent=`이번 달 생성 ${readUsage()} / ${CUSTOM_CARD_LIMIT}장 · 박물관 저장 ${readCustomCards().length}장`;connection.textContent=config.space?'이미지 연구실 연결됨':'이미지 연구실 연결 대기';connection.classList.toggle('connected',Boolean(config.space))};updateQuota();
      document.querySelectorAll('.style-option').forEach(button=>button.onclick=()=>{document.querySelectorAll('.style-option').forEach(item=>item.classList.remove('selected'));button.classList.add('selected');style=button.textContent});
      // 멘토가 한 번에 한 질문씩 보여줍니다. 이미 학습한 단어라면 뜻도 자동으로 도와줍니다.
      const revealStep=step=>{step.classList.remove('waiting');step.classList.add('revealed')};
      const updateMentor=()=>{
        const word=wordInput.value.trim(),meaning=meaningInput.value.trim(),scene=sceneInput.value.trim();
        if(word)revealStep(meaningStep);
        if(meaning)revealStep(sceneStep);
        if(scene)revealStep(mentorFinish);
        const activeStep=scene?3:meaning?2:word?1:0;
        roadmapSteps.forEach((step,index)=>step.classList.toggle('active',index===activeStep));
        mentorReady.textContent=!word?'단어를 적으면 다음 질문을 이어갈게요.':!meaning?'좋아요. 이제 우리말 뜻만 알려주세요.':!scene?'거의 다 됐어요. 기억하고 싶은 모습을 적어주세요.':'준비됐어요! 그림 느낌을 고르고 카드를 만들어보세요.';
      };
      wordInput.oninput=()=>{const known=findKnownWord(wordInput.value);if(known)meaningInput.value=known.meaning;updateMentor()};
      meaningInput.oninput=updateMentor;sceneInput.oninput=updateMentor;updateMentor();
      generateButton.onclick=async()=>{
        const word=wordInput.value.trim().toLowerCase(),known=findKnownWord(word),scene=sceneInput.value.trim();
        // 챕터에 등록된 단어는 사용자가 뜻을 지웠더라도 검증된 뜻을 다시 채웁니다.
        // 영어 단어와 엉뚱한 한글 뜻이 한 카드에 저장되는 실수를 막기 위한 안전장치입니다.
        let meaning=meaningInput.value.trim();
        if(known){meaning=known.meaning;meaningInput.value=known.meaning}
        if(!word){notify('먼저 카드로 만들 단어를 알려주세요.');wordInput.focus();return}
        if(!meaning){revealStep(meaningStep);notify('이 단어의 우리말 뜻을 알려주세요.');meaningInput.focus();return}
        if(!scene){revealStep(sceneStep);notify('기억하고 싶은 모습을 짧게 알려주세요.');sceneInput.focus();return}
        if(readUsage()>=CUSTOM_CARD_LIMIT){notify('이번 달 새 그림 10장을 모두 만들었습니다.');return}
        currentGeneratedCard=null;saveButton.disabled=true;saveButton.classList.remove('show');generateButton.disabled=true;generateButton.textContent='학습 카드를 만드는 중…';status.textContent='';preview.innerHTML='<div class="generate-empty"><strong>카드를 준비하고 있어요…</strong>잠시만 기다려주세요.</div>';
        if(!config.space){
          preview.innerHTML='<div class="generate-empty"><strong>화면 준비는 끝났습니다.</strong>자체 이미지 연구실 주소를 연결하면<br>이 장면으로 새 그림이 만들어집니다.</div>';generateButton.disabled=false;generateButton.textContent='새 그림 만들기';status.textContent='기존 그림을 대신 보여주지 않습니다. 생성 서버 연결이 필요합니다.';return;
        }
        try{
          const {Client}=await import('https://cdn.jsdelivr.net/npm/@gradio/client/+esm');
          const client=await Client.connect(config.space);let result;
          try{result=await client.predict(config.apiName||'/generate_card',{word,meaning,scene,style})}catch{result=await client.predict(config.apiName||'/generate_card',[word,meaning,scene,style])}
          const image=extractGeneratedImage(result);if(!image)throw new Error('생성 결과에 이미지가 없습니다.');
          localStorage.setItem(usageKey,String(readUsage()+1));updateQuota();
          currentGeneratedCard={id:`card-${Date.now()}`,word,meaning,scene,style,image,createdAt:new Date().toISOString()};

          // 실시간 붓 스케칭 및 수채화 페이드인 드로잉 연출 적용
          preview.innerHTML=`
            <div class="generate-canvas-container" style="position:relative; width:100%; height:100%; display:flex; align-items:center; justify-content:center; overflow:hidden; background:#fff;">
              <img src="${escapeHtml(image)}" class="sketch-effect-img" style="width:100%; height:100%; object-fit:contain; filter: blur(14px) contrast(1.4); opacity: 0.15; transition: opacity 0.8s, filter 2.2s ease-out, transform 2.2s ease-out; transform: scale(1.025);">
              <div class="brush-mask" style="position:absolute; inset:0; background: #fff; mix-blend-mode: multiply; transition: clip-path 2.4s cubic-bezier(0.25, 1, 0.2, 1); clip-path: inset(0 100% 0 0);"></div>
              <img src="${escapeHtml(image)}" class="final-effect-img" style="position:absolute; inset:0; width:100%; height:100%; object-fit:contain; opacity: 0; transition: opacity 1.0s ease-in-out;">
              <div class="generated-caption" style="position:absolute; left:22px; right:22px; bottom:20px; display:flex; align-items:baseline; gap:10px; padding:12px 16px; background:rgba(255,255,255,.94); border-left:4px solid var(--teal); backdrop-filter:blur(8px); opacity:0; transition: opacity 0.8s ease-out; z-index:3;">
                <strong style="font-family:Pretendard; font-size:26px; color:var(--teal);">${escapeHtml(word)}</strong>
                <span style="font-size:15px; color:var(--sub);">${escapeHtml(meaning)}</span>
              </div>
            </div>
          `;

          setTimeout(() => {
            const container = preview.querySelector('.generate-canvas-container');
            if (!container) return;
            const sketch = container.querySelector('.sketch-effect-img');
            const mask = container.querySelector('.brush-mask');
            const finalImg = container.querySelector('.final-effect-img');
            const caption = container.querySelector('.generated-caption');

            if (sketch) {
              sketch.style.opacity = '0.9';
              sketch.style.filter = 'blur(0px) contrast(1)';
              sketch.style.transform = 'scale(1)';
            }
            if (mask) {
              mask.style.clipPath = 'inset(0 0 0 0)';
            }
            setTimeout(() => {
              if (finalImg) finalImg.style.opacity = '1';
              if (caption) caption.style.opacity = '1';
            }, 1400);
          }, 60);

          saveButton.disabled=false;saveButton.classList.add('show');status.textContent='원하는 장면으로 새 그림 카드를 만들었습니다.';
        }catch(error){preview.innerHTML='<div class="generate-empty"><strong>지금은 이미지를 만들 수 없습니다.</strong>잠시 후 다시 시도해주세요.</div>';status.textContent=`이미지 연구실 연결 오류: ${error.message}`}
        finally{generateButton.disabled=false;generateButton.textContent='다시 만들기'}
      };
      saveButton.onclick=()=>{
        if(!currentGeneratedCard)return;const cards=readCustomCards(),sameIndex=cards.findIndex(card=>card.word===currentGeneratedCard.word);
        if(sameIndex<0&&cards.length>=CUSTOM_CARD_LIMIT){notify('박물관에는 최대 10장까지 저장할 수 있어요.');return}
        if(sameIndex>=0)cards.splice(sameIndex,1);cards.unshift(currentGeneratedCard);writeCustomCards(cards.slice(0,CUSTOM_CARD_LIMIT));updateQuota();saveButton.disabled=true;status.textContent='나의 박물관에 저장했습니다.';notify(`${currentGeneratedCard.word} 카드를 박물관에 저장했습니다.`);
      };
    }
    document.getElementById('featureBack').onclick=closeFeature;
    document.getElementById('museumNav').onclick=()=>openFeature('museum');
    document.getElementById('studioNav').onclick=()=>openFeature('studio');
    document.getElementById('playNav').onclick=()=>openFeature('play');
    document.querySelectorAll('[data-world]').forEach(b=>b.onclick=()=>openFeature(b.dataset.world));
    document.getElementById('allBtn').onclick=()=>notify('챕터 1에는 8개의 단어 학습이 있습니다.');
    document.getElementById('courseBtn').onclick=()=>notify('12개 챕터를 순서대로 학습합니다.');

    // 부모 React 앱에서 로그인 계정과 실제 학습 기록을 받아 화면에 반영합니다.
    window.addEventListener('message',event=>{
      if(event.origin!==location.origin||event.data?.type!=='inkword:init')return;
      const user=event.data.user||{},progress=event.data.progress||{};
      currentAccountKey=String(user.uid||user.email||'guest').replace(/[^a-zA-Z0-9@._-]/g,'_');
      const accountName=user.displayName||user.email?.split('@')[0]||'학습자';
      const accountText=document.querySelector('.account span');
      const accountMark=document.querySelector('.account-mark');
      if(accountText)accountText.textContent=`${accountName} 님`;
      if(accountMark)accountMark.textContent=accountName.slice(0,1).toUpperCase();

      // ── 결제 게이팅 ── 미구매 계정은 무료 장면 이후를 잠근다
      isPaid=event.data.paid===true;
      const FREE_SCENES=3;
      works.forEach((w,i)=>{
        let lock = false;
        if (!isPaid) {
          if (currentChapterId === 1) lock = i >= FREE_SCENES;
          else lock = true;
        }
        w.locked=lock;
        w.needsPurchase=lock;
      });
      document.querySelectorAll('.work').forEach(el=>{const w=works[Number(el.dataset.index)];el.classList.toggle('locked',!!w.locked)});
      
      document.querySelectorAll('.chapter-card').forEach((card, i) => {
        if (isPaid || i === 0) {
          card.classList.remove('locked-chapter');
          card.classList.add('open');
          const key = card.querySelector('.key');
          if(key) key.remove();
        } else {
          card.classList.add('locked-chapter');
          card.classList.remove('open');
          if(!card.querySelector('.key')) {
            const key = document.createElement('i');
            key.className = 'key';
            key.setAttribute('aria-hidden', 'true');
            card.insertBefore(key, card.querySelector('h3'));
          }
        }
      });
      const gateBadge=document.getElementById('gateBadge');
      if(gateBadge)gateBadge.style.display=paid?'none':'';
      const completedIds=Array.isArray(progress.completedSceneIds)?progress.completedSceneIds:[];
      completedSceneCount=Math.min(8,completedIds.filter(id=>String(id).startsWith('ch1-')).length);
      const learnedWordIds=Array.isArray(progress.learnedWordIds)?progress.learnedWordIds:[];
      const collectedCardIds=Array.isArray(progress.collectedCardIds)?progress.collectedCardIds:[];
      const progressButton=document.getElementById('progressEnter');
      const progressBar=document.querySelector('.brief-progress .bar i');
      if(progressButton)progressButton.innerHTML=`챕터 1 · ${completedSceneCount}/8 학습 <b>→</b>`;
      if(progressBar)progressBar.style.width=`${completedSceneCount/8*100}%`;
      const nextWork=works[Math.min(completedSceneCount,works.length-1)];
      document.getElementById('dashboardName').textContent=`${accountName} 님`;
      document.getElementById('dashboardProgressText').textContent=`${completedSceneCount} / 8 장면`;
      document.getElementById('dashboardProgressBar').style.width=`${completedSceneCount/8*100}%`;
      document.getElementById('dashboardScenes').textContent=String(completedSceneCount);
      document.getElementById('dashboardWords').textContent=String(learnedWordIds.length);
      document.getElementById('dashboardCards').textContent=String(new Set([...collectedCardIds,...readCustomCards().map(card=>card.id)]).size);
      document.getElementById('dashboardNextTitle').textContent=`${nextWork.n} · ${nextWork.title}`;
      document.getElementById('dashboardNextCopy').textContent=completedSceneCount?'지난 학습 다음 장면부터 이어서 시작합니다.':'첫 장면부터 천천히 시작해보세요.';
      document.getElementById('dashboardContinue').textContent=completedSceneCount?'이어서 학습하기 →':'첫 학습 시작하기 →';
    });
    // ── 구매 안내 / 사전신청 모달 ──
    function openGate(){
      const m=document.getElementById('gateModal'),cDef=document.getElementById('gateCardDefault'),cPre=document.getElementById('gateCardPrereg');
      if(cDef)cDef.style.display='block';
      if(cPre)cPre.style.display='none';
      if(m)m.classList.add('show');
    }
    function closeGate(){const m=document.getElementById('gateModal');if(m)m.classList.remove('show')}
    (function(){
      const close=document.getElementById('gateClose'),
            preregClose=document.getElementById('preregClose'),
            buy=document.getElementById('gateBuy'),
            modal=document.getElementById('gateModal'),
            preregForm=document.getElementById('preregForm'),
            preregEmail=document.getElementById('preregEmail'),
            preregDone=document.getElementById('preregDone'),
            cDef=document.getElementById('gateCardDefault'),
            cPre=document.getElementById('gateCardPrereg');

      if(close)close.onclick=closeGate;
      if(preregClose)preregClose.onclick=closeGate;

      if(buy)buy.onclick=()=>{
        if(cDef)cDef.style.display='none';
        if(cPre)cPre.style.display='block';
        if(preregDone)preregDone.style.display='none';
        if(preregForm)preregForm.style.display='flex';
        try{window.parent.postMessage({type:'inkword:need-purchase'},location.origin)}catch(e){}
      };

      if(preregForm)preregForm.onsubmit=(e)=>{
        e.preventDefault();
        const email=(preregEmail?preregEmail.value:'').trim();
        if(!email)return;
        try{
          const list=JSON.parse(localStorage.getItem('inkword-preregistrations')||'[]');
          list.push({email, createdAt:new Date().toISOString(), source:'learning-gate'});
          localStorage.setItem('inkword-preregistrations',JSON.stringify(list));
        }catch(err){}
        if(preregForm)preregForm.style.display='none';
        if(preregDone)preregDone.style.display='block';
        notify('사전신청이 완료되었습니다.');
      };

      if(modal)modal.onclick=e=>{if(e.target===modal)closeGate()};
      document.addEventListener('keydown',e=>{if(e.key==='Escape')closeGate()});
    })();
    function notify(msg){const n=document.getElementById('notice');n.textContent=msg;n.classList.add('show');setTimeout(()=>n.classList.remove('show'),1900)}
    try{window.parent.postMessage({type:'inkword:ready'},'*');}catch(e){}
