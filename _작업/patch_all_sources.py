# -*- coding: utf-8 -*-
from fix_hub_prompts_ro import patch_prompt

# build_next_10_prompts.py
with open("_작업/build_next_10_prompts.py", "r", encoding="utf-8") as f:
    c = f.read()
from build_next_10_prompts import NEXT_10_PROMPTS
for p in NEXT_10_PROMPTS:
    p["prompt"] = patch_prompt(p["prompt"])

# build_set3_prompts.py
from build_set3_prompts import SET3_PROMPTS
for p in SET3_PROMPTS:
    p["prompt"] = patch_prompt(p["prompt"])

import build_master_hub_ultimate
print("전체 프롬프트 원장 4곳 일괄 정본 패치 완료!")
