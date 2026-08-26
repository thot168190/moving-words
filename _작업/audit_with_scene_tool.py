# -*- coding: utf-8 -*-
import os, json, re

# 1. 1200 마스터 단어
with open("_작업/all1200.txt", "r", encoding="utf-8") as f:
    all_1200 = [line.strip().lower() for line in f if line.strip()]

# 2. 사이트 index.html에서 현재 확정된 단어 추출
with open("public/learning/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# chapterSpots에서 단어 추출
# ["dock", "부두", [35, 62]] 형식
spots_raw = re.findall(r'\[\s*"([^"]+)"\s*,\s*"([^"]+)"\s*,\s*\[\s*\d+\s*,\s*\d+\s*\]\s*\]', html)
site_words = {w[0].lower().strip(): w[1] for w in spots_raw}

print(f"1. 사이트 현재 확정 단어: 총 {len(site_words)}개")

# 3. Set 04 ~ Set 13의 모든 단어 중복 감사
with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("\n=== [전수 조사] 사이트 확정 단어와 100편 단어의 중복 매칭 보고서 ===")
for s in data:
    set_name = s["set_name"]
    set_id = s["set_id"]
    
    site_overlap = []
    pure_new = []
    
    for p in s["prompts"]:
        for w in p["words"]:
            wl = w.lower().strip()
            if wl in site_words:
                site_overlap.append((wl, site_words[wl], p["title"]))
            else:
                pure_new.append(wl)
                
    overlap_rate = len(site_overlap) / (len(site_overlap) + len(pure_new)) * 100
    print(f"\n📁 [{set_name}] (총 {len(site_overlap) + len(pure_new)}단어)")
    print(f" - 100% 신규 단어: {len(pure_new)}개 ({100-overlap_rate:.1f}%)")
    if site_overlap:
        print(f" - ⚠️ 기존 사이트에 이미 있는 단어 ({len(site_overlap)}건):")
        for en, ko, title in site_overlap:
            print(f"    * '{en}' ({ko}) in [{title}]")
    else:
        print(" - ✓ 기존 사이트 중복 0건 (100% 신규 단어)")

