# -*- coding: utf-8 -*-
import io, json, os, subprocess

# 1. 기존 데이터 로드
all_1200 = set(io.open("_작업/all1200.txt", encoding="utf-8").read().split())

s = io.open("public/learning/index.html", encoding="utf-8").read()
i = s.index("const chapterData = {"); st = s.index("{", i); d = 0
for j in range(st, len(s)):
    if s[j] == "{": d += 1
    elif s[j] == "}":
        d -= 1
        if d == 0: en = j + 1; break
data = json.loads(s[st:en])

used_words = set()
used_meanings = set()
for ch in data:
    for w in data[ch]["works"]:
        for a, b in w["words"]:
            used_words.add(a)
            used_meanings.add(b)

free_words = all_1200 - used_words
print(f"현재 미사용 정본 단어: {len(free_words)}개")

# 정본 사전 (단어 -> 대표 한국어 뜻)
DICTIONARY = {
    # 사물/명사/특성 (Level 1)
    "shape": "모양", "unit": "개체", "category": "분류 갈래", "pair": "한 쌍",
    "tool": "도구", "resource": "자원", "balance": "균형", "square": "네모",
    "triangle": "삼각형", "volume": "부피", "blank": "여백", "empty": "텅 빈",
    "single": "하나의", "section": "부분", "item": "항목", "piece": "조각",
    "shelter": "쉼터", "frame": "틀", "spot": "장소", "basis": "기초",
    "bunch": "다발", "content": "내용물", "mass": "덩어리", "grand": "웅대한",
    "block": "나무토막", "link": "연결고리", "structure": "구조", "element": "요소",
    "wide": "넓은", "handle": "손잡이", "motion": "동작", "step": "걸음",
    "district": "구역", "scale": "규모", "height": "높이", "edge": "가장자리",
    "fur": "털", "branch": "가지", "wing": "날개", "bark": "나무껍질",
    "ant": "개미", "surface": "표면", "round": "둥근", "neat": "말끔한",
    "species": "종", "seed": "씨", "solid": "단단한", "log": "통나무",
    "line": "선", "tip": "끝", "thin": "얇은", "flat": "평평한",
    "net": "그물", "stick": "막대", "sky": "하늘", "sharp": "날카로운",
    "angle": "각도", "dish": "접시", "feed": "먹이", "grain": "곡물",
    "rim": "테두리", "nest": "둥지", "straw": "짚", "circle": "원",
    "shell": "껍데기", "track": "자국", "trail": "자취", "spiral": "나선",
    
    # 동작/상태/동사 (Level 2)
    "develop": "자라나다", "create": "만들다", "stable": "안정된", "freshness": "신선함",
    "dig": "파다", "produce": "생산하다", "repair": "고치다", "direct": "향하다",
    "combine": "결합하다", "separate": "분리하다", "remain": "남다", "defense": "방어",
    "divide": "나누다", "remove": "없애다", "grace": "기품", "snap": "부러뜨리다",
    "hang": "걸다", "survive": "살아남다", "protect": "보호하다", "settle": "정착하다",
    "gather": "모으다", "contain": "담다", "period": "기간", "plenty": "풍부함",
    "bind": "묶다", "shut": "닫다", "adapt": "맞추다", "constant": "끊임없는",
    "roll": "구르다", "drag": "끌다", "force": "힘", "shift": "이동하다",
    "raise": "기르다", "equal": "동등한", "maintain": "유지하다", "extend": "뻗다",
    "annual": "한해의", "stand": "서다", "continue": "계속되다", "lead": "이끌다",
    "regular": "규칙적인", "shine": "빛나다", "bow": "숙이다", "lean": "기울이다",
    "wild": "야생의", "pause": "멈추다", "crawl": "기어가다", "odd": "특이한",
    "tiny": "작은", "slow": "느린", "bend": "접다", "soft": "부드러운",
    "drop": "떨어지다", "smooth": "매끄러운", "season": "계절", "tight": "꽉 죈",
    "float": "뜨다", "light": "가벼운", "silent": "조용한", "drift": "떠돌다",
    "rush": "돌진하다", "fast": "빠른", "clear": "맑은", "hover": "맴돌다",
    "spin": "돌다", "wind": "바람", "spread": "퍼지다", "glide": "미끄러지다",
    "fill": "채우다", "share": "나누다", "visit": "찾아가다", "peck": "쪼다",
    "warm": "따뜻한", "lay": "놓다", "wait": "기다리다", "hatch": "부화하다",
    "count": "세다", "quiet": "조용한", "moist": "축축한", "creep": "기어가다",
    "plant": "식물", "leaf": "잎", "root": "뿌리", "bloom": "꽃피다"
}

# 20개 장면에 정확히 배정할 씬 목록
scenes_plan = [
    # 14. 화분 속 새싹
    ("14", "화분 속 새싹", "흙에서 자라나는 초록 잎",
     ["shape", "unit", "category", "pair"],
     ["develop", "create", "stable", "steady"]),
    # 15. 정원 도구
    ("15", "정원 도구", "식물을 돌보는 시간",
     ["tool", "resource", "balance", "square"],
     ["dig", "produce", "repair", "direct"]),
    # 16. 유리 테라리움
    ("16", "유리 테라리움", "작은 유리병 속 자연",
     ["triangle", "volume", "blank", "empty"],
     ["combine", "separate", "remain", "defense"]),
    # 17. 꽃과 원예 가위
    ("17", "꽃과 원예 가위", "향기로운 꽃 줄기 다듬기",
     ["single", "section", "item", "piece"],
     ["divide", "remove", "grace", "snap"]),
    # 18. 작은 새집
    ("18", "작은 새집", "새들이 쉬어가는 나무 집",
     ["shelter", "frame", "spot", "basis"],
     ["hang", "survive", "protect", "settle"]),
    # 19. 풍성한 수확
    ("19", "풍성한 수확", "바구니에 담긴 가을 열매",
     ["bunch", "content", "mass", "grand"],
     ["gather", "contain", "period", "plenty"]),
    # 20. 꽃 누르개
    ("20", "꽃 누르개", "말린 꽃을 보관하는 나무틀",
     ["block", "link", "structure", "element"],
     ["bind", "shut", "adapt", "constant"]),
    # 21. 정원 손수레
    ("21", "정원 손수레", "흙과 화분을 싣는 수레",
     ["wide", "handle", "motion", "step"],
     ["roll", "drag", "force", "shift"]),
    # 22. 작은 온실
    ("22", "작은 온실", "햇살이 비치는 유리 집",
     ["district", "scale", "extend", "height"],
     ["raise", "equal", "maintain", "solid"]),
    # 23. 키 큰 해바라기
    ("23", "키 큰 해바라기", "담장 옆 활짝 핀 꽃",
     ["annual", "stand", "edge", "shine"],
     ["continue", "lead", "regular", "bloom"]),
    # 24. 나뭇가지 위 박새
    ("24", "나뭇가지 위 박새", "숲속 작은 깃털 새",
     ["fur", "branch", "wing", "bark"],
     ["bow", "lean", "wild", "pause"]),
    # 25. 풀잎 위 무당벌레
    ("25", "풀잎 위 무당벌레", "동글동글 점박이 딱정벌레",
     ["ant", "surface", "round", "neat"],
     ["crawl", "odd", "tiny", "slow"]),
    # 26. 화려한 호랑나비
    ("26", "화려한 호랑나비", "우아한 날갯짓의 나비",
     ["pattern", "species", "soft", "body"],
     ["bend", "flutter", "fast", "glide"]),
    # 27. 숲속 도토리
    ("27", "숲속 도토리", "모자를 쓴 참나무 열매",
     ["seed", "log", "season", "tight"],
     ["drop", "smooth", "fall", "root"]),
    # 28. 올빼미 깃털
    ("28", "올빼미 깃털", "바람에 날려온 부드러운 깃",
     ["line", "tip", "thin", "flat"],
     ["float", "light", "silent", "drift"]),
    # 29. 왕잠자리
    ("29", "왕잠자리", "맑고 투명한 네 장의 날개",
     ["net", "stick", "sky", "sharp"],
     ["rush", "clear", "hover", "spread"]),
    # 30. 단풍 씨앗 날개
    ("30", "단풍 씨앗 날개", "빙글빙글 날아가는 날개 씨앗",
     ["angle", "wind", "leaf", "plant"],
     ["spin", "fly", "circle", "air"]),
    # 31. 새 모이 그릇
    ("31", "새 모이 그릇", "작은 새들을 위한 식탁",
     ["dish", "feed", "grain", "rim"],
     ["fill", "share", "visit", "peck"]),
    # 32. 둥지 속 새알
    ("32", "둥지 속 새알", "나뭇가지로 엮은 아늑한 둥지",
     ["nest", "straw", "egg", "count"],
     ["warm", "lay", "wait", "hatch"]),
    # 33. 정원 달팽이
    ("33", "정원 달팽이", "나선형 껍질을 진 달팽이",
     ["shell", "track", "trail", "spiral"],
     ["creep", "moist", "quiet", "home"])
]

