"""
validate_8s.py — 「보는 단어장」 8초 영상 프롬프트 기계 검증기 (돼지 전용)

사용법:
  python3 validate_8s.py --file 프롬프트.txt
  python3 validate_8s.py "프롬프트 전문"

실행 위치: **로부장 샌드박스에서만.** 코다리 로컬 파이썬 금지(3.14 세그폴트).

판정: PASS / FAIL + 실패 항목. LLM 아님 → 언제 돌려도 같은 결과.
★ 규칙은 아래 대문자 목록만 고친다. 라이브러리 문서와 반드시 동기화.
  (문서와 어긋나면 이 스크립트가 진실 — 돼지 금고 규칙)
"""
import argparse, re, sys

# ── 1) 고정부 필수 문구 — 하나라도 없으면 FAIL ────────────────────────
REQUIRED = [
    ("헤더-순백배경",  "solid pure bright white background (#FFFFFF)"),
    ("헤더-빈첫프레임", "entirely empty white field"),
    ("헤더-고정카메라", "Static locked-off camera, one continuous 8-second take"),
    ("드로잉-획추적",  "traced visibly from endpoint to endpoint"),
    ("드로잉-단번획",  "each stroke confident, drawn once"),
    ("드로잉-비대칭",  "The composition is asymmetric"),
    ("드로잉-페이드금지","Built progressively, never fading in"),
    ("채색-선안에서",  "fills the shapes FROM INSIDE, staying within the ink lines"),
    ("채색-원색금지",  "no primary crayon colors"),
    ("채색-빛한방향",  "One consistent light direction"),
    ("채색-그림자",    "soft believable shadows"),
    ("채색-흰배경유지", "white background above stays clean"),
    ("동작-나머지정지", "Everything else stays still"),
    ("스타일-선굵기",  "varied line weight and rich observational detail"),
    ("스타일-여름광",  "clear summer daylight"),
    ("스타일-3층깊이", "cinematic depth of foreground"),
    ("스타일-도감앵커", "beautiful illustrated atlas for curious teenagers"),
    ("스타일-유치원금지","never a kindergarten picture book"),
    ("스타일-미술관",  "Museum-quality contemporary illustration"),
    ("Never블록",     "Never:"),
]

# ── 2) 전체 어디에도 있으면 FAIL — 매체 소환어 (R4) ──────────────────
#    실측: paper 는 실패 2회 모두 존재, 성공본 0회. 부정문에 넣어도 소환된다.
FORBIDDEN_ANYWHERE = [          # 단어 경계로 검사한다
    "paper", "parchment", "canvas", "cream ground", "picture frame",
    "border", "hand", "pen", "watermark",
]
FORBIDDEN_ANYWHERE_EXCEPT = {"frame": ["first frame", "the frame", "of the frame"]}

# ── 3) 본문(Never: 앞)에 있으면 FAIL — 우울/조감/비율 유발어 ─────────
FORBIDDEN_BODY = [
    "sepia", "ink-wash", "muted grey", "muted gray", "slate mood", "slate blue",
    "storm", "fog", "mist", "smoke", "fluffy", "billowing", "gloomy", "sombre", "somber",
    "seen from above", "bird's-eye", "birds-eye", "aerial", "top-down",
    "vertical", "horizontal", "16:9", "9:16",
    "children's picture-book", "uncluttered", "cartoon", "anime", "photoreal",
    "texture,",             # 텍스처 지시 남발 방지 (R7)
    "engraving",            # 판화 해칭 유발 — v3에서 폐기한 단어
]

# ── 4) Never 블록 필수 항목 ──────────────────────────────────────────
REQUIRED_IN_NEVER = [
    "text", "primary crayon colors", "dead-center composition",
    "camera movement", "cuts", "color outside the lines",
]

# ── 5) 슬롯 충족 검사 ────────────────────────────────────────────────
SLOT_A_CROP = ["cropped by the", "off-center", "running past the"]      # 비대칭 장치
SLOT_A_SCALE = ["towering", "monumental", "vast", "stretching to a far", "far luminous horizon"]
COLOR_WORDS = ["cerulean","turquoise","golden","ochre","emerald","viridian","rose","amber",
               "indigo","teal","silver","olive","umber","crimson","cobalt","aquamarine",
               "sand","green","white","grey","gray","blue","warm"]
MOTION_WORDS = ["glides","arc","leap","rises","swells","lifts","drifts","brightens",
                "sparkling","glittering","spreads","opens","tilts","sways","surges","appears"]

def _has(text, pat):
    for alt in pat.split("|"):
        if alt.lower() in text.lower():
            return True
    return False

def check(p: str) -> list[str]:
    fails = []
    p = re.sub(r"\s+", " ", p).strip()      # 줄바꿈 정규화 — 없으면 오탐
    low = p.lower()
    body = re.split(r"never\s*:", p, flags=re.I)[0]
    never = re.split(r"never\s*:", p, flags=re.I)[1] if re.search(r"never\s*:", p, re.I) else ""

    for name, pat in REQUIRED:
        if not _has(p, pat):
            fails.append(f"[고정부 누락] {name}  ← \"{pat.split('|')[0][:45]}\"")

    for w in FORBIDDEN_ANYWHERE:
        if re.search(r"\b" + re.escape(w) + r"\b", low):
            fails.append(f"[매체소환어] '{w.strip()}' — 부정문에 써도 소환된다 (R4)")
    for w, oks in FORBIDDEN_ANYWHERE_EXCEPT.items():
        hits = len(re.findall(r"\b" + re.escape(w) + r"\b", low))
        allowed = sum(low.count(o) for o in oks)
        if hits > allowed:
            fails.append(f"[매체소환어] '{w}' 허용문맥 밖 사용 {hits-allowed}회")

    for w in FORBIDDEN_BODY:
        if w in body.lower():
            fails.append(f"[본문 금지어] '{w.strip()}' — 우울/조감/판화 유발")

    for w in REQUIRED_IN_NEVER:
        if w not in never.lower():
            fails.append(f"[Never 누락] '{w}'")

    if not any(x in low for x in SLOT_A_CROP):
        fails.append("[슬롯A] 비대칭 장치 없음 — 프레임에 잘리는 요소 1개 필수")
    if not any(x in low for x in SLOT_A_SCALE):
        fails.append("[슬롯A] 스케일 대비 장치 없음 — 거대 구름·광활한 수평선 등 1개 필수")
    nc = sum(1 for c in set(COLOR_WORDS) if c in body.lower())
    if nc < 4:
        fails.append(f"[슬롯B] 구체 색 명명 {nc}개 — 최소 4개 필요")
    seg = re.search(r"5\.5-8s:(.*?)(?:Style:|Never:)", p, re.S)
    if not seg:
        fails.append("[슬롯C] 5.5-8s 구간 없음")
    else:
        if not any(m in seg.group(1).lower() for m in MOTION_WORDS):
            fails.append("[슬롯C] 와 요소 없음 — 빛의 사건 또는 살아있는 동작 1~2개 필수")
    if "more than" not in never.lower():
        fails.append("[개수상한] Never에 'more than N ...' 상한 없음 — 요소 폭주 방지")
    return fails

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt", nargs="?")
    ap.add_argument("--file")
    a = ap.parse_args()
    text = open(a.file, encoding="utf-8").read() if a.file else (a.prompt or sys.stdin.read())
    f = check(text)
    if not f:
        print("검증: PASS — 고정부 20항목 충족, 금지어 0, 슬롯 A·B·C 충족")
        sys.exit(0)
    print(f"검증: FAIL — {len(f)}건")
    for x in f: print("  " + x)
    sys.exit(1)
