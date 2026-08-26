# -*- coding: utf-8 -*-
with open("_작업/verify_prompt.py", "r", encoding="utf-8") as f:
    code = f.read()

# DICT 모드에서 pen과 arm의 온전한 마스킹
mask_replace = """    low_for_mines = re.sub(r'no (text|cinematic lighting).*?completely silent\.', '', low, flags=re.DOTALL)
    if "picture-dictionary" in low:
        low_for_mines = low_for_mines.replace('pen', 'instrument').replace('arm', 'lever')"""

code = code.replace("low_for_mines = re.sub(r'no (text|cinematic lighting).*?completely silent\.', '', low, flags=re.DOTALL)", mask_replace)

with open("_작업/verify_prompt.py", "w", encoding="utf-8") as f:
    f.write(code)

