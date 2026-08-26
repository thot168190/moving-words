# -*- coding: utf-8 -*-
"""
[해결방안 2: 완전한 2D 측면 단면 뷰 (Pure 2D Cross-Section View)]
- 좌측 40%: 2D 측면 노란 스쿨버스 (Yellow School Bus in pure 2D side silhouette)
- 중앙 20%: 완전한 빈 안전 거리 (Empty white safety gap)
- 우측 40%: 수직 차단기 기둥 + 아래로 내려온 차단봉 + 빨간 경광등
- 공간 충돌 0% 완전 해소
"""

prompt_solution2 = """Cinematic progressive line-reveal animation on a solid pure bright white background (#FFFFFF), edge to edge. The very first frame is an entirely empty pure white field. High-key lighting. The main illustration is centered and occupies the central three-quarters of the frame, with equal narrow breathing margins on the left and right. The visual weight is divided evenly across the left and right halves, with a small subject anchor in each outer third. The horizon and camera axis are perfectly level: no Dutch angle, no tilted angle, no composition leaning to either side. Static locked-off camera, one continuous 8-second take. The only visible subjects throughout the sequence are a 2D side-profile yellow school bus on the left half, a wide empty white safety gap in the center, and a vertical railway barrier post with a lowered horizontal gate and two small red warning lamps on the right half. 0-4s: ultra-fine pale warm-grey graphite linework appears progressively from the empty white field. Every outline is very thin, soft and light, never black or dark charcoal; there are no bold contours, heavy edge lines or dense hatch marks. Begin with one perfectly level horizontal road baseline across the bottom. Draw the 2D side-profile school bus entirely on the left half of the frame, with wheels resting squarely on the road. Draw the vertical barrier post and railway signal entirely on the right half of the frame. Draw the lowered horizontal crossing bar extending leftward only into the empty center gap, ending well before the bus front bumper with a clear separation gap. There is no visible person, driver, student, live action element, asphalt darkness, city buildings or moving train anywhere. Keep all outline contours sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs. Every detail becomes visible sequentially, never all at once. Previously revealed lines remain delicate and completely stable. 4-8s: an extremely pale, water-heavy watercolor wash develops gently. All color remains low-saturation and transparent, with white showing through every wash. No area becomes dark, dense or fully filled. Use distinct, believable colors for different materials. Restraint means low saturation, not fewer colors or shared hues. The restrained palette is a soft sunny butter-yellow on the school bus body, sheer cool slate on the wheels and road baseline, and luminous translucent crimson-red on the barrier stripes and warning lamps. The two small red warning lamps pulse softly once; the school bus and all structures remain completely motionless and still. All other elements remain still. The final composition remains centered, readable and surrounded by generous untouched white space. Style: master-level fine-line illustration with exceptionally thin, pale warm-grey graphite strokes and sophisticated control, maximum line value 25% grey, luminous transparent watercolor, restrained tonal contrast, sophisticated contemporary editorial illustration for thoughtful young learners, generous untouched white space."""

clean_prompt = " ".join(prompt_solution2.split())

with open("_작업/prompt_solution2.txt", "w", encoding="utf-8") as f:
    f.write(clean_prompt)

import subprocess
res = subprocess.run(["python3", "_작업/verify_prompt.py", "_작업/prompt_solution2.txt"], capture_output=True, text=True)
print(res.stdout)

