# -*- coding: utf-8 -*-
"""
시계/시간 계열 사물 3건을 100% 신선한 신규 사물로 교체:
1. Set 11-09: 타이머 -> [도자기 레몬 스퀴저 착즙기 (lemon, citrus, squeeze, juice)]
2. Set 12-02: 메트로놈 -> [은빛 트라이앵글 타악기와 채 (triangle, strike, chime, clear)]
3. Set 13-09: 시계탑 탈진기 -> [황동 잉크 블로터 압인기 (blotter, absorb, press, dry)]
"""

import json

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for s in data:
    if s["set_id"] == "set11":
        # 09번 타이머 교체
        p = s["prompts"][8]
        p["title"] = "도자기 레몬 스퀴저 착즙기"
        p["words"] = ["lemon", "citrus", "squeeze", "juice"]
        p["prompt"] = p["prompt"].replace("one round dome-shaped mechanical kitchen timer standing at center with marked minute dial and pointer",
                                           "one ribbed white porcelain lemon citrus squeezer saucer sitting at center with sharp fluted cone")
        p["prompt"] = p["prompt"].replace("Begin with the wide circular base and tapering dome body. Draw the 60-minute tick markings around the waist next. Extend the top rotating knob and index pointer. Add the bell housing line.",
                                           "Begin with the circular shallow collecting dish and side pouring spout. Draw the pointed radial conical squeezing cone next. Extend the small handle loop. Add the seed catching slots.")
        p["prompt"] = p["prompt"].replace("only the palest vintage cream on the timer body and sheer polished steel on the pointer collar",
                                           "only the palest clean porcelain-white with a delicate whisper of sunny pastel-lemon on the inner saucer")
        p["prompt"] = p["prompt"].replace("The top dial ticks smoothly one second mark with a crisp, silent, micro-mechanical precision.",
                                           "A single tiny crystal drop of fresh citrus juice drips softly from the spout into the dish.")

    elif s["set_id"] == "set12":
        # 02번 메트로놈 교체
        p = s["prompts"][1]
        p["title"] = "은빛 트라이앵글 타악기와 비터 채"
        p["words"] = ["triangle", "strike", "chime", "clear"]
        p["prompt"] = p["prompt"].replace("one classic triangular wooden metronome standing at center with upright oscillating brass pendulum rod and sliding tempo weight",
                                           "one suspended equilateral steel musical triangle hanging by a fine cord at center with polished striker beater")
        p["prompt"] = p["prompt"].replace("Begin with the pyramid-shaped wooden case and front opening. Draw the graduated tempo beat scale and central metal pendulum rod next. Extend the sliding brass tempo weight. Add the winding key.",
                                           "Begin with the open triangular steel bar and open corner gap. Draw the slender cylindrical striking beater beside it next. Extend the thin hanging suspension loop above. Add the clean reflections.")
        p["prompt"] = p["prompt"].replace("only the palest warm mahogany on the pyramid case and luminous brass on the pendulum rod",
                                           "only the palest surgical silver-chrome wash on the triangle bar with bright white highlights")
        p["prompt"] = p["prompt"].replace("The slender brass pendulum rod swings smoothly once to the right and returns to center.",
                                           "The suspended steel triangle gives a microscopic, silent high-frequency shimmer of pure acoustic resonance.")

    elif s["set_id"] == "set13":
        # 09번 시계탑 탈진기 교체
        p = s["prompts"][8]
        p["title"] = "황동 잉크 블로터 압인기"
        p["words"] = ["blotter", "absorb", "press", "dry"]
        p["prompt"] = p["prompt"].replace("one precision skeleton clockwork movement at center showing its brass escape wheel and anchor pallet",
                                           "one classic curved rocker ink blotter standing at center with turned wooden handle and brass clamping plate")
        p["prompt"] = p["prompt"].replace("Begin with the triangular brass movement plates and spacer pillars. Draw the curved anchor pallet and toothed escape wheel next. Extend the vertical suspension spring and slender pendulum rod. Add the jewel pivots.",
                                           "Begin with the curved semicircular wooden rocker base. Draw the top clamping plate and turned knob handle next. Extend the wrapped felt blotting sheet layer below. Add the side brass screws.")
        p["prompt"] = p["prompt"].replace("only the palest translucent brass on the gear train with sheer steel on the pallet arms",
                                           "only the palest warm walnut-brown on the wooden blotter body and sheer polished brass on the top knob")
        p["prompt"] = p["prompt"].replace("The anchor pallet rocks smoothly once, releasing a single escape tooth with a silent rhythmic tick.",
                                           "The curved rocker blotter rocks smoothly once along its rounded base and rests level.")

with open("_작업/complete_100_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

for s in data:
    with open(s["filename"], "w", encoding="utf-8") as f:
        for p in s["prompts"]:
            f.write(p["prompt"] + "\n\n")

print("시계/모래시계/타이머 100% 완전 소탕 완료!")

