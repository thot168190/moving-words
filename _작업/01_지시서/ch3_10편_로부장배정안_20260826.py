# -*- coding: utf-8 -*-
import io, json, shutil, datetime
P='public/learning/index.html'
s=io.open(P,encoding='utf-8').read()
i=s.index('const chapterData = {'); st=s.index('{',i); d=0
for j in range(st,len(s)):
    if s[j]=='{': d+=1
    elif s[j]=='}':
        d-=1
        if d==0: en=j+1; break
data=json.loads(s[st:en])

# 그림을 직접 열어 확인한 배정 (정본 1200 내 · 그림에 보이는 것만)
NEW={
"11":{"title":"화분 속 새싹","sub":"흙에서 자라나는 초록 잎",
 "L1":[["shape","모양새",[38,62]],["single","한 포기",[37,22]],["extend","뻗어나가다",[60,35]],["contain","담고 있다",[33,44]]],
 "L2":[["alive","살아 있는",[39,12]],["breathe","숨 쉬다",[51,30]],["develop","자라나다",[56,55]]]},
"12":{"title":"물뿌리개와 모종삽","sub":"흙을 고르는 두 연장",
 "L1":[["tool","연장",[33,55]],["handle","손잡이",[68,72]],["dig","파다",[69,45]],["operate","다루다",[32,25]]],
 "L2":[]},
"13":{"title":"유리 온실 병","sub":"유리 안에 담긴 작은 뜰",
 "L1":[["triangle","세모",[47,17]],["volume","부피",[67,40]],["empty","비어 있는",[31,30]],["include","함께 들어 있다",[50,75]]],
 "L2":[["remain","그대로 있다",[45,50]]]},
"14":{"title":"꽃가위와 라벤더","sub":"한 줄기를 골라 자르다",
 "L1":[["pair","한 쌍",[30,28]],["piece","조각",[65,32]],["divide","가르다",[64,62]],["snap","싹둑 자르다",[29,50]]],
 "L2":[["remove","쳐내다",[50,72]],["bend","휘다",[50,22]]]},
"15":{"title":"그루터기 위 새집","sub":"나무 밑동에 앉은 작은 집",
 "L1":[["frame","뼈대",[30,60]],["block","토막",[47,82]],["settle","자리 잡다",[46,46]]],
 "L2":[["survive","견디어 내다",[45,25]]]},
"16":{"title":"바구니에 담은 가을","sub":"호박과 보리 이삭",
 "L1":[["bunch","다발",[67,28]],["mass","덩어리",[60,70]],["plenty","넉넉함",[33,68]],["several","여럿의",[84,40]]],
 "L2":[["gain","거두다",[36,44]]]},
"17":{"title":"꽃을 누르는 나무틀","sub":"네 귀를 조여 말리다",
 "L1":[["square","네모",[45,87]],["link","잇는 쇠",[61,17]],["shut","꽉 닫다",[61,75]],["bind","묶어 두다",[24,17]]],
 "L2":[["constant","변함없는",[43,47]],["maintain","그대로 지키다",[30,62]]]},
"18":{"title":"외발 손수레","sub":"바퀴 하나로 나르다",
 "L1":[["wide","넓은",[47,33]],["step","발판",[33,70]],["roll","구르다",[61,63]],["drag","끌다",[12,26]]],
 "L2":[["force","밀어붙이는 힘",[25,40]],["shift","옮기다",[50,45]]]},
"19":{"title":"유리로 지은 온실","sub":"빛을 들이는 집",
 "L1":[["grand","웅장한",[30,40]],["upper","위쪽의",[44,11]],["internal","안쪽의",[50,47]]],
 "L2":[["raise","높이다",[58,25]]]},
"20":{"title":"울타리 앞 해바라기","sub":"고르게 늘어선 씨앗",
 "L1":[["regular","고르게 늘어선",[44,42]],["combine","엇갈려 짜이다",[30,72]],["gorgeous","눈부신",[45,13]],["super","아주 큰",[28,30]]],
 "L2":[["continue","계속 자라다",[44,75]]]},
}

ch=data["3"]
idx={w["n"]:k for k,w in enumerate(ch["works"])}
changed=0
for n,spec in NEW.items():
    if n not in idx:
        print("!! ch3_%s 없음" % n); continue
    k=idx[n]
    L1=spec["L1"]; L2=spec["L2"]
    ch["works"][k]["title"]=spec["title"]
    ch["works"][k]["sub"]=spec["sub"]
    ch["works"][k]["words"]=[[w,m] for w,m,_ in L1]+[[w,m] for w,m,_ in L2]
    ch["levelOneWords"][k]=[[w,m] for w,m,_ in L1]
    ch["levelTwoWords"][k]=[[w,m] for w,m,_ in L2]
    ch["levelOneSpots"][k]=[sp for _,_,sp in L1]
    ch["sceneSpots"][k]=[sp for _,_,sp in L2]
    changed+=1

# 5배열 길이 검사
for k,w in enumerate(ch["works"]):
    a=len(ch["levelOneWords"][k]); b=len(ch["levelOneSpots"][k])
    c=len(ch["levelTwoWords"][k]); e=len(ch["sceneSpots"][k])
    if a!=b or c!=e:
        print("!! 길이불일치 ch3_%s L1 %d/%d L2 %d/%d" % (w["n"],a,b,c,e))

shutil.copy(P, P+'.bak_'+datetime.datetime.now().strftime('%m%d_%H%M'))
out=s[:st]+json.dumps(data,ensure_ascii=False,indent=2)+s[en:]
io.open(P,'w',encoding='utf-8').write(out)
print("교체 %d편 완료" % changed)
