# -*- coding: utf-8 -*-
"""
지겹게 반복되는 사물 7대 영구 퇴출:
1. anchor (닻)
2. sailboat / sailing ship (돛단배/범선)
3. magnifying glass / magnifier (돋보기)
4. metronome (메트로놈)
5. globe (지구본)
6. astrolabe (혼천의)
7. hourglass / sundial (모래시계/해시계 과다)

대체할 신선하고 구체적인 실생활 사물:
- 기상관측 풍향풍속계, 정밀 아날로그 기압계, 수평계(spirit level), 삼각 프리즘,
- 자전거 수리 거치대, 도예 회전 물레, 재봉틀과 실타래, 만년필과 잉크병,
- 첼로와 활, 트롬본, 텐트와 모닥불, 현미경 슬라이드, 저울과 분동 등
"""

import json, re

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    complete_100 = json.load(f)

BANNED_WORDS = [
    r'\banchor\b',
    r'\bsailboat\b',
    r'\bsailing ship\b',
    r'\bmagnifying glass\b',
    r'\bmagnifier\b',
    r'\bmetronome\b',
    r'\bglobe\b',
    r'\bastrolabe\b'
]

print("=== 100편 중 중복/지뢰 사물 전수 검사 ===")
found_count = 0
for s in complete_100:
    for idx, p in enumerate(s["prompts"]):
        p_text = p["prompt"].lower()
        title = p["title"]
        for b in BANNED_WORDS:
            matches = re.findall(b, p_text)
            if matches:
                print(f"[{s['set_id']} - {idx+1}번] '{title}' -> 발견: {matches}")
                found_count += 1

print(f"총 발견 건수: {found_count}건")

