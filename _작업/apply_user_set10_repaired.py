# -*- coding: utf-8 -*-
"""
대표님이 직접 주신 [움직이는 그림사전 — 단일 사물 10개 수리본] 100% 원문 그대로 Set 10에 이식!
"""

import json

prompts_text = [
    # 1. Fountain pen
    """Progressive hand-drawn picture-dictionary animation on a completely flat, solid pure-white background (#FFFFFF), edge to edge. The first frame is entirely empty white: no faint guide sketch, ghost image or completed object. The illustration is centered with generous untouched white space. Static locked-off camera, one continuous 8-second take.

The only visible subjects are exactly one simple fountain pen lying horizontally at the optical center and exactly two tiny ink droplets beside its nib. The pen has one long barrel, one cap with a simple clip, one tapered grip and one split nib. It remains one flat 2D drawing with a single unchanging shape. No duplicate pen, detached part, motion trail or additional writing instrument.

0-4s: ultra-fine warm sepia-grey pencil lines are actively traced stroke by stroke across the completely empty white field. Each stroke begins at one visible point, travels slowly to its endpoint and leaves one thin permanent line behind. Trace the upper barrel contour first, then the lower barrel contour, the cap and clip, the tapered grip, the two outer nib curves, the central nib slit, and exactly two tiny ink droplets last. Only completed strokes are visible; every unfinished portion remains blank white. Never reveal the finished pen at once. Never use fade-in, dissolve, opacity reveal, morphing or materialization.

Use sparse, slightly irregular handmade pencil contours, clearly readable but never darker than 30% grey. No graphite filling, hatching, cross-hatching, tonal modelling, gradients, reflected light, highlights, shine, gloss, shadows or material texture.

4-8s: transparent watercolor develops gradually in a few small flat patches inside the completed outlines. Apply a pale muted blue-grey wash to small portions of the barrel, a pale ochre-yellow wash to small portions of the nib and trim, and two tiny muted blue spots to the ink droplets. Leave most of the pen unpainted. The wash remains flat, watery and handmade and never creates volume or polished material.

During the final second, one ink droplet trembles once by only a few millimetres and stops. The pen remains completely fixed. Final style: simple Korean children’s picture-dictionary illustration, flat 2D pencil contour drawing, thin warm sepia-grey lines, sparse transparent watercolor, slightly imperfect handmade shapes, visible stroke-by-stroke drawing process, bright white paper and generous empty space.

No cinematic lighting. No studio lighting. No realistic material. No dark shading. No black contour. No metallic reflection. No glossy highlight. No cast shadow. No product photography. No photorealism. No 3D. No CGI. No background surface. No text, label, border, hand, artist, pencil, brush or separate drawing tool visible. Completely silent.""",

    # 2. Magnifying glass
    """Progressive hand-drawn picture-dictionary animation on a completely flat, solid pure-white background (#FFFFFF), edge to edge. The first frame is entirely empty white: no faint guide sketch, ghost image or completed object. The illustration is centered with generous untouched white space. Static locked-off camera, one continuous 8-second take.

The only visible subject is exactly one simple round magnifying glass resting flat at the optical center. It has exactly one circular outer rim, one empty circular lens and one short rounded wooden handle permanently attached at the lower-right rim and pointing toward five o’clock. No second handle, duplicated rim, detached part, object inside the lens or motion trail.

0-4s: ultra-fine warm sepia-grey pencil lines are actively traced stroke by stroke across the completely empty white field. Each stroke begins at one visible point, travels slowly to its endpoint and leaves one thin permanent line behind. Trace one outer circle first, one smaller concentric lens circle next, the left edge of the single handle, the right edge of the same handle, and two short connection lines last. Only completed strokes are visible; every unfinished portion remains blank white. Never reveal the finished object at once. Never use fade-in, dissolve, opacity reveal, morphing or materialization.

Use sparse, slightly irregular handmade pencil contours, clearly readable but never darker than 30% grey. The lens stays visually empty. No reflection arcs, magnified image, refraction, bubbles, liquid, scenery, face, eye, animal or symbol inside it. No graphite filling, hatching, gradients, highlights, shine, gloss, shadows or material texture.

4-8s: transparent watercolor develops gradually in a few small flat patches inside the completed outlines. Apply a pale muted beige wash to small portions of the rim, a pale warm brown wash to small portions of the handle and one extremely pale flat blue patch inside the otherwise empty lens. Leave most of the object unpainted. The wash remains flat, watery and handmade and never creates glass depth, polished metal or realistic wood.

During the final second, the edge of the pale blue wash spreads slightly inside the lens and stops. The rim and single handle remain completely fixed. Final style: simple Korean children’s picture-dictionary illustration, flat 2D pencil contour drawing, thin warm sepia-grey lines, sparse transparent watercolor, slightly imperfect handmade shapes, visible stroke-by-stroke drawing process, bright white paper and generous empty space.

No cinematic lighting. No studio lighting. No realistic glass. No realistic material. No dark shading. No black contour. No reflection. No glossy highlight. No cast shadow. No product photography. No photorealism. No 3D. No CGI. No text, label, border, hand, artist, pencil, brush or drawing tool visible. Completely silent.""",

    # 3. Handbell
    """Progressive hand-drawn picture-dictionary animation on a completely flat, solid pure-white background (#FFFFFF), edge to edge. The first frame is entirely empty white: no faint guide sketch, ghost image or completed object. The illustration is centered with generous untouched white space. Static locked-off camera, one continuous 8-second take.

The only visible subject is exactly one simple old-fashioned handbell standing upright at the optical center. It has one rounded wooden handle, one narrow collar, one bell-shaped body, one bottom rim and one small clapper. It remains one flat 2D drawing with a single unchanging silhouette.

0-4s: ultra-fine warm sepia-grey pencil lines are actively traced stroke by stroke across the completely empty white field. Each stroke begins at one visible point, travels slowly to its endpoint and leaves one thin permanent line behind. Trace the left handle contour first, the right handle contour next, two collar curves, the left bell-body curve, the right bell-body curve, two simple bottom-rim curves and the single clapper last. Only completed strokes are visible; every unfinished portion remains blank white. Never reveal the finished bell at once. Never use fade-in, dissolve, opacity reveal, morphing or materialization.

Use sparse, slightly irregular handmade pencil contours, clearly readable but never darker than 30% grey. No graphite filling, hatching, cross-hatching, tonal modelling, gradients, highlights, reflected light, shine, gloss, shadows, wood grain or metallic texture.

4-8s: transparent watercolor develops gradually in a few small flat patches inside the completed outlines. Apply a very pale muted ochre-yellow wash to parts of the bell body and a very pale warm brown wash to parts of the handle. Leave large portions completely unpainted. The wash remains flat, watery and handmade and never creates volume, polished metal or realistic wood.

During the final second, the small clapper moves once by only a few millimetres and returns to rest. The bell body and handle remain completely fixed. Final style: simple Korean children’s picture-dictionary illustration, flat 2D pencil contour drawing, thin warm sepia-grey lines, sparse transparent watercolor, slightly imperfect handmade shapes, visible stroke-by-stroke drawing process, bright white paper and generous empty space.

No cinematic lighting. No studio lighting. No realistic material. No dark shading. No black contour. No metallic reflection. No glossy highlight. No cast shadow. No product photography. No photorealism. No 3D. No CGI. No background surface. No text, label, border, hand, artist, pencil, brush or drawing tool visible. Completely silent.""",

    # 4. Inkwell and dropper
    """Progressive hand-drawn picture-dictionary animation on a completely flat, solid pure-white background (#FFFFFF), edge to edge. The first frame is entirely empty white: no faint guide sketch, ghost image or completed object. The illustration is centered with generous untouched white space. Static locked-off camera, one continuous 8-second take.

The only visible subjects are exactly one simple square inkwell at the optical center and exactly one slender dropper lying beside it. The inkwell has one square base, one short neck, one small hinged lid and one horizontal ink-level line. The dropper has one narrow tube and one small rounded bulb. Both remain flat 2D drawings with fixed shapes. No duplicate bottle, extra dropper or detached lid.

0-4s: ultra-fine warm sepia-grey pencil lines are actively traced stroke by stroke across the completely empty white field. Each stroke begins at one visible point, travels slowly to its endpoint and leaves one thin permanent line behind. Build the square base one edge at a time, then trace the short neck, the lid, the single ink-level line, the dropper tube and its rounded bulb last. Use only two short interior facet lines. Only completed strokes are visible; every unfinished portion remains blank white. Never reveal the finished objects at once. Never use fade-in, dissolve, opacity reveal, morphing or materialization.

Use sparse, slightly irregular handmade pencil contours, clearly readable but never darker than 30% grey. No realistic glass edges, refraction, reflections, highlights, shine, gloss, shadows, dense facets, graphite filling or material texture.

4-8s: transparent watercolor develops gradually in a few small flat patches inside the completed outlines. Apply a pale muted indigo-blue wash to the lower portion of the inkwell, an extremely pale blue-grey patch to one side of the bottle and a pale muted beige patch to the lid. Leave most surfaces unpainted. The wash remains flat, watery and handmade and never creates transparent glass volume or polished metal.

During the final second, the simple blue ink-level line makes one tiny horizontal settling movement and stops. The bottle, lid and dropper remain fixed. Final style: simple Korean children’s picture-dictionary illustration, flat 2D pencil contour drawing, thin warm sepia-grey lines, sparse transparent watercolor, slightly imperfect handmade shapes, visible stroke-by-stroke drawing process, bright white paper and generous empty space.

No cinematic lighting. No studio lighting. No realistic glass. No realistic liquid physics. No dark shading. No black contour. No reflection. No glossy highlight. No cast shadow. No product photography. No photorealism. No 3D. No CGI. No text, label, border, hand, artist, pencil, pen, brush or drawing tool visible. Completely silent.""",

    # 5. Folding book lectern
    """Progressive hand-drawn picture-dictionary animation on a completely flat, solid pure-white background (#FFFFFF), edge to edge. The first frame is entirely empty white: no faint guide sketch, ghost image or completed object. The illustration is centered with generous untouched white space. Static locked-off camera, one continuous 8-second take.

The only visible subject is exactly one simple folding book lectern standing open at the optical center. It has one flat base, one angled backrest, one lower shelf ledge, one rear support and exactly two small page clips. It remains one flat 2D drawing with fixed geometry. No book, duplicate stand, detached board or extra clip.

0-4s: ultra-fine warm sepia-grey pencil lines are actively traced stroke by stroke across the completely empty white field. Each stroke begins at one visible point, travels slowly to its endpoint and leaves one thin permanent line behind. Trace the base edges first, then the two backrest edges, the lower shelf ledge, the rear support and the two page clips one by one. Add only three short, widely spaced wood-detail lines last. Only completed strokes are visible; every unfinished portion remains blank white. Never reveal the finished lectern at once. Never use fade-in, dissolve, opacity reveal, morphing or materialization.

Use sparse, slightly irregular handmade pencil contours, clearly readable but never darker than 30% grey. No dense wood grain, graphite filling, hatching, tonal modelling, gradients, highlights, shine, gloss, shadows or material texture.

4-8s: transparent watercolor develops gradually in a few small flat patches inside the completed outlines. Apply a pale muted birch-beige wash to selected portions of the base and backrest and a very pale ochre-yellow wash to the two clips. Leave most of the lectern unpainted. The wash remains flat, watery and handmade and never creates wooden volume, metal shine or realistic depth.

During the final second, the two small clips tilt inward by only a few millimetres and stop. Every wooden part remains fixed. Final style: simple Korean children’s picture-dictionary illustration, flat 2D pencil contour drawing, thin warm sepia-grey lines, sparse transparent watercolor, slightly imperfect handmade shapes, visible stroke-by-stroke drawing process, bright white paper and generous empty space.

No cinematic lighting. No studio lighting. No realistic material. No dark shading. No black contour. No metallic reflection. No glossy highlight. No cast shadow. No product photography. No photorealism. No 3D. No CGI. No text, label, border, hand, artist, pencil, pen, brush or drawing tool visible. Completely silent.""",

    # 6. Tabletop stapler
    """Progressive hand-drawn picture-dictionary animation on a completely flat, solid pure-white background (#FFFFFF), edge to edge. The first frame is entirely empty white: no faint guide sketch, ghost image or completed object. The illustration is centered with generous untouched white space. Static locked-off camera, one continuous 8-second take.

The only visible subject is exactly one simple tabletop stapler shown in clean side view at the optical center. It has one flat base, one lower magazine, one top pressing arm, one small hinge and two small base pads. It remains one flat 2D drawing with fixed geometry. No staple, paper, duplicate arm or detached mechanical part.

0-4s: ultra-fine warm sepia-grey pencil lines are actively traced stroke by stroke across the completely empty white field. Each stroke begins at one visible point, travels slowly to its endpoint and leaves one thin permanent line behind. Trace the upper base edge first, the lower base edge next, the lower magazine, the top pressing arm, the hinge circle and two small pads last. Add only two short alignment marks. Only completed strokes are visible; every unfinished portion remains blank white. Never reveal the finished stapler at once. Never use fade-in, dissolve, opacity reveal, morphing or materialization.

Use sparse, slightly irregular handmade pencil contours, clearly readable but never darker than 30% grey. No mechanical rendering, inner spring detail, graphite filling, hatching, gradients, reflected light, highlights, shine, gloss, shadows or metal texture.

4-8s: transparent watercolor develops gradually in a few small flat patches inside the completed outlines. Apply a pale muted slate-blue wash to small portions of the base and pressing arm, a very pale cool grey wash to the magazine and two tiny warm-grey patches to the pads. Leave most of the stapler unpainted. The wash remains flat, watery and handmade and never creates metal volume or realistic machinery.

During the final second, the top pressing arm lowers by only a few millimetres and returns to its original position. The base and magazine remain fixed. Final style: simple Korean children’s picture-dictionary illustration, flat 2D pencil contour drawing, thin warm sepia-grey lines, sparse transparent watercolor, slightly imperfect handmade shapes, visible stroke-by-stroke drawing process, bright white paper and generous empty space.

No cinematic lighting. No studio lighting. No realistic material. No dark shading. No black contour. No metallic reflection. No glossy highlight. No cast shadow. No product photography. No photorealism. No 3D. No CGI. No text, label, border, hand, artist, pencil, pen, brush or drawing tool visible. Completely silent.""",

    # 7. Wedge pencil sharpener
    """Progressive hand-drawn picture-dictionary animation on a completely flat, solid pure-white background (#FFFFFF), edge to edge. The first frame is entirely empty white: no faint guide sketch, ghost image or completed object. The illustration is centered with generous untouched white space. Static locked-off camera, one continuous 8-second take.

The only visible subject is exactly one small wedge-shaped pencil sharpener at the optical center. It has one simple block body, one circular pencil-entry hole, one flat cutting blade and one round screw. It remains one flat 2D drawing with fixed geometry. No pencil, shaving, duplicate blade or detached screw.

0-4s: ultra-fine warm sepia-grey pencil lines are actively traced stroke by stroke across the completely empty white field. Each stroke begins at one visible point, travels slowly to its endpoint and leaves one thin permanent line behind. Construct the wedge body one edge at a time, then trace the circular entry hole, the single blade outline, the blade edge and the central screw last. Add only three short side-grip marks. Only completed strokes are visible; every unfinished portion remains blank white. Never reveal the finished sharpener at once. Never use fade-in, dissolve, opacity reveal, morphing or materialization.

Use sparse, slightly irregular handmade pencil contours, clearly readable but never darker than 30% grey. No metallic reflection lines, graphite filling, hatching, gradients, reflected light, highlights, shine, gloss, shadows or material texture.

4-8s: transparent watercolor develops gradually in a few small flat patches inside the completed outlines. Apply a pale muted ochre-yellow wash to small portions of the body and an extremely pale cool grey-blue wash to the blade. Leave most of the sharpener unpainted. The wash remains flat, watery and handmade and never creates brass, steel, polished metal or realistic depth.

During the final second, the small round screw makes one tiny quarter-turn and stops while the body and blade remain completely fixed. Final style: simple Korean children’s picture-dictionary illustration, flat 2D pencil contour drawing, thin warm sepia-grey lines, sparse transparent watercolor, slightly imperfect handmade shapes, visible stroke-by-stroke drawing process, bright white paper and generous empty space.

No cinematic lighting. No studio lighting. No realistic material. No dark shading. No black contour. No metallic reflection. No glossy highlight. No cast shadow. No product photography. No photorealism. No 3D. No CGI. No text, label, border, hand, artist, visible pencil, pen, brush or drawing tool. Completely silent.""",

    # 8. Hardcover book
    """Progressive hand-drawn picture-dictionary animation on a completely flat, solid pure-white background (#FFFFFF), edge to edge. The first frame is entirely empty white: no faint guide sketch, ghost image or completed object. The illustration is centered with generous untouched white space. Static locked-off camera, one continuous 8-second take.

The only visible subject is exactly one closed thick hardcover book lying flat at the optical center with exactly one ribbon bookmark trailing from its upper spine. The book has one front cover, one spine and one simple block of page edges. It remains one flat 2D drawing with fixed geometry. No title, letters, decoration, duplicate book or extra ribbon.

0-4s: ultra-fine warm sepia-grey pencil lines are actively traced stroke by stroke across the completely empty white field. Each stroke begins at one visible point, travels slowly to its endpoint and leaves one thin permanent line behind. Trace the front-cover rectangle one edge at a time, then the curved spine, three simple page-edge lines and the single ribbon in one gentle S-curve. Add only three short cloth-detail marks last. Only completed strokes are visible; every unfinished portion remains blank white. Never reveal the finished book at once. Never use fade-in, dissolve, opacity reveal, morphing or materialization.

Use sparse, slightly irregular handmade pencil contours, clearly readable but never darker than 30% grey. No dense cloth weave, individual page rendering, embossing, graphite filling, hatching, gradients, highlights, shine, gloss, shadows or material texture.

4-8s: transparent watercolor develops gradually in a few small flat patches inside the completed outlines. Apply a pale muted sage-green wash to selected parts of the cover, a pale warm ivory wash to a small area of the page block and a small muted brick-red wash to the ribbon. Leave most of the book unpainted. The wash remains flat, watery and handmade and never creates leather, silk, cloth volume or realistic depth.

During the final second, the single ribbon tip lifts once by only a few millimetres and settles back. The book remains fixed. Final style: simple Korean children’s picture-dictionary illustration, flat 2D pencil contour drawing, thin warm sepia-grey lines, sparse transparent watercolor, slightly imperfect handmade shapes, visible stroke-by-stroke drawing process, bright white paper and generous empty space.

No cinematic lighting. No studio lighting. No realistic material. No dark shading. No black contour. No glossy highlight. No cast shadow. No product photography. No photorealism. No 3D. No CGI. No text, letters, label, border, hand, artist, pencil, pen, brush or drawing tool visible. Completely silent.""",

    # 9. Paperclip and pushpins
    """Progressive hand-drawn picture-dictionary animation on a completely flat, solid pure-white background (#FFFFFF), edge to edge. The first frame is entirely empty white: no faint guide sketch, ghost image or completed object. The illustration is centered with generous untouched white space. Static locked-off camera, one continuous 8-second take.

The only visible subjects are exactly one large looped paperclip resting flat at the optical center and exactly three small round-headed pushpins arranged separately beside it. The paperclip is one continuous double-loop shape. Each pushpin has one round head and one short straight point. All subjects remain flat 2D drawings with fixed geometry. No duplicate clip, extra pin, bent point, melted shape or detached fragment.

0-4s: ultra-fine warm sepia-grey pencil lines are actively traced stroke by stroke across the completely empty white field. Each stroke begins at one visible point, travels slowly to its endpoint and leaves one thin permanent line behind. Trace the paperclip’s outer loop first, then its inner return loop. Construct the first pushpin head and point, then the second, then the third. Add no reflection lines. Only completed strokes are visible; every unfinished portion remains blank white. Never reveal the finished objects at once. Never use fade-in, dissolve, opacity reveal, morphing or materialization.

Use sparse, slightly irregular handmade pencil contours, clearly readable but never darker than 30% grey. Keep the paperclip as two simple parallel contour lines without wire texture. No graphite filling, hatching, gradients, reflected light, highlights, shine, gloss, shadows or metallic material texture.

4-8s: transparent watercolor develops gradually in a few small flat patches inside the completed outlines. Apply an extremely pale cool blue-grey wash to small portions of the paperclip and three small pale ochre-yellow washes to the three pushpin heads. Leave most surfaces unpainted. The wash remains flat, watery and handmade and never creates polished steel, brass, sharp photographic needles or realistic depth.

During the final second, the nearest pushpin rotates a few degrees in place and stops. The paperclip and the other two pushpins remain fixed. Final style: simple Korean children’s picture-dictionary illustration, flat 2D pencil contour drawing, thin warm sepia-grey lines, sparse transparent watercolor, slightly imperfect handmade shapes, visible stroke-by-stroke drawing process, bright white paper and generous empty space.

No cinematic lighting. No studio lighting. No realistic material. No dark shading. No black contour. No metallic reflection. No glossy highlight. No cast shadow. No product photography. No photorealism. No 3D. No CGI. No text, label, border, hand, artist, pencil, pen, brush or drawing tool visible. Completely silent.""",

    # 10. Seal stamp
    """Progressive hand-drawn picture-dictionary animation on a completely flat, solid pure-white background (#FFFFFF), edge to edge. The first frame is entirely empty white: no faint guide sketch, ghost image or completed object. The illustration is centered with generous untouched white space. Static locked-off camera, one continuous 8-second take.

The only visible subject is exactly one simple seal stamp standing upright at the optical center. It has one rounded top knob, one gently curved handle, one short neck and one wide circular stamping base. It remains one flat 2D drawing with a single fixed silhouette. No wax, paper, crest, letters, duplicate stamp, second base or detached part.

0-4s: ultra-fine warm sepia-grey pencil lines are actively traced stroke by stroke across the completely empty white field. Each stroke begins at one visible point, travels slowly to its endpoint and leaves one thin permanent line behind. Trace the left handle contour first, the right handle contour next, the rounded top knob, the short neck, the left side of the stamping base, the right side and two simple lower-rim curves last. Add only three short decorative groove lines. Only completed strokes are visible; every unfinished portion remains blank white. Never reveal the finished stamp at once. Never use fade-in, dissolve, opacity reveal, morphing or materialization.

Use sparse, slightly irregular handmade pencil contours, clearly readable but never darker than 30% grey. No engraved crest, lettering, graphite filling, hatching, tonal modelling, gradients, reflected light, highlights, shine, gloss, shadows or metallic texture.

4-8s: transparent watercolor develops gradually in a few small flat patches inside the completed outlines. Apply a pale muted ochre-yellow wash to small portions of the stamp and leave most of its surface completely unpainted. The wash remains flat, watery and handmade and never creates brass, polished metal, weight, volume or realistic depth.

During the final second, the stamp tilts by only one or two degrees and returns upright. Its shape remains unchanged. Final style: simple Korean children’s picture-dictionary illustration, flat 2D pencil contour drawing, thin warm sepia-grey lines, sparse transparent watercolor, slightly imperfect handmade shapes, visible stroke-by-stroke drawing process, bright white paper and generous empty space.

No cinematic lighting. No studio lighting. No realistic material. No dark shading. No black contour. No metallic reflection. No glossy highlight. No cast shadow. No product photography. No photorealism. No 3D. No CGI. No text, letters, label, border, hand, artist, pencil, pen, brush or drawing tool visible. Completely silent."""
]

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for s in data:
    if s["set_id"] == "set10":
        for idx, pt in enumerate(prompts_text):
            s["prompts"][idx]["prompt"] = " ".join(pt.split())

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("_작업/bulk_sets/set10_10.txt", "w", encoding="utf-8") as f:
    for p in data[6]["prompts"]:
        f.write(p["prompt"] + "\n\n")

print("대표님 하달 [단일 사물 10개 수리본] Set 10에 100% 원문 그대로 반영 완료!")

