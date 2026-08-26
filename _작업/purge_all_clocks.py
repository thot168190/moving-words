# -*- coding: utf-8 -*-
"""
시계(Clock, Watch, Hourglass, Timer, Metronome) 관련 사물 100% 영구 퇴출 감사 및 교체!
"""

import json

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

clock_keywords = ["watch", "clock", "hourglass", "timer", "metronome", "clockwork", "escapement", "시계", "모래시계", "타이머", "메트로놈"]

found_clocks = []
for s in data:
    for p in s["prompts"]:
        for kw in clock_keywords:
            if kw in p["title"].lower() or kw in p["prompt"].lower():
                found_clocks.append((s["set_name"], p["title"], kw))
                break

print(f"=== 시계 관련 사물 검색 결과: 총 {len(found_clocks)}건 발견 ===")
for sname, title, kw in found_clocks:
    print(f" - [{sname}] {title} (키워드: {kw})")

