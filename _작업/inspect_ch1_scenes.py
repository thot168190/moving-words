# -*- coding: utf-8 -*-
import scene_tool

_, _, _, cdata = scene_tool.load()
ch1_works = cdata["1"]["works"]
print(f"=== 챕터 1 (INVENTIO 세상을 발견해요) 총 {len(ch1_works)}개 장면 ===")
for w in ch1_works:
    print(f"[{w['n']}] {w['title']} ({w['sub']}) - {w['video']}")
    print("   단어:", [a for a, b in w["words"]])

