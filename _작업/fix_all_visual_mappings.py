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

# 1. 미술공예 Set07 (ch4_04 ~ ch4_13) 10편의 정밀 실물 매핑
set07_real = {
    "ch4_04": {"title": "이젤과 화판", "sub": "이젤 · 화판", "words": [("easel", "이젤"), ("board", "화판"), ("paint", "물감"), ("jar", "병"), ("stand", "받침대"), ("canvas", "캔버스")]},
    "ch4_05": {"title": "물레와 도자기", "sub": "물레 · 점토", "words": [("wheel", "물레"), ("clay", "점토"), ("vase", "꽃병"), ("pot", "도자기"), ("spin", "회전"), ("shape", "형태")]},
    "ch4_06": {"title": "재봉틀과 실토리", "sub": "재봉틀 · 실", "words": [("sewing", "재봉"), ("machine", "기계"), ("thread", "실"), ("spool", "실토리"), ("needle", "바늘"), ("wheel", "바퀴")]},
    "ch4_07": {"title": "목공 대패와 대팻밥", "sub": "대패 · 나무", "words": [("plane", "대패"), ("blade", "칼날"), ("wood", "나무"), ("shaving", "대팻밥"), ("curl", "말림"), ("timber", "목재")]},
    "ch4_08": {"title": "가죽 펀치와 가죽", "sub": "펀치 · 가죽", "words": [("punch", "펀치"), ("leather", "가죽"), ("strap", "가죽띠"), ("hole", "구멍"), ("steel", "쇠"), ("stitch", "바느질")]},
    "ch4_09": {"title": "스테인드글라스 조각", "sub": "유리 · 꽃잎", "words": [("glass", "유리"), ("color", "색채"), ("frame", "틀"), ("piece", "조각"), ("shine", "빛"), ("petal", "꽃잎")]},
    "ch4_10": {"title": "석고상과 조각주걱", "sub": "석고상 · 주걱", "words": [("bust", "석고상"), ("statue", "조각상"), ("spatula", "주걱"), ("stone", "돌"), ("carve", "조각하다"), ("art", "미술")]},
    "ch4_11": {"title": "판화 롤러와 목판", "sub": "롤러 · 목판", "words": [("roller", "롤러"), ("block", "목판"), ("ink", "잉크"), ("print", "판화"), ("wood", "나무"), ("press", "누름")]},
    "ch4_12": {"title": "베틀과 나무 북", "sub": "베틀 · 북", "words": [("loom", "베틀"), ("shuttle", "북"), ("thread", "실"), ("weave", "직조"), ("cloth", "천"), ("warp", "날실")]},
    "ch4_13": {"title": "보석 핀셋과 다이아몬드", "sub": "핀셋 · 보석", "words": [("tweezer", "핀셋"), ("gem", "보석"), ("diamond", "다이아몬드"), ("cushion", "받침"), ("sparkle", "반짝임"), ("bright", "빛나는")]},
}

for ch_k, ch_obj in data.items():
    for idx, w in enumerate(ch_obj["works"]):
        base_k = os.path.basename(w["video"]).replace(".mp4", "")
        if base_k in set07_real:
            info = set07_real[base_k]
            w["title"] = info["title"]
            w["sub"] = info["sub"]
            # 단어 매칭 업데이트
            w["words"] = info["words"]
            ch_obj["levelOneWords"][idx] = info["words"][:4]
            ch_obj["levelTwoWords"][idx] = info["words"][4:6]

new_chapter_json = json.dumps(data, ensure_ascii=False, indent=2)
new_content = s[:st] + new_chapter_json + s[en:]

with open(SRC, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Set07 실물 정확 매칭 반영 완료!")
