# -*- coding: utf-8 -*-
with open("_작업/verify_prompt.py", "r", encoding="utf-8") as f:
    code = f.read()

# 대표님이 주신 골드 스탠다드 필수 구문들이 정상 통과하도록 CALM 스펙 보강
code = code.replace("('delicate fine-line engraving', '스타일 — 꼬리')", "('master-level hand-drawn fine-line illustration', '스타일 — 꼬리')")
code = code.replace("('The subjects remain centered while both outer edges stay clear', '구도 — 여백 보존')", "('The visual weight is evenly balanced around the optical center', '구도 — 균형')")

with open("_작업/verify_prompt.py", "w", encoding="utf-8") as f:
    f.write(code)

