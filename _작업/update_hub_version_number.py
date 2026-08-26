# -*- coding: utf-8 -*-
with open("_작업/rebuild_hub_crystal_clean.py", "r", encoding="utf-8") as f:
    code = f.read()

# 버전 숫자를 명확하게 v5.0 (2026-08-25 16:25 최종정본)으로 크게 표시
code = code.replace("v4.0 Final", "v5.0 FINAL (2026-08-25)")
code = code.replace("Hand Zero Edition", "v5.0 FINAL — 손0%·중복0%·단일히어로 정본")

with open("_작업/rebuild_hub_crystal_clean.py", "w", encoding="utf-8") as f:
    f.write(code)

