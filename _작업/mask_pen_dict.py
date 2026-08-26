# -*- coding: utf-8 -*-
with open("_작업/verify_prompt.py", "r", encoding="utf-8") as f:
    code = f.read()

code = code.replace("low_for_mines.replace('fountain pen', 'instrument').replace('the pen', 'the instrument').replace('a pen', 'an instrument')",
                    "re.sub(r'\\bpen\\b', 'instrument', low_for_mines)")

with open("_작업/verify_prompt.py", "w", encoding="utf-8") as f:
    f.write(code)

