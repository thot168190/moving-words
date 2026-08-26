# -*- coding: utf-8 -*-
import json, os, re

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    master_100 = json.load(f)

# all1200.txt
all_words = set()
with open("_작업/all1200.txt", "r", encoding="utf-8") as f:
    for line in f:
        w = line.strip().lower()
        if w: all_words.add(w)

master_words = set()
for s in master_100:
    for p in s["prompts"]:
        for w in p["words"]:
            master_words.add(w.lower())

print(f"전체 1200 단어장 총 단어: {len(all_words)}개")
print(f"현재 100편 마스터(Set 04~13)에 배치된 단어: {len(master_words)}개")

# Set 12, 13에 배정된 단어
set12_words = [w for p in master_100[8]["prompts"] for w in p["words"]]
set13_words = [w for p in master_100[9]["prompts"] for w in p["words"]]

print(f"Set 12 (음악과 소리 10편) 단어: {len(set12_words)}개 -> {set12_words[:10]}...")
print(f"Set 13 (사회와 제도 10편) 단어: {len(set13_words)}개 -> {set13_words[:10]}...")

