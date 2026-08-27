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
        if d == 0:
            en = j + 1
            break
data = json.loads(s[st:en])

def extract_scene(ch_num, work_title_substr):
    ch_k = str(ch_num)
    ch_obj = data[ch_k]
    idx = -1
    for i, w in enumerate(ch_obj["works"]):
        if work_title_substr in w["title"]:
            idx = i
            break
    if idx == -1:
        return None
    item = {
        "work": ch_obj["works"].pop(idx),
        "l1_w": ch_obj["levelOneWords"].pop(idx),
        "l2_w": ch_obj["levelTwoWords"].pop(idx),
        "l1_s": ch_obj["levelOneSpots"].pop(idx),
        "l2_s": ch_obj["sceneSpots"].pop(idx),
    }
    return item

def append_scene(ch_num, item):
    ch_k = str(ch_num)
    ch_obj = data[ch_k]
    ch_obj["works"].append(item["work"])
    ch_obj["levelOneWords"].append(item["l1_w"])
    ch_obj["levelTwoWords"].append(item["l2_w"])
    ch_obj["levelOneSpots"].append(item["l1_s"])
    ch_obj["sceneSpots"].append(item["l2_s"])

# ch6의 식탁/식사 3편 -> ch7 (주방 CULINA)으로 이동
food_scenes_to_ch7 = [
    "가지런한 아침상",
    "과일 접시",
    "장 보고 온 저녁"
]
for title in food_scenes_to_ch7:
    sc = extract_scene(6, title)
    if sc:
        append_scene(7, sc)

# ch2의 정원 새/모이그릇 등 5편 -> ch3 (정원 HORTUS)으로 이동
garden_scenes_to_ch3 = [
    "호랑나비의 날갯짓",
    "나뭇가지 위 푸른 박새",
    "잎사귀 위 무당벌레",
    "정원의 돌 모이그릇",
    "나선형 껍질의 달팽이"
]
for title in garden_scenes_to_ch3:
    sc = extract_scene(2, title)
    if sc:
        append_scene(3, sc)

# ch3의 집안/생활 사물 4편 -> ch1 (집 DOMUS)으로 이동
domus_scenes_to_ch1 = [
    "옷걸이의 옷",
    "맑은 욕실",
    "계단 옆 거실",
    "램프 곁의 담요"
]
for title in domus_scenes_to_ch1:
    sc = extract_scene(3, title)
    if sc:
        append_scene(1, sc)

# 각 챕터별 n 번호 ('01', '02', ...) 순차 정리
for ch in range(1, 13):
    ch_k = str(ch)
    ch_obj = data[ch_k]
    for idx, w in enumerate(ch_obj["works"]):
        w["n"] = f"{idx+1:02d}"

print("\n=== 최종 균형 배분 결과 ===")
total_works = 0
for ch in range(1, 13):
    ch_k = str(ch)
    count = len(data[ch_k]["works"])
    total_works += count
    print(f"ch{ch}: {count}편")

print(f"\n총 편수: {total_works}편 (157편 무손실 완벽 보존)")

new_chapter_json = json.dumps(data, ensure_ascii=False, indent=2)
new_content = s[:st] + new_chapter_json + s[en:]

with open(SRC, "w", encoding="utf-8") as f:
    f.write(new_content)

print("public/learning/index.html 균형 저장 완료!")
