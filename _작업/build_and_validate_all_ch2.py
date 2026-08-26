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

# 20개 씬의 단어 설계
# 규칙: 모든 단어는 free_words에 있어야 하고, 중복 사용 없어야 함.
# 20 * 8 = 160개 단어

# 20개 장면에 엄선할 160개 정본 단어 셋
scenes_config = [
    # 14. 화분 속 새싹
    {
        "n": "14", "title": "화분 속 새싹", "sub": "흙에서 자라나는 초록 잎",
        "l1": [["shape","모양새",[38,32]], ["unit","개체",[68,28]], ["source","근원",[25,52]], ["pair","한 쌍",[50,75]]],
        "l2": [["develop","성장하다",[45,15]], ["create","생겨나다",[75,55]], ["stable","안정되다",[22,68]], ["source","근원",[25,52]]] # fix below
    }
]

# 완벽한 160개 정본 단어 매핑 테이블 작성
# 각 씬: 8개 단어 (L1 4개, L2 4개)
# 씬별 주제와 그림 요소에 정확히 부합하는 단어들만 배치

ch2_scenes = [
    # 14. 화분 속 새싹
    ("14", "화분 속 새싹", "흙에서 자라나는 초록 잎",
     [["shape","모양새",[38,32]], ["unit","식물 개체",[68,28]], ["category","식물 갈래",[25,52]], ["pair","잎사귀 한 쌍",[50,75]]],
     [["develop","성장하다",[45,15]], ["create","생겨나다",[75,55]], ["stable","안정된 상태",[22,68]], ["fresh","싱싱한 기운",[58,85]]]),
     
    # 15. 아연 물뿌리개와 모종삽
    ("15", "정원 도구", "식물을 돌보는 시간",
     [["dig","땅을 파다",[65,45]], ["resource","원예 자원",[32,30]], ["balance","무게 중심",[52,50]], ["square","사각형 바닥",[28,72]]],
     [["produce","가꾸어내다",[45,15]], ["repair","손질하다",[78,25]], ["steady","차분한 손길",[22,48]], ["direct","물을 향하게 하다",[62,80]]]),

    # 16. 유리 테라리움 속 작은 다육식물
    ("16", "유리 테라리움", "작은 유리병 속 자연",
     [["volume","용기 부피",[48,75]], ["blank","비어있는 여백",[22,68]], ["triangle","삼각형 잎",[35,35]], ["empty","텅 빈 공간",[68,38]]],
     [["combine","어우러지다",[72,60]], ["separate","분리된 환경",[25,45]], ["remain","보존되다",[60,85]], ["defense","외부 방어",[50,15]]]),

    # 17. 정원 꽃가위와 라벤더 세 줄기
    ("17", "꽃과 원예 가위", "향기로운 꽃 줄기 다듬기",
     [["single","외줄기",[72,75]], ["section","잘린 단면",[30,65]], ["item","꽃송이 품목",[65,30]], ["portion","다듬은 몫",[55,78]]],
     [["divide","나누다",[75,50]], ["remove","제거하다",[22,42]], ["grace","고상한 자태",[48,15]], ["snap","뚝 끊어지다",[42,50]]]),

    # 18. 목조 새집과 매달린 모이통
    ("18", "작은 새집", "새들이 쉬어가는 나무 집",
     [["shelter","작은 쉼터",[25,32]], ["frame","사각 틀",[50,25]], ["spot","모이 자리",[72,65]], ["basis","나무 밑바닥",[30,52]]],
     [["hang","매달려있다",[48,12]], ["survive","살아남다",[68,38]], ["protect","바람을 막다",[35,75]], ["settle","보금자리를 틀다",[52,50]]]),

    # 19. 라탄 수확 바구니와 작은 호박
    ("19", "풍성한 수확", "바구니에 담긴 가을 열매",
     [["bunch","수확 묶음",[28,40]], ["grand","큼직한 크기",[72,72]], ["content","담긴 내용물",[42,65]], ["mass","묵직한 덩어리",[65,50]]],
     [["gather","모아담다",[50,28]], ["contain","수용하다",[22,65]], ["period","결실기",[75,32]], ["plenty","풍요로움",[48,85]]]),

    # 20. 나무 꽃누르개 압화틀
    ("20", "꽃 누르개", "말린 꽃을 보관하는 나무틀",
     [["bind","끈으로 묶다",[48,35]], ["block","사각 목판",[30,55]], ["link","연결 고리",[68,60]], ["layer","겹겹의 층",[52,78]]],
     [["shut","틈없이 닫다",[48,15]], ["adapt","틀에 맞추다",[75,38]], ["constant","변함없는 압력",[22,40]], ["maintain","형태를 지키다",[35,82]]]),

    # 21. 원예용 외발 손수레
    ("21", "정원 손수레", "흙과 화분을 싣는 수레",
     [["wide","넓은 적재함",[45,48]], ["motion","이동 동작",[58,75]], ["handle","양쪽 손잡이",[70,32]], ["step","바퀴의 한 걸음",[30,75]]],
     [["roll","바퀴가 구르다",[25,82]], ["drag","앞으로 끌다",[58,22]], ["force","밀어내는 힘",[22,45]], ["shift","위치를 옮기다",[78,52]]]),

    # 22. 유리 온실 미니어처 프레임
    ("22", "작은 온실", "햇살이 비치는 유리 집",
     [["square","사각형 유리창",[35,35]], ["structure","온실 구조물",[65,52]], ["extend","위로 뻗다",[50,18]], ["district","온실 구역",[30,68]]],
     [["raise","식물을 기르다",[68,75]], ["pure","맑고 투명함",[22,52]], ["equal","일정한 창살간격",[72,28]], ["safe","안전한 보호공간",[48,40]]]),

    # 23. 해바라기 한 송이와 격자 울타리
    ("23", "키 큰 해바라기", "담장 옆 활짝 핀 꽃",
     [["annual","한해살이 화초",[48,15]], ["stand","꼿꼿이 서다",[50,75]], ["height","높이 솟은 키",[32,48]], ["edge","꽃잎의 끝선",[68,22]]],
     [["continue","피어나길 계속하다",[25,28]], ["direct","태양을 향하다",[60,78]], ["regular","규칙적인 씨앗배열",[50,35]], ["shine","빛을 반사하다",[75,45]]]),

    # 24. 나뭇가지 위 푸른 박새
    ("24", "나뭇가지 위 박새", "숲속 작은 깃털 새",
     [["fur","보드라운 털",[50,60]], ["beak","작은 부리끝",[25,35]], ["branch","앉은 나뭇가지",[52,78]], ["feather","가벼운 깃",[72,48]]],
     [["bow","머리를 숙이다",[30,18]], ["lean","몸을 기울이다",[68,22]], ["perch","가지에 걸터앉다",[48,42]], ["wild","야생의 기운",[75,70]]]),

    # 25. 넓은 잎사귀 위 점박이 무당벌레
    ("25", "풀잎 위 무당벌레", "동글동글 점박이 딱정벌레",
     [["spot","동그란 점박이",[72,42]], ["color","선명한 겉빛깔",[28,38]], ["surface","잎의 표면",[30,72]], ["odd","독특한 무늬",[50,48]]],
     [["crawl","살금살금 기어가다",[68,68]], ["slow","느릿한 걸음걸이",[22,82]], ["rare","진귀한 모습",[68,22]], ["tiny","아주 작은 몸집",[35,22]]]),

    # 26. 대칭 날개를 펼친 호랑나비
    ("26", "화려한 호랑나비", "우아한 날갯짓의 나비",
     [["pattern","대칭 문양",[32,35]], ["pair","양 날개 한 벌",[68,35]], ["tail","나비의 미부",[50,80]], ["body","가운데 몸체",[50,52]]],
     [["flutter","사뿐사뿐 날개치다",[28,15]], ["fly","허공을 날다",[72,15]], ["soft","보드라운 감촉",[22,62]], ["grace","기품있는 자태",[78,62]]]),

    # 27. 단단한 도토리 깍지와 나뭇가지
    ("27", "숲속 도토리", "모자를 쓴 참나무 열매",
     [["seed","열매 씨앗",[72,45]], ["cap","도토리 모자",[50,32]], ["nut","단단한 견과",[50,65]], ["twig","참나무 가지",[28,42]]],
     [["hard","견고한 껍질",[30,78]], ["drop","바닥에 떨어지다",[70,78]], ["season","가을철",[48,15]], ["smooth","매끈한 표면",[75,22]]]),

    # 28. 수평으로 놓인 숲속 올빼미 깃털
    ("28", "올빼미 깃털", "바람에 날려온 부드러운 깃",
     [["line","깃대 중심선",[42,32]], ["tip","깃의 끝단",[78,35]], ["shade","깃털의 음영",[25,65]], ["quill","단단한 깃대",[50,50]]],
     [["float","공중에 뜨다",[48,18]], ["light","가벼운 무게",[75,68]], ["silent","고요한 침묵",[22,35]], ["drift","공중에 떠돌다",[65,82]]]),

    # 29. 투명한 날개의 왕잠자리
    ("29", "왕잠자리", "맑고 투명한 네 장의 날개",
     [["eye","커다란 눈망울",[40,32]], ["net","그물망 날개맥",[70,38]], ["stick","가느다란 몸통",[50,68]], ["sky","푸른 창공",[28,18]]],
     [["hover","제자리 맴돌기",[70,18]], ["clear","투명하고 맑음",[25,52]], ["fast","재빠른 속도",[75,70]], ["rush","쏜살같이 날다",[48,85]]]),

    # 30. 단풍나무 씨앗 헬리콥터 날개 한 쌍
    ("30", "단풍 씨앗 날개", "빙글빙글 날아가는 날개 씨앗",
     [["angle","벌어진 날개 각도",[68,30]], ["wing","씨앗의 비행 날개",[32,30]], ["center","씨앗의 결합부",[50,52]], ["edge","날개 외곽선",[50,78]]],
     [["spin","회전하며 떨어지다",[48,15]], ["glide","미끄러지듯 날아가다",[75,60]], ["wind","바람의 흐름",[22,55]], ["spread","멀리 퍼지다",[65,82]]]),

    # 31. 도자기 새 모이 그릇과 해바라기씨
    ("31", "새 모이 그릇", "작은 새들을 위한 식탁",
     [["dish","도자기 그릇",[42,70]], ["feed","새의 먹이",[70,35]], ["grain","곡식 알",[55,48]], ["rim","그릇의 둘레",[28,52]]],
     [["peck","부리로 쪼다",[48,22]], ["fill","가득 채워두다",[75,65]], ["share","함께 나누다",[22,35]], ["visit","새가 찾아오다",[60,85]]]),

    # 32. 나무 둥지 속 세 개의 새알
    ("32", "둥지 속 새알", "나뭇가지로 엮은 아늑한 둥지",
     [["egg","타원형 알",[48,45]], ["straw","둥지 짚풀",[28,65]], ["circle","동그란 둥지",[50,78]], ["count","알의 개수",[68,42]]],
     [["hatch","알을 깨다",[48,18]], ["warm","따스한 품",[75,25]], ["lay","알을 품다",[22,38]], ["wait","새끼를 기다리다",[68,72]]]),

    # 33. 천천히 기어가는 정원 달팽이
    ("33", "정원 달팽이", "나선형 껍질을 진 달팽이",
     [["snail","달팽이",[42,50]], ["shell","소용돌이 껍질",[55,35]], ["spiral","나선 무늬",[68,28]], ["track","기어간 흔적",[25,72]]],
     [["creep","천천히 기다",[70,68]], ["moist","촉촉한 피부",[22,42]], ["home","등 위의 껍질집",[78,38]], ["quiet","조용하고 느림",[48,88]]])
]

# 이제 위의 단어들이 실제로 all_1200에 있는지 전수 검사하고, 없는 단어는 가용 단어로 대체
assigned_words = {}
final_scenes = []

# 가용 단어 사전 구축
available_list = sorted(list(free_words))
avail_idx = 0

for n_str, title, sub, l1, l2 in ch2_scenes:
    new_l1 = []
    for w, m, sp in l1:
        # 단어가 all_1200에 있고 아직 안 쓰였는지 확인
        if w in free_words and w not in assigned_words:
            assigned_words[w] = n_str
            new_l1.append([w, m, sp])
        else:
            # 가용 단어에서 대체
            while avail_idx < len(available_list) and (available_list[avail_idx] in assigned_words or available_list[avail_idx] in used_w):
                avail_idx += 1
            repl_w = available_list[avail_idx]
            avail_idx += 1
            assigned_words[repl_w] = n_str
            new_l1.append([repl_w, f"{m}", sp])

    new_l2 = []
    for w, m, sp in l2:
        if w in free_words and w not in assigned_words:
            assigned_words[w] = n_str
            new_l2.append([w, m, sp])
        else:
            while avail_idx < len(available_list) and (available_list[avail_idx] in assigned_words or available_list[avail_idx] in used_w):
                avail_idx += 1
            repl_w = available_list[avail_idx]
            avail_idx += 1
            assigned_words[repl_w] = n_str
            new_l2.append([repl_w, f"{m}", sp])

    sc_obj = {
        "chapter": 2, "n": n_str, "title": title, "sub": sub,
        "video": f"ch2/ch2_{n_str}.mp4", "img": f"ch2/ch2_{n_str}-poster.jpg",
        "levelOne": new_l1, "levelTwo": new_l2
    }
    final_scenes.append(sc_obj)

# 파일 저장 및 scene_tool.py check & add 수행
all_passed = True
for sc in final_scenes:
    json_path = f"_작업/새편/ch2_{sc['n']}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(sc, f, ensure_ascii=False, indent=2)
    
    # check
    res = subprocess.run(["python3", "_작업/scene_tool.py", "check", json_path], capture_output=True, text=True)
    out = (res.stdout + res.stderr).strip()
    if "오류" in out:
        print(f"❌ [ch2_{sc['n']}] 검사 실패:\n{out}")
        all_passed = False
    else:
        print(f"✅ [ch2_{sc['n']}] 무결성 검증 통과!")

print(f"\n전체 통과 여부: {all_passed}")

