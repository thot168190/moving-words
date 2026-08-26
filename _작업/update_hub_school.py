# -*- coding: utf-8 -*-
from build_set3_prompts import SET3_PROMPTS
with open("_작업/prompt_school_ruler.txt", "r", encoding="utf-8") as f:
    ruler_p = f.read().strip()

SET3_PROMPTS[1] = {
    "id": "set3-02",
    "chapter": "New Chapter (ACADEMY)",
    "title": "단정한 원목 눈금자와 유리 모래시계 (현실 학급 사물)",
    "words": ["rule (규칙·자)", "order (정돈·순서)", "judge (판단하다)", "law (법칙·원칙)", "right (옳음·오른쪽)"],
    "prompt": ruler_p
}

# 텍스트 파일 갱신
with open("_작업/google_flow_bulk_next10.txt", "w", encoding="utf-8") as f:
    for p in SET3_PROMPTS:
        f.write(" ".join(p["prompt"].split()) + "\n\n")

import build_master_hub_v2
print("허브 내 3차 2번 학급 눈금자 씬으로 전면 교체 완료!")
