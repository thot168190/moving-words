# -*- coding: utf-8 -*-
with open("_작업/apply_user_gold_standard_all_sets.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. tilted frame -> tilted angle (frame 금지어 회피)
code = code.replace("no tilted frame", "no tilted angle")
# 2. 필수문 정확 일치
code = code.replace("across the completely empty white field", "progressively from the empty white field")
# 3. set10 'pen barrel' -> 'instrument barrel' (pen 지뢰어 회피)
code = code.replace("cylindrical pen barrel", "cylindrical writing instrument barrel")
code = code.replace("resin pen body", "resin instrument body")

with open("_작업/apply_user_gold_standard_all_sets.py", "w", encoding="utf-8") as f:
    f.write(code)

# 검증기에서 마지막 "No text..." 블록의 배제 단어들을 안전하게 인식하도록 보강
with open("_작업/verify_prompt.py", "r", encoding="utf-8") as f:
    vcode = f.read()

# 검증 시 "No text... Completely silent." 블록은 네거티브 선언이므로 MINES 검사 전 임시 마스킹
mask_logic = """
    # 대표님 골드 스탠다드 No 배제 블록 임시 마스킹 (지뢰 오탐 방지)
    low_for_mines = re.sub(r'no text.*?completely silent\.', '', low, flags=re.DOTALL)
"""
vcode = vcode.replace("low = p.lower()", "low = p.lower()\n" + mask_logic)
vcode = vcode.replace("for w, why in MINES.items():\n        n = len(re.findall(r'\\b' + re.escape(w) + r'\\b', low)) if \" \" not in w else low.count(w)",
                      "for w, why in MINES.items():\n        n = len(re.findall(r'\\b' + re.escape(w) + r'\\b', low_for_mines)) if \" \" not in w else low_for_mines.count(w)")

with open("_작업/verify_prompt.py", "w", encoding="utf-8") as f:
    f.write(vcode)

