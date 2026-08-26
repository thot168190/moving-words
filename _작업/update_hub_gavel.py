# -*- coding: utf-8 -*-
from build_set3_prompts import SET3_PROMPTS
with open("_작업/prompt_gavel_fixed.txt", "r", encoding="utf-8") as f:
    fixed_p = f.read().strip()

SET3_PROMPTS[1]["prompt"] = fixed_p

import build_master_hub_v2
print("허브 내 3차 2번 의사봉 보정본 갱신 완료!")
