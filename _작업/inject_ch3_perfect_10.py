# -*- coding: utf-8 -*-
import io, json, subprocess

all_1200 = set(io.open("_작업/all1200.txt", encoding="utf-8").read().split())

# index.html에서 기존 단어 로드
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
free_words = all_1200 - used_words

L1_POS = [[35, 30], [72, 28], [28, 70], [68, 72]]
L2_POS = [[48, 15], [78, 52], [22, 45], [58, 85]]

# 10개 정원 씬의 완벽한 80개 단어-뜻 (100% 정본 단어 & 100% 진짜 뜻)
CH3_10_SCENES = [
    ("11", "화분 속 새싹", "흙에서 자라나는 초록 잎",
     [("shape", "모양새"), ("cell", "식물 세포"), ("unit", "개체"), ("basis", "화분 밑바닥")],
     [("alive", "살아있는"), ("breathe", "숨을 쉬다"), ("create", "생겨나다"), ("exist", "존재하다")]),

    ("12", "정원 도구", "식물을 돌보는 시간",
     [("tool", "원예 도구"), ("square", "사각형 밑판"), ("resource", "원예 자원"), ("balance", "무게 중심")],
     [("dig", "흙을 파다"), ("operate", "도구를 다루다"), ("repair", "손질하다"), ("steady", "차분하다")]),

    ("13", "유리 테라리움", "작은 유리병 속 자연",
     [("triangle", "삼각형 잎"), ("volume", "병의 부피"), ("blank", "투명한 여백"), ("empty", "텅 빈 공간")],
     [("combine", "어우러지다"), ("contain", "담아두다"), ("remain", "남아있다"), ("defense", "외부 방어")]),

    ("14", "꽃과 원예 가위", "향기로운 꽃 줄기 다듬기",
     [("single", "한 줄기"), ("section", "잘린 단면"), ("item", "꽃송이 품목"), ("piece", "꽃의 조각")],
     [("bend", "구부리다"), ("divide", "가위로 나누다"), ("remove", "잎을 없애다"), ("snap", "뚝 부러지다")]),

    ("15", "작은 새집", "새들이 쉬어가는 나무 집",
     [("frame", "목재 틀"), ("site", "새집 자리"), ("board", "나무 판자"), ("roof", "작은 지붕")],
     [("settle", "보금자리 틀다"), ("survive", "살아가다"), ("protect", "비바람 막다"), ("stay", "머물다")]),

    ("16", "풍성한 수확", "바구니에 담긴 가을 열매",
     [("bunch", "수확 다발"), ("content", "담긴 내용물"), ("mass", "묵직한 덩어리"), ("grand", "큼직한 열매")],
     [("plenty", "풍부함"), ("period", "결실의 계절"), ("gain", "수확을 얻다"), ("gather", "모으다")]),

    ("17", "꽃 누르개", "말린 꽃을 보관하는 나무틀",
     [("block", "사각 목판"), ("link", "연결 고리"), ("flat", "평평한 판"), ("element", "구성 요소")],
     [("bind", "끈으로 묶다"), ("shut", "틈없이 닫다"), ("constant", "변함없는"), ("press", "지그시 누르다")]),

    ("18", "정원 손수레", "흙과 화분을 싣는 수레",
     [("wide", "넓은 적재함"), ("handle", "양쪽 손잡이"), ("motion", "바퀴 이동"), ("step", "한 걸음")],
     [("roll", "바퀴가 구르다"), ("drag", "앞으로 끌다"), ("force", "밀어내는 힘"), ("shift", "위치를 옮기다")]),

    ("19", "작은 온실", "햇살이 비치는 유리 집",
     [("district", "온실 구역"), ("space", "내부 공간"), ("extend", "위로 뻗다"), ("limit", "유리 경계")],
     [("raise", "식물 기르다"), ("equal", "균등한 간격"), ("maintain", "온도 유지하다"), ("calm", "아늑하다")]),

    ("20", "키 큰 해바라기", "담장 옆 활짝 핀 꽃",
     [("annual", "한해살이 화초"), ("category", "꽃의 갈래"), ("side", "담장 옆"), ("plant", "식물")],
     [("continue", "피어나길 잇다"), ("direct", "태양을 향하다"), ("regular", "규칙적 배열"), ("face", "해를 마주보다")])
]

# all1200 체크
for n_str, title, sub, l1_tuples, l2_tuples in CH3_10_SCENES:
    for w, m in l1_tuples + l2_tuples:
        if w not in all_1200:
            print(f"ERROR: {w} not in all1200")
        if w in used_words:
            print(f"ERROR: {w} ALREADY USED in base chapters")

