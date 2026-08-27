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

# 11편 데이터 정의 (ch5_06 ~ ch5_16) - 좌표 간격 20% 이상 확보 및 뜻 고유화
ch5_new_scenes = [
    # 06. 노란 스쿨버스
    {
        "n": "06",
        "title": "노란 스쿨버스와 정지판",
        "sub": "안전하게 건너는 길",
        "video": "ch5/ch5_06.mp4",
        "img": "ch5/ch5_06-poster.jpg",
        "levelOne": [
            ["transport", "수송·탈것", [50, 48]],
            ["traffic", "교통", [75, 70]],
            ["discipline", "질서·규율", [25, 78]],
            ["prevent", "예방하다", [78, 30]]
        ],
        "levelTwo": [
            ["van", "승합차", [60, 52]],
            ["accident", "사고", [20, 45]],
            ["avoid", "조심하다·피하다", [35, 25]]
        ]
    },
    # 07. 삼색 신호등
    {
        "n": "07",
        "title": "거리의 삼색 신호등",
        "sub": "멈춤과 출발의 신호",
        "video": "ch5/ch5_07.mp4",
        "img": "ch5/ch5_07-poster.jpg",
        "levelOne": [
            ["switch", "전환하다", [52, 28]],
            ["law", "법규·규칙", [30, 55]],
            ["legal", "합법의·정상", [70, 75]],
            ["instruct", "지시하다", [75, 25]]
        ],
        "levelTwo": [
            ["direct", "지휘하다·가리키다", [25, 78]],
            ["order", "순서·명령", [35, 30]],
            ["standard", "기준·표준", [50, 85]]
        ]
    },
    # 08. 자전거와 헬멧
    {
        "n": "08",
        "title": "안전등 켠 자전거",
        "sub": "헬멧을 쓰고 달리는 길",
        "video": "ch5/ch5_08.mp4",
        "img": "ch5/ch5_08-poster.jpg",
        "levelOne": [
            ["motion", "움직임", [50, 50]],
            ["steady", "안정된", [25, 75]],
            ["rapid", "신속한·급격한", [75, 30]],
            ["effort", "노력·힘", [75, 75]]
        ],
        "levelTwo": [
            ["parade", "행렬", [50, 85]],
            ["forward", "앞으로", [25, 30]]
        ]
    },
    # 09. 소방차와 소화전
    {
        "n": "09",
        "title": "붉은 소방차와 소화전",
        "sub": "물을 뿜는 호스",
        "video": "ch5/ch5_09.mp4",
        "img": "ch5/ch5_09-poster.jpg",
        "levelOne": [
            ["alarm", "경보·사이렌", [50, 25]],
            ["ambulance", "구급차·구조", [80, 45]],
            ["pump", "펌프·소화전", [22, 70]],
            ["crisis", "위기·화재", [65, 75]]
        ],
        "levelTwo": [
            ["deliver", "전달하다·공급", [45, 80]],
            ["threat", "위협·위험", [78, 22]],
            ["assist", "돕다·구조", [25, 35]]
        ]
    },
    # 10. 경찰차와 경광등
    {
        "n": "10",
        "title": "순찰 경찰차와 삼각콘",
        "sub": "도로를 지키는 불빛",
        "video": "ch5/ch5_10.mp4",
        "img": "ch5/ch5_10-poster.jpg",
        "levelOne": [
            ["cop", "경찰", [52, 45]],
            ["justice", "정의·공정", [25, 70]],
            ["arrest", "단속·체포", [75, 65]],
            ["crime", "범죄", [35, 25]]
        ],
        "levelTwo": [
            ["civil", "시민의", [75, 25]],
            ["innocent", "무고한·시민", [80, 82]],
            ["punish", "처벌하다", [50, 85]]
        ]
    },
    # 11. 증기 기관차
    {
        "n": "11",
        "title": "철길 건널목의 기관차",
        "sub": "연기를 뿜는 기차",
        "video": "ch5/ch5_11.mp4",
        "img": "ch5/ch5_11-poster.jpg",
        "levelOne": [
            ["rail", "철도·선로", [45, 80]],
            ["engine", "기관·엔진", [48, 45]],
            ["coal", "석탄", [78, 55]],
            ["station", "기차역", [25, 35]]
        ],
        "levelTwo": [
            ["burst", "뿜어져 나오다", [60, 22]],
            ["advance", "전진하다", [25, 75]]
        ]
    },
    # 12. 도로 표지판
    {
        "n": "12",
        "title": "길목의 도로 표지판",
        "sub": "방향과 거리를 알리는 판",
        "video": "ch5/ch5_12.mp4",
        "img": "ch5/ch5_12-poster.jpg",
        "levelOne": [
            ["inform", "알리다·통지", [55, 50]],
            ["section", "구간·구역", [30, 75]],
            ["label", "표지·라벨", [70, 25]],
            ["limit", "제한·한계", [25, 40]]
        ],
        "levelTwo": [
            ["locate", "위치하다", [65, 80]],
            ["common", "공통의·일반", [45, 20]]
        ]
    },
    # 13. 기차 선로 갈림길
    {
        "n": "13",
        "title": "갈라지는 기차 선로",
        "sub": "길을 바꾸는 전철기",
        "video": "ch5/ch5_13.mp4",
        "img": "ch5/ch5_13-poster.jpg",
        "levelOne": [
            ["alter", "바꾸다·전환", [55, 62]],
            ["choice", "선택", [35, 35]],
            ["transfer", "환승·갈아타기", [75, 72]],
            ["proceed", "나아가다", [25, 70]]
        ],
        "levelTwo": [
            ["manage", "관리하다", [65, 30]],
            ["item", "항목·부품", [45, 85]]
        ]
    },
    # 14. 비행기와 활주로
    {
        "n": "14",
        "title": "활주로의 은빛 비행기",
        "sub": "하늘로 오르는 날개",
        "video": "ch5/ch5_14.mp4",
        "img": "ch5/ch5_14-poster.jpg",
        "levelOne": [
            ["rocket", "로켓·비행체", [50, 40]],
            ["foreign", "외국의·해외", [78, 30]],
            ["leave", "떠나다·출발", [28, 55]],
            ["capital", "수도·대도시", [65, 75]]
        ],
        "levelTwo": [
            ["vision", "시야·전망", [70, 20]],
            ["schedule", "일정·시각표", [25, 75]]
        ]
    },
    # 15. 여객선과 구명환
    {
        "n": "15",
        "title": "항구의 거대한 여객선",
        "sub": "닻을 내린 배",
        "video": "ch5/ch5_15.mp4",
        "img": "ch5/ch5_15-poster.jpg",
        "levelOne": [
            ["captain", "선장", [48, 35]],
            ["guest", "손님·승객", [75, 45]],
            ["belong", "소속되다·선적", [28, 62]],
            ["reserve", "예약하다·비축", [60, 80]]
        ],
        "levelTwo": [
            ["share", "함께 타다·나누다", [35, 40]],
            ["crowd", "군중·승객들", [75, 25]]
        ]
    },
    # 16. 주유소 주유기
    {
        "n": "16",
        "title": "주유소의 주유기",
        "sub": "기름을 넣는 노즐",
        "video": "ch5/ch5_16.mp4",
        "img": "ch5/ch5_16-poster.jpg",
        "levelOne": [
            ["automatic", "자동의", [62, 32]],
            ["monitor", "계량화면", [35, 25]],
            ["charge", "충전·요금", [72, 70]],
            ["supply", "공급하다·주유", [28, 68]]
        ],
        "levelTwo": [
            ["rate", "요율·비율", [60, 85]],
            ["value", "가치·금액", [48, 52]]
        ]
    }
]

# ch5 기존 works 및 5개 배열 정리
ch5_obj = data["5"]
existing_works = [w for w in ch5_obj["works"] if int(w["n"]) <= 5]
existing_l1_words = ch5_obj["levelOneWords"][:len(existing_works)]
existing_l2_words = ch5_obj["levelTwoWords"][:len(existing_works)]
existing_l1_spots = ch5_obj["levelOneSpots"][:len(existing_works)]
existing_l2_spots = ch5_obj["sceneSpots"][:len(existing_works)]

clean_works = list(existing_works)
clean_l1_words = list(existing_l1_words)
clean_l2_words = list(existing_l2_words)
clean_l1_spots = list(existing_l1_spots)
clean_l2_spots = list(existing_l2_spots)

for scene in ch5_new_scenes:
    words_pair = [[w[0], w[1]] for w in scene["levelOne"] + scene["levelTwo"]]
    l1_words = [[w[0], w[1]] for w in scene["levelOne"]]
    l2_words = [[w[0], w[1]] for w in scene["levelTwo"]]
    l1_spots = [w[2] for w in scene["levelOne"]]
    l2_spots = [w[2] for w in scene["levelTwo"]]
    
    clean_works.append({
        "n": scene["n"],
        "title": scene["title"],
        "sub": scene["sub"],
        "video": scene["video"],
        "img": scene["img"],
        "words": words_pair
    })
    clean_l1_words.append(l1_words)
    clean_l2_words.append(l2_words)
    clean_l1_spots.append(l1_spots)
    clean_l2_spots.append(l2_spots)

ch5_obj["works"] = clean_works
ch5_obj["levelOneWords"] = clean_l1_words
ch5_obj["levelTwoWords"] = clean_l2_words
ch5_obj["levelOneSpots"] = clean_l1_spots
ch5_obj["sceneSpots"] = clean_l2_spots

# index.html 저장
new_chapter_json = json.dumps(data, ensure_ascii=False, indent=2)
new_content = s[:st] + new_chapter_json + s[en:]

with open(SRC, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"🎉 ch5 11편 좌표 및 뜻 개선 주입 완료!")
