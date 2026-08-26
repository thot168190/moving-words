# -*- coding: utf-8 -*-
from build_set3_prompts import SET3_PROMPTS
with open("_작업/prompt_railway_perfect.txt", "r", encoding="utf-8") as f:
    railway_p = f.read().strip()

SET3_PROMPTS[1] = {
    "id": "set3-02",
    "chapter": "New Chapter (SAFETY)",
    "title": "철길 건널목 차단기와 신호대기 스쿨버스 (수평 아이레벨 뷰)",
    "words": ["traffic (교통)", "govern (통제하다)", "order (질서)", "prevent (예방하다)", "barrier (차단기)"],
    "prompt": railway_p
}

# 텍스트 파일 갱신
with open("_작업/google_flow_bulk_next10.txt", "w", encoding="utf-8") as f:
    for p in SET3_PROMPTS:
        f.write(" ".join(p["prompt"].split()) + "\n\n")

import build_master_hub_ultimate
print("허브 내 3차 2번 수평 아이레벨 철길 건널목 씬 갱신 완료!")
