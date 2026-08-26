#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
움직이는그림사전 · 통합 검증기
코다리는 대표님께 보고하기 전에 반드시 이것을 돌리고, 출력을 그대로 붙일 것.
  python3 _작업/검증_전체.py

node --check 는 문법만 본다. 없는 변수를 읽는 오류는 실행해야 드러난다.
그래서 이 검사기가 필요하다.
"""
import io, re, json, subprocess, sys, os

P = 'public/learning/index.html'
FAIL = []
WARN = []

def head(t): print("\n" + "=" * 46 + "\n" + t + "\n" + "=" * 46)

s = io.open(P, encoding='utf-8').read()

# ─────────────────────────────── 1. JS 문법
head("1. JS 문법")
scripts = re.findall(r'<script[^>]*>(.*?)</script>', s, re.S)
for i, sc in enumerate(scripts):
    if not sc.strip(): continue
    io.open('/tmp/_chk.js', 'w', encoding='utf-8').write(sc)
    r = subprocess.run(['node', '--check', '/tmp/_chk.js'], capture_output=True, text=True)
    if r.returncode: FAIL.append("스크립트 #%d 문법오류" % i); print("  ★ #%d\n%s" % (i, r.stderr[:400]))
    else: print("  OK  스크립트 #%d" % i)

# ─────────────────────────────── 2. 미선언 전역 참조  ★오늘 사고
head("2. 미선언 전역 참조  (따옴표 벗겨진 문자열)")
body = scripts[-1]
body = re.sub(r'`(?:[^`\\]|\\.)*`', '``', body)
body = re.sub(r'"(?:[^"\\]|\\.)*"', '""', body)
body = re.sub(r"'(?:[^'\\]|\\.)*'", "''", body)
body = re.sub(r'//[^\n]*', '', body)
body = re.sub(r'/\*.*?\*/', '', body, flags=re.S)
declared = set(re.findall(r'\b(?:var|let|const|function|class)\s+([A-Za-z_$][\w$]*)', body))
BUILTIN = set('''window document console Math JSON Object Array String Number Boolean Date RegExp
Promise Map Set WeakMap Symbol Error parseInt parseFloat isNaN encodeURIComponent decodeURIComponent
setTimeout setInterval clearTimeout clearInterval fetch localStorage sessionStorage location
navigator alert confirm prompt requestAnimationFrame getSelection true false null undefined
this new typeof instanceof in of return if else for while do switch case break continue
function var let const class try catch finally throw delete void yield await async
Infinity NaN globalThis structuredClone URL URLSearchParams Intl'''.split())
# 흔한 오타 후보: CSS 값 / 상태 문자열이 맨몸으로 쓰인 자리
PATTERNS = [
    (r'\.style\.\w+\s*=\s*([A-Za-z_$][\w$]*)\s*;', "style 값"),
    (r'getElementById\(\s*([A-Za-z_$][\w$]*)\s*\)', "getElementById 인자"),
    (r'querySelector(?:All)?\(\s*([A-Za-z_$][\w$]*)\s*\)', "querySelector 인자"),
    (r'===\s*([A-Za-z_$][\w$]*)\s*\)', "=== 비교 대상"),
    (r'classList\.\w+\(\s*([A-Za-z_$][\w$]*)\s*\)', "classList 인자"),
]
found = []
for pat, label in PATTERNS:
    for m in re.finditer(pat, body):
        v = m.group(1)
        if v in declared or v in BUILTIN: continue
        ln = body[:m.start()].count('\n') + 1
        found.append((label, v, ln))
if found:
    for label, v, ln in found:
        FAIL.append("미선언 %s: %s" % (label, v))
        print("  ★ %-18s `%s`  (스크립트 내 %d행)" % (label, v, ln))
    print("\n  → 따옴표가 벗겨졌을 가능성이 큽니다. '%s' 처럼 감싸야 합니다." % found[0][1])
else:
    print("  OK  없음")

# ─────────────────────────────── 3. chapterData 5배열
head("3. chapterData 5배열 길이")
i = s.index('const chapterData = {'); st = s.index('{', i); d = 0
for j in range(st, len(s)):
    if s[j] == '{': d += 1
    elif s[j] == '}':
        d -= 1
        if d == 0: en = j + 1; break
data = json.loads(s[st:en])
bad = 0
for ck in sorted(data, key=int):
    c = data[ck]
    n = len(c['works'])
    for key in ('levelOneWords', 'levelTwoWords', 'levelOneSpots', 'sceneSpots'):
        if len(c.get(key, [])) != n:
            FAIL.append("ch%s %s 길이 %d≠%d" % (ck, key, len(c.get(key, [])), n)); bad += 1
            print("  ★ ch%s %s %d개 (works %d개)" % (ck, key, len(c.get(key, [])), n))
    for k, w in enumerate(c['works']):
        a, b = len(c['levelOneWords'][k]), len(c['levelOneSpots'][k])
        e, f = len(c['levelTwoWords'][k]), len(c['sceneSpots'][k])
        if a != b or e != f:
            FAIL.append("ch%s_%s 단어/좌표 불일치" % (ck, w['n'])); bad += 1
            print("  ★ ch%s_%s  L1 단어%d/좌표%d · L2 단어%d/좌표%d" % (ck, w['n'], a, b, e, f))
        if a == 0:
            WARN.append("ch%s_%s 레벨1 0개" % (ck, w['n']))
if not bad: print("  OK  전 챕터 일치")

# ─────────────────────────────── 4. 단어 중복
head("4. 단어 중복 (같은 챕터 안)")
dup = 0
for ck in sorted(data, key=int):
    seen = {}
    for k, w in enumerate(data[ck]['works']):
        for word, _ in w['words']:
            if word in seen:
                FAIL.append("ch%s %s 중복" % (ck, word)); dup += 1
                print("  ★ ch%s  `%s`  (%s · %s)" % (ck, word, seen[word], w['n']))
            else: seen[word] = w['n']
if not dup: print("  OK  중복 없음")

# ─────────────────────────────── 5. 뜻 빈칸 / 뜻 중복
head("5. 뜻 빈칸 · 뜻 겹침")
blank = 0; mean = {}
for ck in data:
    for w in data[ck]['works']:
        for word, ko in w['words']:
            if not ko.strip(): FAIL.append("%s 뜻 빈칸" % word); blank += 1; print("  ★ %s 뜻이 비었습니다" % word)
            else: mean.setdefault(ko.strip(), set()).add(word)
same = {k: v for k, v in mean.items() if len(v) > 1}
if not blank: print("  OK  빈칸 없음")
for ko, ws in sorted(same.items()):
    WARN.append("뜻 겹침 %s" % ko); print("  · 「%s」 ← %s" % (ko, ', '.join(sorted(ws))))
if not same: print("  OK  겹치는 뜻 없음")

# ─────────────────────────────── 6. 좌표
head("6. 좌표")
r = subprocess.run([sys.executable, '_작업/verify_spots.py'], capture_output=True, text=True)
out = (r.stdout or '') + (r.stderr or '')
for line in out.strip().split('\n')[-6:]: print("  " + line)
if '오류' in out or '배포 금지' in out: FAIL.append("좌표 오류")

# ─────────────────────────────── 7. 영상·포스터 파일
head("7. 영상 / 포스터 파일 존재")
miss = 0
for ck in data:
    for w in data[ck]['works']:
        for key in ('video', 'img'):
            p = os.path.join('public/learning', w[key])
            if not os.path.exists(p):
                FAIL.append("파일 없음 %s" % w[key]); miss += 1
                print("  ★ ch%s_%s  %s" % (ck, w['n'], w[key]))
if not miss: print("  OK  전부 있음")

# ─────────────────────────────── 8. dist 동기화
head("8. dist 동기화")
D = 'dist/learning/index.html'
if not os.path.exists(D): FAIL.append("dist 없음"); print("  ★ dist/learning/index.html 이 없습니다")
elif io.open(D, encoding='utf-8').read() != s:
    FAIL.append("dist 불일치")
    print("  ★ public 과 dist 가 다릅니다  →  cp %s %s" % (P, D))
else: print("  OK  동일")

# ─────────────────────────────── 결과
head("결과")
tot = sum(len(c['works']) for c in data.values())
wds = sum(len(w['words']) for c in data.values() for w in c['works'])
print("  총 %d편 / 단어 %d개" % (tot, wds))
print("  챕터별: " + " · ".join("ch%s %d편" % (k, len(data[k]['works'])) for k in sorted(data, key=int)))
if WARN:
    print("\n  살펴볼 것 %d건" % len(WARN))
    for w in WARN[:12]: print("    · " + w)
    if len(WARN) > 12: print("    · ... 외 %d건" % (len(WARN) - 12))
if FAIL:
    print("\n  ★★ 고쳐야 할 것 %d건 — 배포하지 마십시오 ★★" % len(FAIL))
    for f in FAIL[:20]: print("    ★ " + f)
    sys.exit(1)
print("\n  ✅ 전 항목 통과 — 배포 가능")
