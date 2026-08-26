# -*- coding: utf-8 -*-
import io, json, os, subprocess, math

all_1200 = set(io.open("_작업/all1200.txt", encoding="utf-8").read().split())

# 1. 기존 데이터에서 ch2 14~33 완전 롤백
s = io.open("public/learning/index.html", encoding="utf-8").read()
i = s.index("const chapterData = {"); st = s.index("{", i); d = 0
for j in range(st, len(s)):
    if s[j] == "{": d += 1
    elif s[j] == "}":
        d -= 1
        if d == 0: en = j + 1; break
data = json.loads(s[st:en])
data["2"]["works"] = data["2"]["works"][:13]
data["2"]["levelOneWords"] = data["2"]["levelOneWords"][:13]
data["2"]["levelTwoWords"] = data["2"]["levelTwoWords"][:13]
data["2"]["levelOneSpots"] = data["2"]["levelOneSpots"][:13]
data["2"]["sceneSpots"] = data["2"]["sceneSpots"][:13]

new_json = json.dumps(data, ensure_ascii=False, indent=2)
new_html = s[:st] + new_json + s[en:]
with open("public/learning/index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

# 기존 사용 단어 & 뜻 수집
used_words = set()
used_meanings = set()
for ch in data:
    for w in data[ch]["works"]:
        for a, b in w["words"]:
            used_words.add(a)
            used_meanings.add(b)

free_words = all_1200 - used_words
print(f"가용 1200 단어: {len(free_words)}개")

# 20개 장면에 정확히 배정할 단어-뜻 (모두 all1200에 속하며 진짜 뜻)
# 각 단어 고유 뜻 부여
WORD_DEFS = {
    # 14. 화분 속 새싹
    "shape": "모양새", "unit": "식물 개체", "category": "식물 갈래", "pair": "잎사귀 쌍",
    "develop": "자라나다", "create": "생겨나다", "stable": "안정되다", "steady": "차분하다",

    # 15. 정원 도구
    "tool": "원예 도구", "resource": "원예 자원", "balance": "무게 중심", "square": "사각형 밑판",
    "dig": "흙을 파다", "produce": "길러내다", "repair": "손질하다", "direct": "물을 향하다",

    # 16. 유리 테라리움
    "triangle": "삼각형 잎", "volume": "병의 부피", "blank": "비어있는 여백", "empty": "텅 빈 공간",
    "combine": "어우러지다", "separate": "분리되다", "remain": "남아있다", "defense": "외부 방어",

    # 17. 꽃과 원예 가위
    "single": "한 줄기", "section": "잘린 단면", "item": "꽃송이 품목", "piece": "꽃의 조각",
    "divide": "가위로 나누다", "remove": "잎을 없애다", "grace": "고상한 기품", "snap": "뚝 부러지다",

    # 18. 작은 새집
    "shelter": "작은 쉼터", "frame": "목재 틀", "spot": "모이 장소", "basis": "나무 밑바닥",
    "hang": "가지에 걸다", "survive": "살아남다", "protect": "비바람을 막다", "settle": "보금자리 틀다",

    # 19. 풍성한 수확
    "bunch": "수확 묶음", "content": "담긴 내용물", "mass": "묵직한 덩어리", "grand": "큼직한 열매",
    "gather": "모아담다", "contain": "바구니에 담다", "period": "결실의 계절", "plenty": "풍부함",

    # 20. 꽃 누르개
    "block": "사각 목판", "link": "연결 고리", "structure": "압화틀 구조", "element": "구성 요소",
    "bind": "끈으로 묶다", "shut": "틈없이 닫다", "adapt": "틀에 맞추다", "constant": "변함없는",

    # 21. 정원 손수레
    "wide": "넓은 적재함", "handle": "양쪽 손잡이", "motion": "바퀴 이동", "step": "한 걸음",
    "roll": "바퀴가 구르다", "drag": "앞으로 끌다", "force": "밀어내는 힘", "shift": "위치 옮기다",

    # 22. 작은 온실
    "district": "온실 구역", "scale": "온실 규모", "extend": "위로 뻗다", "height": "온실 높이",
    "raise": "식물 기르다", "equal": "균등한 간격", "maintain": "온도 유지하다", "solid": "단단한 유리",

    # 23. 키 큰 해바라기
    "annual": "한해살이 화초", "stand": "꼿꼿이 서다", "edge": "꽃잎 가장자리", "shine": "빛을 반사하다",
    "continue": "피어나길 잇다", "lead": "해를 향해 이끌다", "regular": "규칙적 배열", "bloom": "활짝 피어나다",

    # 24. 나뭇가지 위 박새
    "fur": "보드라운 털", "branch": "앉은 나뭇가지", "wing": "작은 날개", "bark": "거친 나무껍질",
    "bow": "고개를 숙이다", "lean": "몸을 기울이다", "wild": "야생의 숨결", "pause": "잠시 멈칫하다",

    # 25. 풀잎 위 무당벌레
    "ant": "작은 곤충", "surface": "잎사귀 겉면", "round": "동그란 몸", "neat": "말끔한 모양",
    "crawl": "살금살금 기다", "odd": "특이한 무늬", "tiny": "조그마한 몸", "slow": "느릿한 걸음",

    # 26. 화려한 호랑나비
    "pattern": "대칭 날개무늬", "species": "나비의 한 종", "soft": "부드러운 날개", "body": "가운데 몸체",
    "bend": "날개를 접다", "flutter": "사뿐 날개치다", "fast": "날렵한 비행", "glide": "미끄러지듯 날다",

    # 27. 숲속 도토리
    "seed": "참나무 열매씨", "log": "작은 통나무", "season": "풍성한 가을철", "tight": "단단히 닫힌",
    "drop": "바닥에 떨어지다", "smooth": "매끄러운 껍질", "fall": "가지에서 지다", "root": "참나무 뿌리",

    # 28. 올빼미 깃털
    "line": "가운데 깃대선", "tip": "깃털의 끝부분", "thin": "가느다란 깃", "flat": "수평으로 놓인",
    "float": "공중에 뜨다", "light": "가벼운 무게", "silent": "고요한 침묵", "drift": "바람에 떠돌다",

    # 29. 왕잠자리
    "net": "그물망 날개맥", "stick": "가느다란 몸통", "sky": "푸른 창공", "sharp": "날카로운 눈",
    "rush": "쏜살같이 날다", "clear": "맑고 투명함", "hover": "허공에 맴돌다", "spread": "날개를 펼치다",

    # 30. 단풍 씨앗 날개
    "angle": "벌어진 각도", "wind": "바람의 흐름", "leaf": "단풍잎", "plant": "어린 나무",
    "spin": "회전하며 날다", "fly": "허공을 날다", "circle": "원을 그리다", "air": "맑은 공기",

    # 31. 새 모이 그릇
    "dish": "도자기 접시", "feed": "새들의 먹이", "grain": "곡식 알갱이", "rim": "그릇의 테두리",
    "fill": "가득 채워두다", "share": "모이를 나누다", "visit": "새가 찾아오다", "peck": "부리로 쪼다",

    # 32. 둥지 속 새알
    "nest": "나뭇가지 둥지", "straw": "마른 짚풀", "egg": "세 개의 새알", "count": "알을 세어보다",
    "warm": "따스한 온기", "lay": "알을 품어두다", "wait": "새끼 기다리다", "hatch": "껍질을 깨다",

    # 33. 정원 달팽이
    "shell": "소용돌이 껍데기", "track": "기어간 흔적선", "trail": "남겨진 자취", "spiral": "나선형 무늬",
    "creep": "천천히 기어가다", "moist": "축축한 피부", "quiet": "조용한 걸음", "home": "등 위의 집"
}

# 안전 비대칭 좌표
L1_POS = [[35, 30], [72, 28], [28, 70], [68, 72]]
L2_POS = [[48, 15], [78, 52], [22, 45], [58, 85]]

scenes = [
    ("14", "화분 속 새싹", "흙에서 자라나는 초록 잎", ["shape", "unit", "category", "pair"], ["develop", "create", "stable", "steady"]),
    ("15", "정원 도구", "식물을 돌보는 시간", ["tool", "resource", "balance", "square"], ["dig", "produce", "repair", "direct"]),
    ("16", "유리 테라리움", "작은 유리병 속 자연", ["triangle", "volume", "blank", "empty"], ["combine", "separate", "remain", "defense"]),
    ("17", "꽃과 원예 가위", "향기로운 꽃 줄기 다듬기", ["single", "section", "item", "piece"], ["divide", "remove", "grace", "snap"]),
    ("18", "작은 새집", "새들이 쉬어가는 나무 집", ["shelter", "frame", "spot", "basis"], ["hang", "survive", "protect", "settle"]),
    ("19", "풍성한 수확", "바구니에 담긴 가을 열매", ["bunch", "content", "mass", "grand"], ["gather", "contain", "period", "plenty"]),
    ("20", "꽃 누르개", "말린 꽃을 보관하는 나무틀", ["block", "link", "structure", "element"], ["bind", "shut", "adapt", "constant"]),
    ("21", "정원 손수레", "흙과 화분을 싣는 수레", ["wide", "handle", "motion", "step"], ["roll", "drag", "force", "shift"]),
    ("22", "작은 온실", "햇살이 비치는 유리 집", ["district", "scale", "extend", "height"], ["raise", "equal", "maintain", "solid"]),
    ("23", "키 큰 해바라기", "담장 옆 활짝 핀 꽃", ["annual", "stand", "edge", "shine"], ["continue", "lead", "regular", "bloom"]),
    ("24", "나뭇가지 위 박새", "숲속 작은 깃털 새", ["fur", "branch", "wing", "bark"], ["bow", "lean", "wild", "pause"]),
    ("25", "풀잎 위 무당벌레", "동글동글 점박이 딱정벌레", ["ant", "surface", "round", "neat"], ["crawl", "odd", "tiny", "slow"]),
    ("26", "화려한 호랑나비", "우아한 날갯짓의 나비", ["pattern", "species", "soft", "body"], ["bend", "flutter", "fast", "glide"]),
    ("27", "숲속 도토리", "모자를 쓴 참나무 열매", ["seed", "log", "season", "tight"], ["drop", "smooth", "fall", "root"]),
    ("28", "올빼미 깃털", "바람에 날려온 부드러운 깃", ["line", "tip", "thin", "flat"], ["float", "light", "silent", "drift"]),
    ("29", "왕잠자리", "맑고 투명한 네 장의 날개", ["net", "stick", "sky", "sharp"], ["rush", "clear", "hover", "spread"]),
    ("30", "단풍 씨앗 날개", "빙글빙글 날아가는 날개 씨앗", ["angle", "wind", "leaf", "plant"], ["spin", "fly", "circle", "air"]),
    ("31", "새 모이 그릇", "작은 새들을 위한 식탁", ["dish", "feed", "grain", "rim"], ["fill", "share", "visit", "peck"]),
    ("32", "둥지 속 새알", "나뭇가지로 엮은 아늑한 둥지", ["nest", "straw", "egg", "count"], ["warm", "lay", "wait", "hatch"]),
    ("33", "정원 달팽이", "나선형 껍질을 진 달팽이", ["shell", "track", "trail", "spiral"], ["creep", "moist", "quiet", "home"])
]

all_passed = True
for n_str, title, sub, l1_words, l2_words in scenes:
    l1 = [[w, WORD_DEFS[w], L1_POS[k]] for k, w in enumerate(l1_words)]
    l2 = [[w, WORD_DEFS[w], L2_POS[k]] for k, w in enumerate(l2_words)]
    
    obj = {
        "chapter": 2, "n": n_str, "title": title, "sub": sub,
        "video": f"ch2/ch2_{n_str}.mp4", "img": f"ch2/ch2_{n_str}-poster.jpg",
        "levelOne": l1, "levelTwo": l2
    }
    jp = f"_작업/새편/ch2_{n_str}.json"
    with open(jp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

    r1 = subprocess.run(["python3", "_작업/scene_tool.py", "check", jp], capture_output=True, text=True)
    out1 = (r1.stdout + r1.stderr).strip()
    if "오류" in out1:
        print(f"❌ [ch2_{n_str}] 에러:\n{out1}")
        all_passed = False
        break
    else:
        subprocess.run(["python3", "_작업/scene_tool.py", "add", jp], capture_output=True, text=True)
        print(f"✅ [ch2_{n_str}] 주입 완료: {title}")

print("\n=== 최종 전체 verify ===")
subprocess.run(["python3", "_작업/scene_tool.py", "verify"])

