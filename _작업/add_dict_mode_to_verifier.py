# -*- coding: utf-8 -*-
with open("_작업/verify_prompt.py", "r", encoding="utf-8") as f:
    vcode = f.read()

# DICT(그림사전) 판정 모드 추가
dict_mode_code = """
    # 3. DICT(단일 사물 그림사전 — 2026-08-25 대표님 정본)
    if "picture-dictionary" in p:
        branch = "DICT(그림사전·단일사물)"
        required = [
            ("Progressive hand-drawn picture-dictionary animation on a completely flat, solid pure-white background (#FFFFFF), edge to edge", "헤더"),
            ("The first frame is entirely empty white", "첫 프레임"),
            ("The illustration is centered with generous untouched white space", "구도"),
            ("Static locked-off camera, one continuous 8-second take", "카메라"),
            ("The only visible subject", "요소 한정"),
            ("0-4s: ultra-fine warm sepia-grey pencil lines are actively traced stroke by stroke", "연필선 — 시간"),
            ("Each stroke begins at one visible point, travels slowly to its endpoint", "연필선 — 물리적 궤적"),
            ("Never reveal the finished", "페이드인 방지"),
            ("4-8s: transparent watercolor develops gradually in a few small flat patches", "수채 — 시간"),
            ("Final style: simple Korean children’s picture-dictionary illustration", "스타일 — 꼬리"),
            ("No cinematic lighting. No studio lighting", "배제 — 조명"),
            ("No photorealism. No 3D. No CGI", "배제 — 3D"),
            ("Completely silent", "무음"),
        ]
"""

vcode = vcode.replace("    if \"line-reveal\" in p or \"CALM\" in p:\n        branch = \"CALM(망원경·line-reveal)\"",
                      "    if \"picture-dictionary\" in p:\n        branch = \"DICT(그림사전·단일사물)\"\n        required = [\n            (\"Progressive hand-drawn picture-dictionary animation on a completely flat, solid pure-white background (#FFFFFF), edge to edge\", \"헤더\"),\n            (\"The first frame is entirely empty white\", \"첫 프레임\"),\n            (\"The illustration is centered with generous untouched white space\", \"구도\"),\n            (\"Static locked-off camera, one continuous 8-second take\", \"카메라\"),\n            (\"The only visible subject\", \"요소 한정\"),\n            (\"0-4s: ultra-fine warm sepia-grey pencil lines are actively traced stroke by stroke\", \"연필선 — 시간\"),\n            (\"Each stroke begins at one visible point, travels slowly to its endpoint\", \"연필선 — 물리적 궤적\"),\n            (\"4-8s: transparent watercolor develops gradually in a few small flat patches\", \"수채 — 시간\"),\n            (\"Final style: simple Korean children’s picture-dictionary illustration\", \"스타일 — 꼬리\"),\n            (\"No cinematic lighting. No studio lighting\", \"배제 — 조명\"),\n            (\"No photorealism. No 3D. No CGI\", \"배제 — 3D\"),\n            (\"Completely silent\", \"무음\"),\n        ]\n    elif \"line-reveal\" in p or \"CALM\" in p:\n        branch = \"CALM(망원경·line-reveal)\"")

with open("_작업/verify_prompt.py", "w", encoding="utf-8") as f:
    f.write(vcode)

