# -*- coding: utf-8 -*-
with open("_작업/verify_prompt.py", "r", encoding="utf-8") as f:
    code = f.read()

# 단일 사물용 그림사전 정본 필수문 등록
code = code.replace("('Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge', '헤더')",
                    "('Progressive hand-drawn picture-dictionary animation on a completely flat, solid pure-white background (#FFFFFF), edge to edge', '헤더')")

code = code.replace("('Style: master-level hand-drawn fine-line illustration', '스타일 — 꼬리')",
                    "('Final style: simple Korean children’s picture-dictionary illustration', '스타일 — 꼬리')")

code = code.replace("('4-8s: an extremely pale, water-heavy watercolor wash develops gently', '수채 — 시간')",
                    "('4-8s: transparent watercolor develops gradually in a few small flat patches', '수채 — 시간')")

with open("_작업/verify_prompt.py", "w", encoding="utf-8") as f:
    f.write(code)

