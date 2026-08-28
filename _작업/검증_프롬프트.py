#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""line-reveal 정본(MENSA 계열) 10항목 전수 검증"""
import io, json, re, sys
NEED=[
 "Cinematic progressive line-reveal animation on a solid pure bright white background, edge to edge.",
 "The very first frame is an entirely empty pure white field.",
 "no sheet, board, panel, card, mat, textured surface, visible edge or border",
 "High-key lighting.",
 "occupies the central three-quarters of the frame with equal narrow white margins on both sides",
 "Static locked-off camera, one continuous 8-second take.",
 "The only visible subjects are",
 "These are the only objects present. No people, hands, animals, signs or drawing tools appear.",
 "0-4s: soft pale silver-grey graphite strokes appear progressively",
 "Each pale silver-grey graphite line appears progressively from its own endpoint, one complete line at a time.",
 "Nothing appears through a wipe, fade or dissolve.",
 "Use only a few economical contour lines for every object. Leave most interiors as untouched white space.",
 "4-7s: an extremely pale, transparent watercolor wash develops gently inside the drawn contours.",
 "White remains clearly visible through every wash. No dark, dense or fully filled areas.",
 "7-8s:",
 "The finished composition still contains every subject listed above and nothing more",
 "The finished image reads immediately as",
 "Style: delicate fine-line editorial illustration",
 "Audio: absolutely no audio of any kind.",
 "Never: hex codes, color codes, #FFFFFF, printed text",
]
LETTER=["numbered","dial face","ledger"," menu","recipe","receipt","newspaper","type block",
        "ruled","plaque","postage","monogram","digit","inscription","engraved word"]
HEAVY=["deep ","rich ","vivid","saturated","bold ","dark ","mahogany","crimson","golden ","brass ","ochre"]
def main():
    all1200=set(open('_작업/all1200.txt',encoding='utf-8').read().split())
    s=io.open('public/learning/index.html',encoding='utf-8').read()
    i=s.index('const chapterData = {'); st=s.index('{',i); d=0
    for j in range(st,len(s)):
        if s[j]=='{': d+=1
        elif s[j]=='}':
            d-=1
            if d==0: en=j+1; break
    data=json.loads(s[st:en])
    used={a for ck in data for w in data[ck]['works'] for a,_ in w['words']}
    EXIST={"법정":"ch5_07","법봉":"ch5_07","저울":"ch5_14","현미경":"ch11_02","베틀":"ch12_06",
           "헬리콥터":"ch11_11","얼룩말":"ch2_02","모닥불":"ch12_01","온실":"ch3_15","돋보기":"ch4_06",
           "타자기":"ch4_02","독서대":"ch4_09","물레":"ch6_04","재봉틀":"ch6_05"}
    P=json.loads(io.open('_작업/_proms25.json',encoding='utf-8').read())
    fails=[];seen={}
    for i,(t,el,l1,l2,ch,p) in enumerate(P,1):
        tag="%02d %s"%(i,t)
        k=p.find("Never:"); front=p[:k].lower() if k>0 else p.lower()
        for n in NEED:
            if n not in p: fails.append("%s | 골격누락 %s"%(tag,n[:40]))
        for w in LETTER:
            if w in front: fails.append("%s | 글자소환어 %s"%(tag,w.strip()))
        m=re.search(r'4-7s: an extremely pale.*?contours\. (.*?) White remains',p,re.S)
        col=m.group(1).lower() if m else ""
        for h in HEAVY:
            if h in col: fails.append("%s | 짙은색어휘 %s"%(tag,h.strip()))
        if "Use only" not in (m.group(1) if m else ""): fails.append("%s | 색 지시에 'Use only' 없음"%tag)
        mm=re.search(r'7-8s: (.*?) All subjects remain',p,re.S)
        mot=mm.group(1).lower() if mm else ""
        for w in ["illuminates","ray of","beam of"]:
            if w in mot: fails.append("%s | 빛 연출 동작"%tag)
        for w in l1+l2:
            if w in used: fails.append("%s | 단어 이미사용 %s"%(tag,w))
            elif w not in all1200: fails.append("%s | 단어 정본밖 %s"%(tag,w))
            elif w in seen: fails.append("%s | 단어 내부중복 %s(%02d)"%(tag,w,seen[w]))
            else: seen[w]=i
        for kw,where in EXIST.items():
            if kw in t: fails.append("%s | 기존그림 중복 %s→%s"%(tag,kw,where))
        if not l1: fails.append("%s | 레벨1 없음"%tag)
    print("장면 %d · 단어 %d개"%(len(P),len(seen)))
    if fails:
        print("\n★★ %d건 — 배포 금지 ★★"%len(fails))
        for f in fails[:50]: print("  ",f)
        sys.exit(1)
    print("\n✅ 10항목 전부 통과 (line-reveal 정본)")
if __name__=="__main__": main()
