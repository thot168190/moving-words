# -*- coding: utf-8 -*-
with open("_작업/verify_prompt.py", "r", encoding="utf-8") as f:
    code = f.read()

pencil_spec = """
PENCIL = [
    ("Progressive detailed fine-pencil construction, transparent watercolor and gentle object-motion animation on a solid pure bright white background (#FFFFFF), edge to edge.", "헤더"),
    ("The first frame is an entirely empty pure white field.", "첫 프레임"),
    ("Static locked-off camera, one continuous 8-second take.", "카메라"),
    ("0-3.5s: exceptionally fine pale-neutral 2H graphite strokes are visibly traced one by one", "2H연필선"),
    ("3.5-5.5s: clear transparent watercolor develops in layered color.", "수채"),
    ("5.5-8s:", "모션"),
    ("Style: intricate premium pencil-and-watercolor plate", "스타일 — 꼬리"),
    ("Completely silent.", "무음"),
]
"""

code = code.replace("CALM = [", pencil_spec + "\nCALM = [")

# 판별 로직 보강
old_judge = """    # 계열 판별
    if "picture-dictionary" in low:
        spec, kind = (DICT, "DICT(그림사전·단일사물)")
        calm = True"""

new_judge = """    # 계열 판별
    if "fine-pencil construction" in low:
        spec, kind = (PENCIL, "PENCIL(세필수채·주방사물)")
        calm = True
    elif "picture-dictionary" in low:
        spec, kind = (DICT, "DICT(그림사전·단일사물)")
        calm = True"""

code = code.replace(old_judge, new_judge)

# PENCIL 모드에서 배제 블록 마스킹
code = code.replace("low_for_mines = re.sub(r'no (text|cinematic lighting).*?completely silent\.', '', low, flags=re.DOTALL)",
                    "low_for_mines = re.sub(r'no (text|cinematic lighting|dark outline).*?completely silent\.', '', low, flags=re.DOTALL)")

code = code.replace("if kind.startswith('DICT') and w in ['sepia', 'paper', 'border', 'shading']:",
                    "if (kind.startswith('DICT') or kind.startswith('PENCIL')) and w in ['sepia', 'paper', 'border', 'shading', 'cream', 'cartoon']:")

with open("_작업/verify_prompt.py", "w", encoding="utf-8") as f:
    f.write(code)

