# -*- coding: utf-8 -*-
from build_set3_prompts import SET3_PROMPTS
with open("_작업/prompt_railway_aligned.txt", "r", encoding="utf-8") as f:
    railway_p = f.read().strip()

SET3_PROMPTS[1]["prompt"] = railway_p

# 텍스트 파일 갱신
with open("_작업/google_flow_bulk_next10.txt", "w", encoding="utf-8") as f:
    for p in SET3_PROMPTS:
        f.write(" ".join(p["prompt"].split()) + "\n\n")

import build_master_hub_ultimate
print("허브 내 3차 2번 주행 방향 일치 철길 건널목 씬 갱신 완료!")
