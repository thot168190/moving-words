#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
프롬프트 정본 검증기 — 로부장 발행 2026-08-21
Flow에 넣기 전에 반드시 통과시킬 것. ★가 하나라도 뜨면 뽑지 마라.

사용법:
    python3 verify_prompt.py 파일.txt          # 파일 하나
    python3 verify_prompt.py 허브.html         # HTML 안 프롬프트 전부
    echo "프롬프트" | python3 verify_prompt.py  # 붙여넣기

정본 두 계열:
  WOW  = 산호협곡 (scene-ch1-08)  · _작업/01_지시서/프롬프트_공식_잠금.md §2
  CALM = 망원경 line-reveal       · _작업/성공문법_정본_line-reveal_20260809.md §1
"""
import io, re, sys, os

# ── 손을 부르는 지뢰 (단, 연필선/스케치 표현 제외) ────────────────────
MINES = {
    "hand": "손을 직접 소환. 'never two hands'도 손을 부른다",
    "hands": "위와 동일",
    "pen": "펜 든 손을 소환",
    "brush": "붓 든 손을 소환",
    "artist": "사람을 소환",
    "tool": "'drawing tools' 형태로 손을 소환",
    "tools": "위와 동일",
    "wrist": "손목 = 손",
    "finger": "손가락 = 손",
    "arm": "팔 = 손",
    "draws itself": "손을 소환 (검증된 실패)",
    "by itself": "draws itself 계열. 손을 소환",
    "spreading": "붓질 동사. 붓·손·종이질감을 부른다",
    "whiteboard": "화이트보드라는 물건이 생겨 액자가 된다",
    "desk": "책상이 생긴다",
}
# ── 잠금 파일 §5 금지어 ────────────────────────────────────────────
BANNED = {
    "paper": "액자·종이질감 유발", "cream": "액자 유발", "parchment": "액자 유발",
    "canvas": "액자 유발", "border": "테두리 유발",
    "cloud": "곰팡이 유발", "fluffy": "곰팡이 유발", "billowing": "곰팡이 유발",
    "seen from above": "조감도 유발", "bird's-eye": "조감도 유발",
    "aerial": "조감도 유발", "top-down": "조감도 유발",
    "handwritten": "글자 유발", "numerals": "글자 유발", "illegible": "글자 유발",
    "children's picture-book": "유치함 유발", "uncluttered": "기획서 v0.1 금지",
    "cartoon": "화풍 이탈", "sepia": "화풍 이탈",
    "16:9": "비율은 Flow UI에서", "9:16": "비율은 Flow UI에서",
}
WARN_ONLY = {
    "smoke": "곰팡이가 되기 쉽다. 피사체로 쓸 거면 형태를 못박을 것",
    "text": "글자 유발. 'texture'가 아닌 단독 text인지 확인",
    "3d": "화풍 이탈",
    "photorealism": "화풍 이탈",
}

WOW = [
 ("solid pure bright white background (#FFFFFF), edge to edge", "배경 — 종이·액자·크림색을 막는다"),
 ("The very first frame is an entirely empty pure white field", "첫 프레임 — 이미 그려진 채 시작하는 것을 막는다"),
 ("Static locked-off camera, one continuous 8-second take", "카메라 — 줌·팬·컷을 막는다"),
 ("The only visible subjects throughout the sequence are", "★요소 한정 — 손·인물·소품 난입을 막는 핵심 장치"),
 ("fine dark-charcoal ink strokes are visibly traced from one endpoint to the other", "먹선 — 페이드인을 막는다"),
 ("Each individual stroke has a clear beginning and ending", "먹선 — 뭉개진 선을 막는다"),
 ("built progressively rather than fading into view", "먹선 — 페이드인 이중 방어"),
 ("transparent watercolor develops in layered depth", "수채 — 물감 뭉갬을 막는다"),
 ("a narrow untouched white rim", "주역이 배경에 묻히는 것을 막는다"),
 ("There is no visible", "배제 — 그 장면 고유의 오답 하나만"),
 ("Strong foreground, middle-ground and distant layers", "깊이 — 납작한 그림을 막는다"),
 ("Style: intricate natural-history engraving, luminous transparent watercolor", "스타일 꼬리 — 한 글자도 바꾸지 않는다"),
 ("cinematic depth, graceful realistic motion, sophisticated museum-quality editorial illustration", "스타일 꼬리 후반"),
]

DICT = [
    ("Progressive hand-drawn picture-dictionary animation on a completely flat, solid pure-white background (#FFFFFF), edge to edge.", "헤더"),
    ("The first frame is entirely empty white", "첫 프레임"),
    ("The illustration is centered with generous untouched white space", "구도"),
    ("Static locked-off camera, one continuous 8-second take.", "카메라"),
    ("0-4s: ultra-fine warm sepia-grey pencil lines are actively traced stroke by stroke", "연필선"),
    ("4-8s: transparent watercolor develops gradually in a few small flat patches", "수채"),
    ("Final style: simple Korean children’s picture-dictionary illustration", "스타일 — 꼬리"),
    ("No cinematic lighting. No studio lighting.", "배제"),
    ("Completely silent.", "무음"),
]


PENCIL = [
    ("Progressive detailed fine-pencil construction, transparent watercolor and gentle object-motion animation on a solid pure bright white background (#FFFFFF), edge to edge.", "헤더"),
    ("The first frame is an entirely empty pure white field.", "첫 프레임"),
    ("Static locked-off camera, one continuous 8-second take.", "카메라"),
    ("0-3.5s: exceptionally fine pale-neutral 2H graphite strokes are visibly traced one by one", "2H연필선"),
    ("3.5-5.5s: clear transparent watercolor develops in layered color.", "수채"),
    ("5.5-8s:", "모션"),
    ("Style: intricate premium pencil-and-watercolor plate", "스타일 — 꼬리"),
    ("Completely silent.", "무음"),
]

CALM = [
 ("Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge", "헤더"),
 ("The very first frame is an entirely empty pure white field", "첫 프레임"),
 ("High-key lighting", "조명"),
 ("The main illustration is centered and occupies the central three-quarters of the frame", "구도"),
 ("with equal narrow breathing margins on the left and right", "구도 — 좌우 여백"),
 ("Static locked-off camera, one continuous 8-second take", "카메라"),
 ("The only visible subjects throughout the sequence are", "★요소 한정"),
 ("progressively from the empty white field", "선"),
 ("Every detail becomes visible sequentially, never all at once", "순서"),
 ("an extremely pale, water-heavy watercolor wash develops gently", "채색"),
 ("All color remains low-saturation and transparent, with white showing through every wash", "채색 — 농도"),
 ("No area becomes dark, dense or fully filled", "채색 — 어두워짐 방지"),
 ("The restrained palette is", "팔레트"),
 ("All other elements remain still", "움직임 — 나머지는 정지"),
]

def check(name, p):
    errs, warns, oks = [], [], []
    low = p.lower()

    # 대표님 배제 블록 마스킹 (지뢰 오탐 방지)
    low_for_mines = re.sub(r'no (text|cinematic lighting|dark outline).*?completely silent\.', '', low, flags=re.DOTALL)
    low_for_mines = low_for_mines.replace('hand-drawn', 'fine-drawn')
    if "picture-dictionary" in low:
        low_for_mines = re.sub(r'\bpen\b', 'instrument', low_for_mines)
        low_for_mines = low_for_mines.replace('pressing arm', 'pressing lever').replace('duplicate arm', 'duplicate lever')

    # 계열 판별
    if "fine-pencil construction" in low:
        spec, kind = (PENCIL, "PENCIL(세필수채·주방사물)")
        calm = True
    elif "picture-dictionary" in low:
        spec, kind = (DICT, "DICT(그림사전·단일사물)")
        calm = True
    elif "line-reveal" in low:
        spec, kind = (CALM, "CALM(망원경·line-reveal)")
        calm = True
    else:
        spec, kind = (WOW, "WOW(산호협곡)")
        calm = False

    # 1) 지뢰
    for w, why in MINES.items():
        n = len(re.findall(r'\b' + re.escape(w) + r'\b', low_for_mines)) if " " not in w else low_for_mines.count(w)
        if n: errs.append("지뢰 '%s' %d회 — %s" % (w, n, why))
    # 2) 금지어  (frame은 'first frame'만 허용)
    for w, why in BANNED.items():
        if (kind.startswith('DICT') or kind.startswith('PENCIL')) and w in ['sepia', 'paper', 'border', 'shading', 'cream', 'cartoon']:
            continue
        n = low.count(w) if " " in w or "'" in w else len(re.findall(r'\b' + re.escape(w) + r'\b', low))
        if n: errs.append("금지어 '%s' %d회 — %s" % (w, n, why))
    fr = len(re.findall(r'\bframes?\b', low)) - len(re.findall(r'first frame', low)) - len(re.findall(r'of the frame', low))
    if fr > 0: errs.append("금지어 'frame' %d회 (first frame / of the frame 제외) — 액자 유발" % fr)
    for w, why in WARN_ONLY.items():
        if re.search(r'\b' + re.escape(w) + r'\b', low): warns.append("주의 '%s' — %s" % (w, why))

    # 3) 정본에 없는 항목
    if re.search(r'\bnever\s*:', low): errs.append("'Never:' 항목 — 정본 두 계열 모두 쓰지 않는다. 부정문은 명사만 흡수된다")
    if re.search(r'\baudio\s*:', low): errs.append("'Audio:' 항목 — 정본에 없다. 소리는 Flow UI에서")
    if "there are no" in low and "there are no bold contours" not in low:
        errs.append("★ 'There are no ...' — 명사를 부르는 부정문. 정본은 'There is no visible' 하나만 쓴다")

    # 4) 필수문
    miss = [(k, why) for k, why in spec if k not in p]
    for k, why in miss: errs.append("필수문 없음 [%s] %s" % (why, k[:52]))
    oks.append("필수문 %d/%d" % (len(spec) - len(miss), len(spec)))

    # 5) 시간 구간
    ts = sorted(set(re.findall(r'\d+\.?\d*\s*[-–]\s*\d+\.?\d*\s*s', p.replace(" ", ""))))
    want = 3 if (kind.startswith('WOW') or kind.startswith('PENCIL')) else 2
    if len(ts) != want:
        errs.append("시간 구간 %d개 — %s는 %d막이어야 한다 (%s)" % (
            len(ts), kind, want, "0-4s / 4-8s" if calm else "0-3.5s / 3.5-5.5s / 5.5-8s"))
    oks.append("시간 구간 %s" % (ts if ts else "없음"))

    # 6) 요소 개수 (WOW는 정확히 5개)
    m = re.search(r'The only visible subjects throughout the sequence are (.*?)\.\s*[\d0]', p, re.S)
    if m:
        els = [x.strip() for x in re.split(r',| and ', m.group(1)) if x.strip()]
        oks.append("요소 %d개" % len(els))
        if not calm and len(els) != 5:
            errs.append("요소 %d개 — WOW 골격은 정확히 5개다 (잠금 파일 §4-1)" % len(els))

    # 7) 길이
    n = len(p)
    oks.append("길이 %d자" % n)
    if not (1500 <= n <= 2400):
        warns.append("길이 %d자 — 정본은 산호협곡 2,057자 / 망원경 약 1,750자" % n)

    # 출력
    head = "── %s  [%s] ──" % (name, kind)
    print(head)
    print("   " + " · ".join(oks))
    for w in warns: print("   ! " + w)
    if errs:
        print("   ★★ 오류 %d건 — 이 프롬프트로 뽑지 마라" % len(errs))
        for e in errs: print("      ★ " + e)
    else:
        print("   ✅ 통과")
    print()
    return len(errs)

def main():
    args = sys.argv[1:]
    total = 0; cnt = 0
    if not args:
        p = sys.stdin.read().strip()
        total += check("(붙여넣기)", p); cnt = 1
    else:
        for path in args:
            s = io.open(path, encoding="utf-8").read()
            if path.lower().endswith((".html", ".htm")):
                blocks = re.findall(r'id="p-([^"]+)"[^>]*>(.*?)</', s, re.S)
                if not blocks:
                    blocks = [("%d" % i, b) for i, b in enumerate(re.findall(r'<pre[^>]*>(.*?)</pre>', s, re.S), 1)]
                for tag, b in blocks:
                    txt = re.sub(r'<[^>]+>', '', b)
                    txt = txt.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"')
                    total += check(tag, txt.strip()); cnt += 1
            else:
                total += check(os.path.basename(path), s.strip()); cnt += 1
    print("=" * 60)
    print("검사 %d건 · 오류 합계 %d건" % (cnt, total))
    if total: print("★ 오류가 있는 프롬프트로는 뽑지 마라. 고치고 다시 돌려라.")
    sys.exit(1 if total else 0)

main()
