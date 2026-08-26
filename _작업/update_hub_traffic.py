# -*- coding: utf-8 -*-
from build_set3_prompts import SET3_PROMPTS
with open("_작업/prompt_traffic_rules.txt", "r", encoding="utf-8") as f:
    traffic_p = f.read().strip()

SET3_PROMPTS[1] = {
    "id": "set3-02",
    "chapter": "New Chapter (CITIZEN)",
    "title": "교통 신호등과 횡단보도 정지선 (질서와 규칙)",
    "words": ["rule (규칙)", "order (질서·정돈)", "law (법칙·원칙)", "signal (신호)", "cross (건너다)"],
    "prompt": traffic_p
}

# 텍스트 파일 갱신
with open("_작업/google_flow_bulk_next10.txt", "w", encoding="utf-8") as f:
    for p in SET3_PROMPTS:
        f.write(" ".join(p["prompt"].split()) + "\n\n")

import build_master_hub_v2
print("허브 내 3차 2번 교통 신호등 씬 갱신 완료!")
