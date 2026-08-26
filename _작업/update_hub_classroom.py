# -*- coding: utf-8 -*-
from build_set3_prompts import SET3_PROMPTS
with open("_작업/prompt_classroom.txt", "r", encoding="utf-8") as f:
    class_p = f.read().strip()

SET3_PROMPTS[1] = {
    "id": "set3-02",
    "chapter": "New Chapter (ACADEMY)",
    "title": "아늑한 교실의 스탠딩 칠판과 학생 의자 (글자/손 0% 현실 교실)",
    "words": ["board (칠판)", "clock (시계)", "rule (규칙)", "order (질서/정돈)", "class (수업)"],
    "prompt": class_p
}

# 텍스트 파일 갱신
with open("_작업/google_flow_bulk_next10.txt", "w", encoding="utf-8") as f:
    for p in SET3_PROMPTS:
        f.write(" ".join(p["prompt"].split()) + "\n\n")

import build_master_hub_v2
print("허브 내 3차 2번 아늑한 교실 씬 갱신 완료!")
