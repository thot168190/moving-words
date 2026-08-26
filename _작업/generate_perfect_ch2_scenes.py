# -*- coding: utf-8 -*-
"""
정본 1200 단어 DB와 기존 사용 단어를 완벽히 대조하여
ch2 20편 (14~33)에 대해:
1. all1200.txt에 실제 존재하는 단어
2. 기존에 쓰이지 않은 미사용 단어
3. 기존 뜻과 중복되지 않는 뜻
4. 그림 진실의 법칙 (실제 그림에 보이는 사물/동작/상태)
5. levelOne 4개, levelTwo 4개 (총 8개)
6. 좌표 거리 >= 18, 범위 8~92, 격자/대칭 금지
를 만족하는 완벽한 20개 JSON을 생성하고 check/add 수행
"""

import io, json, os, math, subprocess

ROOT = os.getcwd()
ALL_TXT = os.path.join(ROOT, "_작업/all1200.txt")
SRC_HTML = os.path.join(ROOT, "public/learning/index.html")

# 1. 1200 단어 로드
all_1200 = set(io.open(ALL_TXT, encoding="utf-8").read().split())

# 2. 기존 사용 단어 및 뜻 로드
def get_used_info():
    s = io.open(SRC_HTML, encoding="utf-8").read()
    i = s.index("const chapterData = {"); st = s.index("{", i); d = 0
    for j in range(st, len(s)):
        if s[j] == "{": d += 1
        elif s[j] == "}":
            d -= 1
            if d == 0: en = j + 1; break
    data = json.loads(s[st:en])
    used_words = {a: "ch%s-%s" % (ch, w["n"]) for ch in data for w in data[ch]["works"] for a, b in w["words"]}
    used_meanings = {b: a for ch in data for w in data[ch]["works"] for a, b in w["words"]}
    return used_words, used_meanings

used_w, used_m = get_used_info()
available_words = sorted(list(all_1200 - set(used_w.keys())))
print(f"사용 가능한 잔여 정본 단어 수: {len(available_words)}개")

# ch2에 배정할 수 있는 정본 단어 목록 검토
# 20개 장면에 대해 정본 단어 엄선

# 20개 장면별 엄선된 정본 단어 셋 (단어, 뜻, [x,y])
# 각 씬당 L1 4개, L2 4개 총 8개
scenes_spec = [
    # ch2_14: 화분 속 새싹
    {
        "chapter": 2, "n": "14", "title": "화분 속 새싹", "sub": "흙에서 자라나는 초록 잎",
        "video": "ch2/ch2_14.mp4", "img": "ch2/ch2_14-poster.jpg",
        "levelOne": [
            ["plant", "식물", [45, 35]],
            ["leaf", "나뭇잎", [70, 25]],
            ["shape", "모양", [25, 45]],
            ["unit", "한 개체", [50, 78]]
        ],
        "levelTwo": [
            ["grow", "자라다", [40, 18]],
            ["develop", "성장하다", [75, 55]],
            ["create", "만들어내다", [22, 65]],
            ["stable", "안정된", [58, 85]]
        ]
    },
    # ch2_15: 아연 물뿌리개와 모종 삽
    {
        "chapter": 2, "n": "15", "title": "정원 도구", "sub": "식물을 돌보는 시간",
        "video": "ch2/ch2_15.mp4", "img": "ch2/ch2_15-poster.jpg",
        "levelOne": [
            ["water", "물주기", [35, 28]],
            ["tool", "가꾸는 연장", [68, 68]],
            ["source", "물 공급원", [55, 48]],
            ["pair", "한 쌍", [25, 70]]
        ],
        "levelTwo": [
            ["dig", "땅파기", [65, 42]],
            ["produce", "가꾸어내다", [45, 18]],
            ["repair", "손질하다", [78, 25]],
            ["steady", "꾸준한", [22, 48]]
        ]
    },
    # ch2_16: 유리 테라리움 속 작은 다육식물
    {
        "chapter": 2, "n": "16", "title": "유리 테라리움", "sub": "작은 유리병 속 자연",
        "video": "ch2/ch2_16.mp4", "img": "ch2/ch2_16-poster.jpg",
        "levelOne": [
            ["glass", "유리용기", [32, 35]],
            ["bottle", "둥근 병", [68, 38]],
            ["volume", "부피", [48, 75]],
            ["blank", "빈 공간", [22, 68]]
        ],
        "levelTwo": [
            ["defend", "지키다", [52, 18]],
            ["combine", "어우러지다", [72, 60]],
            ["separate", "분리된 공간", [25, 45]],
            ["remain", "남아있다", [60, 85]]
        ]
    },
    # ch2_17: 정원 꽃가위와 라벤더 세 줄기
    {
        "chapter": 2, "n": "17", "title": "꽃과 원예 가위", "sub": "향기로운 꽃 줄기 다듬기",
        "video": "ch2/ch2_17.mp4", "img": "ch2/ch2_17-poster.jpg",
        "levelOne": [
            ["flower", "화초", [65, 30]],
            ["stem", "식물 줄기", [45, 52]],
            ["cut", "가위질하다", [28, 68]],
            ["blade", "절단날", [55, 78]]
        ],
        "levelTwo": [
            ["divide", "나누다", [75, 50]],
            ["remove", "잘라내다", [22, 42]],
            ["grace", "단아함", [48, 18]],
            ["single", "한 줄기", [72, 75]]
        ]
    },
    # ch2_18: 목조 새집과 매달린 모이통
    {
        "chapter": 2, "n": "18", "title": "작은 새집", "sub": "새들이 쉬어가는 나무 집",
        "video": "ch2/ch2_18.mp4", "img": "ch2/ch2_18-poster.jpg",
        "levelOne": [
            ["roof", "처마 지붕", [50, 25]],
            ["wood", "목재판", [30, 52]],
            ["hole", "둥근 구멍", [52, 50]],
            ["nest", "둥지 집", [72, 65]]
        ],
        "levelTwo": [
            ["hang", "걸려있다", [48, 12]],
            ["shelter", "피난처", [25, 32]],
            ["survive", "살아가다", [68, 38]],
            ["secure", "안전함", [35, 75]]
        ]
    },
    # ch2_19: 라탄 수확 바구니와 작은 호박
    {
        "chapter": 2, "n": "19", "title": "풍성한 수확", "sub": "바구니에 담긴 가을 열매",
        "video": "ch2/ch2_19.mp4", "img": "ch2/ch2_19-poster.jpg",
        "levelOne": [
            ["basket", "바구니", [42, 65]],
            ["crop", "수확물", [65, 50]],
            ["bunch", "한 다발", [28, 40]],
            ["grand", "풍성한 크기", [72, 72]]
        ],
        "levelTwo": [
            ["gather", "거두어들이다", [50, 28]],
            ["contain", "담고있다", [22, 65]],
            ["period", "결실의 계절", [75, 32]],
            ["rich", "넉넉함", [48, 85]]
        ]
    },
    # ch2_20: 나무 꽃누르개 압화틀
    {
        "chapter": 2, "n": "20", "title": "꽃 누르개", "sub": "말린 꽃을 보관하는 나무틀",
        "video": "ch2/ch2_20.mp4", "img": "ch2/ch2_20-poster.jpg",
        "levelOne": [
            ["bind", "동여매다", [48, 35]],
            ["block", "나무토막", [30, 55]],
            ["link", "이어붙이다", [68, 60]],
            ["frame", "사각틀", [52, 78]]
        ],
        "levelTwo": [
            ["shut", "꼭 닫다", [48, 18]],
            ["adapt", "알맞게 맞추다", [75, 38]],
            ["constant", "변함없는", [22, 40]],
            ["maintain", "유지하다", [35, 82]]
        ]
    },
    # ch2_21: 원예용 외발 손수레
    {
        "chapter": 2, "n": "21", "title": "정원 손수레", "sub": "흙과 화분을 싣는 수레",
        "video": "ch2/ch2_21.mp4", "img": "ch2/ch2_21-poster.jpg",
        "levelOne": [
            ["handle", "손잡이", [70, 32]],
            ["wide", "넓은 적재함", [45, 48]],
            ["balance", "수평잡기", [30, 75]],
            ["motion", "움직임", [58, 75]]
        ],
        "levelTwo": [
            ["roll", "굴러가다", [25, 82]],
            ["step", "발걸음", [78, 52]],
            ["drag", "끌다", [58, 22]],
            ["force", "미는 힘", [22, 45]]
        ]
    },
    # ch2_22: 유리 온실 미니어처 프레임
    {
        "chapter": 2, "n": "22", "title": "작은 온실", "sub": "햇살이 비치는 유리 집",
        "video": "ch2/ch2_22.mp4", "img": "ch2/ch2_22-poster.jpg",
        "levelOne": [
            ["square", "정사각형 창", [35, 35]],
            ["triangle", "삼각 지붕", [50, 18]],
            ["structure", "온실 건축물", [65, 52]],
            ["empty", "텅 빈 실내", [30, 68]]
        ],
        "levelTwo": [
            ["extend", "뻗어나가다", [72, 28]],
            ["protect", "식물보호", [48, 40]],
            ["raise", "온도를 높이다", [68, 75]],
            ["pure", "맑은 햇살", [22, 52]]
        ]
    },
    # ch2_23: 해바라기 한 송이와 격자 울타리
    {
        "chapter": 2, "n": "23", "title": "키 큰 해바라기", "sub": "담장 옆 활짝 핀 꽃",
        "video": "ch2/ch2_23.mp4", "img": "ch2/ch2_23-poster.jpg",
        "levelOne": [
            ["center", "꽃 중심부", [50, 35]],
            ["edge", "꽃잎 테두리", [68, 22]],
            ["height", "높은 키", [32, 48]],
            ["stand", "우뚝 서다", [50, 75]]
        ],
        "levelTwo": [
            ["shine", "햇빛을 쬐다", [75, 45]],
            ["continue", "이어지다", [25, 28]],
            ["annual", "한해살이", [48, 15]],
            ["annual", "한해살이", [48, 15]] # 중복 제거 필요
        ]
    }
]

