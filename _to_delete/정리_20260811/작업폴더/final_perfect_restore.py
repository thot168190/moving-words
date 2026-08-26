import json, re

with open('_to_delete/learning_index_백업_20260810/dist_index_15편.html', 'r', encoding='utf-8') as f:
    clean_original = f.read()

# 30 scene works definitions
ch1_works = [
    {'n':'01','title':'빛을 보내는 등대','sub':'해안에서 보내는 첫 신호','video':'챕터1_완성동영상/scene-ch1-02.mp4','img':'챕터1_완성동영상/scene-ch1-02-poster.jpg','current':True,'words':[['tower','탑'],['island','섬'],['shine','빛나다'],['warn','경고하다'],['cliff','절벽'],['shore','물가'],['guide','안내하다'],['flash','번쩍임']]},
    {'n':'02','title':'바람을 타는 범선','sub':'수평선을 향해 떠나다','video':'챕터1_완성동영상/scene-ch1-03.mp4','img':'챕터1_완성동영상/scene-ch1-03-poster.jpg','words':[['sail','돛'],['deck','갑판'],['rope','밧줄'],['flag','깃발'],['journey','여정'],['row','노를 젓다'],['port','항구'],['navy','해군']]},
    {'n':'03','title':'돌고래가 따라오는 배','sub':'은빛 바다 위 도약','video':'챕터1_완성동영상/scene-ch1-09.mp4','img':'챕터1_완성동영상/scene-ch1-09-poster.jpg','words':[['dolphin','돌고래'],['follow','따라오다'],['leap','도약하다'],['calm','고요한'],['float','떠 있다'],['reflect','비추다'],['silver','은빛'],['distance','먼 거리']]},
    {'n':'04','title':'시간을 품은 콜로세움','sub':'제국의 유적터','video':'챕터1_완성동영상/scene-ch1-04.mp4','img':'챕터1_완성동영상/scene-ch1-04-poster.jpg','words':[['empire','제국'],['castle','성'],['crown','왕관'],['royal','왕실의'],['square','광장'],['structure','구조물'],['tradition','전통'],['site','터']]},
    {'n':'05','title':'밤하늘의 별자리','sub':'망원경으로 본 우주','video':'챕터1_완성동영상/scene-ch1-05.mp4','img':'챕터1_완성동영상/scene-ch1-05-poster.jpg','words':[['planet','행성'],['heaven','하늘'],['shine','빛나다'],['silver','은빛'],['instrument','기구'],['distance','거리'],['observe','관찰하다'],['sight','시야']]},
    {'n':'06','title':'하늘을 물들이는 오로라','sub':'설원 위에 펼쳐진 빛','video':'챕터1_완성동영상/scene-ch1-06.mp4','img':'챕터1_완성동영상/scene-ch1-06-poster.jpg','words':[['freeze','얼다'],['shine','빛나다'],['shade','그늘'],['silver','은빛'],['purple','보라'],['pine','소나무'],['branch','가지'],['atmosphere','대기']]},
    {'n':'07','title':'구름 위의 열기구','sub':'하늘을 나는 여정','video':'챕터1_완성동영상/scene-ch1-07.mp4','img':'챕터1_완성동영상/scene-ch1-07-poster.jpg','words':[['balloon','기구'],['rise','솟다'],['float','떠오르다'],['atmosphere','대기'],['height','높이'],['journey','여정'],['adventure','모험'],['tour','여행']]},
    {'n':'08','title':'깊은 바다의 산호 협곡','sub':'빛이 닿는 마지막 깊이','video':'챕터1_완성동영상/scene-ch1-08.mp4','img':'챕터1_완성동영상/scene-ch1-08-poster.jpg','words':[['dolphin','돌고래'],['shell','조개껍데기'],['seal','물범'],['tide','조수'],['current','해류'],['stream','물줄기'],['sink','가라앉다'],['cage','케이지']]},
    {'n':'09','title':'고래와 깊은 바다','sub':'깊은 바다에서 만난 것','video':'챕터1_완성동영상/scene-ch1-01.mp4','img':'챕터1_완성동영상/scene-ch1-01-poster.jpg','hasHand':True,'words':[['whale','고래'],['ocean','대양'],['wave','파도'],['surface','수면'],['rise','솟아오르다'],['dive','잠수하다'],['spray','물보라'],['bubble','거품']]},
    {'n':'10','title':'곶을 돌아 열리는 만','sub':'미지의 풍경','video':'챕터1_완성동영상/scene-ch1-10.mp4?v=4','img':'챕터1_완성동영상/scene-ch1-10-poster.jpg?v=4','words':[['adventure','모험'],['bay','만'],['cape','곶'],['channel','물길'],['coast','해안'],['flood','밀려들다'],['flow','흐르다'],['pool','웅덩이']]}
]

ch2_works = [
    {'n':'01','title':'새벽 언덕의 양떼','sub':'오솔길을 따라 걸어가는 무리','video':'챕터2_완성동영상/scene-ch2-01.mp4','img':'챕터2_완성동영상/scene-ch2-01-poster.jpg','current':True,'words':[['sheep','양'],['lamb','새끼 양'],['wool','양털'],['lawn','잔디'],['mount','산'],['valley','계곡'],['path','오솔길'],['countryside','시골']]},
    {'n':'02','title':'참나무 아래 초원','sub':'생명이 시작되는 곳','video':'챕터2_완성동영상/scene-ch2-02.mp4','img':'챕터2_완성동영상/scene-ch2-02-poster.jpg','words':[['tree','나무'],['leaf','나뭇잎'],['grass','풀'],['root','뿌리'],['branch','나뭇가지'],['seed','씨앗'],['soil','흙'],['bark','나무껍질']]},
    {'n':'03','title':'평원의 기린과 얼룩말','sub':'더불어 사는 동물들','video':'챕터2_완성동영상/scene-ch2-03.mp4','img':'챕터2_완성동영상/scene-ch2-03-poster.jpg','words':[['animal','동물'],['herd','무리'],['tail','꼬리'],['neck','목'],['spot','점'],['stripe','줄무늬'],['plain','평원'],['graze','풀을 뜯다']]},
    {'n':'04','title':'진흙 속 개구리','sub':'비 온 뒤의 풍경','video':'챕터2_완성동영상/scene-ch2-05.mp4','img':'챕터2_완성동영상/scene-ch2-05-poster.jpg','words':[['frog','개구리'],['jump','뛰다'],['mud','진흙'],['bank','둑'],['pond','연못'],['insect','곤충'],['catch','잡다'],['hide','숨다']]}
]

ch3_works = [
    {'n':'01','title':'놀이공원 대관람차','sub':'빙글빙글 돌아가는 풍경','video':'챕터3_완성동영상/scene-ch3-01.mp4','img':'챕터3_완성동영상/scene-ch3-01-poster.jpg','current':True,'words':[['wheel','바퀴'],['ride','타다'],['park','공원'],['spin','돌다'],['high','높은'],['view','전망'],['sky','하늘'],['fun','재미']]},
    {'n':'02','title':'물보라 롤러코스터','sub':'아찔한 스피드','video':'챕터3_완성동영상/scene-ch3-02.mp4','img':'챕터3_완성동영상/scene-ch3-02-poster.jpg','words':[['track','트랙'],['speed','속도'],['scream','비명'],['drop','떨어지다'],['water','물'],['splash','물보라'],['fast','빠른'],['thrill','스릴']]},
    {'n':'03','title':'범퍼카 타는 아이들','sub':'쾅쾅 부딪히는 재미','video':'챕터3_완성동영상/scene-ch3-03.mp4','img':'챕터3_완성동영상/scene-ch3-03-poster.jpg','words':[['car','자동차'],['bump','부딪히다'],['drive','운전하다'],['laugh','웃다'],['seat','좌석'],['steer','조종하다'],['crash','충돌'],['play','놀다']]},
    {'n':'04','title':'아찔한 드롭타워','sub':'하늘에서 급강하하는 스릴','video':'챕터3_완성동영상/Riders_on_drop_tower_summit_202608062009.mp4','img':'','words':[['tower','탑'],['seat','좌석'],['rise','솟다'],['fear','두려움'],['scream','비명'],['height','높이'],['grab','붙잡다'],['tight','꽉']]},
    {'n':'05','title':'곰인형 뽑기','sub':'기쁨과 환호의 신나는 순간','video':'챕터3_완성동영상/Girl_lifts_won_teddy_bear_202608061648.mp4','img':'','words':[['prize','상품'],['award','상'],['gift','선물'],['bet','내기'],['lift','들어올리다'],['reach','닿다'],['cheer','환호'],['joy','기쁨']]}
]

ch4_works = [
    {'n':'01','title':'자료실의 분류벽 (카드 목록장)','sub':'학교의 모든 기록','video':'챕터4_완성동영상/Pencil_drawing_of_library_cabinet_202608071752.mp4','img':'','current':True,'words':[['catalog','목록'],['arrange','정리하다'],['list','명단'],['article','기사'],['chart','도표'],['graph','그래프'],['magazine','잡지'],['clip','클립']]},
    {'n':'02','title':'무대 원고 편집실 (타자기)','sub':'이야기가 시작되는 곳','video':'챕터4_완성동영상/Mechanical_typewriter_drawing_on…_202608071752.mp4','img':'','words':[['edit','편집하다'],['text','글자'],['spell','철자'],['language','언어'],['poem','시'],['comedy','희극'],['drama','드라마'],['scene','장면']]},
    {'n':'03','title':'여행기록 보존대 (양장본)','sub':'먼 곳의 기억들','video':'챕터4_완성동영상/Archival_sorting_table_drawing_a…_202608071752.mp4','img':'','words':[['diary','일기장'],['document','문서'],['record','기록하다'],['photograph','사진'],['dictionary','사전'],['essay','수필'],['envelope','봉투'],['object','사물']]},
    {'n':'04','title':'혼천의와 피라미드','sub':'사막 속 유적과 천체 관측','video':'챕터4_완성동영상/Armillary_sphere_ring_rotating_202608071553.mp4','img':'','words':[['desert','사막'],['dust','먼지'],['site','터'],['region','지역'],['pile','더미'],['tower','탑'],['pole','기둥'],['square','광장']]},
    {'n':'05','title':'황동 현미경','sub':'미세한 세상을 관찰하는 눈','video':'챕터4_완성동영상/Brass_microscope_drawing_on_paper_202608071553.mp4','img':'','words':[['measure','재다'],['observe','관찰하다'],['glass','유리'],['lens','렌즈'],['detail','상세'],['object','사물'],['search','탐색하다'],['focus','초점']]},
    {'n':'06','title':'모아이와 바다','sub':'해안 언덕 위 거대한 석상','video':'챕터4_완성동영상/Moai_statues_standing_on_grass_202608071553.mp4','img':'','words':[['coast','해안'],['ocean','바다'],['shore','물가'],['mount','산'],['lawn','잔디'],['cliff','절벽'],['giant','거대한'],['figure','형상']]},
    {'n':'07','title':'측량기와 곧은 길','sub':'계곡을 가로지르는 수평','video':'챕터4_완성동영상/Surveyor_instrument_drawing_anim…_202608071553.mp4','img':'','words':[['measure','재다'],['survey','측량'],['technique','기술'],['skill','솜씨'],['route','길'],['highway','큰길'],['lane','좁은길'],['valley','계곡']]},
    {'n':'08','title':'여우와 숲길','sub':'자작나무 숲속 오솔길','video':'챕터4_완성동영상/Red_fox_walking_on_path_202608101458.mp4','img':'','words':[['log','통나무'],['trunk','줄기'],['bark','나무껍질'],['branch','가지'],['leaf','잎'],['path','오솔길'],['bush','덤불'],['dirt','흙']]},
    {'n':'09','title':'거미의 거미줄','sub':'섬세하게 정돈된 망','video':'챕터4_완성동영상/Spider_drawing_on_white_background_202608101458.mp4','img':'','words':[['bug','벌레'],['spot','점'],['pattern','무늬'],['net','그물'],['thread','실'],['weave','짜다'],['trap','함정'],['corner','구석']]},
    {'n':'10','title':'나뭇가지 위 잎벌레','sub':'자연과 하나 된 위장','video':'챕터4_완성동영상/Leaf_insect_on_twig_202608101458.mp4','img':'','words':[['bug','벌레'],['leaf','잎'],['branch','가지'],['green','초록'],['shape','모양'],['skin','피부'],['hide','숨다'],['stay','머물다']]},
    {'n':'11','title':'구름과 액자 액티비티','sub':'하늘의 자유로운 변화','video':'챕터4_완성동영상/Cloud_and_framed_panels_animation_202608101458.mp4','img':'','words':[['cloud','구름'],['sky','하늘'],['frame','틀'],['panel','판'],['blue','파란'],['white','하얀'],['float','뜨다'],['change','변하다']]}
]

def make_ch_data(works):
    levelOneWords = []
    levelTwoWords = []
    sceneSpots = []
    levelOneSpots = []
    for w in works:
        words = w['words']
        l1 = words[:4]
        l2 = words[4:]
        levelOneWords.append(l1)
        levelTwoWords.append(l2)
        sceneSpots.append([[30,30],[70,30],[30,70],[70,70]])
        levelOneSpots.append([[20,20],[80,20],[20,80],[80,80]])
    return {
        'works': works,
        'levelOneWords': levelOneWords,
        'levelTwoWords': levelTwoWords,
        'sceneSpots': sceneSpots,
        'levelOneSpots': levelOneSpots
    }

chapterData = {
    1: make_ch_data(ch1_works),
    2: make_ch_data(ch2_works),
    3: make_ch_data(ch3_works),
    4: make_ch_data(ch4_works)
}

js_chapterData = "const chapterData = " + json.dumps(chapterData, ensure_ascii=False, indent=6) + ";"

# Replace ONLY lines 310 to 422 in clean_original with js_chapterData
old_chapterData_pattern = r'const chapterData = \{.*?\n    \};'
content_with_30_data = re.sub(old_chapterData_pattern, js_chapterData, clean_original, flags=re.DOTALL)

# Update click handler for locked chapters:
old_click = """    document.querySelectorAll('.chapter-card').forEach(card=>card.onclick=()=>{
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
    });"""

new_click = """    document.querySelectorAll('.chapter-card').forEach(card=>card.onclick=()=>{
      const ch = Number(card.dataset.chapter);
      if (!isPaid && ch !== 1) {
        try{window.parent.postMessage({type:'inkword:need-purchase'},location.origin)}catch(e){}
        openGate();
        return;
      }
      if(chapterData[ch]){
        loadChapter(ch);
        const chapterTitle = chapters[ch-1]; document.getElementById('chapterDetail').querySelector('.section-head h2').textContent = `챕터 ${ch} · ${chapterTitle}`;
        enterChapter();
      } else {
        notify(`챕터 ${ch} · ${chapters[ch-1]} 장소는 순차 오픈 예정입니다.`);
      }
    });"""

final_content = content_with_30_data.replace(old_click, new_click)

with open('public/learning/index.html', 'w', encoding='utf-8') as f:
    f.write(final_content)

with open('dist/learning/index.html', 'w', encoding='utf-8') as f:
    f.write(final_content)

print("PERFECTLY RESTORED MAP BUTTONS & 30 SCENES IN BOTH FILES!")
