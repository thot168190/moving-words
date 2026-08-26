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

# 1~10번 기준 사용 단어
used_1_10 = {a for ch in data for w in (data[ch]["works"][:10] if ch=="3" else data[ch]["works"]) for a, b in w["words"]}
free = all_1200 - used_1_10

test_words = [
    # 15 새집
    "frame", "stuff", "piece", "pole", "site", "settle", "survive", "found", "establish", "exist", "stay", "rest", "shelter", "protect",
    # 17 압화틀
    "block", "link", "pair", "tight", "bind", "shut", "constant", "fit", "press", "hold", "keep", "maintain",
    # 19 온실
    "district", "range", "extend", "limit", "raise", "equal", "maintain", "pure", "calm", "safe", "grow"
]

print("단어 상태 검사:")
for tw in test_words:
    print(f"{tw:12s}: {'✅ 가용' if tw in free else '❌ 불가'}")

