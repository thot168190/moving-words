# -*- coding: utf-8 -*-
import io, json, subprocess

# 1. ch2_14.json 수정: pair -> soil (흙), category -> pot (화분)
# 그림 진실의 법칙: 화분(pot), 흙(soil), 식물(unit/plant), 모양(shape)
ch2_14_data = {
  "chapter": 2,
  "n": "14",
  "title": "화분 속 새싹",
  "sub": "흙에서 자라나는 초록 잎",
  "video": "ch2/ch2_14.mp4",
  "img": "ch2/ch2_14-poster.jpg",
  "levelOne": [
    ["shape", "모양새", [35, 30]],
    ["unit", "식물 개체", [72, 28]],
    ["soil", "화분의 흙", [28, 70]],
    ["pot", "테라코타 화분", [68, 72]]
  ],
  "levelTwo": [
    ["develop", "자라나다", [48, 15]],
    ["create", "생겨나다", [78, 52]],
    ["stable", "안정되다", [22, 45]],
    ["steady", "차분하다", [58, 85]]
  ]
}

with open("_작업/새편/ch2_14.json", "w", encoding="utf-8") as f:
    json.dump(ch2_14_data, f, ensure_ascii=False, indent=2)

# check & add
r1 = subprocess.run(["python3", "_작업/scene_tool.py", "check", "_작업/새편/ch2_14.json"], capture_output=True, text=True)
out1 = (r1.stdout + r1.stderr).strip()
print("Check 결과:\n", out1)

r2 = subprocess.run(["python3", "_작업/scene_tool.py", "add", "_작업/새편/ch2_14.json"], capture_output=True, text=True)
print("Add 결과:\n", (r2.stdout + r2.stderr).strip())

