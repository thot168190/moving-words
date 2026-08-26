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
used_meanings = {b for ch in data for w in data[ch]["works"] for a, b in w["words"]}

# ch2_14 단어 빼고 계산
if "2" in data and len(data["2"]["works"]) >= 14:
    for a, b in data["2"]["works"][13]["words"]:
        used_words.discard(a)
        used_meanings.discard(b)

free_words = all_1200 - used_words

candidates = ["dirt", "single", "cell", "shape", "alive", "breathe", "exist", "create", "grow", "green", "stem", "seed", "sprout", "plant", "root", "pure", "nature", "fresh"]
print("후보 단어 가용 여부:")
for c in candidates:
    if c in free_words:
        print(f"✅ {c}: 가용")
    else:
        print(f"❌ {c}: 사용불가 (1200에 없거나 이미 사용됨)")

