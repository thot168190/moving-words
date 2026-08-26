# -*- coding: utf-8 -*-
"""
단어 중복 전수 정밀 감사:
1. 기존 사이트 확정 단어 (index.html 내 406단어)
2. 1~7차(Set 01~07)에서 사용된 단어들
3. Set 08 및 추천 단어들 중복 여부 확인
"""

import json, re

# 1. index.html에서 기존 단어 추출
with open("public/learning/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# chapterSpots 등에서 단어 추출
existing_words = set(re.findall(r'"word":\s*"([^"]+)"', html))
print(f"1. 기존 사이트(index.html) 확정 단어 수: {len(existing_words)}개")

# 2. complete_100_data.json 분석
with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("\n=== 세트별 단어 중복 감사 ===")
seen_words = set(existing_words)
for s in data:
    set_id = s["set_id"]
    set_name = s["set_name"]
    duplicates_in_set = []
    new_words_in_set = []
    
    for p in s["prompts"]:
        for w in p["words"]:
            clean_w = w.lower().strip()
            if clean_w in seen_words:
                duplicates_in_set.append((clean_w, p["title"]))
            else:
                new_words_in_set.append(clean_w)
                seen_words.add(clean_w)
                
    print(f"\n[{set_name}]")
    print(f" - 신규 단어: {len(new_words_in_set)}개")
    if duplicates_in_set:
        print(f" - ⚠️ 중복 발생 단어 ({len(duplicates_in_set)}건):")
        for dw, title in duplicates_in_set:
            print(f"    * '{dw}' in [{title}]")
    else:
        print(" - ✓ 중복 없음 (100% 신규 단어)")

