#!/usr/bin/env python3
# qc_scene.py v2 — 장면 프롬프트 기계 검문소 (로부장 작성, 수정 금지)
# v2 (2026-07-30): 코다리 우회 사고 후 4개 검사 추가 — 한글 금지 / 템플릿 문구 금지 / 단어 재사용 금지 / 피사체 문장 중복 금지
import sys, os, json, csv, re
from collections import Counter
HERE=os.path.dirname(os.path.abspath(__file__))
HEAD="Cinematic progressive pencil-and-ink line animation on a solid pure bright white background, edge to edge. The very first frame is an entirely empty white field. Static locked-off camera, one continuous 8-second take."
STYLE="beautiful illustrated atlas for curious teenagers, never a kindergarten picture book"
NEVER="Never: text, letters, numbers, hashtags, watermarks, a visible drawing hand, pen, pencil or brush in frame, primary crayon colors, muted grey or slate mood, sepia, ink-wash painting mood, fog, smiling sun, V-shaped birds, rainbows, dense cross-hatching, engraving-style shading, heavy dark outlines, dead-center composition, paint splatter, color outside the lines, paper texture, visible paper grain, window light streaks, ambient room shadows, vignette, camera movement, cuts, dissolve"
BAN=["sepia","ink-wash","muted grey","slate","fog","mist","gloomy","somber","cartoon","anime","photoreal","9:16","vertical","rainbow","smiling sun"]
TPL=["main scene depicting","subtle accents","cropped border element","detailed middleground scenery","generic","placeholder"]
import re as _re4
def _norm4(line, words):
    for w in sorted(words, key=len, reverse=True):
        line=_re4.sub(r"\b"+_re4.escape(w)+r"\b","W",line,flags=_re4.I)
    line=_re4.sub(r"\d+","N",line)
    return _re4.sub(r"\s+"," ",line.strip())
lvl={}
for r in csv.reader(open(os.path.join(HERE,"1200_레벨태그_v3.csv"),encoding="utf-8")):
    if r and r[0]!="단어": lvl[r[0].lower()]=r[2]

# === v3 추가 (2026-07-30 코다리 2차 사고 후): 갈래 무결성 + 골조 복제 ===
import json as _j, re as _re, os as _os
def _v3(d, scenes):
    from collections import Counter
    cls=_j.load(open(_os.path.join(HERE,"1200_분류.json"),encoding="utf-8"))["갈래"]
    cmap={}
    for g,ws in cls.items():
        for w in ws: cmap[w.lower()]=g
    skel=Counter(); skel_of={}
    out={}
    for s in scenes:
        e=[]
        g=s.get("갈래","")
        if g not in cls: e.append("갈래 불명(65갈래 아님): "+str(g)[:20])
        else:
            W=[w.lower() for w in s["words"]]
            guest=[w for w in W if cmap.get(w)!=g]
            if len(guest)>2 and 'guest' not in _wv(s['_fn']): e.append("갈래 밖 단어 %d개(허용 2): "%len(guest)+",".join(guest[:5]))
        if _re.search(r"scene\s*\d+", s["prompt"], _re.I):
            out.setdefault(s["_fn"],[]).append("프롬프트 안 장면 번호(유니크 해킹)")
        keys=[]
        m=_re.search(r"The subjects?:\s*([^\n]+)", s["prompt"])
        if m: keys.append("S:"+_norm4(m.group(1), s["words"]))
        m2=_re.search(r"5\.5-8s?:\s*([^\n]+)", s["prompt"])
        if m2: keys.append("M:"+_norm4(m2.group(1), s["words"]))
        for k in keys: skel[k]+=1
        skel_of[s["_fn"]]=keys
        if e: out[s["_fn"]]=e
    for s in scenes:
        for k in skel_of.get(s["_fn"],[]):
            if skel[k]>1:
                out.setdefault(s["_fn"],[]).append(("피사체" if k.startswith("S:") else "움직임")+" 문장 골조가 타 장면과 동일(매드립스)")
                break
    return out


# === 재편성 특례 (2026-08-01 대표님 승인 재편성표 — 자투리_재편성표_로부장확정안.md) ===
WAIVE={'056':{'ratio'},'146':{'ratio','guest'},'137':{'ratio'},'148':{'ratio'},'154':{'ratio'},'133b':{'guest','ratio','count'},'054':{'guest'},'134':{'count','ratio'},'138':{'ratio','guest'},'139':{'ratio'},'146':{'ratio','guest'},'152':{'ratio'},'153':{'guest'},'133':{'guest'}}
def _wv(fn):
    import re as _r
    m=_r.match(r'scene_(\w+?)_', fn)
    return WAIVE.get(m.group(1), set()) if m else set()

d=sys.argv[1]
word_use=Counter(); subj=Counter(); scenes=[]
for fn in sorted(os.listdir(d)):
    if fn.endswith(".json"):
        s=json.load(open(os.path.join(d,fn),encoding="utf-8")); s["_fn"]=fn; scenes.append(s)
        for w in s["words"]: word_use[w.lower()]+=1
        m=re.search(r"The subjects?:\s*([^\n]+)", s["prompt"])
        if m: subj[m.group(1).strip()[:100]]+=1
fails=0
_v3errs=_v3(d, scenes)
for s in scenes:
    errs=[]; W=[w.lower() for w in s["words"]]; p=s["prompt"]
    bad=[w for w in W if w not in lvl]
    if bad: errs.append("정본 밖 단어: "+",".join(bad))
    if not (5<=len(W)<=10) and 'count' not in _wv(s['_fn']): errs.append("단어 수 %d (5~10)"%len(W))
    l2=sum(1 for w in W if lvl.get(w)=="레벨2")
    if W and l2/len(W)<0.33 and 'ratio' not in _wv(s['_fn']): errs.append("레벨2 %d/%d (<1/3)"%(l2,len(W)))
    reuse=[w for w in W if word_use[w]>1]
    if reuse: errs.append("단어 재사용(장면 간 중복): "+",".join(sorted(set(reuse))))
    if re.search(r"[가-힣]", p): errs.append("프롬프트 안 한글")
    hits_t=[t for t in TPL if t in p]
    if hits_t: errs.append("복붙 템플릿 문구: "+",".join(hits_t))
    m=re.search(r"The subjects?:\s*([^\n]+)", p)
    if not m: errs.append("피사체 문장(The subjects:) 없음")
    elif subj[m.group(1).strip()[:100]]>1: errs.append("피사체 문장이 다른 장면과 동일")
    if HEAD not in p: errs.append("HEAD 불일치")
    if STYLE not in p: errs.append("STYLE 누락")
    if NEVER not in p: errs.append("NEVER 불일치")
    hits=[b for b in BAN if b in p.lower().replace(NEVER.lower(),"")]
    if hits: errs.append("금지어: "+",".join(hits))
    if not re.search(r"5\.5-8", p): errs.append("움직임 구간 누락")
    errs+= _v3errs.get(s["_fn"],[])
    if errs: fails+=1; print("[반려]", s["_fn"], "→", " / ".join(errs))
    else: print("[통과]", s["_fn"], "| 레벨2 %d/%d"%(l2,len(W)))
print("\n=== 결과: %d/%d 통과, %d 반려 ==="%(len(scenes)-fails,len(scenes),fails))
sys.exit(1 if fails else 0)
