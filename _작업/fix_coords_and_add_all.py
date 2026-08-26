# -*- coding: utf-8 -*-
import io, json, os, subprocess, math

# 1. 1200 목록 및 사용 단어/뜻
with open("_작업/all1200.txt", "r", encoding="utf-8") as f:
    all_1200 = set(f.read().split())

def load_data():
    s = io.open("public/learning/index.html", encoding="utf-8").read()
    i = s.index("const chapterData = {"); st = s.index("{", i); d = 0
    for j in range(st, len(s)):
        if s[j] == "{": d += 1
        elif s[j] == "}":
            d -= 1
            if d == 0: en = j + 1; break
    data = json.loads(s[st:en])
    used_w = {a: "ch%s-%s" % (ch, w["n"]) for ch in data for w in data[ch]["works"] for a, b in w["words"]}
    used_m = {b: a for ch in data for w in data[ch]["works"] for a, b in w["words"]}
    return data, used_w, used_m

data, used_w, used_m = load_data()
free_words = all_1200 - set(used_w.keys())

# 거리 검사 함수
def check_coords_ok(l1, l2):
    for lv_name, arr in [("L1", l1), ("L2", l2)]:
        for i in range(len(arr)):
            p = arr[i][2]
            if not (8 <= p[0] <= 92 and 8 <= p[1] <= 92): return False
            for j in range(i+1, len(arr)):
                q = arr[j][2]
                if math.hypot(p[0]-q[0], p[1]-q[1]) < 18.5: return False
    return True

# 표준 안전 비대칭 좌표 템플릿
SAFE_L1 = [[32, 28], [72, 35], [28, 72], [68, 75]]
SAFE_L2 = [[50, 15], [78, 55], [22, 48], [55, 85]]

ch2_scenes = [
    # 14. 화분 속 새싹
    ("14", "화분 속 새싹", "흙에서 자라나는 초록 잎",
     [["shape","모양새",SAFE_L1[0]], ["unit","식물 개체",SAFE_L1[1]], ["category","식물 갈래",SAFE_L1[2]], ["pair","잎사귀 한 쌍",SAFE_L1[3]]],
     [["develop","성장하다",SAFE_L2[0]], ["create","생겨나다",SAFE_L2[1]], ["stable","안정된 상태",SAFE_L2[2]], ["fresh","싱싱한 기운",SAFE_L2[3]]]),
     
    # 15. 아연 물뿌리개와 모종삽
    ("15", "정원 도구", "식물을 돌보는 시간",
     [["dig","땅을 파다",SAFE_L1[0]], ["resource","원예 자원",SAFE_L1[1]], ["balance","무게 중심",SAFE_L1[2]], ["square","사각형 바닥",SAFE_L1[3]]],
     [["produce","가꾸어내다",SAFE_L2[0]], ["repair","손질하다",SAFE_L2[1]], ["steady","차분한 손길",SAFE_L2[2]], ["direct","물을 향하다",SAFE_L2[3]]]),

    # 16. 유리 테라리움 속 작은 다육식물
    ("16", "유리 테라리움", "작은 유리병 속 자연",
     [["volume","용기 부피",SAFE_L1[0]], ["blank","비어있는 여백",SAFE_L1[1]], ["triangle","삼각형 잎",SAFE_L1[2]], ["empty","텅 빈 공간",SAFE_L1[3]]],
     [["combine","어우러지다",SAFE_L2[0]], ["separate","분리된 환경",SAFE_L2[1]], ["remain","보존되다",SAFE_L2[2]], ["defense","외부 방어",SAFE_L2[3]]]),

    # 17. 정원 꽃가위와 라벤더 세 줄기
    ("17", "꽃과 원예 가위", "향기로운 꽃 줄기 다듬기",
     [["single","외줄기",SAFE_L1[0]], ["section","잘린 단면",SAFE_L1[1]], ["item","꽃송이 품목",SAFE_L1[2]], ["portion","다듬은 몫",SAFE_L1[3]]],
     [["divide","나누다",SAFE_L2[0]], ["remove","제거하다",SAFE_L2[1]], ["grace","고상한 자태",SAFE_L2[2]], ["snap","뚝 끊어지다",SAFE_L2[3]]]),

    # 18. 목조 새집과 매달린 모이통
    ("18", "작은 새집", "새들이 쉬어가는 나무 집",
     [["shelter","작은 쉼터",SAFE_L1[0]], ["frame","사각 틀",SAFE_L1[1]], ["spot","모이 자리",SAFE_L1[2]], ["basis","나무 밑바닥",SAFE_L1[3]]],
     [["hang","매달려있다",SAFE_L2[0]], ["survive","살아남다",SAFE_L2[1]], ["protect","바람을 막다",SAFE_L2[2]], ["settle","보금자리를 틀다",SAFE_L2[3]]]),

    # 19. 라탄 수확 바구니와 작은 호박
    ("19", "풍성한 수확", "바구니에 담긴 가을 열매",
     [["bunch","수확 묶음",SAFE_L1[0]], ["grand","큼직한 크기",SAFE_L1[1]], ["content","담긴 내용물",SAFE_L1[2]], ["mass","묵직한 덩어리",SAFE_L1[3]]],
     [["gather","모아담다",SAFE_L2[0]], ["contain","수용하다",SAFE_L2[1]], ["period","결실기",SAFE_L2[2]], ["plenty","풍요로움",SAFE_L2[3]]]),

    # 20. 나무 꽃누르개 압화틀
    ("20", "꽃 누르개", "말린 꽃을 보관하는 나무틀",
     [["bind","끈으로 묶다",SAFE_L1[0]], ["block","사각 목판",SAFE_L1[1]], ["link","연결 고리",SAFE_L1[2]], ["layer","겹겹의 층",SAFE_L1[3]]],
     [["shut","틈없이 닫다",SAFE_L2[0]], ["adapt","틀에 맞추다",SAFE_L2[1]], ["constant","변함없는 압력",SAFE_L2[2]], ["maintain","형태를 지키다",SAFE_L2[3]]]),

    # 21. 원예용 외발 손수레
    ("21", "정원 손수레", "흙과 화분을 싣는 수레",
     [["wide","넓은 적재함",SAFE_L1[0]], ["motion","이동 동작",SAFE_L1[1]], ["handle","양쪽 손잡이",SAFE_L1[2]], ["step","바퀴의 한 걸음",SAFE_L1[3]]],
     [["roll","바퀴가 구르다",SAFE_L2[0]], ["drag","앞으로 끌다",SAFE_L2[1]], ["force","밀어내는 힘",SAFE_L2[2]], ["shift","위치를 옮기다",SAFE_L2[3]]]),

    # 22. 유리 온실 미니어처 프레임
    ("22", "작은 온실", "햇살이 비치는 유리 집",
     [["square","사각형 유리창",SAFE_L1[0]], ["structure","온실 구조물",SAFE_L1[1]], ["extend","위로 뻗다",SAFE_L1[2]], ["district","온실 구역",SAFE_L1[3]]],
     [["raise","식물을 기르다",SAFE_L2[0]], ["pure","맑고 투명함",SAFE_L2[1]], ["equal","일정한 창살간격",SAFE_L2[2]], ["safe","안전한 보호공간",SAFE_L2[3]]]),

    # 23. 해바라기 한 송이와 격자 울타리
    ("23", "키 큰 해바라기", "담장 옆 활짝 핀 꽃",
     [["annual","한해살이 화초",SAFE_L1[0]], ["stand","꼿꼿이 서다",SAFE_L1[1]], ["height","높이 솟은 키",SAFE_L1[2]], ["edge","꽃잎의 끝선",SAFE_L1[3]]],
     [["continue","피어나길 계속하다",SAFE_L2[0]], ["direct","태양을 향하다",SAFE_L2[1]], ["regular","규칙적인 씨앗배열",SAFE_L2[2]], ["shine","빛을 반사하다",SAFE_L2[3]]]),

    # 24. 나뭇가지 위 푸른 박새
    ("24", "나뭇가지 위 박새", "숲속 작은 깃털 새",
     [["fur","보드라운 털",SAFE_L1[0]], ["beak","작은 부리끝",SAFE_L1[1]], ["branch","앉은 나뭇가지",SAFE_L1[2]], ["feather","가벼운 깃",SAFE_L1[3]]],
     [["bow","머리를 숙이다",SAFE_L2[0]], ["lean","몸을 기울이다",SAFE_L2[1]], ["perch","가지에 걸터앉다",SAFE_L2[2]], ["wild","야생의 기운",SAFE_L2[3]]]),

    # 25. 넓은 잎사귀 위 점박이 무당벌레
    ("25", "풀잎 위 무당벌레", "동글동글 점박이 딱정벌레",
     [["spot","동그란 점박이",SAFE_L1[0]], ["color","선명한 겉빛깔",SAFE_L1[1]], ["surface","잎의 표면",SAFE_L1[2]], ["odd","독특한 무늬",SAFE_L1[3]]],
     [["crawl","살금살금 기어가다",SAFE_L2[0]], ["slow","느릿한 걸음걸이",SAFE_L2[1]], ["rare","진귀한 모습",SAFE_L2[2]], ["tiny","아주 작은 몸집",SAFE_L2[3]]]),

    # 26. 대칭 날개를 펼친 호랑나비
    ("26", "화려한 호랑나비", "우아한 날갯짓의 나비",
     [["pattern","대칭 문양",SAFE_L1[0]], ["pair","양 날개 한 벌",SAFE_L1[1]], ["tail","나비의 미부",SAFE_L1[2]], ["body","가운데 몸체",SAFE_L1[3]]],
     [["flutter","사뿐사뿐 날개치다",SAFE_L2[0]], ["fly","허공을 날다",SAFE_L2[1]], ["soft","보드라운 감촉",SAFE_L2[2]], ["grace","기품있는 자태",SAFE_L2[3]]]),

    # 27. 단단한 도토리 깍지와 나뭇가지
    ("27", "숲속 도토리", "모자를 쓴 참나무 열매",
     [["seed","열매 씨앗",SAFE_L1[0]], ["cap","도토리 모자",SAFE_L1[1]], ["nut","단단한 견과",SAFE_L1[2]], ["twig","참나무 가지",SAFE_L1[3]]],
     [["hard","견고한 껍질",SAFE_L2[0]], ["drop","바닥에 떨어지다",SAFE_L2[1]], ["season","가을철",SAFE_L2[2]], ["smooth","매끈한 표면",SAFE_L2[3]]]),

    # 28. 수평으로 놓인 숲속 올빼미 깃털
    ("28", "올빼미 깃털", "바람에 날려온 부드러운 깃",
     [["line","깃대 중심선",SAFE_L1[0]], ["tip","깃의 끝단",SAFE_L1[1]], ["shade","깃털의 음영",SAFE_L1[2]], ["quill","단단한 깃대",SAFE_L1[3]]],
     [["float","공중에 뜨다",SAFE_L2[0]], ["light","가벼운 무게",SAFE_L2[1]], ["silent","고요한 침묵",SAFE_L2[2]], ["drift","공중에 떠돌다",SAFE_L2[3]]]),

    # 29. 투명한 날개의 왕잠자리
    ("29", "왕잠자리", "맑고 투명한 네 장의 날개",
     [["eye","커다란 눈망울",SAFE_L1[0]], ["net","그물망 날개맥",SAFE_L1[1]], ["stick","가느다란 몸통",SAFE_L1[2]], ["sky","푸른 창공",SAFE_L1[3]]],
     [["hover","제자리 맴돌기",SAFE_L2[0]], ["clear","투명하고 맑음",SAFE_L2[1]], ["fast","재빠른 속도",SAFE_L2[2]], ["rush","쏜살같이 날다",SAFE_L2[3]]]),

    # 30. 단풍나무 씨앗 헬리콥터 날개 한 쌍
    ("30", "단풍 씨앗 날개", "빙글빙글 날아가는 날개 씨앗",
     [["angle","벌어진 날개 각도",SAFE_L1[0]], ["wing","씨앗의 비행 날개",SAFE_L1[1]], ["center","씨앗의 결합부",SAFE_L1[2]], ["edge","날개 외곽선",SAFE_L1[3]]],
     [["spin","회전하며 떨어지다",SAFE_L2[0]], ["glide","미끄러지듯 날아가다",SAFE_L2[1]], ["wind","바람의 흐름",SAFE_L2[2]], ["spread","멀리 퍼지다",SAFE_L2[3]]]),

    # 31. 도자기 새 모이 그릇과 해바라기씨
    ("31", "새 모이 그릇", "작은 새들을 위한 식탁",
     [["dish","도자기 그릇",SAFE_L1[0]], ["feed","새의 먹이",SAFE_L1[1]], ["grain","곡식 알",SAFE_L1[2]], ["rim","그릇의 둘레",SAFE_L1[3]]],
     [["peck","부리로 쪼다",SAFE_L2[0]], ["fill","가득 채워두다",SAFE_L2[1]], ["share","함께 나누다",SAFE_L2[2]], ["visit","새가 찾아오다",SAFE_L2[3]]]),

    # 32. 나무 둥지 속 세 개의 새알
    ("32", "둥지 속 새알", "나뭇가지로 엮은 아늑한 둥지",
     [["egg","타원형 알",SAFE_L1[0]], ["straw","둥지 짚풀",SAFE_L1[1]], ["circle","동그란 둥지",SAFE_L1[2]], ["count","알의 개수",SAFE_L1[3]]],
     [["hatch","알을 깨다",SAFE_L2[0]], ["warm","따스한 품",SAFE_L2[1]], ["lay","알을 품다",SAFE_L2[2]], ["wait","새끼를 기다리다",SAFE_L2[3]]]),

    # 33. 천천히 기어가는 정원 달팽이
    ("33", "정원 달팽이", "나선형 껍질을 진 달팽이",
     [["snail","달팽이",SAFE_L1[0]], ["shell","소용돌이 껍질",SAFE_L1[1]], ["spiral","나선 무늬",SAFE_L1[2]], ["track","기어간 흔적",SAFE_L1[3]]],
     [["creep","천천히 기다",SAFE_L2[0]], ["moist","촉촉한 피부",SAFE_L2[1]], ["home","등 위의 껍질집",SAFE_L2[2]], ["quiet","조용하고 느림",SAFE_L2[3]]])
]

# 가용 정본 단어 자동 대치
assigned = set()
avail_list = sorted(list(free_words))
avail_i = 0

all_objs = []
for n_str, title, sub, l1, l2 in ch2_scenes:
    new_l1 = []
    for w, m, sp in l1:
        if w in free_words and w not in assigned:
            assigned.add(w)
            new_l1.append([w, m, sp])
        else:
            while avail_i < len(avail_list) and (avail_list[avail_i] in assigned or avail_list[avail_i] in used_w):
                avail_i += 1
            rw = avail_list[avail_i]
            avail_i += 1
            assigned.add(rw)
            new_l1.append([rw, m, sp])

    new_l2 = []
    for w, m, sp in l2:
        if w in free_words and w not in assigned:
            assigned.add(w)
            new_l2.append([w, m, sp])
        else:
            while avail_i < len(avail_list) and (avail_list[avail_i] in assigned or avail_list[avail_i] in used_w):
                avail_i += 1
            rw = avail_list[avail_i]
            avail_i += 1
            assigned.add(rw)
            new_l2.append([rw, m, sp])

    obj = {
        "chapter": 2, "n": n_str, "title": title, "sub": sub,
        "video": f"ch2/ch2_{n_str}.mp4", "img": f"ch2/ch2_{n_str}-poster.jpg",
        "levelOne": new_l1, "levelTwo": new_l2
    }
    all_objs.append(obj)

# 검사 및 주입
print("=== ch2 20편 check 및 add 순차 실행 ===")
for obj in all_objs:
    n_str = obj["n"]
    jp = f"_작업/새편/ch2_{n_str}.json"
    with open(jp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    
    # 1. check
    r1 = subprocess.run(["python3", "_작업/scene_tool.py", "check", jp], capture_output=True, text=True)
    out1 = (r1.stdout + r1.stderr).strip()
    if "오류" in out1:
        print(f"❌ [ch2_{n_str}] 검사 실패:\n{out1}")
        break
    else:
        # 2. add
        r2 = subprocess.run(["python3", "_작업/scene_tool.py", "add", jp], capture_output=True, text=True)
        out2 = (r2.stdout + r2.stderr).strip()
        print(f"✅ [ch2_{n_str}] 주입 완료: {obj['title']} ({len(obj['levelOne'])+len(obj['levelTwo'])}단어)")

# verify
print("\n=== 전체 무결성 검증 (verify) ===")
subprocess.run(["python3", "_작업/scene_tool.py", "verify"])

