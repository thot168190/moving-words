# -*- coding: utf-8 -*-
"""
기존 406개 확정 단어 + Set 04~13 전체 단어의 정확한 중복 감사 보고서
"""

import re, json

with open("public/learning/index.html", "r", encoding="utf-8") as f:
    c = f.read()

# 406개 확정 단어 추출
# chapterSpots 안의 단어들
spot_words = set(re.findall(r'\[\s*\d+\s*,\s*\d+\s*,\s*"([^"]+)"', c))
spot_words_lower = {w.lower().strip() for w in spot_words}

print(f"=== 기존 사이트(1~3차) 확정 단어: 총 {len(spot_words_lower)}개 ===")

# Set 08 단어 정밀 검사
with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

set08 = None
for s in data:
    if s["set_id"] == "set08":
        set08 = s
        break

print("\n=== Set 08 (철도·교통 & 계절·날씨) 50개 단어 전수 감사 ===")
set08_existing_overlap = []
set08_new_words = []

for p in set08["prompts"]:
    for w in p["words"]:
        wl = w.lower().strip()
        if wl in spot_words_lower:
            set08_existing_overlap.append((wl, p["title"]))
        else:
            set08_new_words.append(wl)

print(f"Set 08 총 50단어 중:")
print(f" - 100% 신규 단어: {len(set08_new_words)}개 ({len(set08_new_words)/50*100:.1f}%)")
print(f" - 기존 406단어와 중복된 단어: {len(set08_existing_overlap)}개")
for w, title in set08_existing_overlap:
    print(f"   * '{w}' (in {title}) -> 이미 기존 406단어에 있음!")

