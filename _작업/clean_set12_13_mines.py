# -*- coding: utf-8 -*-
with open("_작업/apply_gold_standard_all_remaining_sets.py", "r", encoding="utf-8") as f:
    code = f.read()

# Set 12 정제
code = code.replace("brass finger cymbals", "circular brass clash cymbals")
code = code.replace("music desk tray", "sheet music tray")
code = code.replace("stand desk", "stand tray")
code = code.replace("pearl-cream", "pearl-ivory")

# Set 13 정제
code = code.replace("paper crease lines", "surface seal marks")
code = code.replace("wooden frame pillars", "wooden upright pillars")

with open("_작업/apply_gold_standard_all_remaining_sets.py", "w", encoding="utf-8") as f:
    f.write(code)

