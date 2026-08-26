# -*- coding: utf-8 -*-
import io, json, subprocess

s = io.open("public/learning/index.html", encoding="utf-8").read()
i = s.index("const chapterData = {"); st = s.index("{", i); d = 0
for j in range(st, len(s)):
    if s[j] == "{": d += 1
    elif s[j] == "}":
        d -= 1
        if d == 0: en = j + 1; break
data = json.loads(s[st:en])

# ch2_14의 words, levelOne, levelTwo, spots 정확하게 수정
# 잎사귀 한 쌍(pair) 완전 삭제 -> cell (식물 세포), origin (생명의 근원)
ch2_14_idx = 13
work = data["2"]["works"][ch2_14_idx]
print("기존 ch2_14 title:", work["title"])

work["words"] = [
    ["shape", "모양새"],
    ["cell", "식물 세포"],
    ["origin", "생명의 근원"],
    ["sample", "어린 잎 표본"],
    ["alive", "살아있는"],
    ["breathe", "숨을 쉬다"],
    ["create", "생겨나다"],
    ["exist", "존재하다"]
]

data["2"]["levelOneWords"][ch2_14_idx] = [
    ["shape", "모양새"],
    ["cell", "식물 세포"],
    ["origin", "생명의 근원"],
    ["sample", "어린 잎 표본"]
]

data["2"]["levelTwoWords"][ch2_14_idx] = [
    ["alive", "살아있는"],
    ["breathe", "숨을 쉬다"],
    ["create", "생겨나다"],
    ["exist", "존재하다"]
]

data["2"]["levelOneSpots"][ch2_14_idx] = [[35, 30], [72, 28], [28, 70], [68, 72]]
data["2"]["sceneSpots"][ch2_14_idx] = [[48, 15], [78, 52], [22, 45], [58, 85]]

new_json = json.dumps(data, ensure_ascii=False, indent=2)
new_html = s[:st] + new_json + s[en:]
with open("public/learning/index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("ch2_14 수정 완료!")
subprocess.run(["python3", "_작업/scene_tool.py", "verify"])

