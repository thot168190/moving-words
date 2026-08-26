# -*- coding: utf-8 -*-
with open("_작업/verify_prompt.py", "r", encoding="utf-8") as f:
    code = f.read()

dict_spec = """
DICT = [
    ("Progressive hand-drawn picture-dictionary animation on a completely flat, solid pure-white background (#FFFFFF), edge to edge.", "헤더"),
    ("The first frame is entirely empty white", "첫 프레임"),
    ("The illustration is centered with generous untouched white space", "구도"),
    ("Static locked-off camera, one continuous 8-second take.", "카메라"),
    ("0-4s: ultra-fine warm sepia-grey pencil lines are actively traced stroke by stroke", "연필선"),
    ("4-8s: transparent watercolor develops gradually in a few small flat patches", "수채"),
    ("Final style: simple Korean children’s picture-dictionary illustration", "스타일 — 꼬리"),
    ("No cinematic lighting. No studio lighting.", "배제"),
    ("Completely silent.", "무음"),
]
"""

code = code.replace("CALM = [", dict_spec + "\nCALM = [")

# 판별 로직
old_judge = """    # 계열 판별
    calm = "line-reveal" in low
    spec, kind = (CALM, "CALM(망원경·line-reveal)") if calm else (WOW, "WOW(산호협곡)")"""

new_judge = """    # 계열 판별
    if "picture-dictionary" in low:
        spec, kind = (DICT, "DICT(그림사전·단일사물)")
        calm = True
    elif "line-reveal" in low:
        spec, kind = (CALM, "CALM(망원경·line-reveal)")
        calm = True
    else:
        spec, kind = (WOW, "WOW(산호협곡)")
        calm = False"""

code = code.replace(old_judge, new_judge)

# BANNED / MINES 에서 DICT 정본 단어 (sepia, paper, border 등) 예외 처리
code = code.replace("for w, why in BANNED.items():",
                    "for w, why in BANNED.items():\n        if kind.startswith('DICT') and w in ['sepia', 'paper', 'border', 'shading']:\n            continue")

with open("_작업/verify_prompt.py", "w", encoding="utf-8") as f:
    f.write(code)

