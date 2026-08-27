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

ch5_real_words = {
    # 06. 서재 정리대와 고서
    "ch5_06": {
        "title": "서재 정리대와 고서",
        "sub": "선반 · 고서",
        "levelOne": [
            ["shelf", "정리대·선반", [48, 45]],
            ["clip", "문서 클립", [28, 65]],
            ["neat", "가지런한", [75, 42]],
            ["record", "기록 문서", [52, 22]]
        ],
        "levelTwo": [
            ["arrange", "정리하다·배치", [25, 32]],
            ["contain", "내용을 담다", [72, 70]]
        ]
    },
    # 07. 법정 판사봉과 법전
    "ch5_07": {
        "title": "판사봉과 법전",
        "sub": "판사봉 · 법전",
        "levelOne": [
            ["law", "법·법률", [72, 45]],
            ["judge", "판사·판결", [42, 38]],
            ["strike", "봉을 내려치다", [36, 58]],
            ["order", "질서·명령", [72, 68]]
        ],
        "levelTwo": [
            ["rule", "규칙·원칙", [45, 68]],
            ["legal", "법률의·공식적인", [22, 48]]
        ]
    },
    # 08. 항구와 닻
    "ch5_08": {
        "title": "항구와 닻",
        "sub": "항구 · 닻",
        "levelOne": [
            ["port", "항구·부두", [72, 45]],
            ["rope", "굵은 밧줄", [60, 62]],
            ["chain", "쇠사슬 체인", [42, 58]],
            ["wave", "물결·파도", [75, 78]]
        ],
        "levelTwo": [
            ["tie", "단단히 묶다", [25, 65]],
            ["steady", "안정된·정박한", [42, 35]]
        ]
    },
    # 09. 벌통과 꿀단지
    "ch5_09": {
        "title": "벌통과 꿀단지",
        "sub": "벌통 · 꿀",
        "levelOne": [
            ["honey", "달콤한 꿀", [25, 68]],
            ["sweet", "달콤한 맛", [32, 48]],
            ["roof", "벌통 지붕", [48, 25]],
            ["pure", "순수한 꿀", [42, 78]]
        ],
        "levelTwo": [
            ["wild", "야생의 벌과 꽃", [72, 65]],
            ["feed", "꿀을 먹이다", [70, 38]]
        ]
    },
    # 10. 물레와 도자기
    "ch5_10": {
        "title": "물레와 도자기",
        "sub": "물레 · 도자기",
        "levelOne": [
            ["pot", "도자기 화병", [52, 45]],
            ["round", "둥근 곡선", [46, 25]],
            ["tool", "나무 성형도구", [28, 72]],
            ["roll", "회전하며 돌다", [68, 76]]
        ],
        "levelTwo": [
            ["shape", "형태를 빚다", [72, 65]],
            ["surface", "매끄러운 겉면", [24, 48]]
        ]
    },
    # 11. 온실과 분무기
    "ch5_11": {
        "title": "온실과 분무기",
        "sub": "온실 · 분무기",
        "levelOne": [
            ["plant", "초록 화초", [38, 55]],
            ["leaf", "넓은 잎사귀", [28, 32]],
            ["spray", "분무기 물뿌림", [78, 52]],
            ["shine", "유리창 햇빛", [62, 32]]
        ],
        "levelTwo": [
            ["alive", "생기 있게 자라다", [24, 68]],
            ["pour", "물을 주다", [72, 75]]
        ]
    },
    # 12. 동판 에칭 판화
    "ch5_12": {
        "title": "동판 에칭 판화",
        "sub": "동판 · 판화",
        "levelOne": [
            ["plate", "금속 동판", [42, 48]],
            ["press", "눌러 찍다", [68, 65]],
            ["pattern", "새겨진 무늬", [36, 28]],
            ["mark", "판화 새김자국", [60, 38]]
        ],
        "levelTwo": [
            ["skill", "섬세한 솜씨", [25, 62]],
            ["detail", "세부 선묘", [75, 36]]
        ]
    },
    # 13. 오크통과 포도
    "ch5_13": {
        "title": "오크통과 포도",
        "sub": "오크통 · 포도",
        "levelOne": [
            ["tap", "오크통 꼭지", [32, 52]],
            ["bunch", "포도 송이", [22, 72]],
            ["firm", "단단한 나무통", [50, 32]],
            ["flow", "흘러나오다", [48, 68]]
        ],
        "levelTwo": [
            ["solid", "견고한 오크통", [68, 45]],
            ["spread", "향이 퍼지다", [70, 72]]
        ]
    },
    # 14. 양팔저울과 추
    "ch5_14": {
        "title": "양팔저울과 추",
        "sub": "저울 · 분동",
        "levelOne": [
            ["scale", "양팔 저울", [45, 45]],
            ["balance", "균형을 맞추다", [48, 25]],
            ["measure", "무게를 재다", [26, 52]],
            ["level", "수평을 이루다", [48, 68]]
        ],
        "levelTwo": [
            ["equal", "양쪽 무게가 같은", [72, 52]],
            ["exact", "정확한 측정", [24, 75]]
        ]
    },
    # 15. 천구의와 궤도
    "ch5_15": {
        "title": "천구의와 궤도",
        "sub": "천구의 · 궤도",
        "levelOne": [
            ["pole", "회전축 기둥", [50, 75]],
            ["chart", "천체 별자리도", [38, 38]],
            ["sight", "천체 관측 시야", [68, 42]],
            ["frame", "황동 궤도 틀", [52, 20]]
        ],
        "levelTwo": [
            ["guide", "안내하는 별자리", [28, 52]],
            ["metal", "황동 링 금속", [70, 70]]
        ]
    },
    # 16. 스쿨버스와 정지판
    "ch5_16": {
        "title": "스쿨버스와 정지판",
        "sub": "버스 · 정지판",
        "levelOne": [
            ["route", "운행 노선", [45, 38]],
            ["traffic", "거리 교통", [72, 45]],
            ["vehicle", "통학 차량", [35, 68]],
            ["direct", "바른 길로 가다", [68, 68]]
        ],
        "levelTwo": [
            ["sign", "정지 표지판", [75, 26]],
            ["warn", "승하차 경고", [24, 45]]
        ]
    }
}

ch5_obj = data["5"]
for idx, w in enumerate(ch5_obj["works"]):
    base_k = os.path.basename(w["video"]).replace(".mp4", "")
    if base_k in ch5_real_words:
        m = ch5_real_words[base_k]
        w["title"] = m["title"]
        w["sub"] = m["sub"]
        
        l1_w = [[p[0], p[1]] for p in m["levelOne"]]
        l1_s = [p[2] for p in m["levelOne"]]
        
        l2_w = [[p[0], p[1]] for p in m["levelTwo"]]
        l2_s = [p[2] for p in m["levelTwo"]]
        
        w["words"] = l1_w + l2_w
        ch5_obj["levelOneWords"][idx] = l1_w
        ch5_obj["levelTwoWords"][idx] = l2_w
        ch5_obj["levelOneSpots"][idx] = l1_s
        ch5_obj["sceneSpots"][idx] = l2_s

new_chapter_json = json.dumps(data, ensure_ascii=False, indent=2)
new_content = s[:st] + new_chapter_json + s[en:]

with open(SRC, "w", encoding="utf-8") as f:
    f.write(new_content)

print("ch5 완전 무결점 주입 완료!")
