# -*- coding: utf-8 -*-
import json, os, re

# 1. 100편 마스터 데이터 내 세트 확인
with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    master_100 = json.load(f)

print(f"=== 1. 현재 100편 마스터 DB 내 세트 목록 (총 {len(master_100)}개 세트) ===")
for s in master_100:
    print(f"- {s['set_id']}: {s['set_name']} ({len(s['prompts'])}편)")

# 2. 52편 로드맵 확인
roadmap_path = "/Users/mihyunlee/Downloads/코다리_지시서_20260825_52편로드맵.md"
if os.path.exists(roadmap_path):
    with open(roadmap_path, "r", encoding="utf-8") as f:
        rm_text = f.read()
    print("\n=== 2. 52편 로드맵 문서 요약 ===")
    lines = [line.strip() for line in rm_text.splitlines() if line.strip().startswith("#") or "편" in line][:15]
    for l in lines:
        print(l)

# 3. 전체 1200단어 및 사용 현황
with open("_작업/all1200.txt", "r", encoding="utf-8") as f:
    all_words = set([w.strip().lower() for w in f if w.strip()])

# 기존 406단어
existing_words = set()
with open("_작업/existing_406_words.txt", "r", encoding="utf-8") as f:
    existing_words = set([w.strip().lower() for w in f if w.strip()])

# 이번 100편에 배정된 단어
master_words = set()
for s in master_100:
    for p in s["prompts"]:
        for w in p["words"]:
            master_words.add(w.lower())

covered = existing_words | master_words
remaining_words = all_words - covered

print(f"\n=== 3. 전체 1200단어장 커버리지 현황 ===")
print(f"- 전체 목표 단어: {len(all_words)}개")
print(f"- 기존 기제작 단어: {len(existing_words)}개")
print(f"- 이번 100편(Set 04~13) 단어: {len(master_words)}개")
print(f"- 현재 확보/배정 완료 총 단어: {len(covered)}개 (전체 대비 {len(covered)/len(all_words)*100:.1f}%)")
print(f"- 100편 완주 후 남는 잔여 미배정 단어: {len(remaining_words)}개")

