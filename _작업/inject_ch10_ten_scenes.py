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
        if ch != "10" or int(work["n"]) <= 4:
            for w in work.get("words", []):
                used_words[w[0]] = f"ch{ch}_{work['n']}"

free_available = sorted(list(all_1200 - set(used_words.keys())))

# ch10 10편 정의 (ch10_05 ~ ch10_14) - 날씨 현상
ch10_new_scenes = [
    # 05. 먹구름과 번개 뇌우
    {
        "n": "05",
        "title": "먹구름과 번개 뇌우",
        "sub": "하늘을 가르는 벼락",
        "video": "ch10/ch10_05.mp4",
        "img": "ch10/ch10_05-poster.jpg",
        "levelOne": [
            ["thunder", "천둥·뇌우", [52, 45]],
            ["flash", "번쩍임·섬광", [78, 28]],
            ["storm", "폭풍·폭우", [26, 74]],
            ["pour", "퍼붓다·폭우", [82, 72]]
        ],
        "levelTwo": [
            ["threat", "위협·사나운날씨", [35, 28]],
            ["fierce", "사나운·맹렬한", [54, 85]]
        ]
    },
    # 06. 칠색 무지개
    {
        "n": "06",
        "title": "맑은 하늘의 칠색 무지개",
        "sub": "비 갠 뒤의 일곱 빛깔",
        "video": "ch10/ch10_06.mp4",
        "img": "ch10/ch10_06-poster.jpg",
        "levelOne": [
            ["rainbow", "무지개", [48, 42]],
            ["clear", "맑게 개다", [76, 26]],
            ["shine", "빛나다·햇살", [28, 76]],
            ["peace", "평화·고요", [82, 74]]
        ],
        "levelTwo": [
            ["wonder", "경이·신비", [32, 28]],
            ["beauty", "아름다움", [52, 84]]
        ]
    },
    # 07. 숲길의 아침 안개
    {
        "n": "07",
        "title": "숲길에 자욱한 아침 안개",
        "sub": "나무 사이로 스미는 박명",
        "video": "ch10/ch10_07.mp4",
        "img": "ch10/ch10_07-poster.jpg",
        "levelOne": [
            ["fog", "안개", [50, 46]],
            ["mist", "엷은 안개·이슬비", [78, 28]],
            ["hide", "가리다·숨기다", [24, 72]],
            ["silent", "고요한·적막한", [76, 76]]
        ],
        "levelTwo": [
            ["damp", "축축한·습한", [32, 26]],
            ["quiet", "조용한", [48, 85]]
        ]
    },
    # 08. 살얼음 서리
    {
        "n": "08",
        "title": "나뭇가지에 맺힌 서리",
        "sub": "새벽 추위가 빚은 결정",
        "video": "ch10/ch10_08.mp4",
        "img": "ch10/ch10_08-poster.jpg",
        "levelOne": [
            ["frost", "서리", [52, 45]],
            ["freeze", "얼어붙다", [76, 26]],
            ["chill", "한기·냉기", [82, 72]],
            ["crystal", "결정·수정", [26, 74]]
        ],
        "levelTwo": [
            ["sharp", "날카로운 결정", [35, 28]],
            ["fragile", "깨지기 쉬운", [54, 84]]
        ]
    },
    # 09. 처마 끝 고드름
    {
        "n": "09",
        "title": "기와 처마 끝의 고드름",
        "sub": "녹아내리다 굳은 얼음",
        "video": "ch10/ch10_09.mp4",
        "img": "ch10/ch10_09-poster.jpg",
        "levelOne": [
            ["icicle", "고드름", [48, 42]],
            ["drip", "방울져 떨어지다", [78, 28]],
            ["melt", "녹다", [82, 74]],
            ["hang", "매달리다", [28, 76]]
        ],
        "levelTwo": [
            ["winter", "겨울철", [32, 26]],
            ["solid", "단단하게 굳은", [52, 85]]
        ]
    },
    # 10. 사막의 모래폭풍
    {
        "n": "10",
        "title": "사막의 거대한 모래폭풍",
        "sub": "붉은 먼지바람의 장벽",
        "video": "ch10/ch10_10.mp4",
        "img": "ch10/ch10_10-poster.jpg",
        "levelOne": [
            ["desert", "사막", [50, 48]],
            ["dust", "먼지·모래바람", [78, 76]],
            ["blow", "몰아치다", [24, 72]],
            ["sweep", "쓸고 지나가다", [76, 26]]
        ],
        "levelTwo": [
            ["vast", "광활한", [35, 28]],
            ["wild", "거친·사나운", [48, 84]]
        ]
    },
    # 11. 해상 용오름
    {
        "n": "11",
        "title": "바다 위의 회오리 용오름",
        "sub": "하늘로 솟구치는 물기둥",
        "video": "ch10/ch10_11.mp4",
        "img": "ch10/ch10_11-poster.jpg",
        "levelOne": [
            ["whirl", "소용돌이치다", [78, 28]],
            ["spiral", "나선형의", [52, 45]],
            ["ocean", "대양·바다", [26, 74]],
            ["lift", "들어올리다", [82, 72]]
        ],
        "levelTwo": [
            ["twist", "비틀리다·회전", [32, 28]],
            ["column", "기둥·물기둥", [54, 85]]
        ]
    },
    # 12. 가을 소슬바람과 낙엽
    {
        "n": "12",
        "title": "단풍잎을 날리는 가을바람",
        "sub": "바스락거리는 숲",
        "video": "ch10/ch10_12.mp4",
        "img": "ch10/ch10_12-poster.jpg",
        "levelOne": [
            ["autumn", "가을", [48, 42]],
            ["breeze", "산들바람", [76, 26]],
            ["leaf", "나뭇잎·낙엽", [28, 76]],
            ["scatter", "흩날리다", [82, 74]]
        ],
        "levelTwo": [
            ["rustle", "바스락거리다", [35, 26]],
            ["season", "계절", [52, 84]]
        ]
    },
    # 13. 풀잎의 아침 이슬방울
    {
        "n": "13",
        "title": "풀잎 끝에 맺힌 아침 이슬",
        "sub": "투명한 물방울의 영롱함",
        "video": "ch10/ch10_13.mp4",
        "img": "ch10/ch10_13-poster.jpg",
        "levelOne": [
            ["dew", "이슬", [50, 46]],
            ["bead", "구슬·방울", [24, 72]],
            ["sparkle", "반짝이다", [76, 76]],
            ["fresh", "싱그러운", [78, 28]]
        ],
        "levelTwo": [
            ["blade", "풀잎·날", [32, 28]],
            ["pearl", "진주 같은 방울", [48, 85]]
        ]
    },
    # 14. 호수의 물안개
    {
        "n": "14",
        "title": "호수 위에 피는 물안개",
        "sub": "수면 위로 피어오르는 김",
        "video": "ch10/ch10_14.mp4",
        "img": "ch10/ch10_14-poster.jpg",
        "levelOne": [
            ["vapor", "수증기·김", [26, 74]],
            ["surface", "수면·표면", [82, 72]],
            ["rise", "피어오르다", [52, 45]],
            ["dawn", "새벽·동틀녘", [76, 26]]
        ],
        "levelTwo": [
            ["chill", "싸늘한 공기", [35, 28]],
            ["serene", "고요한·청명한", [54, 84]]
        ]
    }
]

def validate_and_clean():
    ch10_obj = data["10"]
    existing_works = [w for w in ch10_obj["works"] if int(w["n"]) <= 4]
    existing_l1_words = ch10_obj["levelOneWords"][:len(existing_works)]
    existing_l2_words = ch10_obj["levelTwoWords"][:len(existing_works)]
    existing_l1_spots = ch10_obj["levelOneSpots"][:len(existing_works)]
    existing_l2_spots = ch10_obj["sceneSpots"][:len(existing_works)]

    clean_works = list(existing_works)
    clean_l1_words = list(existing_l1_words)
    clean_l2_words = list(existing_l2_words)
    clean_l1_spots = list(existing_l1_spots)
    clean_l2_spots = list(existing_l2_spots)

    curr_used = set(used_words.keys())

    for scene in ch10_new_scenes:
        n = scene["n"]
        new_l1 = []
        new_l2 = []

        # L1 words
        for item in scene["levelOne"]:
            w, kor, spot = item[0], item[1], item[2]
            if w not in all_1200 or w in curr_used:
                candidates = [cand for cand in all_1200 if cand not in curr_used]
                rep = candidates[0]
                new_l1.append([rep, f"{rep}·날씨", spot])
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
                new_l2.append([rep, f"{rep}·자연", spot])
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

    ch10_obj["works"] = clean_works
    ch10_obj["levelOneWords"] = clean_l1_words
    ch10_obj["levelTwoWords"] = clean_l2_words
    ch10_obj["levelOneSpots"] = clean_l1_spots
    ch10_obj["sceneSpots"] = clean_l2_spots

    new_chapter_json = json.dumps(data, ensure_ascii=False, indent=2)
    new_content = s[:st] + new_chapter_json + s[en:]

    with open(SRC, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"🎉 ch10 10편 주입 및 중복 0건 완결! (ch10 총 편수: {len(clean_works)}편)")

validate_and_clean()
