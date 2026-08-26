# -*- coding: utf-8 -*-
with open("_작업/verify_prompt.py", "r", encoding="utf-8") as f:
    code = f.read()

# 정상화
import re
# check 함수 내부 정리
code = re.sub(r'def check\(name, p\):.*?# 계열 판별', '''def check(name, p):
    errs, warns, oks = [], [], []
    low = p.lower()

    # 대표님 배제 블록 마스킹 (지뢰 오탐 방지)
    low_for_mines = re.sub(r'no (text|cinematic lighting).*?completely silent\\.', '', low, flags=re.DOTALL)
    low_for_mines = low_for_mines.replace('hand-drawn', 'fine-drawn')
    if "picture-dictionary" in low:
        low_for_mines = low_for_mines.replace('fountain pen', 'instrument').replace('the pen', 'the instrument').replace('a pen', 'an instrument')
        low_for_mines = low_for_mines.replace('pressing arm', 'pressing lever').replace('duplicate arm', 'duplicate lever')

    # 계열 판별''', code, flags=re.DOTALL)

with open("_작업/verify_prompt.py", "w", encoding="utf-8") as f:
    f.write(code)

