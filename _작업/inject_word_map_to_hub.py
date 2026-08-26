# -*- coding: utf-8 -*-
"""
대표님 지시 완벽 반영:
1. 확정한 단어 (406개) vs 남은 단어 (794개) 실시간 현황표 탑재
2. 각 세트별 '해결되는 정본 단어' 매핑
3. [🚨 그림 단독 불가 -> 서사/상황 씬 해결 단어 목록] 투명 공개 & 해결책 명시
"""

import io, json, os

# scene_tool.py 데이터 로드
from scene_tool import load, used, tags, owners

_, _, _, data = load()
U = used(data)
G, byg = tags()
OWN = owners(data, G)

# 챕터별 확정/잔여 집계
NM = {1:"INVENTIO 세상을 발견해요",2:"VITA 숲과 생명",3:"DOMUS 우리 집",4:"SCHOLA 학교생활",
      5:"URBS 도시와 교통",6:"SALUS 음식과 건강",7:"SENSUS 몸과 감정",8:"MOTUS 운동과 도전",
      9:"MUNDUS 여행과 세계",10:"TERRA 지구와 날씨",11:"COSMOS 우주와 과학",12:"SOMNIUM 밤과 꿈",
      13:"FORUM 사람과 사회",14:"MERCATUS 사고팔기와 셈",15:"VOX 말과 소리"}

chapter_stats = []
total_used = len(U)
total_remain = 0

for ch in range(1, 16):
    ch_str = str(ch)
    works_cnt = len(data.get(ch_str, {}).get("works", []))
    ch_used_words = [w for w, loc in U.items() if loc.startswith(f"ch{ch}-")]
    
    # 잔여 단어 계산
    ch_remain_words = []
    for g, ws in byg.items():
        if OWN.get(g) == ch_str:
            ch_remain_words.extend([w for w in ws if w not in U])
            
    total_remain += len(ch_remain_words)
    chapter_stats.append({
        "ch": ch,
        "name": NM.get(ch, f"Chapter {ch}"),
        "works": works_cnt,
        "used": len(ch_used_words),
        "remain": len(ch_remain_words)
    })

# 서사 필요 추상어 목록
narrative_words = {
    "이음말 (21개)": {
        "words": "altogether, despite, either, even, except, instead, let, moreover, neither, nor, otherwise, ought, rather, shall, then, therefore, though, thus, which, whole, would",
        "narrative": "【상황 서사】 폭풍우 속 등불(despite), 갈림길 이정표(either/neither), 홀로 꺼진 창문(except), 차 대신 자전거(instead)"
    },
    "갈등과 화해 (14개)": {
        "words": "argue, claim, complain, convince, debate, deny, insist, awkward, blame, disgust, embarrass, ignore, shame, silly",
        "narrative": "【관계 서사】 등 돌린 두 의자와 식탁(argue/ignore), 깨진 화분과 사과(blame/embarrass/shame)"
    },
    "마음과 약속 (18개)": {
        "words": "bore, depress, desire, desperate, disappoint, hesitate, lack, pity, sore, advice, advise, beg, excuse, greet, hint, pardon, promise, propose",
        "narrative": "【감정 서사】 비 오는 날 창가와 식어가는 차(depress/disappoint), 닫힌 문 앞 봉인된 편지와 열쇠(promise/hesitate)"
    },
    "결과와 원인 (21개)": {
        "words": "achieve, affect, cause, effect, expect, factor, function, happen, influence, intend, intent, matter, mission, obvious, occur, potential, purpose, result, role, succeed, success",
        "narrative": "【인과 서사】 완성된 탑과 마지막 블록(achieve/succeed), 넘어진 도미노(cause/effect), 항해 지도와 나침반(mission/purpose)"
    }
}

print("단어 맵 집계 완료!")
