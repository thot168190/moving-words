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

# 1. 미술공예 Set07 (001~010) 실물 전수 정밀 매핑
# 001(ch4_04): 이젤과 화판
# 002(ch4_05): 물레와 도자기
# 003(ch4_06): 재봉틀과 실토리 (Sewing machine)
# 004(ch4_07): 목공 대패와 대팻밥 (Wood plane)
# 005(ch4_08): 가죽 펀치와 가죽 (Leather punch)
# 006(ch4_09): 스테인드글라스 조각 (Stained glass)
# 007(ch4_10): 석고상과 조각주걱 (Plaster bust)
# 008(ch4_11): 판화 롤러와 목판 (Printmaking roller)
# 009(ch4_12): 베틀과 북 (Weaving loom)
# 010(ch4_13): 핀셋과 보석 (Jeweler's tweezers)

set07_map = {
    "ch4_04": ("이젤과 화판", "이젤 · 화판"),
    "ch4_05": ("물레와 점토", "물레 · 점토"),
    "ch4_06": ("재봉틀과 실토리", "재봉틀 · 실토리"),
    "ch4_07": ("목공 대패와 대팻밥", "대패 · 대팻밥"),
    "ch4_08": ("가죽 펀치와 가죽", "펀치 · 가죽"),
    "ch4_09": ("스테인드글라스 조각", "유리 · 꽃잎"),
    "ch4_10": ("석고상과 조각주걱", "석고상 · 주걱"),
    "ch4_11": ("판화 롤러와 목판", "롤러 · 목판"),
    "ch4_12": ("베틀과 북", "베틀 · 북"),
    "ch4_13": ("핀셋과 보석", "핀셋 · 보석"),
}

for ch_k, ch_obj in data.items():
    for idx, w in enumerate(ch_obj["works"]):
        base_k = os.path.basename(w["video"]).replace(".mp4", "")
        if base_k in set07_map:
            w["title"] = set07_map[base_k][0]
            w["sub"] = set07_map[base_k][1]

new_chapter_json = json.dumps(data, ensure_ascii=False, indent=2)
new_content = s[:st] + new_chapter_json + s[en:]

with open(SRC, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Set07 실물 정확 일치 반영 완료!")
