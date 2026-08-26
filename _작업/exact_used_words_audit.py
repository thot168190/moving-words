# -*- coding: utf-8 -*-
import scene_tool, json

# 1. 사이트 실제 사용 단어 406개
_, _, _, cdata = scene_tool.load()
site_used = scene_tool.used(cdata)
print(f"=== 1. 사이트에 실제 확정 주입된 단어: 총 {len(site_used)}개 ===")

# 2. Set 04 ~ Set 13 100편 단어 분석
with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

total_set_words = []
for s in data:
    for p in s["prompts"]:
        for w in p["words"]:
            total_set_words.append((w.lower().strip(), p["title"], s["set_name"]))

print(f"\n=== 2. Set 04~13 전체 100편 단어 (총 {len(total_set_words)}개) 대조 결과 ===")

site_overlap = []
set_internal_overlap = {}

seen = set()
for w, title, set_name in total_set_words:
    # 사이트와 중복
    if w in site_used:
        site_overlap.append((w, site_used[w], title, set_name))
    # 세트 간 중복
    if w in seen:
        if w not in set_internal_overlap:
            set_internal_overlap[w] = []
        set_internal_overlap[w].append(f"{set_name} [{title}]")
    seen.add(w)

print(f"1) 기존 사이트 확정 단어({len(site_used)}개)와 중복된 단어: 총 {len(site_overlap)}건")
if site_overlap:
    for w, ch, title, sname in site_overlap:
        print(f"   - '{w}' : 이미 {ch}에 확정됨! (발견 위치: {sname} - {title})")
else:
    print("   -> 기존 사이트와 중복 0건!")

print(f"\n2) 신규 100편 내부에서 중복된 단어: 총 {len(set_internal_overlap)}개")
for w, occ in sorted(set_internal_overlap.items()):
    print(f"   - '{w}' : {len(occ)+1}회 중복 ({', '.join(occ)})")

