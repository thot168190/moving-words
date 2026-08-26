# -*- coding: utf-8 -*-
import os, json

folder = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1/11차완성본_Set12_음악소리"
files = sorted([f for f in os.listdir(folder) if f.endswith(".mp4")])

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

set12_titles = [p["title"] for p in data[8]["prompts"]]

print("=== Set 12 (음악과 소리) 10개 장면별 3개 베리에이션 보관 현황 ===")
for i in range(1, 11):
    num_str = str(i).zfill(3)
    matching = [f for f in files if f.startswith(num_str)]
    title = set12_titles[i-1] if i <= len(set12_titles) else "알 수 없음"
    print(f"🎬 [{num_str}] {title} : 총 {len(matching)}개 버전 보관 중")
    for mf in matching:
        print(f"     └─ {mf}")

