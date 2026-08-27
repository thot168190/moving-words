# -*- coding: utf-8 -*-
import io, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "public/learning/index.html")

s = io.open(SRC, encoding="utf-8").read()
i = s.index("const chapterData = {")
st = s.index("{", i)
d = 0
for j in range(st, len(s)):
    if s[j] == "{": d += 1
    elif s[j] == "}":
        d -= 1
        if d == 0: en = j + 1; break
data = json.loads(s[st:en])

ch6_real_words = {
    # 04. 물레와 점토
    "ch4_05": {
        "title": "물레와 점토",
        "sub": "물레 · 점토",
        "levelOne": [
            ["shape", "형태를 빚다", [48, 42]],
            ["spin", "회전하다·돌다", [72, 75]],
            ["round", "둥근 곡선", [48, 22]],
            ["firm", "단단하게 굳히다", [25, 45]]
        ],
        "levelTwo": [
            ["skill", "도예 솜씨·기술", [48, 80]],
            ["surface", "매끄러운 겉면", [25, 70]]
        ]
    },
    # 05. 재봉틀과 실토리
    "ch4_06": {
        "title": "재봉틀과 실토리",
        "sub": "재봉틀 · 실토리",
        "levelOne": [
            ["machine", "재봉틀·기계", [45, 38]],
            ["sew", "바느질하다·깁다", [45, 68]],
            ["wheel", "회전 바퀴", [78, 28]],
            ["steel", "강철 본체", [68, 52]]
        ],
        "levelTwo": [
            ["iron", "무쇠 주물", [26, 58]],
            ["straight", "곧은 박음질", [70, 72]]
        ]
    },
    # 06. 목공 대패와 대팻밥
    "ch4_07": {
        "title": "목공 대패와 대팻밥",
        "sub": "대패 · 대팻밥",
        "levelOne": [
            ["handle", "둥근 나무 손잡이", [36, 50]],
            ["sharp", "날카로운 칼날", [62, 36]],
            ["shave", "나무를 깎다", [72, 72]],
            ["curl", "말린 대팻밥", [42, 76]]
        ],
        "levelTwo": [
            ["flat", "평평한 바닥면", [26, 68]],
            ["slide", "미끄러지듯 밀다", [52, 56]]
        ]
    },
    # 07. 가죽 펀치와 가죽
    "ch4_08": {
        "title": "가죽 펀치와 가죽",
        "sub": "펀치 · 가죽",
        "levelOne": [
            ["punch", "타공 펀치 도구", [38, 38]],
            ["hole", "펀칭 구멍", [52, 62]],
            ["metal", "금속 도구", [24, 58]],
            ["tight", "단단히 조이다", [72, 48]]
        ],
        "levelTwo": [
            ["row", "구멍 줄·열", [70, 70]],
            ["strike", "내려쳐 뚫다", [48, 24]]
        ]
    },
    # 08. 스테인드글라스 조각
    "ch4_09": {
        "title": "스테인드글라스 조각",
        "sub": "유리 · 꽃잎",
        "levelOne": [
            ["piece", "유리 조각", [65, 38]],
            ["frame", "금속 테두리", [50, 72]],
            ["pattern", "꽃 모양 무늬", [35, 38]],
            ["shine", "빛나다", [70, 62]]
        ],
        "levelTwo": [
            ["fit", "맞춰 끼우다", [48, 48]],
            ["thin", "얇은 유리판", [28, 60]]
        ]
    },
    # 09. 석고상과 조각주걱
    "ch4_10": {
        "title": "석고상과 조각주걱",
        "sub": "석고상 · 주걱",
        "levelOne": [
            ["tool", "조각 주걱·도구", [75, 55]],
            ["feature", "얼굴 이목구비", [42, 30]],
            ["smooth", "표면을 다듬다", [36, 55]],
            ["edge", "조각칼의 날", [60, 38]]
        ],
        "levelTwo": [
            ["mark", "조각 자국", [26, 70]],
            ["solid", "단단한 석고", [48, 78]]
        ]
    },
    # 10. 양장본 책과 리본
    "ch4_21": {
        "title": "양장본 책과 리본",
        "sub": "책 · 리본",
        "levelOne": [
            ["bind", "제본하다·묶다", [70, 36]],
            ["thick", "두꺼운 책", [48, 46]],
            ["record", "기록하다·책", [36, 30]],
            ["detail", "세부 장식", [74, 62]]
        ],
        "levelTwo": [
            ["sheet", "종이 장·낱장", [28, 65]],
            ["contain", "내용을 담다", [52, 72]]
        ]
    }
}

all_1200 = set(io.open(os.path.join(ROOT, "_작업/all1200.txt"), encoding="utf-8").read().split())

ch6_obj = data["6"]
for idx, w in enumerate(ch6_obj["works"]):
    base_k = os.path.basename(w["video"]).replace(".mp4", "")
    if base_k in ch6_real_words:
        m = ch6_real_words[base_k]
        w["title"] = m["title"]
        w["sub"] = m["sub"]
        
        l1_w = [[p[0], p[1]] for p in m["levelOne"]]
        l1_s = [p[2] for p in m["levelOne"]]
        
        l2_w = [[p[0], p[1]] for p in m["levelTwo"]]
        l2_s = [p[2] for p in m["levelTwo"]]
        
        w["words"] = l1_w + l2_w
        ch6_obj["levelOneWords"][idx] = l1_w
        ch6_obj["levelTwoWords"][idx] = l2_w
        ch6_obj["levelOneSpots"][idx] = l1_s
        ch6_obj["sceneSpots"][idx] = l2_s

new_chapter_json = json.dumps(data, ensure_ascii=False, indent=2)
new_content = s[:st] + new_chapter_json + s[en:]

with open(SRC, "w", encoding="utf-8") as f:
    f.write(new_content)

print("ch6 정밀 단어 및 좌표 주입 완료!")
