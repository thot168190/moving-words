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

# 10개 정원 씬에 적합한 후보 단어들 필터링
pool = sorted(list(free_words))
print(f"가용 1200 단어 수: {len(pool)}개")

# 정원 관련 가용 단어 매핑 검토
candidates = [
    # 모양/크기/형태
    "shape", "unit", "cell", "triangle", "volume", "blank", "empty", "square", "single", "section", "item", "piece",
    "bunch", "content", "mass", "grand", "block", "link", "wide", "handle", "motion", "step", "district", "pole", "pot",
    # 동작/상태/성질
    "alive", "breathe", "create", "exist", "develop", "stable", "steady", "dig", "operate", "repair", "direct",
    "combine", "contain", "remain", "defense", "bend", "divide", "remove", "snap", "settle", "survive", "plenty",
    "period", "bind", "shut", "constant", "roll", "drag", "force", "shift", "raise", "equal", "maintain",
    "annual", "continue", "regular", "bloom", "feed", "nest", "fur", "species", "seed", "drop", "smooth"
]

print("\n후보 단어 상태:")
for c in candidates:
    if c in free_words:
        print(f"  ✅ {c}: 가용")
    else:
        print(f"  ❌ {c}: 이미 사용됨 또는 1200에 없음")

