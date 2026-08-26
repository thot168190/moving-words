#!/usr/bin/env python3
"""남은 16편 프롬프트를 성공문법 정본으로 재조립한다.

한 곳의 장면 데이터로 개별 txt와 대표님 확인용 HTML을 함께 갱신해
두 파일의 내용이 달라지는 사고를 막는다.
"""

from pathlib import Path
import html
import re

ROOT = Path(__file__).resolve().parent
HUB = ROOT / "제작허브_남은16편.html"

HEADER = (
    "Cinematic progressive line-reveal animation on a solid pure bright white "
    "background (#FFFFFF), edge to edge. The very first frame is an entirely empty "
    "pure white field. High-key lighting. The main illustration is centered and "
    "occupies the central three-quarters of the frame, with equal narrow breathing "
    "margins on the left and right. The visual weight is divided evenly across the "
    "left and right halves, with a small subject anchor in each outer third. The "
    "horizon and camera axis are perfectly level: no Dutch angle, no tilted frame, "
    "no composition leaning to either side. Static locked-off camera, one continuous "
    "8-second take."
)

LINE = (
    "0-4s: ultra-fine pale warm-grey graphite linework appears progressively from "
    "the empty white field. Every outline is very thin, soft and light, never black "
    "or dark charcoal; there are no bold contours, heavy edge lines or dense hatch "
    "marks. {draw} Every detail becomes visible sequentially, never all at once. "
    "Previously revealed lines remain delicate and completely stable."
)

COLOR = (
    "4-8s: an extremely pale, water-heavy watercolor wash develops gently. All "
    "color remains low-saturation and transparent, with white showing through every "
    "wash. No area becomes dark, dense or fully filled. Use distinct, believable "
    "colors for different materials. Restraint means low saturation, not fewer "
    "colors or shared hues. The restrained palette is {palette}. {action} All other elements remain still. The final composition "
    "remains centered, readable and surrounded by generous untouched white space."
)

STYLE = (
    "Style: master-level fine-line illustration with exceptionally thin, pale "
    "warm-grey graphite strokes and sophisticated control, maximum line value 25% "
    "grey, luminous transparent "
    "watercolor, restrained tonal contrast, sophisticated contemporary editorial "
    "illustration for thoughtful young learners, generous white space. No text, "
    "labels, borders, panels, drawing tools or visible artist. Completely silent."
)

HUMAN_SAFETY = (
    "Human-figure rule: every person is a clearly illustrated educational character, "
    "not a portrait and not photorealistic. Use simplified natural facial features, "
    "pleasant ordinary proportions, a calm approachable presence, soft minimal eyes, "
    "a naturally closed or gently relaxed mouth, sparse hair lines and smooth flat "
    "skin washes. Keep both eyes aligned and modest in size, the face symmetrical, "
    "the expression subtle, and all limbs and fingers anatomically normal. No uncanny "
    "or disturbing expression, bulging eyes, staring pupils, gaping mouth, exposed "
    "teeth, streaming tears, grimace, distorted face, asymmetrical features, duplicate "
    "features, extra fingers, extra limbs or broken anatomy. No pores, "
    "wrinkles, individual eyelashes, facial hair texture, veins, defined muscles or "
    "anatomical rendering. Every person remains fully and modestly clothed in an "
    "opaque crew-neck top and appropriate bottoms; no bare torso, underwear, sheer "
    "fabric, cleavage, nipples, groin contours or sexualized pose."
)

# words는 학습 배정 원문을 보존한다. subjects는 '소품 8개'가 아니라
# 하나의 중심 사건 안에서 단어들이 자연스럽게 연결되도록 설계한다.
SCENES = {
    "p-terra-1": dict(
        file="프롬프트/ch10_TERRA/terra-01_새벽안개.txt",
        subjects="one broad countryside road at dawn, a low bank of fog crossing the road, one farmhouse with a single chimney just right of center, a fence continuing toward the right outer third, and a light trail of dust beside the near wheel tracks",
        draw="Begin with one perfectly horizontal dawn horizon. Draw the broad road symmetrically from the lower center toward the farmhouse without rotating the scene. Extend the left hedgerow and the right fence to equal distances from their frame edges so neither side looks empty. Draw the farmhouse just right of center, followed by the low fog bank, dust marks and one thin ribbon of chimney smoke",
        palette="pale dawn blue, restrained meadow green and one faint warm-grey accent on the farmhouse",
        action="The fog drifts once across the road while the thin smoke rises a short distance",
    ),
    "p-terra-2": dict(
        file="프롬프트/ch10_TERRA/terra-02_폭풍우와물결.txt",
        subjects="one sturdy coastal rock with a seal at the optical center, a single sweeping tide extending across both outer thirds, and two modest clusters of wind-bent sea grass balancing the left and right edges",
        draw="Begin with one perfectly level sea horizon. Draw the low central rock and seal next, keeping the combined silhouette horizontal rather than diagonal. Extend one quiet current line and two tide crests equally toward the left and right outer thirds. Add one small grass cluster at lower left and one matching cluster at lower right. There is no thermometer, gauge, dial, instrument, sign or man-made object anywhere. Keep storm clouds sparse, pale and softly broken, never darker than 15% grey and never filled as solid outlined blobs",
        palette="natural warm grey on the spotted seal, cool stone grey and pale umber on the rock, muted blue-green in the sea, quiet sage on the grass, and a very pale lavender-grey in the clouds",
        action="One brief blow of coastal wind bends the grass and lifts a single tide crest; the seal raises its head",
    ),
    "p-terra-3": dict(
        file="프롬프트/ch10_TERRA/terra-03_무지개.txt",
        subjects="one open town square at noon, a large planet globe sculpture centered on a low pedestal, one shallow arc of fountain mist and a rainbow formed inside that mist",
        draw="The clean perspective lines of the square are drawn first, spreading evenly across the central width. The pedestal and planet globe appear next, followed by the high noon sun, the thin fountain mist and one clear rainbow arc",
        palette="pale turquoise on the globe, restrained stone beige in the square and a delicate spectrum limited to the rainbow",
        action="The fountain mist rises once and the rainbow becomes gently visible within it",
    ),
    "p-terra-4": dict(
        file="프롬프트/ch10_TERRA/terra-04_녹는얼음.txt",
        subjects="one county highway sweeping through an industrial district, one factory stack on the far-left skyline with a controlled steam plume attached only to the top of that stack, one separate safety flame on a second far-left stack, and a single roadside block of winter ice in the lower-right foreground beginning to melt as the temperature rises",
        draw="The highway curve is drawn first across the full central composition. The compact industrial district appears along the far side. Draw the two far-left factory stacks next: steam begins exactly at the rim of the first stack and the small safety flame stays exactly at the tip of the second stack. Draw the roadside ice block last in the lower-right foreground, far away from both stacks. Temperature is shown only by a slightly smaller ice block and a shallow clear meltwater puddle touching its base. No heat shimmer, thermometer, gauge, campfire or unrelated prop appears",
        palette="pale cool blue on the ice, restrained blue-grey on the district and one tiny muted coral accent on the safety flame",
        action="The factory steam plume moves downwind once while remaining connected to the first stack. Separately, the ice block becomes slightly smaller and two clear drops join the shallow puddle at its base. The ice never emits steam, smoke, mist, vapor, haze, fog or any airborne effect. A faint haze remains high above the distant district to show how industrial emissions pollute the air",
    ),
    "p-sensus-1": dict(
        file="프롬프트/ch07_SENSUS/sensus-01_거울앞.txt",
        human=True,
        subjects="one fully visible young adult educational character wearing a loose opaque crew-neck T-shirt and knee-length shorts, standing in a relaxed three-quarter pose with one bare foot slightly forward and one hand raised near the shoulder",
        draw="Draw the clothed character as a simple contemporary textbook figure, not an anatomy model. Economical contours define cheek and jaw; a small friendly open-mouth expression allows only the tip of the tongue to be seen. The T-shirt indicates the chest area without revealing anatomy, its sleeve edge indicates the shoulder, the shorts end above the knee, the forward bare foot shows toe and toenail, and the raised relaxed hand shows one fingernail. No mirror, body-part collage or exposed torso appears",
        palette="natural low-saturation skin tone, muted teal on the T-shirt, soft navy on the shorts and a pale warm-grey ground shadow",
        action="The character gently turns the raised hand outward and shifts the forward foot once while remaining fully clothed",
    ),
    "p-sensus-2": dict(
        file="프롬프트/ch07_SENSUS/sensus-02_아픈사람.txt",
        human=True,
        subjects="one weak patient resting upright in a simple clinic bed, one cool compress, one bandaged knee and one small medicine cup on the bedside table",
        draw="The patient and bed are drawn first as one central group. A tense brow and guarded posture show fever and pain; the bandaged knee shows an injury. The bedside table, medicine cup and cool compress appear last",
        palette="pale hospital blue, soft sage green and one restrained coral accent on the compress edge",
        action="The ill patient takes the medicine, exhales slowly and settles back as the tense shoulders relax",
    ),
    "p-sensus-3": dict(
        file="프롬프트/ch07_SENSUS/sensus-03_놀란표정.txt",
        human=True,
        subjects="one waist-up educational character in an opaque crew-neck sweater, centered against the white field, with one fallen paper cup near the lower edge",
        draw="Draw the sweater and simplified face first using sparse textbook-style contours. Slightly widened eyes and raised brows suggest surprise, shock and fright without bulging eyes, exposed teeth, tears, wrinkles or realistic skin detail. A lowered brow may suggest brief anger or panic, but the expression remains gentle and suitable for young learners",
        palette="pale skin tones, muted blue on the cup and a restrained coral accent in the cheeks",
        action="The startled expression softens in one continuous change: the jaw releases, the shoulders lower and the face arrives at calm peace",
    ),
    "p-sensus-4": dict(
        file="프롬프트/ch07_SENSUS/sensus-04_잠과깨어남.txt",
        human=True,
        subjects="one sleeping child curled on a simple bed, one bitten apple on the bedside table and a subtle anatomical-style breath contour through chest and stomach",
        draw="The bed and asleep child are drawn first. The relaxed face, chest, stomach and bent leg muscles appear next through sparse contours. The bitten apple is drawn last as a clear memory cue, with no floating brain or disconnected anatomy icons",
        palette="pale lavender bedding, muted sky blue and one soft apple green accent",
        action="One visible breath gently raises the chest and stomach; the child then opens the eyes and becomes awake",
    ),
    "p-motus-1": dict(
        file="프롬프트/ch08_MOTUS/motus-01_공항.txt",
        subjects="one passenger plane centered on an airport runway, one open boarding gate in the terminal behind it and one compact service vehicle near the engine",
        draw="The runway and airport terminal are drawn first across the central width. The plane appears next from nose to tail, followed by the airline tail mark without letters, the open gate, engine, landing brake assembly, service vehicle and a clearly open terminal exit",
        palette="pale aviation blue, restrained silver-grey and one muted coral tail accent",
        action="The service vehicle rolls clear, the plane begins one short controlled taxi and the landing brake releases",
    ),
    "p-motus-2": dict(
        file="프롬프트/ch08_MOTUS/motus-02_자전거와수레.txt",
        subjects="one family cargo cycle carrying a picnic basket, traveling beside a quiet rail crossing while one van waits behind it in light traffic",
        draw="The cycle and attached cargo cart are drawn first as the clear central vehicle. The picnic basket appears inside the cart, followed by the road, rail crossing, waiting van and two restrained traffic lines. No vehicle showroom or scattered transport icons appear",
        palette="pale leaf green, muted sky blue and a restrained warm-red accent on the cycle frame",
        action="The crossing barrier rises and the motor-assisted cycle moves forward while the van remains stopped",
    ),
    "p-motus-3": dict(
        file="프롬프트/ch08_MOTUS/motus-03_던지고당기기.txt",
        human=True,
        subjects="one athlete beside a heavy training bag in a clean practice area, one tied resistance rope and one medicine ball",
        draw="The athlete, training bag and anchored rope are drawn first. The tied knot, packed bag, medicine ball and a single floor sweep mark appear next. The pose clearly prepares a controlled pull rather than eight unrelated action icons",
        palette="pale cobalt, restrained warm grey and one muted coral accent on the medicine ball",
        action="The athlete pulls the rope once, pivots and throws the medicine ball; it knocks the training pad with one clean impact",
    ),
    "p-motus-4": dict(
        file="프롬프트/ch08_MOTUS/motus-04_군인과경비.txt",
        human=True,
        subjects="one uniformed rescue officer guiding a small civilian group through an open checkpoint gate while one guard watches the safe route",
        draw="The open checkpoint and safe route are drawn first. The rescue officer and guard appear next, followed by the small civilian group. A secured military vehicle and one holstered service weapon remain distant and understated, never aimed or used",
        palette="pale olive, muted navy and one restrained safety-orange route accent",
        action="The officer signals the safe escape route and the group moves through the gate while the guard remains alert",
    ),
    "p-somnium-1": dict(
        file="프롬프트/ch12_SOMNIUM/somnium-01_밤이야기.txt",
        human=True,
        subjects="one child pretending to tell a tale beneath a small blanket tent, with one open picture book and two soft shadow shapes resembling a ghost and an angel",
        draw="The blanket tent and seated storyteller are drawn first. The open book appears next, followed by the two strange shadow shapes and a small cluster of magic-like stars. No shelf of symbolic props appears",
        palette="pale midnight blue, restrained lavender and one faint warm-gold accent on the stars",
        action="As the child makes one quiet speech gesture, the two mysterious shadows gently change from ghost-like to angel-like shapes",
    ),
    "p-somnium-2": dict(
        file="프롬프트/ch12_SOMNIUM/somnium-02_속삭임과외침.txt",
        human=True,
        subjects="two friends seated face to face, one small sleeping cat between them and one message card awaiting a reply",
        draw="The two friends and sleeping cat are drawn first. One friend leans close for a whisper while the other listens. The message card appears last; expression and posture carry chat, joke and reply without speech bubbles or text",
        palette="pale teal, muted coral and a faint warm-grey on the cat",
        action="A whisper makes one friend smile; the other replies aloud with a brief laugh, then both fold their hands for a quiet wish so the cat remains asleep. No shout or yell is acted out violently",
    ),
    "p-somnium-3": dict(
        file="프롬프트/ch12_SOMNIUM/somnium-03_생각하는자리.txt",
        human=True,
        subjects="one thoughtful student concentrating on a compact wooden shape puzzle, with one reminder token beside the unfinished space",
        draw="The student and puzzle board are drawn first. Three possible pieces appear beside one empty space, followed by the small reminder token. The student's gaze and hand position make attention and consideration clear without floating icons, diagrams or a cluttered desk",
        palette="pale cobalt, muted amber and restrained leaf green on the puzzle pieces",
        action="The student notices the shape, considers the alternatives, selects a method and slides the correct piece into place, solving the puzzle for a visible reason",
    ),
    "p-somnium-4": dict(
        file="프롬프트/ch12_SOMNIUM/somnium-04_전하는말.txt",
        human=True,
        subjects="one young field reporter speaking to a small camera beside a community notice board, holding one picture report with no readable text",
        draw="The reporter and camera are drawn first. The picture report and notice board appear next, followed by one attentive listener. Clear posture connects message, report, announce and inform without a desk full of symbolic objects",
        palette="pale navy, muted coral and one restrained warm-yellow accent on the picture report",
        action="The reporter points to the picture, describes what happened, mentions one detail and turns toward the source image to refer to it; the listener's expression shows the message has been understood",
    ),
}


def make_prompt(scene: dict) -> str:
    blocks = [
            HEADER,
            "The only visible subjects throughout the sequence are " + scene["subjects"] + ".",
            LINE.format(draw=scene["draw"] + "."),
            COLOR.format(palette=scene["palette"], action=scene["action"] + "."),
        ]
    if scene.get("human"):
        blocks.append(HUMAN_SAFETY)
    blocks.append(STYLE)
    return "\n\n".join(blocks)


def main() -> None:
    hub = HUB.read_text(encoding="utf-8")
    for prompt_id, scene in SCENES.items():
        prompt = make_prompt(scene)
        target = ROOT / scene["file"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(prompt + "\n", encoding="utf-8")

        pattern = rf'(<textarea id="{re.escape(prompt_id)}" readonly>).*?(</textarea>)'
        hub, count = re.subn(
            pattern,
            lambda m: m.group(1) + html.escape(prompt, quote=False) + m.group(2),
            hub,
            count=1,
            flags=re.S,
        )
        if count != 1:
            raise RuntimeError(f"허브에서 {prompt_id}를 찾지 못했습니다")

    # 대표님 확정 이동: temperature는 물범보다 녹는 얼음 장면에서 인과가 자연스럽다.
    hub = hub.replace(
        "storm · blow · tide · current · seal · temperature",
        "storm · blow · tide · current · seal",
    )
    hub = re.sub(
        r"melt · steam · flame · highway · district · county · pollute(?: · temperature)*",
        "melt · steam · flame · highway · district · county · pollute · temperature",
        hub,
    )

    hub = hub.replace("16/16 완료 (100% PASS)", "16/16 구조 재설계 완료 · Flow 실물 검증 전")
    hub = hub.replace("QC PASS", "실물 검증 전")
    hub = hub.replace('class="badge badge-pass">실물 검증 전', 'class="badge badge-review">실물 검증 전')
    hub = re.sub(
        r"✓ qc_prompt\.py 검사 결과: PASS[^<]*",
        "△ 성공문법 구조검사 완료 · Flow 생성 결과는 대표님 판정 전",
        hub,
    )
    HUB.write_text(hub, encoding="utf-8")

    print(f"개별 프롬프트 {len(SCENES)}개와 허브를 갱신했습니다.")


if __name__ == "__main__":
    main()
