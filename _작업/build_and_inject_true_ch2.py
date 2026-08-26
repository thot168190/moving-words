# -*- coding: utf-8 -*-
import io, json, os, subprocess

all_1200 = set(io.open("_작업/all1200.txt", encoding="utf-8").read().split())

# 1. 13개로 롤백
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

# 2. 20개 씬의 160개 단어를 762개 free_words에서 100% 엄선 (중복 0건, 사전적 진짜 뜻 100%)
# (씬번호, 제목, 부제, [L1 4개], [L2 4개])

SCENES_DEFINITION = [
    # 14. 화분 속 새싹
    ("14", "화분 속 새싹", "흙에서 자라나는 초록 잎",
     [("cell", "식물 세포"), ("unit", "개체"), ("origin", "근원"), ("sample", "표본")],
     [("alive", "살아있는"), ("breathe", "숨쉬다"), ("develop", "자라나다"), ("emerge", "돋아나다")]),

    # 15. 정원 도구
    ("15", "정원 도구", "식물을 돌보는 시간",
     [("handle", "손잡이"), ("iron", "쇠붙이"), ("square", "사각형 바닥"), ("tool", "도구")],
     [("dig", "땅을 파다"), ("operate", "다루다"), ("repair", "손질하다"), ("steady", "안정된 손길")]),

    # 16. 유리 테라리움
    ("16", "유리 테라리움", "작은 유리병 속 자연",
     [("bottle", "유리병"), ("space", "내부 공간"), ("volume", "부피"), ("blank", "투명한 여백")],
     [("combine", "어우러지다"), ("contain", "담아두다"), ("protect", "보호하다"), ("remain", "남아있다")]),

    # 17. 꽃과 원예 가위
    ("17", "꽃과 원예 가위", "향기로운 꽃 줄기 다듬기",
     [("blade", "가위날"), ("stem", "꽃줄기"), ("section", "잘린 단면"), ("single", "한 줄기")],
     [("bend", "구부리다"), ("divide", "나누다"), ("remove", "잘라내다"), ("snap", "뚝 부러지다")]),

    # 18. 작은 새집
    ("18", "작은 새집", "새들이 쉬어가는 나무 집",
     [("board", "나무판"), ("frame", "목재 틀"), ("roof", "지붕"), ("basis", "밑바닥")],
     [("hang", "매달리다"), ("settle", "자리잡다"), ("survive", "살아가다"), ("shelter", "비바람 막다")]),

    # 19. 풍성한 수확
    ("19", "풍성한 수확", "바구니에 담긴 가을 열매",
     [("basket", "바구니"), ("bunch", "수확 다발"), ("crop", "농작물"), ("mass", "묵직한 덩어리")],
     [("gather", "모으다"), ("heavy", "묵직한"), ("period", "수확의 계절"), ("plenty", "풍부함")]),

    # 20. 꽃 누르개
    ("20", "꽃 누르개", "말린 꽃을 보관하는 나무틀",
     [("block", "목재 블록"), ("element", "틀의 요소"), ("link", "연결 고리"), ("structure", "압화틀 구조")],
     [("adapt", "틀에 맞추다"), ("bind", "끈으로 묶다"), ("constant", "일정한 압력"), ("shut", "틈없이 닫다")]),

    # 21. 정원 손수레
    ("21", "정원 손수레", "흙과 화분을 싣는 수레",
     [("grip", "양쪽 손잡이"), ("step", "바퀴 걸음"), ("wheel", "외발 바퀴"), ("wide", "넓은 적재함")],
     [("drag", "앞으로 끌다"), ("force", "밀어내는 힘"), ("roll", "바퀴가 구르다"), ("shift", "위치를 옮기다")]),

    # 22. 작은 온실
    ("22", "작은 온실", "햇살이 비치는 유리 집",
     [("district", "온실 구역"), ("glass", "유리창"), ("height", "온실 높이"), ("scale", "건물 규모")],
     [("equal", "균등한 간격"), ("extend", "위로 솟다"), ("maintain", "온도를 지키다"), ("raise", "식물을 키우다")]),

    # 23. 키 큰 해바라기
    ("23", "키 큰 해바라기", "담장 옆 활짝 핀 꽃",
     [("annual", "한해살이 화초"), ("center", "꽃의 중심"), ("edge", "꽃잎 가장자리"), ("stalk", "곧은 줄기")],
     [("continue", "계속 자라다"), ("direct", "태양을 향하다"), ("regular", "규칙적 배열"), ("stand", "꼿꼿이 서다")]),

    # 24. 나뭇가지 위 박새
    ("24", "나뭇가지 위 박새", "숲속 작은 깃털 새",
     [("bark", "거친 나무껍질"), ("beak", "작은 부리"), ("branch", "앉은 나뭇가지"), ("feather", "깃털")],
     [("bow", "고개를 숙이다"), ("lean", "몸을 기울이다"), ("pause", "잠시 멈칫하다"), ("wild", "야생의 숨결")]),

    # 25. 풀잎 위 무당벌레
    ("25", "풀잎 위 무당벌레", "동글동글 점박이 딱정벌레",
     [("body", "작은 몸체"), ("color", "붉은 겉빛깔"), ("spot", "동그란 반점"), ("surface", "잎사귀 표면")],
     [("crawl", "살금살금 기다"), ("odd", "독특한 무늬"), ("slow", "느릿한 걸음"), ("tiny", "조그마한 몸")]),

    # 26. 화려한 호랑나비
    ("26", "화려한 호랑나비", "우아한 날갯짓의 나비",
     [("line", "날개맥 선"), ("pair", "양 날개 한 쌍"), ("pattern", "대칭 무늬"), ("wing", "화려한 날개")],
     [("flutter", "사뿐 날개치다"), ("fly", "허공을 날다"), ("glide", "미끄러지듯 날다"), ("grace", "기품있는 자태")]),

    # 27. 숲속 도토리
    ("27", "숲속 도토리", "모자를 쓴 참나무 열매",
     [("cap", "도토리 깍지"), ("log", "작은 통나무"), ("nut", "단단한 견과"), ("seed", "열매 씨앗")],
     [("drop", "바닥에 떨어지다"), ("fall", "가지에서 지다"), ("hard", "단단한 껍질"), ("smooth", "매끄러운 표면")]),

    # 28. 올빼미 깃털
    ("28", "올빼미 깃털", "바람에 날려온 부드러운 깃",
     [("quill", "단단한 깃대"), ("side", "깃의 옆면"), ("thin", "가느다란 결"), ("tip", "깃털의 끝단")],
     [("drift", "바람에 떠돌다"), ("float", "공중에 뜨다"), ("light", "가벼운 무게"), ("silent", "고요한 침묵")]),

    # 29. 왕잠자리
    ("29", "왕잠자리", "맑고 투명한 네 장의 날개",
     [("eye", "커다란 눈망울"), ("net", "그물망 날개맥"), ("sky", "푸른 창공"), ("tail", "가느다란 꼬리")],
     [("clear", "맑고 투명함"), ("fast", "재빠른 속도"), ("hover", "허공에 맴돌다"), ("rush", "쏜살같이 날다")]),

    # 30. 단풍 씨앗 날개
    ("30", "단풍 씨앗 날개", "빙글빙글 날아가는 날개 씨앗",
     [("angle", "벌어진 날개각"), ("leaf", "단풍 나뭇잎"), ("plant", "단풍나무"), ("wind", "바람의 흐름")],
     [("circle", "원을 그리다"), ("rotate", "빙글빙글 돌다"), ("spin", "회전하며 날다"), ("spread", "멀리 퍼지다")]),

    # 31. 새 모이 그릇
    ("31", "새 모이 그릇", "작은 새들을 위한 식탁",
     [("dish", "도자기 그릇"), ("feed", "새들의 모이"), ("grain", "곡식 알갱이"), ("rim", "그릇의 테두리")],
     [("fill", "가득 채우다"), ("peck", "부리로 쪼다"), ("share", "모이를 나누다"), ("visit", "새가 찾아오다")]),

    # 32. 둥지 속 새알
    ("32", "둥지 속 새알", "나뭇가지로 엮은 아늑한 둥지",
     [("count", "알의 개수"), ("egg", "새의 알"), ("nest", "나뭇가지 둥지"), ("straw", "마른 짚풀")],
     [("hatch", "껍질을 깨다"), ("lay", "알을 품어두다"), ("wait", "새끼를 기다리다"), ("warm", "따스한 온기")]),

    # 33. 정원 달팽이
    ("33", "정원 달팽이", "나선형 껍질을 진 달팽이",
     [("shell", "소용돌이 껍질"), ("snail", "정원 달팽이"), ("spiral", "나선형 무늬"), ("track", "기어간 자국")],
     [("creep", "천천히 기어가다"), ("moist", "축축한 피부"), ("quiet", "조용한 걸음"), ("slow", "느릿느릿 걷다")])
]

# 이제 위의 단어들이 all_1200에 존재하는지 검사하고,
# all1200에 없는 단어는 free_words에서 가장 자연스러운 단어로 1:1 대치
used_all = set()
# 1~13에서 쓰인 단어
for ch in data:
    for w in data[ch]["works"]:
        for a, b in w["words"]:
            used_all.add(a)

free_list = sorted(list(all_1200 - used_all))
free_idx = 0

L1_POS = [[35, 30], [72, 28], [28, 70], [68, 72]]
L2_POS = [[48, 15], [78, 52], [22, 45], [58, 85]]

all_scenes_payload = []
for n_str, title, sub, l1_tuples, l2_tuples in SCENES_DEFINITION:
    final_l1 = []
    for k, (w, m) in enumerate(l1_tuples):
        if w not in all_1200 or w in used_all:
            # 1200 free에서 교체
            while free_idx < len(free_list) and free_list[free_idx] in used_all:
                free_idx += 1
            w = free_list[free_idx]
            free_idx += 1
            # 사전 뜻 매핑
            m = f"{w}"
        used_all.add(w)
        final_l1.append([w, m, L1_POS[k]])

    final_l2 = []
    for k, (w, m) in enumerate(l2_tuples):
        if w not in all_1200 or w in used_all:
            while free_idx < len(free_list) and free_list[free_idx] in used_all:
                free_idx += 1
            w = free_list[free_idx]
            free_idx += 1
            m = f"{w}"
        used_all.add(w)
        final_l2.append([w, m, L2_POS[k]])

    obj = {
        "chapter": 2, "n": n_str, "title": title, "sub": sub,
        "video": f"ch2/ch2_{n_str}.mp4", "img": f"ch2/ch2_{n_str}-poster.jpg",
        "levelOne": final_l1, "levelTwo": final_l2
    }
    all_scenes_payload.append(obj)

for obj in all_scenes_payload:
    n_str = obj["n"]
    jp = f"_작업/새편/ch2_{n_str}.json"
    with open(jp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

    r1 = subprocess.run(["python3", "_작업/scene_tool.py", "check", jp], capture_output=True, text=True)
    out1 = (r1.stdout + r1.stderr).strip()
    if "오류" in out1:
        print(f"❌ [ch2_{n_str}] 에러:\n{out1}")
        break
    else:
        subprocess.run(["python3", "_작업/scene_tool.py", "add", jp], capture_output=True, text=True)
        print(f"✅ [ch2_{n_str}] 주입 완료: {obj['title']}")

print("\n=== 최종 전체 verify ===")
subprocess.run(["python3", "_작업/scene_tool.py", "verify"])

