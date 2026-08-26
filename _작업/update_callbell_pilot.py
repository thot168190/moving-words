# -*- coding: utf-8 -*-
"""
대표님 하달 [단일 사물용 그림사전 정본 파일럿 — Call Bell] Set 10에 정확히 이식:
"""

import json

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

call_bell_pilot = """Progressive hand-drawn picture-dictionary animation on a completely flat, solid pure-white background (#FFFFFF), edge to edge.

The first frame is entirely empty white. No faint guide sketch, ghost image or completed object is visible.

The illustration is centered with generous untouched white space. Static locked-off camera, one continuous 8-second take.

The only visible subject is exactly one simple old-fashioned handbell standing upright at the optical center. It has one rounded wooden handle, one simple bell-shaped body, one bottom rim and one small clapper.

The object must remain a flat 2D drawing. It must never resemble a real photographed bell, an antique product photograph, a studio product shot, a realistic metal object, a 3D render or CGI.

0-4s: ultra-fine warm sepia-grey pencil lines are actively traced stroke by stroke across the completely empty white field.

Each stroke begins at one visible point and travels slowly toward its endpoint, leaving one thin permanent line behind. Only the lines already traced are visible. Every unfinished portion remains completely blank white.

Begin by tracing the left outer contour of the rounded handle.

Trace the right outer contour of the handle next.

Draw the narrow collar beneath the handle with two short curved strokes.

Trace the left curve of the bell body from top to bottom.

Trace the right curve separately.

Draw the wide bottom rim with two simple horizontal curves.

Draw the single small clapper last.

Never reveal the completed bell at once. Never use fade-in, dissolve, opacity reveal, morphing or materialization. Previously drawn lines remain still and unchanged.

Use sparse, slightly irregular handmade pencil contours. Lines remain clearly readable but delicate, never darker than 30% grey.

Do not add graphite shading inside the bell. Do not use hatching, cross-hatching, tonal modelling, gradients, highlights, reflected light, shine, gloss, shadows, surface texture, wood grain or metallic texture.

4-8s: transparent watercolor appears gradually in a few small flat patches inside the completed outlines.

Apply a very pale muted ochre-yellow wash to parts of the bell body.

Apply a very pale warm brown wash to parts of the handle.

Leave large portions of both forms completely unpainted, allowing the white paper to remain visible.

The watercolor must look flat, watery and handmade. It must not create volume, depth, shine, polished metal, realistic wood or photographic material.

During the final second, the small clapper moves once by only a few millimetres and returns to rest. The bell body and handle remain completely fixed.

Final style: simple Korean children’s picture-dictionary illustration, flat 2D pencil contour drawing, thin warm sepia-grey lines, sparse transparent watercolor, slightly imperfect handmade shapes, visible stroke-by-stroke drawing process, bright clean white paper and generous empty space.

No cinematic lighting. No studio lighting. No realistic materials. No dark shading. No black contours. No metallic reflection. No glossy highlight. No cast shadow. No product photography. No photorealism. No 3D. No CGI. No background surface. No text. No labels. No border. No hands. No artist. No pencils, pens or brushes visible. Completely silent."""

clean_bell = " ".join(call_bell_pilot.split())

for s in data:
    if s["set_id"] == "set10":
        s["prompts"][2]["prompt"] = clean_bell  # 03. 작은 황동 탁상종 핸드벨

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("_작업/bulk_sets/set10_10.txt", "w", encoding="utf-8") as f:
    for p in data[6]["prompts"]:
        f.write(p["prompt"] + "\n\n")

print("Call Bell 파일럿 Set 10 마스터 및 벌크 텍스트 이식 완료!")

