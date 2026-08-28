# -*- coding: utf-8 -*-
import io, json, html

HEAD=("Progressive detailed fine-pencil construction, transparent watercolor and gentle object-motion animation "
"on a solid pure bright white background (#FFFFFF), edge to edge. The first frame is an entirely empty pure white field. "
"Static locked-off camera, one continuous 8-second take. The only visible subjects are ")
DRAW_H="0-3.5s: exceptionally fine pale-neutral 2H graphite strokes are visibly traced one by one across the empty white field. "
DRAW_T=(" Use many precise structural contours and short directional texture marks; do not simplify the subjects into icons "
"or basic outlines. Each stroke has a clear beginning and endpoint. The illustration is built progressively rather than "
"fading into view. Previously completed lines remain stable.")
COL_H="3.5-5.5s: clear transparent watercolor develops in layered color. "
COL_T=(" Every wash stays pale and translucent, applied once and never built up to full saturation. "
"Preserve narrow white-paper highlights while keeping the colors fresh, luminous and distinguishable, "
"with graphite details visible through every layer.")
MOT_H="5.5-8s: "
MOT_T=" All other elements remain fixed. All graphite construction lines and watercolor boundaries remain stable."
STY_H=("Style: intricate premium pencil-and-watercolor plate, numerous hair-thin pale graphite construction lines, "
"accurate object anatomy, luminous layered transparent watercolor, ")
STY_T=", sophisticated museum-quality illustrated-dictionary artwork, clearly hand-drawn and never photographic."
NEG=("No dark outline, black ink, sepia ink, charcoal, thick contour, product photography, studio lighting, "
"realistic reflection, glossy highlight, cast shadow, 3D, CGI, text, label, border, hand, artist or visible drawing tool. ")
NEG_T=" Completely silent."

D=[
("exactly one illustrated wooden post office counter with an arched clerk window, one illustrated brown parcel box tied with twine and one illustrated canvas mail sack leaning beside it",
 "The counter frame is constructed first through separate hair-thin graphite lines, followed by the arched window opening, the square parcel with its knotted twine, and the slumped folds of the canvas mail sack.",
 "A pale warm amber wash settles lightly on the wooden counter, faint teal-grey tints the window glass, soft ochre touches the parcel, and pale oatmeal-grey colors the sack.",
 "the knotted twine bow on the parcel loosens two millimetres and settles. The counter, window and sack remain fixed.",
 "delicate postal artifact textures","Exactly one parcel and one sack."),
("exactly one illustrated white medical ambulance with cross markings, one illustrated rooftop beacon lamp and one illustrated folded wheeled stretcher beside it",
 "The boxy contours of the ambulance body are traced first, followed by the wheel arches, headlamps, rooftop beacon housing, side window panels and the slender frame of the folded stretcher.",
 "A pale white-grey wash defines the ambulance panels, soft crimson tints the cross markings, faint cobalt touches the windows, and pale amber colors the beacon lamp.",
 "the rooftop beacon lamp brightens faintly once and dims again. The vehicle and stretcher remain fixed.",
 "crisp hand-drawn vehicle contours","Exactly one ambulance and one stretcher."),
("exactly one illustrated leather document case standing open, one illustrated stack of folded legal papers and one illustrated brass desk seal beside them",
 "The buckled flap and stitched seams of the leather case are traced first, followed by the fanned edges of the folded paper stack and the turned handle of the brass desk seal.",
 "A pale tan wash settles lightly on the leather case, faint cream tints the paper stack, and soft ochre touches the brass seal.",
 "the topmost folded paper lifts one millimetre at its corner and settles back. The case and seal remain fixed.",
 "quiet legal-office textures","Exactly one case, one paper stack and one seal."),
("exactly one illustrated vintage steam locomotive at a platform, exactly two illustrated parallel steel rails and one illustrated round hanging station clock",
 "The cylindrical boiler, chimney stack, cowcatcher and spoked driving wheels are constructed through fine graphite contours, followed by the straight parallel rails, the wooden sleepers, and the circular hanging clock.",
 "A pale slate-grey wash settles lightly on the locomotive body, faint steel-blue tints the rails, and soft ochre touches the clock casing.",
 "a small wisp of pale translucent steam rises three centimetres from the chimney and drifts. The train, rails and clock remain fixed.",
 "intricate hand-drawn machinery details","Exactly one locomotive and one clock."),
("exactly one illustrated museum glass showcase cabinet on a stone pedestal and one illustrated ancient carved clay urn displayed inside it",
 "The rectilinear glass cabinet frame is drawn with clean graphite lines, followed by the fluted stone pedestal, and the delicate handles and textured relief band of the ancient urn.",
 "A faint mint-grey tint fills the glass panes, pale terracotta settles lightly on the urn, and soft warm grey veins the stone stand.",
 "the small clay urn shifts a single millimetre on the glass shelf and settles. The cabinet and pedestal remain fixed.",
 "museum artifact precision","Exactly one cabinet and one urn."),
("exactly one illustrated curved wooden hotel reception desk, one illustrated brass call bell, exactly one illustrated room key with a numbered tag and one illustrated leather travel case",
 "The sweep of the reception counter is traced with fine graphite, followed by the domed call bell, the notched key with its oval tag, and the buckled straps of the leather travel case.",
 "A pale walnut wash settles lightly on the counter, soft ochre touches the bell and key tag, and faint tan tints the travel case.",
 "the numbered key tag sways gently two millimetres and comes to rest. The desk, bell and case remain fixed.",
 "vintage hospitality textures","Exactly one bell, one key and one case."),
("exactly one illustrated vintage cinema film projector with two spoked reels, one illustrated lens barrel and one illustrated trailing strip of perforated film",
 "The mechanical body of the projector, the two circular reels with their cut-out spokes, the lens barrel, and the winding film strip are drawn with hair-thin graphite lines.",
 "A pale slate-grey wash settles lightly on the projector body, soft ochre touches the lens rim, and faint amber tints the translucent film ribbon.",
 "the upper film reel turns one quarter revolution and stops. The projector body, lens and film remain fixed.",
 "vintage cinema apparatus details","Exactly one projector."),
("exactly one illustrated stone castle keep with crenellated battlements, one illustrated arched wooden gate and one illustrated jewelled crown resting on a cushion before it",
 "The stacked stone courses of the keep are traced first, followed by the square crenellations, the arched gate with iron studs, and the banded circle of the crown with its cushion folds.",
 "A pale sandstone wash settles lightly on the castle walls, soft oak-brown tints the gate, and faint ochre with small rose and cobalt points colors the crown.",
 "one small jewel on the crown catches a faint pale gleam and fades. The castle and gate remain fixed.",
 "weathered stonework textures","Exactly one castle, one gate and one crown."),
("exactly five illustrated vertical iron prison bars, one illustrated horizontal crossbar and one illustrated heavy padlock hanging from a ring",
 "Each vertical bar is traced separately as a hair-thin graphite column, followed by the crossbar joints, the riveted collars, and the shackle and body of the hanging padlock.",
 "A pale slate wash settles lightly on the bars with faint rust-ochre specks at the joints, and soft grey tints the padlock body.",
 "the hanging padlock swings two millimetres on its ring and stills. The bars remain fixed.",
 "cold ironwork textures","Exactly five bars and one padlock."),
("exactly one illustrated telephone switchboard panel with rows of round jack sockets, one illustrated braided cord with a plug and one illustrated brass toggle lever",
 "The rectangular switchboard face is drawn first, followed by the evenly spaced rows of circular sockets, the coiled braided cord with its tapered plug, and the small toggle lever.",
 "A pale olive-grey wash settles lightly on the panel, soft ochre touches the socket rims and lever, and faint indigo tints the braided cord.",
 "the small brass toggle lever tips down one millimetre and holds. The panel and cord remain fixed.",
 "early telephony apparatus details","Exactly one panel, one cord and one lever."),
("exactly one illustrated round stone mill wheel standing upright, one illustrated open flour sack slumped beside it and one illustrated wooden scoop",
 "The circular rim and radial dressing grooves of the mill stone are traced first, followed by the sagging folds and rolled collar of the flour sack, and the shaped bowl and handle of the wooden scoop.",
 "A pale grey wash settles lightly on the mill stone, faint cream tints the spilled flour and sack cloth, and soft honey-brown touches the wooden scoop.",
 "a small pinch of pale flour slides two millimetres down the sack and settles. The mill stone and scoop remain fixed.",
 "coarse stone and cloth textures","Exactly one mill stone, one sack and one scoop."),
("exactly one illustrated cast iron fire hydrant, one illustrated coiled canvas hose lying beside it and one illustrated brass nozzle",
 "The domed cap, hexagonal bonnet and side outlets of the hydrant are traced first, followed by the flat spiral coils of the canvas hose and the tapered brass nozzle.",
 "A pale vermilion wash settles lightly on the hydrant, faint oatmeal tints the coiled hose, and soft ochre touches the nozzle.",
 "one outer coil of the hose relaxes two millimetres outward and stops. The hydrant and nozzle remain fixed.",
 "municipal ironwork textures","Exactly one hydrant, one hose and one nozzle."),
("exactly one illustrated multi-stage rocket standing upright on a launch stand, with a tapered nose cone, exactly three illustrated fins and one illustrated lattice service tower beside it",
 "The tall cylindrical body of the rocket is traced first, followed by the tapered nose cone, the three angled fins, the stage joint rings, and the criss-cross lattice of the service tower.",
 "A pale ivory wash settles lightly on the rocket hull with faint orange bands at the stage joints, and soft grey tints the lattice tower.",
 "a thin curl of pale translucent vapour drifts two centimetres from the rocket base and fades. The rocket and tower remain fixed.",
 "clean aerospace contours","Exactly one rocket and one tower."),
("exactly one illustrated open-sided parade van decorated with bunting, one illustrated brass marching horn resting on its bed and exactly two illustrated small pennant flags",
 "The boxy van body and spoked wheels are traced first, followed by the draped triangular bunting, the curled tubing and flared bell of the marching horn, and the two small pennants.",
 "A pale sky-blue wash settles lightly on the van, soft ochre touches the horn, and faint rose and cream tint the bunting and pennants.",
 "the strung bunting lifts two millimetres in a breath of air and settles. The van and horn remain fixed.",
 "festive parade textures","Exactly one van, one horn and two pennants."),
("exactly one illustrated antique mechanical cash register with a numbered dial front, one illustrated small paper receipt curling from its slot and one illustrated handwritten price tag on a string",
 "The stepped body and rounded crown of the register are traced first, followed by the rows of round keys, the numbered dial face, the curling receipt strip and the small tag with its string.",
 "A pale bronze wash settles lightly on the register body, faint cream tints the receipt, and soft ochre touches the price tag.",
 "the curled paper receipt unrolls two millimetres and stops. The register and tag remain fixed.",
 "antique mechanical retail textures","Exactly one register, one receipt and one tag."),
("exactly one illustrated circular bank vault door with a spoked wheel lock, one illustrated bound ledger book lying flat and one illustrated stacked coin column beside it",
 "The concentric rings of the vault door are traced first, followed by the radial spokes of the wheel lock, the hinge column, the ruled boards of the ledger and the stacked disc edges of the coin column.",
 "A pale graphite-grey wash settles lightly on the vault door, faint forest-green tints the ledger cover, and soft ochre touches the coin stack.",
 "the spoked wheel lock turns one eighth of a revolution and stops. The vault door, ledger and coins remain fixed.",
 "precise strongroom mechanics","Exactly one vault door, one ledger and one coin stack."),
("exactly one illustrated wooden folding menu board, one illustrated open recipe notebook and exactly two illustrated small glass seasoning bottles",
 "The hinged wooden frame of the menu board is traced first, followed by the ruled panel face, the fanned pages and stitched spine of the recipe notebook, and the stoppered necks of the two seasoning bottles.",
 "A pale pine wash settles lightly on the wooden frame, faint sage-green fills the board panel, soft cream tints the notebook pages, and pale amber colors the bottles.",
 "one small seasoning bottle rocks a single millimetre and settles upright. The board and notebook remain fixed.",
 "quiet kitchen-counter textures","Exactly one board, one notebook and two bottles."),
("an illustrated anatomical plate showing exactly one illustrated human head in profile with the brain cross-section visible, one illustrated throat passage and one illustrated knee joint drawn beside it",
 "The profile contour of the head is traced first, followed by the folded convolutions of the brain cross-section, the tubular throat passage with its cartilage rings, and the hinged bones of the knee joint.",
 "A pale dusty-rose wash settles lightly on the brain tissue, faint beige tints the skin contour, and soft ivory colors the knee bones.",
 "a faint pale tint spreads two millimetres through the brain section and holds. The head, throat and knee remain fixed.",
 "restrained anatomical plate precision","Exactly one head, one throat and one knee joint."),
("exactly one illustrated round brass pressure gauge with a needle dial, one illustrated riveted pipe elbow below it and one illustrated hand wheel valve",
 "The circular bezel and graduated dial face of the gauge are traced first, followed by the slender needle, the riveted seams of the pipe elbow and the spoked rim of the hand wheel valve.",
 "A pale ochre wash settles lightly on the brass gauge bezel, faint cream fills the dial face, and soft slate-grey tints the pipe and valve.",
 "the gauge needle swings one small division upward and steadies. The pipe and valve remain fixed.",
 "industrial instrument precision","Exactly one gauge, one pipe elbow and one valve."),
("exactly one illustrated iron mining cart heaped with angular coal lumps, resting on exactly two illustrated short rails, with one illustrated shovel leaning against it",
 "The riveted body panels and small spoked wheels of the cart are traced first, followed by the faceted outlines of the heaped coal lumps, the two short rails and the shaft and blade of the shovel.",
 "A pale slate wash settles lightly on the coal lumps, faint iron-brown tints the cart body, and soft grey colors the rails and shovel.",
 "one small coal lump slides two millimetres down the heap and stops. The cart, rails and shovel remain fixed.",
 "rough mineral and ironwork textures","Exactly one cart, one coal heap and one shovel."),
("exactly one illustrated oval carved picture frame holding a portrait of a couple, one illustrated small oval locket beside it and exactly two illustrated wedding rings",
 "The carved leaf moulding of the oval frame is traced first, followed by the soft portrait silhouettes of the two figures inside, the hinged rim of the locket, and the two plain circular rings.",
 "A pale walnut wash settles lightly on the carved frame, faint umber tints the portrait, and soft ochre touches the locket and rings.",
 "the small locket lid opens two millimetres and stops. The frame and rings remain fixed.",
 "tender keepsake textures","Exactly one frame, one locket and two rings."),
("an illustrated open town square with exactly one illustrated wooden speaker podium, one illustrated cloth banner strung between two poles and exactly six illustrated small standing figures gathered before it",
 "The panelled front and slanted top of the podium are traced first, followed by the two poles and the sagging cloth banner between them, and the simple standing outlines of the six gathered figures.",
 "A pale sandstone wash settles lightly on the podium and paving, faint cream tints the banner cloth, and soft muted blue and rose color the small figures.",
 "the strung banner lifts two millimetres at its centre and settles. The podium and figures remain fixed.",
 "restrained civic scene textures","Exactly one podium, one banner and six figures."),
("exactly one illustrated steel military helmet with a chin strap, one illustrated laced field boot and one illustrated metal canteen flask with a webbing strap",
 "The domed shell and rolled rim of the helmet are traced first, followed by the buckled chin strap, the eyelets and stitched sole of the field boot, and the flattened body and screw cap of the canteen.",
 "A pale olive-drab wash settles lightly on the helmet and canteen, faint brown tints the boot leather, and soft khaki colors the webbing strap.",
 "the buckled chin strap of the helmet swings two millimetres and stills. The boot and canteen remain fixed.",
 "worn field-kit textures","Exactly one helmet, one boot and one canteen."),
("exactly one illustrated cast metal type tray filled with small letter blocks, one illustrated inking roller with a turned handle and one illustrated folded newspaper sheet",
 "The compartment grid of the type tray is traced first, followed by the rows of small rectangular type blocks, the cylindrical roller with its bent handle, and the creased folds of the newspaper sheet.",
 "A pale slate wash settles lightly on the metal type blocks, soft honey-brown tints the roller handle, and faint cream colors the folded newspaper.",
 "the inking roller turns one quarter revolution in place and stops. The type tray and newspaper remain fixed.",
 "letterpress workshop textures","Exactly one type tray, one roller and one newspaper."),
("exactly one illustrated golf putting green with a cup hole, one illustrated flagstick standing in the cup, one illustrated golf ball resting near the rim and one illustrated putter club",
 "The gentle contour of the green and the circular cup rim are traced first, followed by the slender flagstick with its triangular flag, the dimpled sphere of the ball, and the angled head and shaft of the putter.",
 "A pale lime-green wash settles lightly on the grass, faint scarlet tints the small flag, soft white-grey colors the ball, and pale steel-grey touches the putter head.",
 "the small flag on the flagstick lifts two millimetres and settles. The green, ball and putter remain fixed.",
 "clean turf and club textures","Exactly one flagstick, one ball and one putter."),
]
S=json.loads(io.open('_작업/_scenes25.json',encoding='utf-8').read())
assert len(S)==len(D), "장면 수 불일치 %d vs %d"%(len(S),len(D))
BAN=["charcoal","sepia"," black","dark ","thick ","glossy","shadow","polished","metallic","studio","reflection"," ink ","label","border"," 3D","CGI"]
proms=[]; bad=0
for (t,el,l1,l2,ch),(sub,dr,co,mo,sy,lk) in zip(S,D):
    p=HEAD+sub+". "+DRAW_H+dr+DRAW_T+" "+COL_H+co+COL_T+" "+MOT_H+mo+MOT_T+" "+STY_H+sy+STY_T+" "+NEG+lk+NEG_T
    front=p[:p.index("No dark outline")]
    hits=[b.strip() for b in BAN if b in front.lower()]
    if hits: bad+=1; print("★ %s : %s"%(t,hits))
    proms.append((t,el,l1,l2,ch,p))
print("생성 %d장 · 금지어 충돌 %d건"%(len(proms),bad))
io.open('_작업/_proms25.json','w',encoding='utf-8').write(json.dumps(proms,ensure_ascii=False))
