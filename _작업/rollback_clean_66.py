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

# 13개로 완벽 롤백
data["2"]["works"] = data["2"]["works"][:13]
data["2"]["levelOneWords"] = data["2"]["levelOneWords"][:13]
data["2"]["levelTwoWords"] = data["2"]["levelTwoWords"][:13]
data["2"]["levelOneSpots"] = data["2"]["levelOneSpots"][:13]
data["2"]["sceneSpots"] = data["2"]["sceneSpots"][:13]

new_json = json.dumps(data, ensure_ascii=False, indent=2)
new_html = s[:st] + new_json + s[en:]
with open("public/learning/index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("기존 66편으로 완전 원상복구(롤백) 완료!")
subprocess.run(["python3", "_작업/scene_tool.py", "verify"])

