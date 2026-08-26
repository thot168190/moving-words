# -*- coding: utf-8 -*-
"""
대표님 하달 [주방 사물 10개 세필 수채 수리본] Set 11에 100% 원문 그대로 반영!
"""

import json, re

with open("/Users/mihyunlee/Desktop/현재작업다운로드/움직이는그림사전_주방사물_10개_세필수채_수리본.md", "r", encoding="utf-8") as f:
    content = f.read()

# 정규식으로 10개 프롬프트 추출
blocks = re.findall(r'```text\n(.*?)\n```', content, re.DOTALL)
print(f"추출된 수리본 프롬프트 개수: {len(blocks)}개")

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for s in data:
    if s["set_id"] == "set11":
        for idx, block in enumerate(blocks):
            clean_p = " ".join(block.split())
            s["prompts"][idx]["prompt"] = clean_p

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("_작업/bulk_sets/set11_10.txt", "w", encoding="utf-8") as f:
    for block in blocks:
        clean_p = " ".join(block.split())
        f.write(clean_p + "\n\n")

print("Set 11 (주방 사물 10개) 마스터 DB 및 벌크 파일 100% 반영 완료!")

