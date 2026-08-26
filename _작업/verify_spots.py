#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
좌표·단어 검증 스크립트 — 로부장 발행 2026-08-21
사용법:  python3 verify_spots.py public/learning/index.html
배포 전에 반드시 통과해야 한다. 하나라도 ★가 뜨면 배포 금지.
"""
import io, json, re, sys, math

SRC = sys.argv[1] if len(sys.argv) > 1 else "public/learning/index.html"
D1 = [[20,20],[80,20],[20,80],[80,80]]
D2 = [[30,30],[70,30],[30,70],[70,70]]
MIN_XY, MAX_XY = 8, 92      # 가장자리 여백
MIN_DIST = 18               # 두 단어 사이 최소 거리

s = io.open(SRC, encoding="utf-8").read()
i = s.index("const chapterData = {"); st = s.index("{", i); d = 0
for j in range(st, len(s)):
    if s[j] == "{": d += 1
    elif s[j] == "}":
        d -= 1
        if d == 0: en = j + 1; break
data = json.loads(s[st:en])

err = []; warn = []
tot_works = 0; tot_words = 0; still_default = 0

def dist(p, q):
    return math.hypot(p[0]-q[0], p[1]-q[1])

for ch in sorted(data, key=int):
    v = data[ch]
    L = [len(v[k]) for k in ("works","levelOneWords","levelTwoWords","sceneSpots","levelOneSpots")]
    if len(set(L)) != 1:
        err.append("ch%s 5배열 길이 불일치 %s" % (ch, L))
        continue
    for k, w in enumerate(v["works"]):
        tot_works += 1
        tag = "ch%s-%s" % (ch, w["n"])
        words = w["words"]; l1 = v["levelOneWords"][k]; l2 = v["levelTwoWords"][k]
        s1 = v["levelOneSpots"][k]; s2 = v["sceneSpots"][k]
        tot_words += len(words)

        # 1) 개수 일치 — 이게 어긋나면 페이지가 죽는다
        if len(l1) + len(l2) != len(words):
            err.append("%s words %d ≠ L1 %d + L2 %d" % (tag, len(words), len(l1), len(l2)))
        if len(s1) < len(l1):
            err.append("%s levelOneSpots %d < levelOneWords %d  (좌표 부족 → 페이지 죽음)" % (tag, len(s1), len(l1)))
        if len(s2) < len(l2):
            err.append("%s sceneSpots %d < levelTwoWords %d  (좌표 부족 → 페이지 죽음)" % (tag, len(s2), len(l2)))

        # 2) 기본값 좌표가 남아있나
        if s1 == D1 or s2 == D2:
            still_default += 1
            err.append("%s 기본값 좌표 그대로 (그림 안 보고 찍은 값)" % tag)

        # 2-B) 기본값의 변종 — 좌우대칭·격자 패턴 탐지
        #  2026-08-21 추가. [[18,18],[82,18],[20,78],[80,80]] 처럼 숫자만 살짝 비튼 것을
        #  1)번 검사가 못 잡아 8편이 빠져나갔다. 그림을 보고 찍으면 이런 모양이 안 나온다.
        def synthetic(sp):
            n = len(sp)
            if n < 3: return None
            sym = sum(1 for a in range(n) for b in range(a+1, n)
                      if sp[a][0] + sp[b][0] == 100 and abs(sp[a][1] - sp[b][1]) <= 2)
            if sym >= 2: return "좌우대칭 %d쌍" % sym
            xs = set(p[0] for p in sp); ys = set(p[1] for p in sp)
            if len(xs) <= 2 and n >= 4: return "x값이 %d종뿐" % len(xs)
            if len(ys) <= 2 and n >= 4: return "y값이 %d종뿐" % len(ys)
            return None
        for name, sp in (("levelOneSpots", s1), ("sceneSpots", s2)):
            r = synthetic(sp)
            if r:
                still_default += 1
                err.append("%s %s %s — 그림 안 보고 만든 값으로 보인다 %s" % (tag, name, r, sp))

        # 3) 범위
        for name, sp in (("levelOneSpots", s1), ("sceneSpots", s2)):
            for idx, p in enumerate(sp):
                if not (isinstance(p, list) and len(p) == 2):
                    err.append("%s %s[%d] 형식 오류 %s" % (tag, name, idx, p)); continue
                x, y = p
                if not (MIN_XY <= x <= MAX_XY and MIN_XY <= y <= MAX_XY):
                    err.append("%s %s[%d] = [%s,%s] 범위 밖 (%d~%d)" % (tag, name, idx, x, y, MIN_XY, MAX_XY))

        # 4) 겹침 — 실제로 쓰이는 좌표끼리만 본다
        for name, sp, nw in (("levelOneSpots", s1, len(l1)), ("sceneSpots", s2, len(l2))):
            live = sp[:nw]
            for a in range(len(live)):
                for b in range(a+1, len(live)):
                    dd = dist(live[a], live[b])
                    if dd < MIN_DIST:
                        err.append("%s %s[%d]·[%d] 거리 %.1f < %d (단어가 포갬)" % (tag, name, a, b, dd, MIN_DIST))

        # 5) L1 · L2 사이 겹침은 경고만 (레벨이 달라 동시에 안 뜬다)
        for a in range(len(l1)):
            for b in range(len(l2)):
                if dist(s1[a], s2[b]) < 10:
                    warn.append("%s L1[%d]·L2[%d] 매우 가까움" % (tag, a, b))

        # 6) 빈 뜻
        for a, b in words:
            if not b.strip():
                err.append("%s '%s' 뜻 빈칸" % (tag, a))

        # 7) 같은 편 안 뜻 중복
        seen = {}
        for a, b in words:
            if b in seen: err.append("%s 뜻 중복 '%s' ← %s, %s" % (tag, b, seen[b], a))
            seen[b] = a

# 8) 정본 대조
try:
    A = set(io.open("_작업/all1200.txt", encoding="utf-8").read().split())
    U = set(a for ch in data for w in data[ch]["works"] for a, b in w["words"])
    outside = sorted(U - A)
    KNOWN = {'animal','bank','car','catch','drive','drop','fast','fun','grass','graze','herd','high',
             'insect','jump','neck','park','play','pond','sky','speed','splash','steer','stripe','tail',
             'thrill','track','tree','water'}
    new_outside = [w for w in outside if w not in KNOWN]
    if new_outside:
        err.append("정본 1200에 없는 새 단어: %s" % ", ".join(new_outside))
    print("정본 소화: %d / 1200   (남은 %d개)" % (len(U & A), len(A - U)))
except FileNotFoundError:
    warn.append("_작업/all1200.txt 없음 — 정본 대조 건너뜀")

print("총 %d편 / 단어 %d개 / 편당 평균 %.1f" % (tot_works, tot_words, tot_words / max(tot_works, 1)))
print("기본값 좌표 잔존: %d편" % still_default)
print()
if warn:
    print("── 경고 %d건 (배포는 가능) ──" % len(warn))
    for x in warn[:20]: print("   ·", x)
    if len(warn) > 20: print("   … 외 %d건" % (len(warn)-20))
    print()
if err:
    print("★★ 오류 %d건 — 배포 금지 ★★" % len(err))
    for x in err[:60]: print("   ★", x)
    if len(err) > 60: print("   … 외 %d건" % (len(err)-60))
    sys.exit(1)
print("✅ 전 항목 통과 — 배포 가능")
