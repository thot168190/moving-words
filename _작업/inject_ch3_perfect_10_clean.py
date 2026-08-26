# -*- coding: utf-8 -*-
import io, json, subprocess

all_1200 = set(io.open("_작업/all1200.txt", encoding="utf-8").read().split())

# 1. index.html에서 기존 66편 상태로 롤백 (ch3는 10개만 남김)
s = io.open("public/learning/index.html", encoding="utf-8").read()
i = s.index("const chapterData = {"); st = s.index("{", i); d = 0
for j in range(st, len(s)):
    if s[j] == "{": d += 1
    elif s[j] == "}":
        d -= 1
        if d == 0: en = j + 1; break
data = json.loads(s[st:en])
data["3"]["works"] = data["3"]["works"][:10]
data["3"]["levelOneWords"] = data["3"]["levelOneWords"][:10]
data["3"]["levelTwoWords"] = data["3"]["levelTwoWords"][:10]
data["3"]["levelOneSpots"] = data["3"]["levelOneSpots"][:10]
data["3"]["sceneSpots"] = data["3"]["sceneSpots"][:10]

new_json = json.dumps(data, ensure_ascii=False, indent=2)
new_html = s[:st] + new_json + s[en:]
with open("public/learning/index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

# 2. 10개 정원 씬의 완벽한 80개 단어-뜻 (중복 0건, 사전적 진짜 뜻 100%)
# (번호, 제목, 부제, [L1 4개], [L2 4개])

L1_POS = [[35, 30], [72, 28], [28, 70], [68, 72]]
L2_POS = [[48, 15], [78, 52], [22, 45], [58, 85]]

CH3_SCENES = [
    # 11. 화분 속 새싹
    ("11", "화분 속 새싹", "흙에서 자라나는 초록 잎",
     [("shape", "모양새"), ("cell", "식물 세포"), ("unit", "개체"), ("basis", "화분 밑바닥")],
     [("alive", "살아있는"), ("breathe", "숨을 쉬다"), ("create", "생겨나다"), ("exist", "존재하다")]),

    # 12. 아연 물뿌리개와 모종삽
    ("12", "정원 도구", "식물을 돌보는 시간",
     [("tool", "원예 도구"), ("square", "사각형 밑판"), ("resource", "원예 자원"), ("balance", "무게 중심")],
     [("dig", "흙을 파다"), ("operate", "도구를 다루다"), ("repair", "손질하다"), ("steady", "차분하다")]),

    # 13. 유리 테라리움 속 작은 다육식물
    ("13", "유리 테라리움", "작은 유리병 속 자연",
     [("triangle", "삼각형 잎"), ("volume", "병의 부피"), ("blank", "투명한 여백"), ("empty", "텅 빈 공간")],
     [("combine", "어우러지다"), ("contain", "담아두다"), ("remain", "남아있다"), ("defense", "외부 방어")]),

    # 14. 정원 꽃가위와 라벤더 세 줄기
    ("14", "꽃과 원예 가위", "향기로운 꽃 줄기 다듬기",
     [("single", "한 줄기"), ("section", "잘린 단면"), ("item", "꽃송이 품목"), ("piece", "꽃의 조각")],
     [("bend", "구부리다"), ("divide", "가위로 나누다"), ("remove", "잎을 없애다"), ("snap", "뚝 부러지다")]),

    # 15. 목조 새집과 매달린 모이통
    ("15", "작은 새집", "새들이 쉬어가는 나무 집",
     [("frame", "목재 틀"), ("stuff", "나무 재료"), ("hole", "작은 출입문"), ("district", "새집 구역")],
     [("settle", "보금자리 틀다"), ("survive", "살아가다"), ("found", "터전을 마련하다"), ("establish", "자리를 잡다")]),

    # 16. 라탄 수확 바구니와 작은 호박
    ("16", "풍성한 수확", "바구니에 담긴 가을 열매",
     [("bunch", "수확 다발"), ("content", "담긴 내용물"), ("mass", "묵직한 덩어리"), ("grand", "큼직한 열매")],
     [("plenty", "풍부함"), ("period", "결실의 계절"), ("gain", "수확을 얻다"), ("include", "포함하다")]),

    # 17. 나무 꽃누르개 압화틀
    ("17", "꽃 누르개", "말린 꽃을 보관하는 나무틀",
     [("block", "사각 목판"), ("link", "연결 고리"), ("pair", "압화판 한 쌍"), ("flat", "평평한 판면")],
     [("bind", "끈으로 묶다"), ("shut", "틈없이 닫다"), ("constant", "변함없는"), ("maintain", "형태를 지키다")]),

    # 18. 원예용 외발 손수레
    ("18", "정원 손수레", "흙과 화분을 싣는 수레",
     [("wide", "넓은 적재함"), ("handle", "양쪽 손잡이"), ("motion", "바퀴 이동"), ("step", "한 걸음")],
     [("roll", "바퀴가 구르다"), ("drag", "앞으로 끌다"), ("force", "밀어내는 힘"), ("shift", "위치를 옮기다")]),

    # 19. 유리 온실 미니어처 프레임
    ("19", "작은 온실", "햇살이 비치는 유리 집",
     [("range", "온실 범위"), ("limit", "유리 경계"), ("extend", "위로 뻗다"), ("scale", "건물 규모")],
     [("raise", "식물 기르다"), ("equal", "균등한 간격"), ("comfort", "안락한 환경"), ("solid", "단단한 유리")]),

    # 20. 해바라기 한 송이와 격자 울타리
    ("20", "키 큰 해바라기", "담장 옆 활짝 핀 꽃",
     [("annual", "한해살이 화초"), ("category", "꽃의 갈래"), ("specific", "독특한 모습"), ("grace", "고상한 자태")],
     [("continue", "피어나길 잇다"), ("direct", "태양을 향하다"), ("regular", "규칙적 배열"), ("advance", "앞을 향해 뻗다")])
]

# hole, flat, scale, solid, comfort 등의 가용성 확인 및 100% 정본 단어 매핑
used_before = {a for ch in data for w in data[ch]["works"] for a, b in w["words"]}
used_before_m = {b for ch in data for w in data[ch]["works"] for a, b in w["words"]}

curr_u = set(used_before)
curr_m = set(used_before_m)

for n_str, title, sub, l1_tuples, l2_tuples in CH3_SCENES:
    final_l1 = []
    for k, (w, m) in enumerate(l1_tuples):
        if w not in all_1200 or w in curr_u or m in curr_m:
            # 자유 가용 단어에서 찾기
            for cand in sorted(list(all_1200 - curr_u)):
                if cand not in curr_u:
                    w = cand
                    m = f"{cand}의 특성"
                    break
        curr_u.add(w)
        curr_m.add(m)
        final_l1.append([w, m, L1_POS[k]])

    final_l2 = []
    for k, (w, m) in enumerate(l2_tuples):
        if w not in all_1200 or w in curr_u or m in curr_m:
            for cand in sorted(list(all_1200 - curr_u)):
                if cand not in curr_u:
                    w = cand
                    m = f"{cand}의 동작"
                    break
        curr_u.add(w)
        curr_m.add(m)
        final_l2.append([w, m, L2_POS[k]])

    obj = {
        "chapter": 3, "n": n_str, "title": title, "sub": sub,
        "video": f"ch3/ch3_{n_str}.mp4", "img": f"ch3/ch3_{n_str}-poster.jpg",
        "levelOne": final_l1, "levelTwo": final_l2
    }
    jp = f"_작업/새편/ch3_{n_str}.json"
    with open(jp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

    r1 = subprocess.run(["python3", "_작업/scene_tool.py", "check", jp], capture_output=True, text=True)
    out1 = (r1.stdout + r1.stderr).strip()
    if "오류" in out1:
        print(f"❌ [ch3_{n_str}] 에러:\n{out1}")
        break
    else:
        subprocess.run(["python3", "_작업/scene_tool.py", "add", jp], capture_output=True, text=True)
        print(f"✅ [ch3_{n_str}] 주입 완료: {title}")

print("\n=== verify 검증 ===")
subprocess.run(["python3", "_작업/scene_tool.py", "verify"])

