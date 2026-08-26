# -*- coding: utf-8 -*-
import os, sys

# scene_tool.py의 검증 함수를 직접 임포트/실행하여 단어 집합 가져오기
import scene_tool

src_spots = scene_tool.read_array(scene_tool.SRC, "chapterSpots")
site_words = set()
for ch_idx, ch_scenes in enumerate(src_spots):
    for sc_idx, sc in enumerate(ch_scenes):
        for item in sc:
            # item = ["word", "뜻", [x, y]]
            site_words.add(item[0].lower().strip())

print(f"사이트에 실제 주입된 단어: 총 {len(site_words)}개")

# 1200 마스터 단어
with open("_작업/all1200.txt", "r", encoding="utf-8") as f:
    all_1200 = set(line.strip().lower() for line in f if line.strip())

print(f"1200 마스터 단어: 총 {len(all_1200)}개")

import json
with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

total_set_words = set()
for s in data:
    for p in s["prompts"]:
        for w in p["words"]:
            total_set_words.add(w.lower().strip())

print(f"Set 04 ~ Set 13에 등록된 고유 단어: 총 {len(total_set_words)}개")

# 사이트 단어와의 겹침
overlap_with_site = total_set_words.intersection(site_words)
print(f"⚠️ 기존 사이트 주입 단어와 겹치는 단어: {len(overlap_with_site)}개")
if overlap_with_site:
    print("겹치는 단어 목록:", sorted(list(overlap_with_site))[:20])

