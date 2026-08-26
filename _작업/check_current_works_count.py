# -*- coding: utf-8 -*-
import io, json, os

SRC = "public/learning/index.html"
s = io.open(SRC, encoding="utf-8").read()
i = s.index("const chapterData = {"); st = s.index("{", i); d = 0
for j in range(st, len(s)):
    if s[j] == "{": d += 1
    elif s[j] == "}":
        d -= 1
        if d == 0: en = j + 1; break

data = json.loads(s[st:en])
print("=== chapterData 내 챕터별 기존 작품(works) 현황 ===")
for ch_id in sorted(data.keys(), key=lambda x: int(x)):
    works = data[ch_id]["works"]
    print(f"ch{ch_id} ({data[ch_id].get('title', '')}) : {len(works)}개 작품 등록됨")
    for w in works:
        print(f"   └─ n: {w['n']}, video: {w.get('video')}, img: {w.get('img')}")

