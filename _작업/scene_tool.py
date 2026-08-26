#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
장면 매칭·주입 도구 — 로부장 발행 2026-08-21
영상이 나온 뒤 단어를 붙이고 사이트에 넣는 전 과정을 이 파일 하나로 처리한다.
코덱스·코다리 공통. 워크스페이스 루트에서 실행할 것.

  python3 _작업/scene_tool.py remain 8              # ch8에 남은 단어를 갈래별로 본다
  python3 _작업/scene_tool.py remain 8 --words      # 단어만 한 줄로 (복사용)
  python3 _작업/scene_tool.py free                  # 어느 챕터에도 안 들어간 갈래
  python3 _작업/scene_tool.py check 새편.json       # 넣기 전 검사 (필수)
  python3 _작업/scene_tool.py add   새편.json       # 실제 주입 (5배열 자동)
  python3 _작업/scene_tool.py verify               # 전체 무결성 재검사

새 편 JSON 형식 — 좌표를 단어에 붙여 쓴다. 순서가 어긋날 수 없다.
{
  "chapter": 8,
  "n": "05",
  "title": "항구의 새벽",
  "sub": "배가 들어오는 시간",
  "video": "ch8/ch8_05.mp4",
  "img":   "ch8/ch8_05-poster.jpg",
  "levelOne": [ ["dock","부두",[35,62]], ["cargo","화물",[62,58]],
                ["crew","선원",[48,74]], ["harbor","항구",[22,40]] ],
  "levelTwo": [ ["anchor","닻",[70,55]], ["rope","밧줄",[58,80]],
                ["deck","갑판",[44,52]], ["tide","조수",[80,72]] ]
}
  · levelOne 은 4개. 퀴즈에 쓰인다 (코드가 slice(0,4))
  · levelTwo 는 나머지. 편당 합계 8~12개를 권장
  · 좌표는 [가로%, 세로%] · 8~92 범위 · 같은 레벨 안 거리 18 이상
"""
import io, json, csv, os, re, sys, math
from collections import defaultdict, Counter

ROOT = os.getcwd()
SRC  = os.path.join(ROOT, "public/learning/index.html")
DIST = os.path.join(ROOT, "dist/learning/index.html")
ALL  = os.path.join(ROOT, "_작업/all1200.txt")
TAG  = os.path.join(ROOT, "_작업/1200_레벨태그_v3.csv")
NM = {1:"INVENTIO 세상을 발견해요",2:"VITA 숲과 생명",3:"DOMUS 우리 집",4:"SCHOLA 학교생활",
      5:"URBS 도시와 교통",6:"SALUS 음식과 건강",7:"SENSUS 몸과 감정",8:"MOTUS 운동과 도전",
      9:"MUNDUS 여행과 세계",10:"TERRA 지구와 날씨",11:"COSMOS 우주와 과학",12:"SOMNIUM 밤과 꿈"}

def load():
    s = io.open(SRC, encoding="utf-8").read()
    i = s.index("const chapterData = {"); st = s.index("{", i); d = 0
    for j in range(st, len(s)):
        if s[j] == "{": d += 1
        elif s[j] == "}":
            d -= 1
            if d == 0: en = j + 1; break
    return s, st, en, json.loads(s[st:en])

def used(data):
    return {a: "ch%s-%s" % (ch, w["n"]) for ch in data for w in data[ch]["works"] for a, b in w["words"]}

def meanings(data):
    return {b: a for ch in data for w in data[ch]["works"] for a, b in w["words"]}

def tags():
    if not os.path.exists(TAG): return {}, defaultdict(list)
    rows = list(csv.DictReader(io.open(TAG, encoding="utf-8")))
    g = {r["단어"]: r["갈래"] for r in rows}
    byg = defaultdict(list)
    for r in rows: byg[r["갈래"]].append(r["단어"])
    return g, byg

def owners(data, G):
    c = defaultdict(Counter)
    for ch in data:
        for w in data[ch]["works"]:
            for a, b in w["words"]:
                if a in G: c[G[a]][ch] += 1
    return {g: cc.most_common(1)[0][0] for g, cc in c.items()}

def dist(p, q): return math.hypot(p[0]-q[0], p[1]-q[1])

# ── remain ────────────────────────────────────────────────────────
def cmd_remain(ch, words_only=False):
    _,_,_, data = load(); U = used(data); G, byg = tags(); OWN = owners(data, G)
    pool = []
    for g, ws in byg.items():
        if OWN.get(g) != str(ch): continue
        left = [w for w in ws if w not in U]
        if left: pool.append((g, left))
    if words_only:
        print(" ".join(w for _, ws in pool for w in ws)); return
    tot = sum(len(w) for _, w in pool)
    print("ch%d %s — 현재 %d편 · 남은 단어 %d개" % (ch, NM.get(ch,""), len(data[str(ch)]["works"]), tot))
    print("편당 8개면 +%d편 · 편당 12개면 +%d편\n" % (-(-tot//8), -(-tot//12)))
    for g, ws in sorted(pool, key=lambda x: -len(x[1])):
        print("  [%s] %d개" % (g, len(ws)))
        for i in range(0, len(ws), 10): print("     " + ", ".join(ws[i:i+10]))
    if not pool: print("  남은 단어 없음 — 갈래 재배정이 필요하다")

def cmd_free():
    _,_,_, data = load(); U = used(data); G, byg = tags(); OWN = owners(data, G)
    print("=== 어느 챕터에도 배정 안 된 갈래 (새 챕터 후보) ===")
    tot = 0
    for g, ws in sorted(byg.items(), key=lambda x: -len(x[1])):
        if g in OWN: continue
        left = [w for w in ws if w not in U]
        if not left: continue
        tot += len(left)
        print("  [%s] %d개" % (g, len(left)))
        for i in range(0, len(left), 10): print("     " + ", ".join(left[i:i+10]))
    print("\n합계 %d개" % tot)

# ── check ─────────────────────────────────────────────────────────
def cmd_check(path, quiet=False):
    spec = json.load(io.open(path, encoding="utf-8"))
    _,_,_, data = load(); U = used(data); M = meanings(data)
    A = set(io.open(ALL, encoding="utf-8").read().split()) if os.path.exists(ALL) else set()
    errs, warns = [], []
    ch = str(spec["chapter"]); n = spec["n"]
    tag = "ch%s-%s" % (ch, n)

    if ch not in data: errs.append("챕터 %s 가 chapterData에 없다" % ch)
    elif any(w["n"] == n for w in data[ch]["works"]): errs.append("%s 는 이미 있다" % tag)

    for k in ("chapter","n","title","sub","video","img","levelOne","levelTwo"):
        if k not in spec: errs.append("키 '%s' 없음" % k)
    if errs and not quiet:
        pass

    l1, l2 = spec.get("levelOne", []), spec.get("levelTwo", [])
    if len(l1) != 4: warns.append("levelOne %d개 — 퀴즈가 4개를 쓴다. 4개 권장" % len(l1))
    allw = l1 + l2
    if not (6 <= len(allw) <= 14): warns.append("단어 %d개 — 8~12개 권장" % len(allw))

    seen_w, seen_m = {}, {}
    for lv, arr in (("levelOne", l1), ("levelTwo", l2)):
        for it in arr:
            if not (isinstance(it, list) and len(it) == 3):
                errs.append("%s 항목 형식 오류 %s — [\"영어\",\"뜻\",[x,y]] 여야 한다" % (lv, it)); continue
            w, m, sp = it
            if not w or not str(w).strip(): errs.append("%s 빈 단어" % lv)
            if not m or not str(m).strip(): errs.append("'%s' 뜻이 비었다" % w)
            if A and w not in A: errs.append("'%s' 정본 1200에 없다" % w)
            if w in U: errs.append("'%s' 이미 %s 에 쓰였다" % (w, U[w]))
            if w in seen_w: errs.append("'%s' 이 편 안에서 중복" % w)
            seen_w[w] = lv
            if m in M: errs.append("뜻 '%s' 는 이미 '%s' 가 쓰고 있다" % (m, M[m]))
            if m in seen_m: errs.append("뜻 '%s' 가 이 편 안에서 중복 (%s, %s)" % (m, seen_m[m], w))
            seen_m[m] = w
            if not (isinstance(sp, list) and len(sp) == 2): errs.append("'%s' 좌표 형식 오류 %s" % (w, sp)); continue
            x, y = sp
            if not (8 <= x <= 92 and 8 <= y <= 92): errs.append("'%s' 좌표 [%s,%s] 범위 밖 (8~92)" % (w, x, y))
            if len(str(m)) > 9: warns.append("뜻 '%s' 가 길다 — 화면에서 겹치기 쉽다" % m)

    for lv, arr in (("levelOne", l1), ("levelTwo", l2)):
        ok = [it for it in arr if isinstance(it, list) and len(it) == 3 and isinstance(it[2], list) and len(it[2]) == 2]
        for a in range(len(ok)):
            for b in range(a+1, len(ok)):
                d = dist(ok[a][2], ok[b][2])
                if d < 18: errs.append("%s '%s'·'%s' 거리 %.1f < 18 (글자가 포갠다)" % (lv, ok[a][0], ok[b][0], d))
        xs = [it[2][0] for it in ok]; ys = [it[2][1] for it in ok]
        if len(ok) >= 4:
            sym = sum(1 for a in range(len(ok)) for b in range(a+1,len(ok))
                      if ok[a][2][0]+ok[b][2][0] == 100 and abs(ok[a][2][1]-ok[b][2][1]) <= 2)
            if sym >= 2: errs.append("%s 좌우대칭 %d쌍 — 그림을 안 보고 찍은 값이다" % (lv, sym))
            if len(set(xs)) <= 2: errs.append("%s x값이 %d종뿐 — 격자다" % (lv, len(set(xs))))
            if len(set(ys)) <= 2: errs.append("%s y값이 %d종뿐 — 격자다" % (lv, len(set(ys))))

    for k in ("video", "img"):
        v = spec.get(k, "")
        p = os.path.join(ROOT, "public/learning", v)
        if not os.path.exists(p): errs.append("%s 파일 없음: public/learning/%s" % (k, v))
        if re.search(r'[^\x20-\x7e]|\s', v): errs.append("%s 파일명에 공백·특수문자 — 배포에서 누락된다: %s" % (k, v))

    if not quiet:
        print("── %s %s ──" % (tag, spec.get("title","")))
        print("   단어 %d개 (L1 %d · L2 %d)" % (len(allw), len(l1), len(l2)))
        for w in warns: print("   ! " + w)
        if errs:
            print("   ★★ 오류 %d건 — 주입하지 마라" % len(errs))
            for e in errs: print("      ★ " + e)
        else:
            print("   ✅ 통과 — add 로 주입 가능")
    return errs

# ── add ───────────────────────────────────────────────────────────
def cmd_add(path):
    if cmd_check(path, quiet=True):
        print("★ check 를 먼저 통과시켜라:  python3 _작업/scene_tool.py check %s" % path); sys.exit(1)
    spec = json.load(io.open(path, encoding="utf-8"))
    s, st, en, data = load()
    ch = str(spec["chapter"]); v = data[ch]
    l1, l2 = spec["levelOne"], spec["levelTwo"]
    v["works"].append({"n": spec["n"], "title": spec["title"], "sub": spec["sub"],
                       "video": spec["video"], "img": spec["img"],
                       "words": [[w, m] for w, m, _ in l1 + l2]})
    v["levelOneWords"].append([[w, m] for w, m, _ in l1])
    v["levelTwoWords"].append([[w, m] for w, m, _ in l2])
    v["levelOneSpots"].append([sp for _, _, sp in l1])
    v["sceneSpots"].append([sp for _, _, sp in l2])
    out = s[:st] + json.dumps(data, ensure_ascii=False, indent=2) + s[en:]
    io.open("/tmp/_new.html", "w", encoding="utf-8").write(out)
    io.open(SRC, "w", encoding="utf-8").write(out)
    if os.path.exists(os.path.dirname(DIST)):
        io.open(DIST, "w", encoding="utf-8").write(out)
    print("✅ ch%s-%s 주입 완료 · public %s dist 동기화" % (ch, spec["n"], "및 " if os.path.exists(os.path.dirname(DIST)) else "만 (dist 없음) "))
    cmd_verify()

# ── verify ────────────────────────────────────────────────────────
def cmd_verify():
    _,_,_, data = load()
    A = set(io.open(ALL, encoding="utf-8").read().split()) if os.path.exists(ALL) else set()
    errs = []; works = 0; wcnt = 0; U = set()
    for ch in sorted(data, key=int):
        v = data[ch]
        L = [len(v[k]) for k in ("works","levelOneWords","levelTwoWords","sceneSpots","levelOneSpots")]
        if len(set(L)) != 1: errs.append("ch%s 5배열 길이 불일치 %s" % (ch, L)); continue
        for k, w in enumerate(v["works"]):
            works += 1; tag = "ch%s-%s" % (ch, w["n"])
            n1, n2 = len(v["levelOneWords"][k]), len(v["levelTwoWords"][k])
            s1, s2 = len(v["levelOneSpots"][k]), len(v["sceneSpots"][k])
            wcnt += len(w["words"])
            for a, b in w["words"]:
                U.add(a)
                if not b.strip(): errs.append("%s '%s' 뜻 빈칸" % (tag, a))
            if n1 + n2 != len(w["words"]): errs.append("%s words≠L1+L2" % tag)
            if s1 < n1 or s2 < n2: errs.append("%s 좌표 부족 — 이 편이 안 열린다" % tag)
            seen = {}
            for a, b in w["words"]:
                if b in seen: errs.append("%s 뜻 중복 '%s'" % (tag, b))
                seen[b] = a
    print("총 %d편 / 단어 %d개 / 편당 %.1f · 정본 소화 %d/1200 (남은 %d)" % (
        works, wcnt, wcnt/max(works,1), len(U & A), len(A - U)))
    if errs:
        print("★★ 오류 %d건" % len(errs))
        for e in errs[:40]: print("   ★ " + e)
        sys.exit(1)
    print("✅ 무결성 통과")

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(0)
    c = a[0]
    if   c == "remain": cmd_remain(int(a[1]), "--words" in a)
    elif c == "free":   cmd_free()
    elif c == "check":  sys.exit(1 if cmd_check(a[1]) else 0)
    elif c == "add":    cmd_add(a[1])
    elif c == "verify": cmd_verify()
    else: print(__doc__)
