# -*- coding: utf-8 -*-
with open("_작업/제작허브.html", "r", encoding="utf-8") as f:
    hub_content = f.read()

import re, json

# 허브 내부의 set07 첫 번째 씬 텍스트 검증
m = re.search(r'"id":\s*"set07-01".*?"prompt":\s*"([^"]+)"', hub_content)
if m:
    p_text = m.group(1)
    print("=== 허브 실제 파일 속 Set 07-01 프롬프트 ===")
    print(p_text[:250] + "...")
    print("\n[검사 결과]")
    print("1. 'appears progressively':", "appears progressively" in p_text)
    print("2. 'drawn by' (손 유발어) 포함 여부:", "drawn by" in p_text)
    print("3. 'advancing tip' (손 유발어) 포함 여부:", "advancing tip" in p_text)
    print("4. 'warm-grey':", "warm-grey" in p_text)
else:
    print("set07-01 not found!")

