# -*- coding: utf-8 -*-
import io, json, re
P=json.loads(io.open('_작업/_proms25.json',encoding='utf-8').read())
# 25장 색 문장 (부분칠하기 · 흰종이 남기기 · 옅은 어휘만)
COL=[
"A pale sand wash settles lightly along selected panel edges of the wooden counter, faint blue-grey tints only the upper half of the window glass, soft biscuit touches one face of the parcel, and pale oatmeal shades the lower folds of the sack, leaving most of the white paper bare.",
"A faint grey wash settles lightly along selected panel seams of the ambulance, soft rose tints only the cross markings, pale blue touches the upper edge of the windows, and faint straw shades one side of the beacon lamp, leaving most of the white paper bare.",
"A pale biscuit wash settles lightly along selected edges of the leather case, faint cream tints only the outer paper edges, and soft grey touches one side of the desk seal, leaving most of the white paper bare.",
"A pale slate wash settles lightly along selected plate seams of the locomotive, faint steel-blue tints only the inner rail faces, and soft biscuit touches the rim of the clock casing, leaving most of the white paper bare.",
"A faint mint tint runs lightly along selected glass edges of the cabinet, pale terracotta settles only on the shoulder of the urn, and soft grey veins one side of the stone stand, leaving most of the white paper bare.",
"A pale nut-brown wash settles lightly along selected panel edges of the counter, faint straw touches only the dome of the call bell, soft biscuit tints the key tag, and pale tan shades one strap of the travel case, leaving most of the white paper bare.",
"A pale slate wash settles lightly along selected housing seams of the projector, faint straw touches only the lens rim, and soft honey tints the translucent film ribbon, leaving most of the white paper bare.",
"A pale sandstone wash settles lightly along selected stone courses of the keep, faint oak tints only the gate planks, and small points of soft rose and pale blue touch the crown jewels, leaving most of the white paper bare.",
"A pale slate wash settles lightly along selected lengths of the iron bars, faint rust specks only at the joint collars, and soft grey tints one face of the padlock, leaving most of the white paper bare.",
"A pale olive wash settles lightly along selected panel edges of the switchboard, faint straw touches only the socket rims, and soft slate-blue tints the braided cord, leaving most of the white paper bare.",
"A pale grey wash settles lightly along selected grooves of the mill stone, faint cream tints only the spilled flour, and soft honey touches the handle of the wooden scoop, leaving most of the white paper bare.",
"A pale rose wash settles lightly along selected ridges of the hydrant, faint oatmeal tints only the outer hose coil, and soft straw touches the tip of the nozzle, leaving most of the white paper bare.",
"A pale ivory wash settles lightly along selected hull panels of the rocket, faint apricot bands only at the stage joints, and soft grey tints one side of the lattice tower, leaving most of the white paper bare.",
"A pale sky-blue wash settles lightly along selected side panels of the van, faint straw touches only the flared bell of the horn, and soft rose tints the lower edge of the bunting, leaving most of the white paper bare.",
"A pale bronze-grey wash settles lightly along selected mouldings of the register, faint cream tints only the curled receipt, and soft biscuit touches one corner of the price tag, leaving most of the white paper bare.",
"A pale graphite wash settles lightly along selected rings of the vault door, faint sage tints only the ledger cover, and soft straw touches the rim of the coin stack, leaving most of the white paper bare.",
"A pale pine wash settles lightly along selected frame edges of the menu board, faint sage fills only the board panel, soft cream tints the notebook pages, and pale honey touches the necks of the bottles, leaving most of the white paper bare.",
"A pale dusty-rose wash settles lightly along selected folds of the brain section, faint beige tints only the skin contour, and soft ivory touches the upper bones of the knee joint, leaving most of the white paper bare.",
"A pale straw wash settles lightly along selected bezel edges of the gauge, faint cream fills only the dial face, and soft slate tints one side of the pipe elbow, leaving most of the white paper bare.",
"A pale slate wash settles lightly along selected facets of the coal lumps, faint iron-brown tints only the cart panel seams, and soft grey touches the rails and shovel blade, leaving most of the white paper bare.",
"A pale nut-brown wash settles lightly along selected carvings of the oval frame, faint umber tints only the portrait silhouettes, and soft straw touches the rims of the locket and rings, leaving most of the white paper bare.",
"A pale sandstone wash settles lightly along selected paving joints of the square, faint cream tints only the banner cloth, and soft muted blue and rose touch the small standing figures, leaving most of the white paper bare.",
"A pale olive wash settles lightly along selected panels of the helmet, faint brown tints only the boot laces and sole, and soft khaki touches the webbing strap of the canteen, leaving most of the white paper bare.",
"A pale slate wash settles lightly along selected rows of the metal type blocks, faint honey tints only the roller handle, and soft cream touches the folded newspaper edge, leaving most of the white paper bare.",
"A pale sage wash settles lightly along selected contours of the putting green, faint rose tints only the small flag, soft grey touches one side of the ball, and pale steel shades the putter head, leaving most of the white paper bare.",
]
assert len(COL)==len(P)
NEW=[]
for (t,el,l1,l2,ch,p),c in zip(P,COL):
    p2=re.sub(r'(3\.5-5\.5s: clear transparent watercolor develops in layered color\. ).*?( Every wash stays pale)',
              lambda m: m.group(1)+c+m.group(2), p, flags=re.S)
    # 07 illustrated 보강
    p2=p2.replace("with two spoked reels, one illustrated lens barrel","with exactly two illustrated spoked reels, one illustrated lens barrel")
    NEW.append((t,el,l1,l2,ch,p2))
io.open('_작업/_proms25.json','w',encoding='utf-8').write(json.dumps(NEW,ensure_ascii=False))
print("색 문장 %d장 교체 완료"%len(NEW))
