# -*- coding: utf-8 -*-
import io, json

all_1200 = set(io.open("_작업/all1200.txt", encoding="utf-8").read().split())
s = io.open("public/learning/index.html", encoding="utf-8").read()
i = s.index("const chapterData = {"); st = s.index("{", i); d = 0
for j in range(st, len(s)):
    if s[j] == "{": d += 1
    elif s[j] == "}":
        d -= 1
        if d == 0: en = j + 1; break
data = json.loads(s[st:en])
used_words = {a for ch in data for w in data[ch]["works"] for a, b in w["words"]}
free_words = all_1200 - used_words

cats = json.load(io.open("_작업/1200_분류.json", encoding="utf-8"))["갈래"]

print("가용 단어 카테고리별 검색:")
for cat_name in ["만들고 고치기", "크기와 모양", "집의 구조", "살림 도구", "동물", "식물과 나무", "시간과 때", "몸과 감각", "가고 오기", "갖고 지니기", "돕고 섬기기", "하고 다루기", "많고 적음", "같고 다름"]:
    avail = [w for w in cats.get(cat_name, []) if w in free_words]
    print(f"[{cat_name}]: {', '.join(avail)}")

