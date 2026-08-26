# -*- coding: utf-8 -*-
import io, json

all_1200 = set(io.open("_작업/all1200.txt", encoding="utf-8").read().split())

# 13개 기준 사용 단어
s = io.open("public/learning/index.html", encoding="utf-8").read()
i = s.index("const chapterData = {"); st = s.index("{", i); d = 0
for j in range(st, len(s)):
    if s[j] == "{": d += 1
    elif s[j] == "}":
        d -= 1
        if d == 0: en = j + 1; break
data = json.loads(s[st:en])
used_words = {a for ch in data for w in data[ch]["works"] for a, b in w["words"]}
free_words = sorted(list(all_1200 - used_words))

# 1200_분류.json 에서 갈래별로 free_words 분류
cats = json.load(io.open("_작업/1200_분류.json", encoding="utf-8"))["갈래"]

print(f"총 미사용 단어: {len(free_words)}개\n")
for cat_name, words in cats.items():
    avail = [w for w in words if w in free_words]
    if avail:
        print(f"[{cat_name}] ({len(avail)}개): {', '.join(avail)}")

