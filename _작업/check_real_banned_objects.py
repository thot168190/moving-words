# -*- coding: utf-8 -*-
import json, re

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    complete_100 = json.load(f)

REAL_BANNED = [
    r'\bship\b', r'\bsail\b', r'\bboat\b', r'\banchor\b', 
    r'\bmagnifier\b', r'\bmagnifying\b', r'\bloupe\b',
    r'\bmetronome\b', r'\bglobe\b', r'\bastrolabe\b', r'\btelescope\b'
]

print("=== 프롬프트 본문 내 진짜 중복/지뢰 사물 검사 ===")
found = 0
for s in complete_100:
    for idx, p in enumerate(s["prompts"]):
        # 필수문 헤더 제외하고 본문(Draw ...) 부분만 검사
        body = p["prompt"]
        for b in REAL_BANNED:
            matches = re.findall(b, body, re.IGNORECASE)
            # anchor in each outer third 제외
            matches = [m for m in matches if m.lower() != 'anchor']
            if matches:
                print(f"[{s['set_id']} - {idx+1}번] '{p['title']}' -> {matches}")
                found += len(matches)

print(f"진짜 지뢰 사물 총 발견: {found}건")
