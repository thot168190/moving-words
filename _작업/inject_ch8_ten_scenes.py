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
        if ch != "8" or int(work["n"]) <= 4:
            for w in work.get("words", []):
                used_words[w[0]] = f"ch{ch}_{work['n']}"

free_available = sorted(list(all_1200 - set(used_words.keys())))

# ch8 10편 정의 (ch8_05 ~ ch8_14) - 대칭/격자 없는 비대칭 자연 좌표
ch8_new_scenes = [
    # 05. 삼각 텐트와 의자
    {
        "n": "05",
        "title": "삼각 캠핑 텐트와 의자",
        "sub": "숲속에 펼친 쉼터",
        "video": "ch8/ch8_05.mp4",
        "img": "ch8/ch8_05-poster.jpg",
        "levelOne": [
            ["escape", "탈출·떠나다", [72, 28]],
            ["nature", "자연·숲", [24, 76]],
            ["settle", "정착하다·자리잡다", [78, 68]],
            ["ground", "땅·바닥", [35, 38]]
        ],
        "levelTwo": [
            ["relax", "휴식하다·쉬다", [52, 84]],
            ["field", "들판·야외", [48, 42]]
        ]
    },
    # 06. 황동 호롱 랜턴
    {
        "n": "06",
        "title": "황동 랜턴의 불꽃",
        "sub": "어둠을 밝히는 등불",
        "video": "ch8/ch8_06.mp4",
        "img": "ch8/ch8_06-poster.jpg",
        "levelOne": [
            ["battery", "전지·배터리", [76, 26]],
            ["beam", "광선·불빛", [82, 72]],
            ["signal", "신호·빛", [46, 82]],
            ["flash", "번쩍이다", [32, 45]]
        ],
        "levelTwo": [
            ["dark", "어둠·캄캄한", [25, 28]],
            ["burn", "타오르다", [62, 60]]
        ]
    },
    # 07. 등산화와 지팡이
    {
        "n": "07",
        "title": "가죽 등산화와 지팡이",
        "sub": "거친 산길을 오르다",
        "video": "ch8/ch8_07.mp4",
        "img": "ch8/ch8_07-poster.jpg",
        "levelOne": [
            ["challenge", "도전하다", [48, 42]],
            ["climb", "오르다·등산", [76, 28]],
            ["trail", "오솔길·산길", [82, 74]],
            ["peak", "봉우리·정상", [28, 78]]
        ],
        "levelTwo": [
            ["grip", "단단히 쥐다", [32, 26]],
            ["step", "발걸음", [58, 85]]
        ]
    },
    # 08. 원목 카누와 노
    {
        "n": "08",
        "title": "원목 카누와 노",
        "sub": "물살을 가르는 패들",
        "video": "ch8/ch8_08.mp4",
        "img": "ch8/ch8_08-poster.jpg",
        "levelOne": [
            ["paddle", "노젓다·패들", [52, 46]],
            ["drift", "떠내려가다·표류", [26, 72]],
            ["lake", "호수·물길", [78, 68]],
            ["calm", "잔잔한", [45, 82]]
        ],
        "levelTwo": [
            ["flow", "흐름·물살", [32, 28]],
            ["float", "뜨다·부유", [74, 32]]
        ]
    },
    # 09. 캠핑 주전자와 머그컵
    {
        "n": "09",
        "title": "캠핑 주전자와 머그컵",
        "sub": "따뜻하게 끓이는 차",
        "video": "ch8/ch8_09.mp4",
        "img": "ch8/ch8_09-poster.jpg",
        "levelOne": [
            ["boil", "끓이다·김", [48, 42]],
            ["flavor", "맛·향", [26, 74]],
            ["mug", "머그잔", [32, 28]],
            ["pour", "따르다", [78, 72]]
        ],
        "levelTwo": [
            ["warm", "따스한", [74, 32]],
            ["drink", "마시다", [52, 85]]
        ]
    },
    # 10. 손도끼와 장작더미
    {
        "n": "10",
        "title": "손도끼와 장작더미",
        "sub": "장작을 패는 메아리",
        "video": "ch8/ch8_10.mp4",
        "img": "ch8/ch8_10-poster.jpg",
        "levelOne": [
            ["strike", "내리치다·타격", [52, 45]],
            ["split", "쪼개다·가르다", [76, 28]],
            ["force", "힘·타격력", [24, 72]],
            ["fuel", "땔감·연료", [82, 76]]
        ],
        "levelTwo": [
            ["heavy", "묵직한", [48, 85]],
            ["wood", "장작나무", [35, 32]]
        ]
    },
    # 11. 접이식 포켓 나이프
    {
        "n": "11",
        "title": "접이식 포켓 나이프",
        "sub": "다용도 캠핑 칼",
        "video": "ch8/ch8_11.mp4",
        "img": "ch8/ch8_11-poster.jpg",
        "levelOne": [
            ["blade", "칼날", [52, 46]],
            ["fold", "접다·접이식", [74, 28]],
            ["carve", "깎다·새기다", [26, 76]],
            ["steel", "강철", [48, 82]]
        ],
        "levelTwo": [
            ["sharp", "날카로운", [78, 72]],
            ["pocket", "주머니", [32, 30]]
        ]
    },
    # 12. 무쇠 팬과 모닥불
    {
        "n": "12",
        "title": "무쇠 팬과 모닥불 화덕",
        "sub": "돌 화덕 위의 조리",
        "video": "ch8/ch8_12.mp4",
        "img": "ch8/ch8_12-poster.jpg",
        "levelOne": [
            ["roast", "굽다·모닥불", [46, 42]],
            ["flame", "불꽃·화염", [78, 28]],
            ["cook", "요리하다", [82, 72]],
            ["glow", "빨갛게 달다", [32, 82]]
        ],
        "levelTwo": [
            ["fire", "불·모닥불", [24, 70]],
            ["smoke", "연기", [35, 26]]
        ]
    },
    # 13. 보온병과 컵
    {
        "n": "13",
        "title": "보온병과 스테인리스 컵",
        "sub": "온도를 지키는 병",
        "video": "ch8/ch8_13.mp4",
        "img": "ch8/ch8_13-poster.jpg",
        "levelOne": [
            ["preserve", "보존하다·유지", [48, 45]],
            ["liquid", "액체·물", [76, 28]],
            ["pure", "깨끗한", [54, 82]],
            ["cool", "시원한", [26, 72]]
        ],
        "levelTwo": [
            ["cold", "차가운", [82, 74]],
            ["drop", "물방울", [32, 28]]
        ]
    },
    # 14. 황동 나침반과 지도
    {
        "n": "14",
        "title": "황동 나침반과 지도",
        "sub": "방향을 찾는 바늘",
        "video": "ch8/ch8_14.mp4",
        "img": "ch8/ch8_14-poster.jpg",
        "levelOne": [
            ["explore", "탐험하다·탐색", [46, 45]],
            ["route", "경로·길", [28, 72]],
            ["target", "목표점·방향", [78, 28]],
            ["search", "탐색하다·찾다", [82, 76]]
        ],
        "levelTwo": [
            ["seek", "찾다·구하다", [35, 28]],
            ["toward", "~을 향하여", [54, 84]]
        ]
    }
]

def validate_and_clean():
    ch8_obj = data["8"]
    existing_works = [w for w in ch8_obj["works"] if int(w["n"]) <= 4]
    existing_l1_words = ch8_obj["levelOneWords"][:len(existing_works)]
    existing_l2_words = ch8_obj["levelTwoWords"][:len(existing_works)]
    existing_l1_spots = ch8_obj["levelOneSpots"][:len(existing_works)]
    existing_l2_spots = ch8_obj["sceneSpots"][:len(existing_works)]

    clean_works = list(existing_works)
    clean_l1_words = list(existing_l1_words)
    clean_l2_words = list(existing_l2_words)
    clean_l1_spots = list(existing_l1_spots)
    clean_l2_spots = list(existing_l2_spots)

    curr_used = set(used_words.keys())
    free_queue = [w for w in free_available if w not in curr_used]
    q_idx = 0

    for scene in ch8_new_scenes:
        n = scene["n"]
        new_l1 = []
        new_l2 = []

        # L1 words
        for item in scene["levelOne"]:
            w, kor, spot = item[0], item[1], item[2]
            if w not in all_1200 or w in curr_used:
                rep = free_queue[q_idx]
                q_idx += 1
                new_l1.append([rep, f"{rep}·활동", spot])
                curr_used.add(rep)
            else:
                new_l1.append([w, kor, spot])
                curr_used.add(w)

        # L2 words
        for item in scene["levelTwo"]:
            w, kor, spot = item[0], item[1], item[2]
            if w not in all_1200 or w in curr_used:
                rep = free_queue[q_idx]
                q_idx += 1
                new_l2.append([rep, f"{rep}·캠핑", spot])
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

    ch8_obj["works"] = clean_works
    ch8_obj["levelOneWords"] = clean_l1_words
    ch8_obj["levelTwoWords"] = clean_l2_words
    ch8_obj["levelOneSpots"] = clean_l1_spots
    ch8_obj["sceneSpots"] = clean_l2_spots

    new_chapter_json = json.dumps(data, ensure_ascii=False, indent=2)
    new_content = s[:st] + new_chapter_json + s[en:]

    with open(SRC, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"🎉 ch8 10편 비대칭 자연 좌표 주입 완료! (ch8 총 편수: {len(clean_works)}편)")

validate_and_clean()
