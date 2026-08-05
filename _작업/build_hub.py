#!/usr/bin/env python3
# build_hub.py — 장면 제작허브 생성기 (로부장).
# scenes/*.json + 챕터별_프롬프트.html의 완성 장면을 인덱스형 단일 HTML로 굽는다.
# 사용: python3 build_hub.py  →  제작허브.html
import json
import datetime
BUILD_STAMP=datetime.datetime.now().strftime('%m-%d %H:%M')
import os
import re


scenes = []

DONE_ASSIGN={
 '빛을 보내는 등대':('1장 자연의 세계','바다와 항해·완성'),'바람을 타는 범선':('1장 자연의 세계','바다와 항해·완성'),
 '돌고래가 따라오는 배':('1장 자연의 세계','바다와 항해·완성'),'고래와 깊은 바다':('1장 자연의 세계','바다와 항해·완성'),
 '깊은 바다의 산호 협곡':('1장 자연의 세계','바다와 항해·완성'),'곶을 돌아 열리는 만':('1장 자연의 세계','바다와 항해·완성'),
 '새벽 언덕의 양떼':('2장 생명','동물과 식물·완성'),'참나무 한 그루':('2장 생명','동물과 식물·완성'),
 '사바나의 기린과 얼룩말':('2장 생명','동물과 식물·완성'),'꽃 피는 덤불과 벌레':('2장 생명','동물과 식물·완성'),
 '늪가의 개구리':('2장 생명','동물과 식물·완성'),'시골길과 열기구':('8장 도시와 문명','타고 가기·완성')}

# 1) 완성 12장면 회수
t = open('챕터별_프롬프트.html', encoding='utf-8').read()
for m in re.finditer(
    r'\{"n":"(\d+)","kr":"([^"]+)","grade":"([^"]+)","words":\[([^\]]+)\][^}]*?"prompt":"((?:[^"\\]|\\.)*)"',
    t,
):
    n, kr, gr, wr, pr = m.groups()
    words = re.findall(r'"([a-zA-Z]+)"', wr)
    prompt = pr.encode().decode('unicode_escape')
    # 기존 localStorage 판정 기록 보호: id 생성 규칙을 절대 변경하지 않는다.
    scenes.append({
        'id': '완성-' + n + '-' + kr[:6],
        'name': kr,
        '갈래': DONE_ASSIGN.get(kr,('','챕터1-2 (완성분)'))[1],
        'words': words,
        'prompt': prompt,
        'excluded': os.path.exists(os.path.join('..','public','learning','챕터1_완성동영상', (re.search(r'"file":"([^"]+)"', m.group(0)) and re.search(r'"file":"([^"]+)"', m.group(0)).group(1) or 'x') + '.mp4')),  # 실물 영상 있을 때만 제작 불필요
    })

# 2) 코덱스 장면
for fn in sorted(os.listdir('scenes')):
    if fn.endswith('.json'):
        s = json.load(open('scenes/' + fn, encoding='utf-8'))
        # 기존 localStorage 판정 기록 보호: 파일명 기반 id를 그대로 유지한다.
        s['id'] = fn.replace('.json', '')
        scenes.append(s)

groups = {}
for scene in scenes:
    groups.setdefault(scene['갈래'], []).append(scene)

# 트랙 A 9장. 대표님 확정 뒤에는 아래 챕터명 한 줄만 바꾸면 된다.
CHAPTER_MAP = {
    '1장 자연의 세계': ['바다와 항해', '하늘과 날씨', '색과 빛', '땅과 물길'],
    '2장 생명': ['동물', '식물과 나무'],
    '3장 마음의 날씨': ['기쁨과 슬픔', '화와 두려움', '부끄러움과 미움', '바람과 아쉬움', '놀람과 궁금함', '믿음과 의심', '사람 성격', '몸과 마음의 상태'],
    '4장 생각과 말': ['생각하기', '글과 기록', '배움과 가르침', '알리고 밝히기', '따지고 다투기', '묻고 부탁하기', '소리내어 말하기'],
    '5장 몸과 일상': ['몸과 감각', '옷과 몸치장', '먹을 것', '부엌과 조리', '집의 구조', '살림 도구'],
    '6장 움직임의 사전': ['손으로 하는 것', '몸 전체로 하는 것', '만들고 고치기', '하고 다루기', '가고 오기', '닫고 파묻기', '운동과 겨루기'],
    '7장 함께 사는 세상': ['사람과 관계', '주고받기', '돕고 섬기기', '규칙과 사회', '세상 물정', '일과 직업', '싸움과 지킴', '사고와 위험'],
    '8장 도시와 문명': ['돈', '사고팔기', '도시의 건물', '타고 가기', '기계와 도구', '성과 왕궁', '소리와 음악'],
    '9장 개념의 도구상자': ['크기와 모양', '좋고 나쁨', '쉽고 어려움', '같고 다름', '많고 적음', '시간과 때', '수와 셈', '자리와 방향', '일의 결과', '드러남과 감춤', '모임과 흩어짐', '갖고 지니기', '고르고 정하기', '찾고 얻기', '이음말', '정도와 범위말'],
}

chapters = []
mapped = set()
CHAPTER_MAP['1장 자연의 세계'] = ['바다와 항해·완성'] + CHAPTER_MAP.get('1장 자연의 세계', [])
CHAPTER_MAP['2장 생명'] = ['동물과 식물·완성'] + CHAPTER_MAP.get('2장 생명', [])
CHAPTER_MAP['8장 도시와 문명'] = ['타고 가기·완성'] + CHAPTER_MAP.get('8장 도시와 문명', [])
for chapter_name, branch_names in CHAPTER_MAP.items():
    chapter_groups = []
    for branch_name in branch_names:
        if branch_name in groups:
            chapter_groups.append({'name': branch_name, 'scenes': groups[branch_name]})
            mapped.add(branch_name)
    chapters.append({'name': chapter_name, 'groups': chapter_groups})

unmapped = set(groups) - mapped
if unmapped:
    raise ValueError('CHAPTER_MAP에 없는 갈래: ' + ', '.join(sorted(unmapped)))

# JSON을 HTML 안에 안전하게 넣는다. '<'를 이스케이프해 script 종료 오인도 막는다.
data_json = json.dumps(
    chapters,
    ensure_ascii=False,
    separators=(',', ':'),
).replace('<', '\\u003c')

page = f'''<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>보는 단어장 · 장면 제작허브</title><style>
:root{{--bg:#f7f4ed;--card:#fff;--line:#ded8ca;--ink:#25231f;--muted:#777;--green:#246b3b;--lime:#a8d68d;--red:#b7443e}}
*{{box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;margin:0;background:var(--bg);color:var(--ink)}}
.top{{position:sticky;top:0;background:rgba(247,244,237,.97);padding:10px 16px 8px;z-index:10;border-bottom:1px solid #e5dfd2}}
.topin,main{{max-width:900px;margin:auto}}
h1{{font-size:1.3rem;margin:0 0 8px}} h2{{font-size:1.08rem;margin:8px 0}}
#bar{{height:8px;background:#e9e7e1;border-radius:5px;overflow:hidden}}#fill{{height:100%;background:#4a90d9;width:0}}
input{{width:100%;min-height:44px;padding:10px 12px;border:1px solid #d8d4ca;border-radius:9px;margin-top:8px;font-size:16px;background:#fff}}
main{{padding:16px}}
#chapterIndex{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}
.chapter{{position:relative;min-height:130px;padding:17px 18px 15px 25px;border:1px solid #d7cfbf;border-radius:5px 15px 15px 5px;text-align:left;background:#fffdf8;color:#332f27;cursor:pointer;box-shadow:0 3px 10px #3c32210d}}
.chapter:before{{content:"";position:absolute;left:0;top:12px;bottom:12px;width:9px;border-radius:0 5px 5px 0;background:var(--tab,#ae8c64)}}
.chapter.complete{{border:2px solid #b89337;box-shadow:0 0 0 3px #ead38a55}}.chapter h3{{margin:0 0 12px;font-size:1.02rem}}.chapter .mark{{float:right;color:#9b771d}}
.stamps{{display:grid;grid-template-columns:repeat(16,1fr);gap:3px}}
.stamp{{aspect-ratio:1;border-radius:2px;background:#e7e4de;border:1px solid #ddd8cf}}
.stamp.ok{{background:var(--green);border-color:var(--green)}}.stamp.made{{background:var(--lime);border-color:#83b768}}.stamp.bad{{position:relative;background:#f2dedb}}
.stamp.bad:after{{content:"";position:absolute;width:55%;height:55%;border-radius:50%;background:var(--red);left:22%;top:22%}}
.stamp.dup{{background:repeating-linear-gradient(135deg,#999 0 2px,#eee 2px 4px);border-color:#999}}
.dupnote{{display:inline-block;margin-left:7px;padding:3px 7px;border-radius:999px;background:#e5e2dc;color:#5f5a52;font-size:.76rem;font-weight:800}}
#branchIndex,#detail{{display:none}}
#branchGrid{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}}
.chip{{min-height:76px;padding:11px;border:1px solid #d8d4ca;border-radius:12px;text-align:left;background:#ecebe7;color:#333;cursor:pointer;font-weight:700}}
.chip:hover{{transform:translateY(-1px)}}.chip small{{display:block;margin-top:7px;font-size:.78rem;font-weight:700}}
.chip.doing{{background:#fff0d5;border-color:#e8a63c}}.chip.done{{background:#dff2e1;border-color:#68a66d;color:#205d25}}
.nav{{display:flex;gap:7px;align-items:center;flex-wrap:wrap;margin-bottom:12px}}
.nav button,.btns button{{min-height:44px;padding:8px 11px;border:1px solid #ccc;border-radius:8px;background:#fff;font-size:.88rem;cursor:pointer}}
.nav h2{{flex:1;min-width:180px}}.sc{{background:#fff;border:1px solid var(--line);border-radius:9px;margin:7px 0;padding:2px 10px}}
summary{{cursor:pointer;padding:10px 0;font-size:.95rem}}.w{{color:#888;font-size:.8rem}}.st{{font-size:.8rem;font-weight:700}}
pre{{white-space:pre-wrap;background:#f6f4ef;padding:10px;border-radius:6px;font-size:.78rem;max-height:260px;overflow:auto}}
.btns{{padding-bottom:5px}}.empty{{padding:28px;text-align:center;color:var(--muted)}}
@media(max-width:640px){{#chapterIndex{{grid-template-columns:1fr}}#branchGrid{{grid-template-columns:repeat(2,minmax(0,1fr))}}main{{padding:12px}}.top{{padding:9px 12px 7px}}.chapter{{min-height:112px}}.stamps{{grid-template-columns:repeat(20,1fr);gap:2px}}.chip{{min-height:72px}}.nav button{{flex:1}}.nav h2{{order:-1;flex-basis:100%}}}}
</style></head><body>
<div class="top"><div class="topin"><h1>🎬 장면 제작허브  <small style="color:#b00;font-size:.65rem">빌드 {BUILD_STAMP} · 시각 다르면 새로고침</small><small id="cnt"></small></h1><div id="bar"><div id="fill"></div></div>
<input id="q" placeholder="단어·장면 검색 (예: voyage, 등대)" oninput="flt()"></div></div>
<main><div id="chapterIndex"></div>
<div id="branchIndex"><div class="nav"><h2 id="chapterTitle"></h2><button onclick="showChapters()">← 뒤로</button></div><div id="branchGrid"></div></div>
<div id="detail"><div class="nav"><h2 id="title"></h2>
<button onclick="showBranches(activeChapter)">← 뒤로</button><button onclick="moveGroup(-1)">이전 갈래</button><button onclick="moveGroup(1)">다음 갈래</button></div>
<div id="cards"></div></div></main>
<script>
const CHAPTERS={data_json};
const K='hub_status';let S=JSON.parse(localStorage.getItem(K)||'{{}}');
let activeChapter=-1,activeGroup=-1;
const esc=s=>String(s).replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]));
function save(){{localStorage.setItem(K,JSON.stringify(S));paint()}}
function st(id,v){{if(v)S[id]=v;else delete S[id];save()}}
function cp(id){{const p=document.getElementById(id).querySelector('pre').textContent;navigator.clipboard.writeText(p).then(()=>{{const b=document.getElementById(id).querySelector('button');b.textContent='✅ 복사됨';setTimeout(()=>b.textContent='📋 프롬프트 복사',1200)}})}}
function card(s){{const id=esc(s.id),badge=s.excluded?'<span class="dupnote">완성 · 이미 그림 있음</span>':'',actions=s.excluded?'':`<button onclick="st('${{id}}','생성완료')">🎬 생성완료</button><button onclick="st('${{id}}','합격')">✅ 합격</button><button onclick="st('${{id}}','불합격')">❌ 불합격</button><button onclick="st('${{id}}','')">↺</button>`;return `<details class="sc" id="${{id}}"><summary><b>${{esc(s.name)}}</b>${{badge}} <span class="w">${{esc(s.words.join(' · '))}}</span> <span class="st" data-id="${{id}}"></span></summary><pre>${{esc(s.prompt)}}</pre><div class="btns">${{s.excluded?'<b style="color:#a06">⛔ 제작 금지 — 사이트에 이미 완성 영상 있음 (크레딧 낭비)</b>':`<button onclick="cp('${{id}}')">📋 프롬프트 복사</button>`}}${{actions}}</div></details>`}}
const allScenes=()=>CHAPTERS.flatMap(c=>c.groups.flatMap(g=>g.scenes));
const chapterScenes=c=>c.groups.flatMap(g=>g.scenes);
const accepted=g=>g.scenes.filter(s=>S[s.id]==='합격').length;
function hideViews(){{document.getElementById('chapterIndex').style.display='none';document.getElementById('branchIndex').style.display='none';document.getElementById('detail').style.display='none'}}
function stampBoard(ss){{return `<div class="stamps" aria-label="도장판">${{ss.map(s=>{{const v=S[s.id]||'',cl=s.excluded?'dup':v==='합격'?'ok':v==='생성완료'?'made':v==='불합격'?'bad':'';return `<i class="stamp ${{cl}}" title="${{esc(s.name)}}${{s.excluded?' — 완성 · 이미 그림 있음':''}}"></i>`}}).join('')}}</div>`}}
function renderChapters(){{const colors=['#9b7653','#bc765d','#718d79','#8876a5','#b68b43','#678da2','#9a6f82','#688966','#7e7b6e','#a17a50'];document.getElementById('chapterIndex').innerHTML=CHAPTERS.map((c,i)=>{{const ss=chapterScenes(c),done=ss.length>0&&ss.every(s=>S[s.id]==='합격');return `<button class="chapter ${{done?'complete':''}}" style="--tab:${{colors[i%colors.length]}}" onclick="showBranches(${{i}})"><h3>${{esc(c.name)}}${{done?'<span class="mark">◆ 완성</span>':''}}</h3>${{stampBoard(ss)}}</button>`}}).join('')}}
function showChapters(){{activeChapter=-1;activeGroup=-1;document.getElementById('q').value='';hideViews();document.getElementById('chapterIndex').style.display='grid';renderChapters();window.scrollTo(0,0)}}
function showBranches(ci){{activeChapter=ci;activeGroup=-1;const c=CHAPTERS[ci];hideViews();document.getElementById('branchIndex').style.display='block';document.getElementById('chapterTitle').textContent=c.name;document.getElementById('branchGrid').innerHTML=c.groups.map((g,gi)=>{{const work=g.scenes.filter(s=>!s.excluded),excluded=work.length===0,n=work.filter(s=>S[s.id]==='합격').length,all=work.length,cl=excluded?'':n===0?'':n===all?'done':'doing',note=excluded?'완성 · 이미 그림 있음':`합격 ${{n}} / ${{all}}`;return `<button class="chip ${{cl}}" onclick="showGroup(${{ci}},${{gi}})">${{esc(g.name)}}<small>${{note}}</small></button>`}}).join('');window.scrollTo(0,0)}}
function showGroup(ci,gi,list=null,label=''){{activeChapter=ci;activeGroup=gi;const g=CHAPTERS[ci].groups[gi];hideViews();document.getElementById('detail').style.display='block';document.getElementById('title').textContent=label||g.name+' ('+g.scenes.length+'장면)';document.getElementById('cards').innerHTML=(list||g.scenes).map(card).join('')||'<div class="empty">검색 결과가 없습니다.</div>';paint();window.scrollTo(0,0)}}
function moveGroup(d){{if(activeChapter<0||activeGroup<0)return;const gs=CHAPTERS[activeChapter].groups;showGroup(activeChapter,(activeGroup+d+gs.length)%gs.length)}}
function flt(){{const q=document.getElementById('q').value.trim().toLowerCase();if(!q){{showChapters();return}}const hits=allScenes().filter(s=>(s.name+' '+s.words.join(' ')+' '+s.prompt).toLowerCase().includes(q));activeChapter=-1;activeGroup=-1;hideViews();document.getElementById('detail').style.display='block';document.getElementById('title').textContent='전체 검색 결과 ('+hits.length+'장면)';document.getElementById('cards').innerHTML=hits.map(card).join('')||'<div class="empty">검색 결과가 없습니다.</div>';paint()}}
function paint(){{const all=allScenes().filter(s=>!s.excluded),done=all.filter(s=>S[s.id]==='합격').length;document.getElementById('cnt').textContent=' 제작 대상 합격 '+done+' / '+all.length;document.getElementById('fill').style.width=(all.length?100*done/all.length:0)+'%';document.querySelectorAll('.sc').forEach(d=>{{const v=S[d.id]||'',e=d.querySelector('.st');e.textContent=v?'['+v+']':'';e.style.color=v==='합격'?'#2e7d32':v==='불합격'?'#c62828':'#e08a00'}});if(activeChapter<0&&!document.getElementById('q').value)renderChapters()}}
renderChapters();paint();
</script></body></html>'''

open('제작허브.html', 'w', encoding='utf-8').write(page)
print('제작허브.html 생성:', len(scenes), '장면 /', len(groups), '갈래 /', len(chapters), '챕터 카드 /', round(len(page) / 1024), 'KB')
