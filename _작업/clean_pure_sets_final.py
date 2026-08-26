# -*- coding: utf-8 -*-
with open("_작업/build_pure_new_sets_08_13.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. 4-8s 필수문 완벽 복원
old_wash = "4-8s: an extremely pale, water-heavy watercolor wash develops gently as a sparse, sheer accent tint. Most of each object's interior remains unfilled pure white, with translucent color touching only subtle accent areas at 30-40% opacity. Strictly zero opaque solid fill, zero dark tones, and zero metallic reflection."
new_wash = "4-8s: an extremely pale, water-heavy watercolor wash develops gently as a sparse, sheer accent tint. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled; most of each object interior remains unfilled pure white with translucent color touching only subtle accent areas."

code = code.replace(old_wash, new_wash)

# 2. 지뢰어 정제
code = code.replace("wrist cuffs", "base cuffs")
code = code.replace("fluffy downy", "soft downy")
code = code.replace("fluffy", "soft")
code = code.replace("fountain pen", "fountain quill")
code = code.replace("pen barrel", "quill barrel")
code = code.replace("diamond frame", "diamond structure")
code = code.replace("frame structure", "mount structure")
code = code.replace("desktop", "tabletop")
code = code.replace("desk", "tabletop")
code = code.replace("inner crest border", "inner crest perimeter")
code = code.replace("border", "boundary")
code = code.replace("plaque frame", "plaque mount")
code = code.replace("frame pillars", "support pillars")
code = code.replace("scale frame", "scale mount")

with open("_작업/build_pure_new_sets_08_13.py", "w", encoding="utf-8") as f:
    f.write(code)

