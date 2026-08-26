# -*- coding: utf-8 -*-
"""
로부장 지시서 5-1 실행: public/learning/index.html 을 15챕터로 확장
1. chapters 배열에 '사람과 사회','사고팔기와 셈','말과 소리' 추가
2. chapterLatin 배열에 'FORUM','MERCATUS','VOX' 추가
3. chapterGuide 배열에 '포룸 · 사람과 사회','메르카투스 · 사고팔기와 셈','복스 · 말과 소리' 추가
4. chapterSpots 배열에 [24.0,88.0],[50.0,88.0],[77.0,88.0] 추가
5. chapterData에 13, 14, 15 빈 챕터 (5배열 완비) 추가
"""

with open("public/learning/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. chapters 배열 교체
old_chapters = """    const chapters=[
      '세상을 발견하는 순간','숲과 생명','우리 집','학교생활','도시와 교통','음식과 건강',
      '몸과 감정','운동과 도전','여행과 세계','지구와 날씨','우주와 과학','밤과 꿈'
    ];"""

new_chapters = """    const chapters=[
      '세상을 발견하는 순간','숲과 생명','우리 집','학교생활','도시와 교통','음식과 건강',
      '몸과 감정','운동과 도전','여행과 세계','지구와 날씨','우주와 과학','밤과 꿈',
      '사람과 사회','사고팔기와 셈','말과 소리'
    ];"""

# 2. chapterLatin 교체
old_latin = """    const chapterLatin=[
      'INVENTIO','VITA','DOMUS','SCHOLA','URBS','SALUS',
      'SENSUS','MOTUS','MUNDUS','TERRA','COSMOS','SOMNIUM'
    ];"""

new_latin = """    const chapterLatin=[
      'INVENTIO','VITA','DOMUS','SCHOLA','URBS','SALUS',
      'SENSUS','MOTUS','MUNDUS','TERRA','COSMOS','SOMNIUM',
      'FORUM','MERCATUS','VOX'
    ];"""

# 3. chapterGuide 교체
old_guide = """    const chapterGuide=[
      '인벤티오 · 세상을 발견해요','비타 · 숲과 생명','도무스 · 우리 집','스콜라 · 학교생활','우르브스 · 도시와 교통','살루스 · 음식과 건강',
      '센수스 · 몸과 감정','모투스 · 운동과 도전','문두스 · 여행과 세계','테라 · 지구와 날씨','코스모스 · 우주와 과학','솜니움 · 밤과 꿈'
    ];"""

new_guide = """    const chapterGuide=[
      '인벤티오 · 세상을 발견해요','비타 · 숲과 생명','도무스 · 우리 집','스콜라 · 학교생활','우르브스 · 도시와 교통','살루스 · 음식과 건강',
      '센수스 · 몸과 감정','모투스 · 운동과 도전','문두스 · 여행과 세계','테라 · 지구와 날씨','코스모스 · 우주와 과학','솜니움 · 밤과 꿈',
      '포룸 · 사람과 사회','메르카투스 · 사고팔기와 셈','복스 · 말과 소리'
    ];"""

# 4. chapterSpots 교체
old_spots = """    const chapterSpots=[[24.3,25.4],[13.4,44.7],[31.2,44.4],[26.1,70.3],[48.4,22.6],[45.3,41.7],[59.8,48.3],[52.4,70.6],[77.8,20.9],[73.6,38.2],[86.8,50.3],[78.6,70.4]];"""

new_spots = """    const chapterSpots=[[24.3,25.4],[13.4,44.7],[31.2,44.4],[26.1,70.3],[48.4,22.6],[45.3,41.7],[59.8,48.3],[52.4,70.6],[77.8,20.9],[73.6,38.2],[86.8,50.3],[78.6,70.4],[24.0,88.0],[50.0,88.0],[77.0,88.0]];"""

# 5. chapterData 끝에 13, 14, 15 추가
old_chdata_end = """    ]
  }
};"""

new_chdata_end = """    ]
  },
  "13": {"works":[], "levelOneWords":[], "levelTwoWords":[], "sceneSpots":[], "levelOneSpots":[]},
  "14": {"works":[], "levelOneWords":[], "levelTwoWords":[], "sceneSpots":[], "levelOneSpots":[]},
  "15": {"works":[], "levelOneWords":[], "levelTwoWords":[], "sceneSpots":[], "levelOneSpots":[]}
};"""

assert old_chapters in content, "old_chapters not found"
assert old_latin in content, "old_latin not found"
assert old_guide in content, "old_guide not found"
assert old_spots in content, "old_spots not found"
assert old_chdata_end in content, "old_chdata_end not found"

content = content.replace(old_chapters, new_chapters)
content = content.replace(old_latin, new_latin)
content = content.replace(old_guide, new_guide)
content = content.replace(old_spots, new_spots)
content = content.replace(old_chdata_end, new_chdata_end)

with open("public/learning/index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("public/learning/index.html 15챕터 확장 완료!")
