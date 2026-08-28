# -*- coding: utf-8 -*-
"""line-reveal 정본(MENSA 계열)으로 25장 생성"""
import io, json

B1=("Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge. "
"The very first frame is an entirely empty pure white field. The background is one single continuous field of "
"pure white reaching every edge of the frame. The subjects sit directly on that white with nothing underneath them: "
"no sheet, board, panel, card, mat, textured surface, visible edge or border. High-key lighting. "
"The centered illustration occupies the central three-quarters of the frame with equal narrow white margins on both sides. "
"Static locked-off camera, one continuous 8-second take.")
B2H="The only visible subjects are "
B2T=" These are the only objects present. No people, hands, animals, signs or drawing tools appear."
B3H=("0-4s: soft pale silver-grey graphite strokes appear progressively from the empty white field, each stroke drawn "
"with natural hand variation—firmer where it begins and fading slightly, nothing measured, vectorized or stamped. "
"The illustration draws itself. Each pale silver-grey graphite line appears progressively from its own endpoint, "
"one complete line at a time. The lines themselves extend gradually across the empty field; no object, tool, tip, "
"hand or instrument is ever visible. Nothing appears through a wipe, fade or dissolve. ")
B3T=(" Use only a few economical contour lines for every object. Leave most interiors as untouched white space. "
"No dense texture, no heavy shading and no realistic surface rendering.")
B4H="4-7s: an extremely pale, transparent watercolor wash develops gently inside the drawn contours. "
B4T=(" White remains clearly visible through every wash. No dark, dense or fully filled areas. "
"No color spreads behind the objects. The illustration remains airy, quiet and clearly hand-drawn.")
B5H="7-8s: "
B5T=(" All subjects remain 100% fully visible, crisp, opaque and completely still. "
"No object fades, dissolves, disappears, morphs or changes position.")
B6H=("The finished composition still contains every subject listed above and nothing more, all lines crisp and "
"completely stable, resting inside generous untouched white space. The finished image reads immediately as ")
B7=("Style: delicate fine-line editorial illustration, exceptionally thin pale silver-grey graphite contours, "
"sparse selective detail, luminous transparent watercolor, low saturation, restrained tonal contrast, "
"generous untouched white space, mature and understated, illustrated rather than realistic, "
"never photorealistic and never a children's cartoon.")
B8=("Audio: absolutely no audio of any kind. The output is completely silent with an empty audio track. "
"No music, score, instruments, melody, ambient tone, sound effects, foley, narration, voice or background hum.")
B9=("Never: hex codes, color codes, #FFFFFF, printed text, cabinet marks, fading out, opacity loss, ghosting, "
"disappearing objects, vanishing objects, text, letters, numbers, labels, arrows, diagrams, human figures, hands, "
"pens, pencils, brushes, drawing tools, picture frames, split screens, sheets, paper texture, visible paper grain, "
"panels, mats, borders, background rectangles, photorealistic rendering, realistic still-life photography, CGI, "
"3D render, glossy surfaces, dense hatching, cross-hatching, engraving, black ink masses, heavy outlines, "
"grey-dominant mood, sumi-e, dark watercolor, saturated colors, pink, yellow or orange background wash, "
"paint blooms behind the objects, fully painted surfaces, paint splatter, camera movement, cuts, fade-in, "
"dissolve, music, sound effects, or any subject disappearing.")

def build(sub,order,color,motion,reading):
    return " ".join([B1, B2H+sub+"."+B2T, B3H+order+B3T, B4H+color+B4T,
                        B5H+motion+B5T, B6H+reading+".", B7, B8, B9])

D=[
("우체국 창구","우체국 카운터·소포·우편자루",
 "one wooden post office counter with an arched clerk opening, one square parcel box tied with twine, and one canvas mail sack leaning against the counter",
 "Draw the counter outline first, then the arched opening, then the parcel with its twine, and finally the slumped mail sack.",
 "Use only a faint warm tan along the counter front, the palest wheat tint on the parcel, and a whisper of cool grey on the sack. The arched opening stays almost entirely white.",
 "the twine bow on the parcel loosens a few millimetres and settles.",
 "a post office counter with a parcel and a mail sack"),
("응급실 앞","구급차·경광등·들것",
 "one boxy ambulance van with a cross marking on its side, one small beacon lamp on its roof, and one folded wheeled stretcher standing beside it",
 "Draw the ambulance body outline first, then the wheels and windows, then the roof beacon, and finally the folded stretcher frame.",
 "Use only the palest cool grey on the van panels, a faint rose tint on the cross marking, and a whisper of warm amber on the beacon. The stretcher stays almost entirely white.",
 "the roof beacon brightens faintly once and dims again.",
 "an ambulance with a stretcher beside it"),
("변호사 사무실","서류가방·서류뭉치·도장",
 "one open leather document case, one stack of folded papers beside it, and one small desk seal with a turned handle",
 "Draw the case outline and its buckled flap first, then the fanned edges of the paper stack, and finally the seal with its handle.",
 "Use only a faint tan along the case edges, the palest cream on the paper stack, and a whisper of cool grey on the seal.",
 "the top folded paper lifts a millimetre at its corner and settles back.",
 "a document case with papers and a desk seal"),
("기차역 승강장","증기기관차·철로·역 시계",
 "one steam locomotive standing at a platform, two parallel steel rails running beneath it, and one round hanging station clock with a blank face",
 "Draw the locomotive boiler and chimney first, then the driving wheels, then the two rails with a few sleepers, and finally the round clock and its bracket.",
 "Use only a faint cool grey along the locomotive body, the palest steel-blue on the rails, and a whisper of warm tan on the clock rim. The clock face stays white.",
 "a small wisp of pale grey steam rises from the chimney and drifts.",
 "a steam locomotive at a platform with a station clock"),
("박물관 전시실","전시대 위 항아리·벽에 걸린 액자 둘·벨벳 줄 기둥",
 "one low display plinth carrying an ancient two-handled clay urn, two empty picture frames hanging on the wall behind, and one velvet rope barrier post standing in front",
 "Draw the plinth outline first, then the swelling body and looped handles of the urn, then the two hanging frames, and finally the barrier post with its draped rope.",
 "Use only a faint terracotta on the shoulder of the urn, the palest grey along the plinth edge, and a whisper of dusty rose on the draped rope. The frames stay almost entirely white.",
 "the draped rope sways a few millimetres and comes to rest.",
 "a museum display with an urn, wall frames and a rope barrier"),
("호텔 로비","프런트 데스크·열쇠 걸이·호출벨·여행가방",
 "one hotel reception desk, one wall rack of small open pigeonholes with room keys hanging on hooks behind it, one domed call bell on the counter, and one leather travel case standing on the floor",
 "Draw the reception desk outline first, then the grid of open pigeonholes with a few hanging keys, then the domed call bell, and finally the travel case with its straps.",
 "Use only a faint walnut tone along the desk front, a whisper of warm tan on the travel case, and the palest amber on the bell dome. The key rack stays almost entirely white.",
 "one hanging key swings a few millimetres on its hook and stills.",
 "a hotel reception desk with a key rack, a call bell and a travel case"),
("영화관","영사기·필름 릴 둘·필름 띠",
 "one cinema film projector, two spoked film reels mounted on it, and one trailing strip of perforated film hanging from the lower reel",
 "Draw the projector body outline first, then the lens barrel, then the two circular reels with their cut-out spokes, and finally the winding film strip.",
 "Use only a faint cool grey on the projector body, the palest amber on the lens rim, and a whisper of warm tan on the film strip.",
 "the upper reel turns a quarter revolution and stops.",
 "a cinema projector with two reels and a strip of film"),
("옛 성","성벽·아치문·왕관",
 "one stone castle keep with square battlements along its top, one arched wooden gate set into its base, and one banded crown resting on a small cushion in front",
 "Draw the outline of the keep first, then the square battlements, then the arched gate with its few studs, and finally the crown and the folds of its cushion.",
 "Use only a faint sandstone tone along a few stone courses, the palest oak on the gate planks, and small points of warm tan on the crown. Most wall surfaces stay bare white.",
 "one small jewel on the crown catches a faint pale gleam and fades.",
 "a castle keep with an arched gate and a crown"),
("감옥 창살","쇠창살 다섯·가로대·자물쇠",
 "five vertical iron bars, one horizontal crossbar joining them, and one heavy padlock hanging from a ring on the crossbar",
 "Draw each vertical bar in turn as a single thin line, then the crossbar and its riveted collars, and finally the shackle and body of the hanging padlock.",
 "Use only a faint cool grey along the bars, a few specks of pale rust at the joints, and the palest grey on the padlock body.",
 "the hanging padlock swings a few millimetres on its ring and stills.",
 "iron prison bars with a padlock hanging from them"),
("전화 교환대","교환기 판·플러그 코드·레버",
 "one telephone switchboard panel with rows of round jack sockets, one braided cord with a tapered plug lying across it, and one small toggle lever at the side",
 "Draw the rectangular panel outline first, then the evenly spaced rows of round sockets, then the coiled braided cord with its plug, and finally the small toggle lever.",
 "Use only a faint olive-grey along the panel edge, the palest amber on the socket rims, and a whisper of cool blue on the braided cord.",
 "the small toggle lever tips down a millimetre and holds.",
 "a telephone switchboard with a plug cord and a lever"),
("제분소 맷돌","돌 맷돌·밀가루 자루·나무 삽",
 "one round stone mill wheel standing upright, one open flour sack slumped beside it, and one wooden scoop resting against the sack",
 "Draw the circular rim of the mill stone first, then its radial dressing grooves, then the sagging folds of the flour sack, and finally the bowl and handle of the wooden scoop.",
 "Use only a faint cool grey along the rim of the mill stone, the palest cream on the spilled flour, and a whisper of honey-brown on the wooden scoop.",
 "a small pinch of pale flour slides down the sack and settles.",
 "a stone mill wheel with a flour sack and a wooden scoop"),
("소화전과 관","소화전·감긴 관·놋쇠 노즐",
 "one cast iron fire hydrant with a domed cap, one coiled canvas hose lying flat beside it, and one tapered brass nozzle resting on the coil",
 "Draw the hydrant body and its domed cap first, then the side outlets, then the flat spiral coils of the hose, and finally the tapered nozzle.",
 "Use only a faint rose tone along the hydrant ridges, the palest oatmeal on the coiled hose, and a whisper of warm amber on the nozzle.",
 "one outer coil of the hose relaxes outward a few millimetres and stops.",
 "a fire hydrant with a coiled hose and a nozzle"),
("발사대의 로켓","로켓·지지탑·연기",
 "one tall rocket standing upright on a launch stand with a tapered nose cone and three angled fins, and one lattice service tower standing beside it",
 "Draw the tall cylindrical body of the rocket first, then the tapered nose cone, then the three fins and the stage joint rings, and finally the criss-cross lattice of the service tower.",
 "Use only the palest ivory along the rocket hull, a few faint apricot bands at the stage joints, and a whisper of cool grey on the lattice tower.",
 "a thin curl of pale vapour drifts from the rocket base and fades.",
 "a rocket standing on a launch stand beside a service tower"),
("거리 행진","악대차·나팔·삼각깃발",
 "one open-sided parade van hung with triangular bunting, one brass marching horn resting on its bed, and two small pennant flags fixed at its corners",
 "Draw the van body outline first, then its spoked wheels, then the draped triangular bunting, then the curled tubing and flared bell of the horn, and finally the two pennants.",
 "Use only a faint sky-blue along the van panels, the palest amber on the horn bell, and a whisper of rose on the bunting.",
 "the strung bunting lifts a few millimetres in a breath of air and settles.",
 "a parade van with bunting, a marching horn and pennants"),
("가게 계산대","금전등록기·종이띠·가격표",
 "one antique mechanical cash register with a row of round keys and a blank round dial above them, one blank paper strip curling from its slot, and one small tag hanging from a string at its side",
 "Draw the stepped body of the register first, then its rounded crown, then the row of round keys and the blank dial, then the curling paper strip, and finally the small hanging tag.",
 "Use only a faint bronze-grey along the register mouldings, the palest cream on the paper strip, and a whisper of warm tan on the tag.",
 "the curled paper strip unrolls a few millimetres and stops.",
 "a mechanical cash register with a paper strip and a tag"),
("은행 창구","금고문·장부·동전더미",
 "one circular bank vault door with a spoked wheel lock, one closed leather account book lying flat beside it, and one short stacked column of coins",
 "Draw the concentric rings of the vault door first, then the radial spokes of the wheel lock and the hinge column, then the closed boards of the account book, and finally the stacked disc edges of the coin column.",
 "Use only a faint cool grey along the vault rings, the palest sage on the account book cover, and a whisper of warm amber on the coin edges.",
 "the spoked wheel lock turns one eighth of a revolution and stops.",
 "a bank vault door with an account book and a stack of coins"),
("식당 차림표","나무 안내판·수첩·양념병 둘",
 "one small hinged wooden board stand with a blank panel, one closed cloth-bound notebook lying beside it, and two small glass seasoning bottles with stoppers",
 "Draw the hinged wooden frame first, then the blank panel inside it, then the stitched spine and cover of the notebook, and finally the two bottles with their stoppers.",
 "Use only a faint pine tone along the wooden frame, the palest sage inside the panel, and a whisper of warm amber in the two bottles.",
 "one small bottle rocks a single millimetre and settles upright.",
 "a wooden board stand with a notebook and two seasoning bottles"),
("사람의 머리와 목","머리 단면·목·무릎 관절",
 "one human head shown in profile with the brain cross-section visible inside it, one throat passage drawn beside it, and one knee joint drawn below them",
 "Draw the profile contour of the head first, then the folded convolutions of the brain section, then the tubular throat passage with its rings, and finally the hinged bones of the knee joint.",
 "Use only a faint dusty rose inside the brain section, the palest beige along the skin contour, and a whisper of ivory on the knee bones.",
 "a faint pale tint spreads a little further through the brain section and holds.",
 "an anatomical plate of a head, a throat and a knee joint"),
("증기 압력계","압력계·배관·밸브",
 "one round brass pressure gauge with a blank round dial and a slender needle, one riveted pipe elbow below it, and one spoked hand wheel valve on the pipe",
 "Draw the circular bezel of the gauge first, then the blank dial and its slender needle, then the riveted seams of the pipe elbow, and finally the spoked rim of the hand wheel valve.",
 "Use only a faint amber along the gauge bezel, the palest cream inside the blank dial, and a whisper of cool grey on the pipe and valve.",
 "the gauge needle swings a few degrees upward and steadies.",
 "a pressure gauge on a pipe elbow with a hand wheel valve"),
("석탄 광차","석탄 더미·광차·삽",
 "one iron mining cart heaped with angular coal lumps, two short rails beneath its wheels, and one shovel leaning against its side",
 "Draw the riveted body panels of the cart first, then its small spoked wheels, then the faceted outlines of the heaped coal lumps, then the two short rails, and finally the shaft and blade of the shovel.",
 "Use only a faint cool slate along the coal facets, the palest iron-brown on the cart panels, and a whisper of grey on the rails and shovel.",
 "one small coal lump slides down the heap and stops.",
 "a mining cart heaped with coal, with rails and a shovel"),
("가족 사진틀","타원 액자·작은 로켓·반지 둘",
 "one oval carved picture frame holding two soft portrait silhouettes, one small oval locket resting beside it, and two plain wedding rings",
 "Draw the carved oval frame first, then the two soft portrait silhouettes inside it, then the hinged rim of the locket, and finally the two plain circular rings.",
 "Use only a faint walnut along the carved frame, the palest umber on the portrait silhouettes, and a whisper of warm amber on the locket and rings.",
 "the small locket lid opens a few millimetres and stops.",
 "an oval portrait frame with a locket and two rings"),
("광장의 군중","연단·현수막·모인 사람들",
 "one wooden speaker podium standing on paving, one cloth banner strung between two poles behind it, and six small standing figures gathered in front of it",
 "Draw the panelled front and slanted top of the podium first, then the two poles and the sagging banner between them, and finally the simple standing outlines of the six figures.",
 "Use only a faint sandstone along the podium front, the palest cream on the banner cloth, and a whisper of muted blue and rose on the small figures.",
 "the strung banner lifts a few millimetres at its centre and settles.",
 "a town square with a speaker podium, a banner and a small crowd"),
("군용 장비","철모·군화·수통",
 "one steel military helmet with a chin strap, one laced field boot standing beside it, and one metal canteen flask with a webbing strap",
 "Draw the domed shell and rolled rim of the helmet first, then its buckled chin strap, then the eyelets and stitched sole of the boot, and finally the flattened canteen and its strap.",
 "Use only a faint olive along the helmet shell, the palest brown on the boot leather, and a whisper of khaki on the webbing strap.",
 "the buckled chin strap of the helmet swings a few millimetres and stills.",
 "a military helmet, a field boot and a canteen flask"),
("신문 인쇄기","활자판·롤러·접힌 종이",
 "one cast metal tray divided into small compartments holding blank printing blocks, one inking roller with a turned handle resting beside it, and one folded blank paper sheet",
 "Draw the compartment grid of the tray first, then the rows of small blank blocks, then the cylindrical roller with its bent handle, and finally the creased folds of the paper sheet.",
 "Use only a faint cool slate along the tray edges, the palest honey on the roller handle, and a whisper of cream on the folded paper.",
 "the inking roller turns a quarter revolution in place and stops.",
 "a printing tray of blank blocks with a roller and a folded sheet"),
("골프 그린","퍼터·공·깃대",
 "one gently sloping putting green with a round cup hole, one flagstick standing in the cup with a small plain flag, one golf ball resting near the rim, and one putter club lying on the grass",
 "Draw the gentle contour of the green and the circular cup rim first, then the slender flagstick and its small flag, then the dimpled sphere of the ball, and finally the angled head and shaft of the putter.",
 "Use only a faint sage along a few contours of the green, the palest rose on the small flag, and a whisper of cool grey on the ball and putter head.",
 "the small flag on the flagstick lifts a few millimetres and settles.",
 "a putting green with a flagstick, a ball and a putter"),
]
OLD=json.loads(io.open('_작업/_proms25.json',encoding='utf-8').read())
assert len(OLD)==len(D), "%d vs %d"%(len(OLD),len(D))
NEW=[]
for (t,el,l1,l2,ch,_),(t2,el2,sub,order,color,motion,reading) in zip(OLD,D):
    NEW.append((t2,el2,l1,l2,ch,build(sub,order,color,motion,reading)))
io.open('_작업/_proms25.json','w',encoding='utf-8').write(json.dumps(NEW,ensure_ascii=False))
print("line-reveal 정본으로 %d장 재작성"%len(NEW))
