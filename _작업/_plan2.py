# -*- coding: utf-8 -*-
import io,json
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

S=[
("우체국 창구","우체국 카운터·소포·우표·우편가방",["clerk","stamp","label"],["deliver","receive","transfer","offer"],"ch5"),
("응급실 앞","구급차·경광등·들것",["ambulance","alarm","accident"],["injure","hurt","medical","crisis","prevent","avoid"],"ch6"),
("변호사 사무실","서류가방·만년필 놓인 책상·서류철",["lawyer","client"],["justice","civil","policy","moral","standard","private"],"ch4"),
("기차역 승강장","증기기관차·철로·역 시계",["station","rail","engine"],["transport","proceed","schedule","period"],"ch5"),
("박물관 전시실","유리 진열장·고대 항아리",["museum","hall"],["tradition","represent","past","familiar"],"ch4"),
("호텔 로비","프런트 데스크·호출벨·열쇠·여행가방",["hotel","guest"],["serve","rent","charge","reserve"],"ch5"),
("영화관","영사기·필름 릴·필름 띠",["cinema","studio","photo"],["version","popular","fashion","copy"],"ch4"),
("옛 성","성벽·망루·왕관",["castle","palace","royal"],["cast","capital","chief"],"ch11"),
("감옥 창살","쇠창살·자물쇠·열쇠고리",["prison"],["crime","punish","privacy","discipline","innocent"],"ch4"),
("전화 교환대","교환기 플러그판·전선·수화기",["switch","code","click"],["instant","technology","automatic","rapid"],"ch6"),
("제분소 맷돌","돌 맷돌·밀가루 자루·나무 삽",["mill"],["produce","labor","manufacture","establish","industry"],"ch6"),
("소화전과 펌프","소화전·감긴 관·놋쇠 손잡이",["pump"],["assist","favor","recover","react"],"ch6"),
("발사대의 로켓","로켓·발사탑·연기",["rocket"],["mission","success","advance","forward"],"ch11"),
("거리 행진","깃발·악대차·나팔",["van","parade"],["excite","social","boom","lead"],"ch5"),
("가게 계산대","금전등록기·가격표·영수증",["price","fee"],["purchase","value","worth","expense","budget"],"ch7"),
("은행 창구","금고문·장부·도장",["loan","stock"],["finance","fund","loss","profit","tax","property"],"ch7"),
("식당 차림표","메뉴판·조리법 수첩·양념병",["menu","recipe"],["bitter","supply","brand","guarantee"],"ch7"),
("사람의 머리와 목","뇌 단면도·목·무릎 해부도",["brain","throat","knee"],["blind","breath","tear","faint","suffer"],"ch8"),
("증기 압력계","압력계 눈금판·놋쇠 밸브·배관",["monitor"],["limit","maximum","range","slight"],"ch6"),
("석탄 광차","석탄 덩이·광차·삽",["coal"],["waste","pollute","weigh","dozen"],"ch10"),
("가족 사진틀","타원 액자·부부 사진·반지",["twin","female","male"],["bond","relate","engage","divorce","respect","senior"],"ch9"),
("광장의 군중","연단·현수막·모인 사람들",["crowd","citizen"],["protest","oppose","insist","claim","speech","public"],"ch9"),
("군용 장비","철모·군화·수통",["military","bomb"],["enemy","threat","victim","violent","resist","harm"],"ch4"),
("신문 인쇄기","활자판·인쇄기 롤러·신문 뭉치",["register"],["inform","mention","emphasize","quote","refer","remark"],"ch12"),
("골프 그린","골프채·공·깃대",["golf"],["champion","challenge","effort","risk","manage"],"ch8"),
]
seen={}; bad=[]
for idx,(t,el,l1,l2,ch) in enumerate(S,1):
    for w in l1+l2:
        if w in used: bad.append("%02d 이미사용 %s"%(idx,w))
        elif w not in all1200: bad.append("%02d 정본밖 %s"%(idx,w))
        elif w in seen: bad.append("%02d 내부중복 %s(%02d)"%(idx,w,seen[w]))
        else: seen[w]=idx
for b in bad: print("  ★",b)
print("\n문제 %d건 · 장면 %d · 소화 %d개"%(len(bad),len(S),len(seen)))
if not bad:
    io.open('_작업/_scenes25.json','w',encoding='utf-8').write(json.dumps(S,ensure_ascii=False))
    print("확정 저장 → _작업/_scenes25.json")
