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

used_words = {w[0]: f"ch{ch}_{work['n']}" for ch in data for work in data[ch]["works"] for w in work["words"]}

# ch4 20편 정의 (ch4_04 ~ ch4_23)
ch4_new_scenes = [
    # 04. 팔레트와 붓
    {
        "n": "04",
        "title": "나무 팔레트와 붓",
        "sub": "물감을 섞는 작업대",
        "video": "ch4/ch4_04.mp4",
        "img": "ch4/ch4_04-poster.jpg",
        "levelOne": [
            ["create", "창작하다", [48, 45]],
            ["decorate", "장식하다", [75, 30]],
            ["display", "전시하다", [28, 70]],
            ["illustrate", "그리다·설명", [72, 75]]
        ],
        "levelTwo": [
            ["master", "거장·명인", [50, 80]],
            ["studio", "화실·작업실", [30, 30]]
        ]
    },
    # 05. 도자기 물레
    {
        "n": "05",
        "title": "도자기 물레와 점토",
        "sub": "손끝으로 빚는 그릇",
        "video": "ch4/ch4_05.mp4",
        "img": "ch4/ch4_05-poster.jpg",
        "levelOne": [
            ["produce", "빚어내다·생산", [52, 48]],
            ["process", "가공하다·과정", [25, 75]],
            ["practice", "연습하다·숙련", [75, 35]],
            ["craft", "공예·손재주", [72, 75]]
        ],
        "levelTwo": [
            ["patient", "참을성 있는", [28, 30]],
            ["smooth", "매끄러운", [50, 82]]
        ]
    },
    # 06. 목각도와 나무토막
    {
        "n": "06",
        "title": "목각도와 나무토막",
        "sub": "결을 깎아내는 손길",
        "video": "ch4/ch4_06.mp4",
        "img": "ch4/ch4_06-poster.jpg",
        "levelOne": [
            ["scratch", "새기다·긁다", [48, 48]],
            ["sharp", "날카로운", [75, 30]],
            ["damage", "깎아내다·손질", [25, 75]],
            ["smash", "깨뜨리다·다듬다", [75, 75]]
        ],
        "levelTwo": [
            ["chip", "나무조각·대패밥", [28, 30]],
            ["tough", "단단한·질긴", [50, 80]]
        ]
    },
    # 07. 전통 베틀과 북
    {
        "n": "07",
        "title": "전통 베틀과 북",
        "sub": "실을 엮어 짜는 천",
        "video": "ch4/ch4_07.mp4",
        "img": "ch4/ch4_07-poster.jpg",
        "levelOne": [
            ["sew", "짜다·바느질", [50, 50]],
            ["rhythm", "리듬·규칙성", [75, 30]],
            ["weave", "엮다·직조", [25, 75]],
            ["frame", "틀·직조틀", [75, 75]]
        ],
        "levelTwo": [
            ["row", "줄·열", [28, 30]],
            ["plain", "소박한·무늬없는", [50, 80]]
        ]
    },
    # 08. 재봉틀과 실토리
    {
        "n": "08",
        "title": "재봉틀과 실토리",
        "sub": "천을 잇는 바늘",
        "video": "ch4/ch4_08.mp4",
        "img": "ch4/ch4_08-poster.jpg",
        "levelOne": [
            ["repair", "수선하다", [52, 45]],
            ["replace", "교체하다", [75, 30]],
            ["fashion", "의복·패션", [25, 75]],
            ["stitch", "바늘땀", [75, 75]]
        ],
        "levelTwo": [
            ["needle", "바늘", [30, 30]],
            ["precise", "정밀한", [50, 80]]
        ]
    },
    # 09. 스테인드글라스 조각
    {
        "n": "09",
        "title": "스테인드글라스 조각",
        "sub": "빛을 담는 유리공예",
        "video": "ch4/ch4_09.mp4",
        "img": "ch4/ch4_09-poster.jpg",
        "levelOne": [
            ["complex", "정교한·복잡한", [50, 45]],
            ["brilliant", "찬란한·눈부신", [75, 30]],
            ["border", "테두리·납선", [25, 75]],
            ["joint", "이음매·연결", [75, 75]]
        ],
        "levelTwo": [
            ["tint", "빛깔·색조", [28, 30]],
            ["glow", "은은한 빛", [50, 80]]
        ]
    },
    # 10. 동판 에칭 판화
    {
        "n": "10",
        "title": "동판 에칭과 롤러",
        "sub": "잉크를 펴 바르는 판화",
        "video": "ch4/ch4_10.mp4",
        "img": "ch4/ch4_10-poster.jpg",
        "levelOne": [
            ["copy", "판화본·복사", [50, 48]],
            ["stamp", "찍어내다", [75, 30]],
            ["plate", "동판·인쇄판", [25, 75]],
            ["press", "눌러찍다", [75, 75]]
        ],
        "levelTwo": [
            ["surface", "표면·판면", [28, 30]],
            ["trace", "자국·선", [50, 80]]
        ]
    },
    # 11. 만년필 촉과 잉크병
    {
        "n": "11",
        "title": "만년필 촉과 잉크병",
        "sub": "종이에 스미는 생각",
        "video": "ch4/ch4_11.mp4",
        "img": "ch4/ch4_11-poster.jpg",
        "levelOne": [
            ["message", "메시지·글", [50, 45]],
            ["paragraph", "문단", [75, 30]],
            ["sentence", "문장", [25, 75]],
            ["quote", "인용하다", [75, 75]]
        ],
        "levelTwo": [
            ["whisper", "속삭이다·생각", [28, 30]],
            ["tip", "펜촉·끝", [50, 80]]
        ]
    },
    # 12. 실링왁스 스탬프
    {
        "n": "12",
        "title": "실링왁스 인장과 촛불",
        "sub": "봉투를 닫는 붉은 왁스",
        "video": "ch4/ch4_12.mp4",
        "img": "ch4/ch4_12-poster.jpg",
        "levelOne": [
            ["promise", "약속·서약", [50, 48]],
            ["secure", "봉인하다·안전", [75, 30]],
            ["impress", "각인하다·자국", [25, 75]],
            ["melt", "녹이다·왁스", [75, 75]]
        ],
        "levelTwo": [
            ["flame", "촛불", [28, 30]],
            ["confidential", "비밀의·친전", [50, 80]]
        ]
    },
    # 13. 양장본 노트와 리본
    {
        "n": "13",
        "title": "양장본 노트와 책갈피",
        "sub": "두꺼운 가죽 표지",
        "video": "ch4/ch4_13.mp4",
        "img": "ch4/ch4_13-poster.jpg",
        "levelOne": [
            ["topic", "주제", [50, 45]],
            ["title", "제목·표제", [75, 30]],
            ["register", "기록하다·등록", [25, 75]],
            ["content", "내용·목차", [75, 75]]
        ],
        "levelTwo": [
            ["ribbon", "책갈피 끈", [28, 30]],
            ["bound", "제본된", [50, 80]]
        ]
    },
    # 14. 탁상 지구의
    {
        "n": "14",
        "title": "탁상 지구의와 경도환",
        "sub": "책상 위의 세계",
        "video": "ch4/ch4_14.mp4",
        "img": "ch4/ch4_14-poster.jpg",
        "levelOne": [
            ["planet", "행성·지구", [50, 45]],
            ["axis", "자전축·중심축", [75, 30]],
            ["sphere", "구체·지구의", [25, 75]],
            ["degree", "도·경위도", [75, 75]]
        ],
        "levelTwo": [
            ["meridian", "자오선", [28, 30]],
            ["orbit", "궤도·회전", [50, 80]]
        ]
    },
    # 15. 나무 독서대와 고서
    {
        "n": "15",
        "title": "나무 독서대와 고서",
        "sub": "펼쳐진 두꺼운 책",
        "video": "ch4/ch4_15.mp4",
        "img": "ch4/ch4_15-poster.jpg",
        "levelOne": [
            ["research", "연구하다·탐독", [50, 45]],
            ["knowledge", "지식·학문", [75, 30]],
            ["concentrate", "집중하다", [25, 75]],
            ["subject", "과목·학술", [75, 75]]
        ],
        "levelTwo": [
            ["attend", "참석하다·수업", [28, 30]],
            ["educate", "교육하다", [50, 80]]
        ]
    },
    # 16. 유리 잉크웰과 깃펜
    {
        "n": "16",
        "title": "유리 잉크웰과 깃펜",
        "sub": "잉크를 머금은 펜촉",
        "video": "ch4/ch4_16.mp4",
        "img": "ch4/ch4_16-poster.jpg",
        "levelOne": [
            ["feather", "깃털·깃펜", [50, 45]],
            ["well", "잉크병·우물", [75, 30]],
            ["spill", "잉크방울", [25, 75]],
            ["stroke", "필획·필선", [75, 75]]
        ],
        "levelTwo": [
            ["flow", "흘러나오다", [28, 30]],
            ["black", "검은 잉크", [50, 80]]
        ]
    },
    # 17. 황동 양팔저울과 분동
    {
        "n": "17",
        "title": "황동 양팔저울과 분동",
        "sub": "수평을 맞추는 저울",
        "video": "ch4/ch4_17.mp4",
        "img": "ch4/ch4_17-poster.jpg",
        "levelOne": [
            ["weigh", "무게를 달다", [50, 48]],
            ["calculate", "계산하다", [75, 30]],
            ["count", "세다·계수", [25, 75]],
            ["half", "절반·균형", [75, 75]]
        ],
        "levelTwo": [
            ["quarter", "사분의 일·분동", [28, 30]],
            ["balance", "수평·균형", [50, 80]]
        ]
    },
    # 18. 은제 회중시계와 체인
    {
        "n": "18",
        "title": "은제 회중시계와 톱니",
        "sub": "초침이 흐르는 소리",
        "video": "ch4/ch4_18.mp4",
        "img": "ch4/ch4_18-poster.jpg",
        "levelOne": [
            ["minute", "분·시간", [50, 45]],
            ["instant", "순간·찰나", [75, 30]],
            ["century", "세기·시대", [25, 75]],
            ["annual", "연례의·매년", [75, 75]]
        ],
        "levelTwo": [
            ["calendar", "달력·시간표", [28, 30]],
            ["event", "사건·계기", [50, 80]]
        ]
    },
    # 19. 볼록 돋보기와 고문서
    {
        "n": "19",
        "title": "볼록 돋보기와 고문서",
        "sub": "작은 글자를 들여다보다",
        "video": "ch4/ch4_19.mp4",
        "img": "ch4/ch4_19-poster.jpg",
        "levelOne": [
            ["detect", "발견하다·감지", [50, 48]],
            ["define", "정의하다·밝히다", [75, 30]],
            ["detail", "세부사항·작은글자", [25, 75]],
            ["focus", "초점을 맞추다", [75, 75]]
        ],
        "levelTwo": [
            ["inspect", "점검하다", [28, 30]],
            ["fine", "미세한·가는", [50, 80]]
        ]
    },
    # 20. 클래식 타자기
    {
        "n": "20",
        "title": "클래식 타자기 자판",
        "sub": "활자가 종이를 두드리다",
        "video": "ch4/ch4_20.mp4",
        "img": "ch4/ch4_20-poster.jpg",
        "levelOne": [
            ["click", "딸깍거리다", [50, 45]],
            ["code", "부호·코드", [75, 30]],
            ["communicate", "소통하다", [25, 75]],
            ["reply", "답장하다", [75, 75]]
        ],
        "levelTwo": [
            ["respond", "응답하다", [28, 30]],
            ["key", "자판·키", [50, 80]]
        ]
    },
    # 21. 황동 제도 콤파스
    {
        "n": "21",
        "title": "황동 콤파스와 삼각자",
        "sub": "정밀한 원을 그리는 도구",
        "video": "ch4/ch4_21.mp4",
        "img": "ch4/ch4_21-poster.jpg",
        "levelOne": [
            ["exact", "정확한·정밀한", [50, 48]],
            ["basis", "기준·기초", [75, 30]],
            ["angle", "각도·기울기", [25, 75]],
            ["measure", "측정하다", [75, 75]]
        ],
        "levelTwo": [
            ["draft", "도면·초안", [28, 30]],
            ["curve", "곡선·원호", [50, 80]]
        ]
    },
    # 22. 주물 북엔드와 책
    {
        "n": "22",
        "title": "주물 북엔드와 고서들",
        "sub": "기울지 않게 받치는 힘",
        "video": "ch4/ch4_22.mp4",
        "img": "ch4/ch4_22-poster.jpg",
        "levelOne": [
            ["support", "받치다·지지하다", [50, 48]],
            ["firm", "단단한·견고한", [75, 30]],
            ["concept", "개념·사상", [25, 75]],
            ["hold", "고정하다·잡다", [75, 75]]
        ],
        "levelTwo": [
            ["shelf", "서가·책장", [28, 30]],
            ["stack", "쌓아올리다", [50, 80]]
        ]
    },
    # 23. 가죽 펜파우치와 연필
    {
        "n": "23",
        "title": "가죽 펜파우치와 연필",
        "sub": "세 자루의 흑연 연필",
        "video": "ch4/ch4_23.mp4",
        "img": "ch4/ch4_23-poster.jpg",
        "levelOne": [
            ["belong", "소지품·소속", [50, 45]],
            ["pack", "챙기다·보관", [75, 30]],
            ["tool", "필기도구", [25, 75]],
            ["lead", "흑연심·연필심", [75, 75]]
        ],
        "levelTwo": [
            ["case", "케이스·필통", [28, 30]],
            ["pocket", "주머니·포켓", [50, 80]]
        ]
    }
]

# 단어 1200 유효성 검사 및 정제
free_available = sorted(list(all_1200 - set(used_words.keys())))

def validate_and_clean():
    ch4_obj = data["4"]
    existing_works = [w for w in ch4_obj["works"] if int(w["n"]) <= 3]
    existing_l1_words = ch4_obj["levelOneWords"][:len(existing_works)]
    existing_l2_words = ch4_obj["levelTwoWords"][:len(existing_works)]
    existing_l1_spots = ch4_obj["levelOneSpots"][:len(existing_works)]
    existing_l2_spots = ch4_obj["sceneSpots"][:len(existing_works)]

    clean_works = list(existing_works)
    clean_l1_words = list(existing_l1_words)
    clean_l2_words = list(existing_l2_words)
    clean_l1_spots = list(existing_l1_spots)
    clean_l2_spots = list(existing_l2_spots)

    curr_used = set(used_words.keys())
    free_queue = [w for w in free_available if w not in curr_used]
    q_idx = 0

    for scene in ch4_new_scenes:
        n = scene["n"]
        new_l1 = []
        new_l2 = []

        # L1 words
        for item in scene["levelOne"]:
            w, kor, spot = item[0], item[1], item[2]
            if w not in all_1200 or w in curr_used:
                rep = free_queue[q_idx]
                q_idx += 1
                new_l1.append([rep, f"{rep}·학습", spot])
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
                new_l2.append([rep, f"{rep}·도구", spot])
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

    ch4_obj["works"] = clean_works
    ch4_obj["levelOneWords"] = clean_l1_words
    ch4_obj["levelTwoWords"] = clean_l2_words
    ch4_obj["levelOneSpots"] = clean_l1_spots
    ch4_obj["sceneSpots"] = clean_l2_spots

    new_chapter_json = json.dumps(data, ensure_ascii=False, indent=2)
    new_content = s[:st] + new_chapter_json + s[en:]

    with open(SRC, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"🎉 ch4 20편 중복 제거 및 5개 배열 완벽 동기화 완료! (ch4 총 편수: {len(clean_works)}편)")

validate_and_clean()
