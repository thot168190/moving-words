# -*- coding: utf-8 -*-
import io,json,collections
all1200=set(open('_작업/all1200.txt',encoding='utf-8').read().split())
s=io.open('public/learning/index.html',encoding='utf-8').read()
i=s.index('const chapterData = {'); st=s.index('{',i); d=0
for j in range(st,len(s)):
    if s[j]=='{': d+=1
    elif s[j]=='}':
        d-=1
        if d==0: en=j+1; break
data=json.loads(s[st:en])
used=set()
for ck in data:
    for w in data[ck]['works']:
        for a,_ in w['words']: used.add(a)
avail=all1200-used

# 26장 새 배정 (기존 157편 그림과 겹치지 않는 주제로 교체)
S=[
("우체국 창구","우체국 카운터·소포·우표·우편가방",["clerk","stamp","label"],["deliver","receive","transfer","reserve"]),
("응급실 앞","구급차·경광등·들것",["ambulance","alarm","accident"],["injure","hurt","medical","crisis","prevent","avoid"]),
("투표소","투표함·기표용지·도장",["vote","elect"],["public","policy","civil","citizen","standard","moral"]),
("기차역 승강장","증기기관차·철로·역 시계",["station","rail","engine"],["transport","proceed","schedule","period"]),
("박물관 전시실","유리 진열장·고대 항아리",["museum","hall"],["tradition","represent","past","century"]),
("호텔 로비","프런트 데스크·호출벨·열쇠·여행가방",["hotel","guest"],["serve","rent","charge","reserve"]),
("영화관","영사기·필름 릴·필름 띠",["cinema","studio"],["version","popular","fashion","copy","photo"]),
("옛 성","성벽·망루·왕관",["castle","palace","royal"],["cast","empire","defend","guard"]),
("감옥 창살","쇠창살·자물쇠·열쇠고리",["prison"],["crime","punish","escape","private","privacy","guilt"]),
("전화 교환대","교환기 플러그판·전선·수화기",["switch","code","click"],["connect","instant","technology","signal"]),
("제분소 맷돌","돌 맷돌·밀가루 자루·밀알",["mill","grain"],["produce","labor","manufacture","establish"]),
("소방 호스와 소화전","소화전·감긴 호스·놋쇠 노즐",["pump","hose"],["rescue","rapid","crisis","assist"]),
("발사대의 로켓","로켓·발사탑·연기",["rocket"],["launch","mission","success","advance","forward"]),
("거리 행진","깃발·악대차·나팔",["van","parade"],["excite","social","celebrate","lead"]),
("가게 계산대","금전등록기·가격표·영수증",["price","fee"],["purchase","value","worth","expense","budget"]),
("은행 창구","금고문·장부·도장",["loan","stock"],["finance","fund","loss","profit","tax","property"]),
("식당 차림표","메뉴판·조리법 수첩·양념병",["menu","recipe"],["bitter","supply","brand","guarantee"]),
("사람의 머리와 목","뇌 단면도·목·무릎 해부도",["brain","throat","knee"],["blind","breath","tear","faint","suffer"]),
("증기 압력계","압력계 눈금판·황동 밸브·배관",["monitor","gauge"],["automatic","exact","limit","maximum"]),
("석탄 광차","석탄 덩이·광차·삽",["coal"],["waste","pollute","labor","industry"]),
("가족 사진틀","타원 액자·부부 사진·반지",["twin","female","male"],["bond","relate","engage","divorce","respect","senior"]),
("광장의 군중","연단·현수막·모인 사람들",["crowd","citizen"],["protest","oppose","insist","claim","speech"]),
("군용 장비","철모·군화·수통",["military","bomb"],["enemy","threat","victim","violent","resist","harm"]),
("신문 인쇄기","활자판·인쇄기 롤러·신문 뭉치",["register","photo"],["describe","inform","mention","emphasize","quote","refer"]),
("골프 그린","골프채·공·깃대",["golf"],["champion","challenge","effort","react","risk","manage"]),
("우물과 두레박","돌 우물·두레박·도르래",["rope","bucket"],["draw","depth","supply","source"]),
]
print("=== 단어 검사 ===")
seen={}; bad=0
for idx,(t,el,l1,l2) in enumerate(S,1):
    for w in l1+l2:
        if w in used: print("  %02d ★이미사용 %s"%(idx,w)); bad+=1
        elif w not in all1200: print("  %02d ★정본밖 %s"%(idx,w)); bad+=1
        elif w in seen: print("  %02d ★내부중복 %s (%02d와)"%(idx,w,seen[w])); bad+=1
        else: seen[w]=idx
print("문제 %d건 · 소화 %d개 (L1 %d + L2 %d)"%(bad,len(seen),sum(len(a) for _,_,a,_ in S),sum(len(b) for _,_,_,b in S)))
