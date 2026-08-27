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

# 1. ch5_06 ~ ch5_16 실물에 맞춘 간결한 제목 정렬
clean_names = {
    # ch5
    "ch5_06": ("서재 정리대와 고서", "서재와 도구"),
    "ch5_07": ("판사봉과 법전", "법정과 저울"),
    "ch5_08": ("항구와 닻", "닻과 상자"),
    "ch5_09": ("벌통과 꿀단지", "벌통과 꿀"),
    "ch5_10": ("물레와 도자기", "물레와 점토"),
    "ch5_11": ("온실과 분무기", "온실과 식물"),
    "ch5_12": ("동판 에칭 판화", "판화와 롤러"),
    "ch5_13": ("오크통과 포도", "오크통과 과일"),
    "ch5_14": ("양팔저울과 추", "저울과 분동"),
    "ch5_15": ("천구의와 궤도", "천구의와 고리"),
    "ch5_16": ("스쿨버스와 정지판", "버스와 표지판"),
    # ch4 단일사물 10개 실물에 맞춘 간결한 제목 정렬
    "ch4_14": ("만년필과 잉크", "만년필과 잉크방울"),
    "ch4_15": ("돋보기와 렌즈", "돋보기와 손잡이"),
    "ch4_16": ("탁상 핸드벨", "핸드벨과 손잡이"),
    "ch4_17": ("잉크병과 스포이트", "잉크병과 스포이트"),
    "ch4_18": ("나무 독서대", "독서대와 클립"),
    "ch4_19": ("탁상 스테이플러", "스테이플러와 받침"),
    "ch4_20": ("휴대용 연필깎이", "연필깎이와 칼날"),
    "ch4_21": ("양장본 책과 리본", "책과 리본책갈피"),
    "ch4_22": ("클립과 압정", "클립과 고정압정"),
    "ch4_23": ("황동 인장 스탬프", "스탬프와 손잡이"),
}

for ch_k, ch_obj in data.items():
    for w in ch_obj["works"]:
        # img 또는 video에서 key 추출
        base_k = os.path.basename(w["video"]).replace(".mp4", "")
        if base_k in clean_names:
            w["title"] = clean_names[base_k][0]
            w["sub"] = clean_names[base_k][1]
        else:
            # 부제를 간결하게 핵심 관련단어로 정돈
            if "—" in w.get("sub", "") or len(w.get("sub", "")) > 15:
                # 간단한 2단어 형태로 축약
                words_ko = [b for a, b in w["words"][:2]]
                if words_ko:
                    w["sub"] = " · ".join(words_ko)

new_chapter_json = json.dumps(data, ensure_ascii=False, indent=2)
new_content = s[:st] + new_chapter_json + s[en:]

with open(SRC, "w", encoding="utf-8") as f:
    f.write(new_content)

print("public/learning/index.html 간결한 제목 반영 완료!")
