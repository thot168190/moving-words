# -*- coding: utf-8 -*-
import json

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Set 06 (정원원예)
set06 = data[2]["prompts"]
# Set 09 (조류곤충)
set09 = data[5]["prompts"]

print("=== ch2 20편 (ch2_14 ~ ch2_33) 프롬프트 및 단어 목록 ===")
print("\n[5차 정원원예 10편 -> ch2_14 ~ ch2_23]")
for idx, p in enumerate(set06):
    print(f"- ch2_{str(idx+14).zfill(2)} : {p['title']} / 단어 후보: {p['words']}")

print("\n[8차 조류곤충 10편 -> ch2_24 ~ ch2_33]")
for idx, p in enumerate(set09):
    print(f"- ch2_{str(idx+24).zfill(2)} : {p['title']} / 단어 후보: {p['words']}")

