# -*- coding: utf-8 -*-
import io, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "public/learning/index.html")
ALL_TXT = os.path.join(ROOT, "_작업/all1200.txt")

all_1200 = set(io.open(ALL_TXT, encoding="utf-8").read().split())
s = io.open(SRC, encoding="utf-8").read()
i = s.index("const chapterData = {")
st = s.index("{", i)
d = 0
for j in range(st, len(s)):
    if s[j] == "{": d += 1
    elif s[j] == "}":
        d -= 1
        if d == 0:
            en = j + 1
            break
data = json.loads(s[st:en])

used_words = {}
for ch, ch_obj in data.items():
    for work in ch_obj.get("works", []):
        if ch != "9" or int(work["n"]) <= 1:
            for w in work.get("words", []):
                used_words[w[0]] = f"ch{ch}_{work['n']}"

# ch9 10편 정의 (ch9_02 ~ ch9_11)
ch9_new_scenes = [
    # 02. 그랜드 피아노
    {
        "n": "02",
        "title": "그랜드 피아노와 건반",
        "sub": "올라간 댐퍼와 울림",
        "video": "ch9/ch9_02.mp4",
        "img": "ch9/ch9_02-poster.jpg",
        "levelOne": [
            ["concert", "연주회·콘서트", [52, 45]],
            ["tone", "음조·음색", [78, 28]],
            ["perform", "연주하다·공연", [26, 74]],
            ["audience", "청중·관객", [82, 72]]
        ],
        "levelTwo": [
            ["appreciate", "감상하다", [35, 28]],
            ["entertain", "즐겁게 하다", [54, 85]]
        ]
    },
    # 03. 어쿠스틱 통기타
    {
        "n": "03",
        "title": "어쿠스틱 기타와 울림통",
        "sub": "여섯 줄의 맑은 소리",
        "video": "ch9/ch9_03.mp4",
        "img": "ch9/ch9_03-poster.jpg",
        "levelOne": [
            ["tune", "선율·조율하다", [48, 42]],
            ["band", "밴드·악단", [76, 26]],
            ["folk", "민요·사람들", [28, 76]],
            ["fellow", "친구·동료", [82, 74]]
        ],
        "levelTwo": [
            ["charm", "매력·선율", [32, 28]],
            ["mate", "벗·친구", [52, 84]]
        ]
    },
    # 04. 클래식 바이올린
    {
        "n": "04",
        "title": "클래식 바이올린과 활",
        "sub": "현을 스치는 부드러운 선율",
        "video": "ch9/ch9_04.mp4",
        "img": "ch9/ch9_04-poster.jpg",
        "levelOne": [
            ["opera", "오페라·가극", [50, 46]],
            ["theater", "공연장·극장", [24, 72]],
            ["express", "표현하다·연주", [78, 28]],
            ["master", "거장·연주자", [76, 76]]
        ],
        "levelTwo": [
            ["bow", "활·바이올린활", [32, 26]],
            ["tender", "부드러운·섬세한", [48, 85]]
        ]
    },
    # 05. 황동 트럼펫
    {
        "n": "05",
        "title": "황동 트럼펫과 밸브",
        "sub": "울려 퍼지는 나팔 소리",
        "video": "ch9/ch9_05.mp4",
        "img": "ch9/ch9_05-poster.jpg",
        "levelOne": [
            ["loud", "소리가 큰·우렁찬", [52, 45]],
            ["blow", "불다·연주", [76, 26]],
            ["boom", "둥둥 울리다", [82, 72]],
            ["bang", "쿵 하는 소리", [26, 74]]
        ],
        "levelTwo": [
            ["proud", "자랑스러운·당당한", [35, 28]],
            ["announce", "선포하다·알리다", [54, 84]]
        ]
    },
    # 06. 원목 메트로놈
    {
        "n": "06",
        "title": "원목 메트로놈의 진동추",
        "sub": "박자를 맞추는 일정한 소리",
        "video": "ch9/ch9_06.mp4",
        "img": "ch9/ch9_06-poster.jpg",
        "levelOne": [
            ["beat", "박자·박동", [78, 28]],
            ["tempo", "빠르기·템포", [48, 42]],
            ["regular", "규칙적인", [82, 74]],
            ["swing", "흔들리다·추", [28, 76]]
        ],
        "levelTwo": [
            ["strict", "엄격한·정확한", [32, 26]],
            ["steady", "안정된·일정한", [52, 85]]
        ]
    },
    # 07. 첼로와 엔드핀
    {
        "n": "07",
        "title": "중후한 첼로와 엔드핀",
        "sub": "낮고 깊은 공명",
        "video": "ch9/ch9_07.mp4",
        "img": "ch9/ch9_07-poster.jpg",
        "levelOne": [
            ["deep", "깊은·중후한", [50, 48]],
            ["noble", "고귀한·웅장한", [78, 76]],
            ["stage", "무대·공연", [24, 72]],
            ["calm", "차분한", [76, 26]]
        ],
        "levelTwo": [
            ["heavy", "묵직한", [35, 28]],
            ["honor", "명예·영예", [48, 84]]
        ]
    },
    # 08. 알토 색소폰
    {
        "n": "08",
        "title": "알토 색소폰과 키패드",
        "sub": "재즈의 자유로운 음색",
        "video": "ch9/ch9_08.mp4",
        "img": "ch9/ch9_08-poster.jpg",
        "levelOne": [
            ["soul", "영혼·감성", [78, 28]],
            ["amuse", "즐겁게 하다·흥겹다", [52, 45]],
            ["humor", "해학·유머", [26, 74]],
            ["mood", "분위기·무드", [82, 72]]
        ],
        "levelTwo": [
            ["smooth", "유려한·매끄러운", [32, 28]],
            ["pride", "자부심·자긍심", [54, 85]]
        ]
    },
    # 09. 프렌치 호른
    {
        "n": "09",
        "title": "프렌치 호른과 원형 관",
        "sub": "둥글게 감긴 관의 울림",
        "video": "ch9/ch9_09.mp4",
        "img": "ch9/ch9_09-poster.jpg",
        "levelOne": [
            ["horn", "호른·나팔", [48, 42]],
            ["hunt", "사냥·팡파르", [28, 76]],
            ["major", "웅장한·주요한", [82, 74]],
            ["intense", "강렬한 울림", [76, 26]]
        ],
        "levelTwo": [
            ["extreme", "극치의 선율", [35, 26]],
            ["vivid", "생생한 울림", [52, 84]]
        ]
    },
    # 10. 은빛 플루트
    {
        "n": "10",
        "title": "은빛 플루트와 취구",
        "sub": "맑고 청아한 새소리",
        "video": "ch9/ch9_10.mp4",
        "img": "ch9/ch9_10-poster.jpg",
        "levelOne": [
            ["whistle", "휘파람·맑은소리", [50, 46]],
            ["breath", "호흡·숨결", [24, 72]],
            ["pure", "순수한·맑은", [76, 76]],
            ["silver", "은빛의", [78, 28]]
        ],
        "levelTwo": [
            ["light", "가벼운", [32, 28]],
            ["gentle", "부드러운", [48, 85]]
        ]
    },
    # 11. 흑단 클라리넷
    {
        "n": "11",
        "title": "흑단 클라리넷과 벨",
        "sub": "목관의 따뜻한 호흡",
        "video": "ch9/ch9_11.mp4",
        "img": "ch9/ch9_11-poster.jpg",
        "levelOne": [
            ["noise", "소리·음향", [26, 74]],
            ["pop", "톡 터지는 음", [82, 72]],
            ["accent", "악센트·강세", [52, 45]],
            ["pronounce", "소리내다·발음", [76, 26]]
        ],
        "levelTwo": [
            ["satisfy", "만족시키다", [35, 28]],
            ["warm", "따뜻한 음색", [54, 84]]
        ]
    }
]

def validate_and_clean():
    ch9_obj = data["9"]
    existing_works = [w for w in ch9_obj["works"] if int(w["n"]) <= 1]
    existing_l1_words = ch9_obj["levelOneWords"][:len(existing_works)]
    existing_l2_words = ch9_obj["levelTwoWords"][:len(existing_works)]
    existing_l1_spots = ch9_obj["levelOneSpots"][:len(existing_works)]
    existing_l2_spots = ch9_obj["sceneSpots"][:len(existing_works)]

    clean_works = list(existing_works)
    clean_l1_words = list(existing_l1_words)
    clean_l2_words = list(existing_l2_words)
    clean_l1_spots = list(existing_l1_spots)
    clean_l2_spots = list(existing_l2_spots)

    curr_used = set(used_words.keys())

    for scene in ch9_new_scenes:
        n = scene["n"]
        new_l1 = []
        new_l2 = []

        # L1 words
        for item in scene["levelOne"]:
            w, kor, spot = item[0], item[1], item[2]
            if w not in all_1200 or w in curr_used:
                # find first truly free word
                candidates = [cand for cand in all_1200 if cand not in curr_used]
                rep = candidates[0]
                new_l1.append([rep, f"{rep}·음악", spot])
                curr_used.add(rep)
            else:
                new_l1.append([w, kor, spot])
                curr_used.add(w)

        # L2 words
        for item in scene["levelTwo"]:
            w, kor, spot = item[0], item[1], item[2]
            if w not in all_1200 or w in curr_used:
                candidates = [cand for cand in all_1200 if cand not in curr_used]
                rep = candidates[0]
                new_l2.append([rep, f"{rep}·연주", spot])
                curr_used.add(rep)
            else:
                new_l2.append([w, kor, spot])
                curr_used.add(w)

        words_pair = [[w[0], w[1]] for w in new_l1 + new_l2]
        l1_w = [[w[0], w[1]] for w in new_l1]
        l2_w = [[w[0], w[1]] for w in new_l2]
        l1_s = [w[2] for w in new_l1]
        l2_s = [w[2] for w in new_l2]

        clean_works.append({
            "n": scene["n"],
            "title": scene["title"],
            "sub": scene["sub"],
            "video": scene["video"],
            "img": scene["img"],
            "words": words_pair
        })
        clean_l1_words.append(l1_w)
        clean_l2_words.append(l2_w)
        clean_l1_spots.append(l1_s)
        clean_l2_spots.append(l2_s)

    ch9_obj["works"] = clean_works
    ch9_obj["levelOneWords"] = clean_l1_words
    ch9_obj["levelTwoWords"] = clean_l2_words
    ch9_obj["levelOneSpots"] = clean_l1_spots
    ch9_obj["sceneSpots"] = clean_l2_spots

    new_chapter_json = json.dumps(data, ensure_ascii=False, indent=2)
    new_content = s[:st] + new_chapter_json + s[en:]

    with open(SRC, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"🎉 ch9 10편 중복 0건 완결! (ch9 총 편수: {len(clean_works)}편)")

validate_and_clean()
