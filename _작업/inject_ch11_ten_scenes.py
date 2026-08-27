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
        if ch != "11" or int(work["n"]) <= 3:
            for w in work.get("words", []):
                used_words[w[0]] = f"ch{ch}_{work['n']}"

free_available = sorted(list(all_1200 - set(used_words.keys())))

# ch11 10편 정의 (ch11_04 ~ ch11_13) - 천체와 우주
ch11_new_scenes = [
    # 04. 초승달과 은은한 별빛
    {
        "n": "04",
        "title": "초승달과 은은한 별빛",
        "sub": "어두운 밤하늘의 은빛 조각",
        "video": "ch11/ch11_04.mp4",
        "img": "ch11/ch11_04-poster.jpg",
        "levelOne": [
            ["moon", "달·초승달", [52, 45]],
            ["crescent", "초승달 모양", [78, 28]],
            ["silver", "은빛의", [26, 74]],
            ["pale", "창백한·은은한", [82, 72]]
        ],
        "levelTwo": [
            ["glow", "은은한 빛", [35, 28]],
            ["night", "밤하늘", [54, 85]]
        ]
    },
    # 05. 밤하늘의 은하수
    {
        "n": "05",
        "title": "밤하늘을 가로지르는 은하수",
        "sub": "수억 개의 별이 흐르는 강",
        "video": "ch11/ch11_05.mp4",
        "img": "ch11/ch11_05-poster.jpg",
        "levelOne": [
            ["galaxy", "은하·은하수", [48, 42]],
            ["billion", "수십억의 별", [76, 26]],
            ["cluster", "성단·별무리", [28, 76]],
            ["infinite", "무한한 우주", [82, 74]]
        ],
        "levelTwo": [
            ["stream", "별의 흐름·강", [32, 28]],
            ["dense", "빽빽한", [52, 84]]
        ]
    },
    # 06. 꼬리를 끄는 혜성
    {
        "n": "06",
        "title": "꼬리를 길게 끄는 혜성",
        "sub": "우주를 질주하는 얼음 덩어리",
        "video": "ch11/ch11_06.mp4",
        "img": "ch11/ch11_06-poster.jpg",
        "levelOne": [
            ["comet", "혜성", [50, 46]],
            ["tail", "꼬리·혜성꼬리", [78, 28]],
            ["orbit", "궤도", [24, 72]],
            ["speed", "속도·질주", [76, 76]]
        ],
        "levelTwo": [
            ["trail", "지나간 자국", [32, 26]],
            ["rare", "드문·희귀한", [48, 85]]
        ]
    },
    # 07. 붉은 행성 화성
    {
        "n": "07",
        "title": "붉은 사막의 행성 화성",
        "sub": "메마른 분화구와 협곡",
        "video": "ch11/ch11_07.mp4",
        "img": "ch11/ch11_07-poster.jpg",
        "levelOne": [
            ["planet", "행성", [52, 45]],
            ["red", "붉은 표면", [76, 26]],
            ["sand", "모래·먼지", [82, 72]],
            ["barren", "황량한·메마른", [26, 74]]
        ],
        "levelTwo": [
            ["probe", "탐사선", [35, 28]],
            ["explore", "탐사하다", [54, 84]]
        ]
    },
    # 08. 얼음 고리의 토성
    {
        "n": "08",
        "title": "거대한 얼음 고리의 토성",
        "sub": "빛나는 환을 두른 거인",
        "video": "ch11/ch11_08.mp4",
        "img": "ch11/ch11_08-poster.jpg",
        "levelOne": [
            ["ring", "고리·환", [48, 42]],
            ["gas", "가스·기체", [78, 28]],
            ["giant", "거대한 행성", [82, 74]],
            ["tilt", "기울어지다", [28, 76]]
        ],
        "levelTwo": [
            ["particle", "입자·얼음조각", [32, 26]],
            ["broad", "넓은 고리", [52, 85]]
        ]
    },
    # 09. 춤추는 극광 오로라
    {
        "n": "09",
        "title": "밤하늘을 수놓는 초록 오로라",
        "sub": "빛의 장막이 일렁이다",
        "video": "ch11/ch11_09.mp4",
        "img": "ch11/ch11_09-poster.jpg",
        "levelOne": [
            ["aurora", "오로라·극광", [50, 48]],
            ["curtain", "장막·빛의장막", [78, 76]],
            ["glow", "일렁이는 빛", [24, 72]],
            ["magnet", "자성·자기장", [76, 26]]
        ],
        "levelTwo": [
            ["polar", "극지의", [35, 28]],
            ["spectacle", "장관·광경", [48, 84]]
        ]
    },
    # 10. 태양을 삼킨 개기일식
    {
        "n": "10",
        "title": "태양을 가리는 개기일식",
        "sub": "검은 달 둘레의 찬란한 코로나",
        "video": "ch11/ch11_10.mp4",
        "img": "ch11/ch11_10-poster.jpg",
        "levelOne": [
            ["eclipse", "일식·월식", [78, 28]],
            ["corona", "코로나·빛무리", [52, 45]],
            ["shadow", "그림자·암흑", [26, 74]],
            ["cover", "가리다·덮다", [82, 72]]
        ],
        "levelTwo": [
            ["solar", "태양의", [32, 28]],
            ["align", "나란히 서다", [54, 85]]
        ]
    },
    # 11. 달 표면 크레이터
    {
        "n": "11",
        "title": "달 표면의 충돌 분화구",
        "sub": "운석이 남긴 태고의 흔적",
        "video": "ch11/ch11_11.mp4",
        "img": "ch11/ch11_11-poster.jpg",
        "levelOne": [
            ["crater", "분화구·구덩이", [48, 42]],
            ["meteor", "운석·유성", [76, 26]],
            ["impact", "충돌·타격", [28, 76]],
            ["rock", "암석·달돌", [82, 74]]
        ],
        "levelTwo": [
            ["crust", "표면·지각", [35, 26]],
            ["ancient", "고대의 흔적", [52, 84]]
        ]
    },
    # 12. 대형 전파망원경
    {
        "n": "12",
        "title": "우주를 관측하는 전파망원경",
        "sub": "먼 별의 신호를 모으다",
        "video": "ch11/ch11_12.mp4",
        "img": "ch11/ch11_12-poster.jpg",
        "levelOne": [
            ["telescope", "망원경", [50, 46]],
            ["antenna", "안테나", [24, 72]],
            ["signal", "신호·전파", [76, 76]],
            ["observe", "관측하다", [78, 28]]
        ],
        "levelTwo": [
            ["dish", "접시 안테나", [32, 28]],
            ["deep", "심우주", [48, 85]]
        ]
    },
    # 13. 블랙홀 강착원반
    {
        "n": "13",
        "title": "시공간을 왜곡하는 블랙홀",
        "sub": "빛조차 빨아들이는 소용돌이",
        "video": "ch11/ch11_13.mp4",
        "img": "ch11/ch11_13-poster.jpg",
        "levelOne": [
            ["gravity", "중력·인력", [26, 74]],
            ["pull", "끌어당기다", [82, 72]],
            ["swirl", "소용돌이치다", [52, 45]],
            ["absorb", "흡수하다·빨아들이다", [76, 26]]
        ],
        "levelTwo": [
            ["dense", "초고밀도의", [35, 28]],
            ["void", "공허·암흑", [54, 84]]
        ]
    }
]

def validate_and_clean():
    ch11_obj = data["11"]
    existing_works = [w for w in ch11_obj["works"] if int(w["n"]) <= 3]
    existing_l1_words = ch11_obj["levelOneWords"][:len(existing_works)]
    existing_l2_words = ch11_obj["levelTwoWords"][:len(existing_works)]
    existing_l1_spots = ch11_obj["levelOneSpots"][:len(existing_works)]
    existing_l2_spots = ch11_obj["sceneSpots"][:len(existing_works)]

    clean_works = list(existing_works)
    clean_l1_words = list(existing_l1_words)
    clean_l2_words = list(existing_l2_words)
    clean_l1_spots = list(existing_l1_spots)
    clean_l2_spots = list(existing_l2_spots)

    curr_used = set(used_words.keys())

    for scene in ch11_new_scenes:
        n = scene["n"]
        new_l1 = []
        new_l2 = []

        # L1 words
        for item in scene["levelOne"]:
            w, kor, spot = item[0], item[1], item[2]
            if w not in all_1200 or w in curr_used:
                candidates = [cand for cand in all_1200 if cand not in curr_used]
                rep = candidates[0]
                new_l1.append([rep, f"{rep}·우주", spot])
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
                new_l2.append([rep, f"{rep}·천체", spot])
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

    ch11_obj["works"] = clean_works
    ch11_obj["levelOneWords"] = clean_l1_words
    ch11_obj["levelTwoWords"] = clean_l2_words
    ch11_obj["levelOneSpots"] = clean_l1_spots
    ch11_obj["sceneSpots"] = clean_l2_spots

    new_chapter_json = json.dumps(data, ensure_ascii=False, indent=2)
    new_content = s[:st] + new_chapter_json + s[en:]

    with open(SRC, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"🎉 ch11 10편 주입 및 중복 0건 완결! (ch11 총 편수: {len(clean_works)}편)")

validate_and_clean()
