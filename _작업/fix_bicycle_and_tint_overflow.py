# -*- coding: utf-8 -*-
"""
1. 자전거 씬 영구 퇴출 -> [열기구 바구니와 버너 (Hot air balloon)] 씬으로 교체!
2. 색감 100% 실사 렌더링 원천 차단:
   - "Keep 70% of internal areas unpainted pure white. Apply only a whisper-thin water-wash tint on key accents, strictly zero opaque body paint, strictly non-photorealistic."
"""

import json

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Set 08에서 자전거(02번)를 열기구로 교체
for s in data:
    if s["set_id"] == "set08":
        # 02번 교체
        s["prompts"][1]["title"] = "화려한 열기구 바구니와 가스 버너"
        s["prompts"][1]["words"] = ["balloon", "basket", "burner", "float", "soar"]
        
        # 전체 4-8s 채색 문장을 '내부 면 비움 + 30% 미세 틴트 락'으로 전면 강화
        for p in s["prompts"]:
            t = p["prompt"]
            
            # 1. 자전거 프롬프트 내용 교체
            if "vintage roadster bicycle" in t:
                t = t.replace("one vintage roadster bicycle standing in clean side profile at center, with slender spoked wheels, leather saddle and front wicker basket",
                              "one graceful wicker hot air balloon basket suspended under a curved envelope rim at center, with a small brass burner ring")
                t = t.replace("Begin with the circular contours of the two spoked wheels. Draw the diamond chassis tubes and swept handlebars next. Extend the pedal crank and leather saddle. Add the small front woven basket.",
                              "Begin with the square woven wicker basket base. Draw the four corner suspension cables and burner ring next. Extend the lower scalloped envelope skirt above. Add the fuel cylinder.")
                t = t.replace("the palest British racing green on the bike chassis, warm honey-tan on the leather saddle, and sheer straw-buff on the basket",
                              "only the faintest warm straw-buff on the wicker basket, a sheer whisper of sky-blue on the envelope rim, and delicate pale brass on the burner")
                t = t.replace("The front wheel turns smoothly a tiny quarter turn and comes to a complete gentle rest.",
                              "A tiny whisper of transparent amber flame glows softly once inside the burner ring.")
            
            # 2. 색감 100% 덮임 방지: 면 비움 락 강화
            old_wash = "4-8s: an extremely pale, water-heavy watercolor wash develops gently, settling at a delicate 65% translucent tint where the pure white background remains luminous through every wash."
            new_wash = "4-8s: an extremely pale, water-heavy watercolor wash develops gently as a sparse, sheer accent tint. Most of each object's interior remains unfilled pure white, with translucent color touching only subtle accent areas at 30-40% opacity. Strictly zero opaque solid fill, zero dark tones, and zero 3D metallic rendering."
            
            if old_wash in t:
                t = t.replace(old_wash, new_wash)
            
            p["prompt"] = " ".join(t.split())

# Set 07 ~ 13 전체 세트에도 동일한 30-40% 면 비움 틴트 락 일괄 적용!
for s in data:
    for p in s["prompts"]:
        t = p["prompt"]
        old_wash = "4-8s: an extremely pale, water-heavy watercolor wash develops gently, settling at a delicate 65% translucent tint where the pure white background remains luminous through every wash."
        new_wash = "4-8s: an extremely pale, water-heavy watercolor wash develops gently as a sparse, sheer accent tint. Most of each object's interior remains unfilled pure white, with translucent color touching only subtle accent areas at 30-40% opacity. Strictly zero opaque solid fill, zero dark tones, and zero 3D metallic rendering."
        if old_wash in t:
            t = t.replace(old_wash, new_wash)
        p["prompt"] = " ".join(t.split())

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

for s in data:
    with open(s["filename"], "w", encoding="utf-8") as f:
        for p in s["prompts"]:
            f.write(p["prompt"] + "\n\n")

print("자전거 퇴출 -> 열기구 교체 및 허브 전체 30% 면비움 틴트 락 적용 완료!")

