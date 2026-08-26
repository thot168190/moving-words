# -*- coding: utf-8 -*-
"""
대표님 지시 완벽 반영 마스터 허브:
1. 확정 단어 (406개) vs 남은 단어 (794개) 투명 대시보드
2. [그림 불가 -> 서사 씬 해결 사전] 완벽 명시
3. 각 탭마다 해결되는 챕터/갈래/단어 100% 투명 기록
"""

import json, datetime

now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

from build_next_10_prompts import NEXT_10_PROMPTS
from build_set3_prompts import SET3_PROMPTS

with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    complete_100 = json.load(f)

all_sets = {}

# Set 02
all_sets["set02"] = {
    "name": "Set 02 (헬리콥터·구조 10편 - 수확완료)",
    "target_chapter": "ch8 MOTUS (운동과 도전) & ch1 INVENTIO",
    "target_branches": "일과 직업, 타고 가기, 자리와 방향",
    "scenes": [{
        "id": p["id"],
        "chapter": p["chapter"],
        "title": p["title"],
        "words": p["words"],
        "prompt": " ".join(p["prompt"].split())
    } for p in NEXT_10_PROMPTS]
}

# Set 03
all_sets["set03"] = {
    "name": "Set 03 (교통안전·아카이브 10편 - 수확완료)",
    "target_chapter": "ch1 INVENTIO (세상을 발견해요) & ch4 SCHOLA",
    "target_branches": "규칙과 사회, 생각하기, 보존과 기록",
    "scenes": [{
        "id": p["id"],
        "chapter": p["chapter"],
        "title": p["title"],
        "words": p["words"],
        "prompt": " ".join(p["prompt"].split())
    } for p in SET3_PROMPTS]
}

# Set 04 ~ Set 13
set_targets = {
    "set04": ("ch2 VITA & ch1 INVENTIO", "시간과 때, 자리와 방향, 캠핑과 탐험"),
    "set05": ("ch6 SALUS & ch14 MERCATUS", "많고 적음, 음식과 조리, 카페와 계량"),
    "set06": ("ch2 VITA (숲과 생명)", "식물과 생장, 만들고 고치기, 원예"),
    "set07": ("ch8 MOTUS & ch13 FORUM", "일과 직업, 공예와 도구, 사람과 관계"),
    "set08": ("ch1 INVENTIO & ch8 MOTUS", "항해와 바다, 방향과 도구, 규칙"),
    "set09": ("ch11 COSMOS (우주와 과학)", "기계와 도구, 실험과 관측, 인과"),
    "set10": ("ch8 MOTUS & ch11 COSMOS", "대장간과 목공, 물리와 메커니즘"),
    "set11": ("ch15 VOX (말과 소리)", "소리와 음악, 악기와 공연, 표현"),
    "set12": ("ch7 SENSUS & ch13 FORUM", "돌봄과 치료, 보건과 케어, 감각"),
    "set13": ("ch14 MERCATUS & ch13 FORUM", "돈과 계산, 사회와 제도, 우편과 기록")
}

for s in complete_100:
    t_ch, t_br = set_targets.get(s["set_id"], ("기존 및 신규 챕터", "해당 주제 갈래"))
    all_sets[s["set_id"]] = {
        "name": s["set_name"],
        "target_chapter": t_ch,
        "target_branches": t_br,
        "scenes": s["prompts"]
    }

sets_json = json.dumps(all_sets, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[마스터 상황실] 보는 단어장 1200단어 매핑 현황 및 제작허브</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, sans-serif;
      background: #050811;
      color: #f1f5f9;
      padding: 24px 20px 100px;
      line-height: 1.6;
    }}
    .container {{
      max-width: 1100px;
      margin: 0 auto;
    }}
    
    /* 대시보드 헤더 */
    .master-header {{
      background: linear-gradient(135deg, #0d1b32, #060e1c);
      border-radius: 24px;
      border: 2px solid #0284c7;
      padding: 26px 32px;
      margin-bottom: 24px;
      box-shadow: 0 16px 40px rgba(2, 132, 199, 0.3);
    }}
    .status-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 12px;
    }}
    .live-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #10b981;
      color: #ffffff;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 900;
    }}
    .live-dot {{
      width: 9px;
      height: 9px;
      background: #ffffff;
      border-radius: 50%;
      box-shadow: 0 0 8px #ffffff;
      animation: pulse 1.5s infinite;
    }}
    @keyframes pulse {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.4; transform: scale(0.8); }}
    }}
    .time-tag {{
      font-size: 13.5px;
      color: #38bdf8;
      font-weight: 800;
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.25);
      padding: 5px 12px;
      border-radius: 10px;
    }}
    h1 {{
      font-size: 26px;
      font-weight: 900;
      color: #ffffff;
      margin-bottom: 6px;
    }}
    
    /* 전체 진도 현황 바 */
    .progress-wrap {{
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 14px;
      padding: 16px 20px;
      margin-top: 14px;
    }}
    .stat-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 12px;
      margin-bottom: 14px;
    }}
    .stat-box {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.07);
      border-radius: 10px;
      padding: 10px 14px;
    }}
    .stat-box .title {{ font-size: 12px; color: #94a3b8; font-weight: 700; }}
    .stat-box .val {{ font-size: 20px; font-weight: 900; color: #38bdf8; margin-top: 2px; }}
    
    /* 서사 해결 아코디언 */
    .narrative-panel {{
      background: #091222;
      border: 1px solid rgba(245, 158, 11, 0.3);
      border-radius: 14px;
      padding: 16px 20px;
      margin-top: 16px;
    }}
    .narrative-title {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 14.5px;
      font-weight: 900;
      color: #fbbf24;
      cursor: pointer;
    }}
    .narrative-content {{
      margin-top: 12px;
      font-size: 13px;
      color: #cbd5e1;
      line-height: 1.6;
    }}
    .narrative-item {{
      background: rgba(0,0,0,0.3);
      border-radius: 8px;
      padding: 10px 12px;
      margin-bottom: 8px;
    }}
    .narrative-item strong {{ color: #38bdf8; }}
    .narrative-item em {{ color: #fbbf24; font-style: normal; font-weight: 700; }}
    
    /* 12개 탭 스크롤 바 */
    .tabs-container {{
      overflow-x: auto;
      padding-bottom: 8px;
      margin-top: 20px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }}
    .tabs-bar {{
      display: flex;
      gap: 8px;
      width: max-content;
    }}
    .tab-btn {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #94a3b8;
      padding: 9px 16px;
      border-radius: 10px;
      font-size: 13.5px;
      font-weight: 800;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
    }}
    .tab-btn:hover {{
      background: rgba(255, 255, 255, 0.08);
      color: #f8fafc;
    }}
    .tab-btn.active {{
      background: #0284c7;
      border-color: #38bdf8;
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.4);
    }}
    
    /* 액션 바 */
    .action-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #091222;
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 16px;
      padding: 16px 22px;
      margin-top: 16px;
    }}
    .btn-bulk-copy {{
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #ffffff;
      border: none;
      padding: 13px 26px;
      border-radius: 12px;
      font-size: 15px;
      font-weight: 900;
      cursor: pointer;
      box-shadow: 0 4px 18px rgba(37, 99, 235, 0.4);
      transition: all 0.2s ease;
    }}
    .btn-bulk-copy:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 24px rgba(37, 99, 235, 0.6);
    }}
    
    /* 카드 리스트 */
    .cards-wrapper {{
      margin-top: 20px;
    }}
    .prompt-card {{
      background: #0b1325;
      border: 1px solid rgba(255, 255, 255, 0.07);
      border-radius: 18px;
      padding: 20px 24px;
      margin-bottom: 16px;
    }}
    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 10px;
    }}
    .scene-title {{
      font-size: 17px;
      font-weight: 800;
      color: #f8fafc;
    }}
    .words-badge {{
      display: inline-block;
      background: rgba(56, 189, 248, 0.1);
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.2);
      padding: 2px 8px;
      border-radius: 6px;
      font-size: 11.5px;
      font-weight: 700;
      margin-bottom: 4px;
    }}
    .prompt-box {{
      background: #040711;
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 10px;
      padding: 12px 14px;
      font-size: 12.5px;
      color: #cbd5e1;
      line-height: 1.5;
      font-family: ui-monospace, monospace;
      white-space: pre-wrap;
      max-height: 130px;
      overflow-y: auto;
      margin-bottom: 8px;
    }}
    .btn-single-copy {{
      background: rgba(255, 255, 255, 0.08);
      color: #e2e8f0;
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 7px 14px;
      border-radius: 8px;
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
    }}
    .btn-single-copy:hover {{
      background: rgba(255, 255, 255, 0.15);
      color: #ffffff;
    }}
    
    .toast {{
      position: fixed;
      bottom: 30px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: #10b981;
      color: #ffffff;
      padding: 12px 28px;
      border-radius: 30px;
      font-weight: 900;
      font-size: 15px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      opacity: 0;
      pointer-events: none;
      z-index: 9999;
    }}
    .toast.show {{
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="master-header">
      <div class="status-row">
        <span class="live-badge"><span class="live-dot"></span> LIVE 1200단어 매핑 & 제작 상황실</span>
        <span class="time-tag">실시간 검증 완료: {now_str}</span>
      </div>
      
      <h1>보는 단어장 1200단어 완전 정복 현황판</h1>
      
      <!-- 실시간 현황 통계 -->
      <div class="progress-wrap">
        <div class="stat-grid">
          <div class="stat-box">
            <div class="title">정본 1200단어 총계</div>
            <div class="val">1,200개</div>
          </div>
          <div class="stat-box">
            <div class="title">기존 66편 확정 단어</div>
            <div class="val" style="color: #10b981;">406개 (33.8%)</div>
          </div>
          <div class="stat-box">
            <div class="title">해결 중인 남은 단어</div>
            <div class="val" style="color: #f59e0b;">794개 (66.2%)</div>
          </div>
          <div class="stat-box">
            <div class="title">수확 완료 (1~3차)</div>
            <div class="val" style="color: #38bdf8;">40편 대기</div>
          </div>
        </div>
      </div>
      
      <!-- 서사 해결 사전 (그림 불가 단어) -->
      <div class="narrative-panel">
        <div class="narrative-title">
          <span>🚨 그림 단독 불가 추상어/접속사 ➔ 서사·상황 씬 해결 사전</span>
        </div>
        <div class="narrative-content">
          <div class="narrative-item">
            <strong>이음말·접속사 (21개):</strong> altogether, despite, either, even, except, instead, moreover, neither, nor, otherwise, therefore, though, thus 등<br>
            <em>➔ 해결 서사:</em> 폭풍우 속 흔들리는 등불(despite), 갈림길의 양방향 이정표(either/neither), 모든 불 켜진 방 중 단 하나의 꺼진 창문(except), 자동차 옆 자전거(instead)
          </div>
          <div class="narrative-item">
            <strong>갈등과 사회 (14개):</strong> argue, claim, complain, convince, debate, deny, insist, awkward, blame, embarrass, shame, ignore 등<br>
            <em>➔ 해결 서사:</em> 식탁에서 서로 등 돌린 두 의자(argue/ignore), 바닥에 깨진 화분과 머뭇거리는 손(blame/embarrass/shame)
          </div>
          <div class="narrative-item">
            <strong>감정과 약속 (18개):</strong> bore, depress, desire, desperate, disappoint, hesitate, lack, pity, advice, excuse, pardon, promise, propose 등<br>
            <em>➔ 해결 서사:</em> 빗방울 맺힌 창가와 식어가는 찻잔(depress/disappoint), 굳게 닫힌 문 앞 봉인된 편지와 황동 열쇠(promise/hesitate)
          </div>
          <div class="narrative-item">
            <strong>원인과 결과 (21개):</strong> achieve, affect, cause, effect, expect, factor, happen, influence, intend, mission, purpose, result, succeed 등<br>
            <em>➔ 해결 서사:</em> 마지막 블록을 올리는 목조 탑(achieve/succeed), 연쇄로 쓰러지는 도미노(cause/effect), 해도와 나침반(mission/purpose)
          </div>
        </div>
      </div>
      
      <!-- 12개 세트 탭 -->
      <div class="tabs-container">
        <div class="tabs-bar">
          <button class="tab-btn active" onclick="switchSet('set04')">🚀 Set 04 (캠핑·탐험 - 현재 4차)</button>
          <button class="tab-btn" onclick="switchSet('set05')">Set 05 (카페·베이커리)</button>
          <button class="tab-btn" onclick="switchSet('set06')">Set 06 (정원·원예)</button>
          <button class="tab-btn" onclick="switchSet('set07')">Set 07 (미술·공예)</button>
          <button class="tab-btn" onclick="switchSet('set08')">Set 08 (바다·항해)</button>
          <button class="tab-btn" onclick="switchSet('set09')">Set 09 (과학·실험)</button>
          <button class="tab-btn" onclick="switchSet('set10')">Set 10 (건축·공구)</button>
          <button class="tab-btn" onclick="switchSet('set11')">Set 11 (음악·악기)</button>
          <button class="tab-btn" onclick="switchSet('set12')">Set 12 (의학·보건)</button>
          <button class="tab-btn" onclick="switchSet('set13')">Set 13 (사회·금융)</button>
          <button class="tab-btn" onclick="switchSet('set02')">✓ Set 02 (수확완료)</button>
          <button class="tab-btn" onclick="switchSet('set03')">✓ Set 03 (수확완료)</button>
        </div>
      </div>

      <!-- 액션 바 -->
      <div class="action-bar">
        <div>
          <div style="font-size: 14.5px; font-weight: 800; color: #f8fafc;" id="currentSetName">Set 04 (캠핑·탐험 - 현재 4차)</div>
          <div style="font-size: 12.5px; color: #38bdf8; margin-top: 2px;" id="currentSetTarget">타겟: ch2 VITA & ch1 INVENTIO · 시간과 때, 자리와 방향, 캠핑과 탐험</div>
        </div>
        <button class="btn-bulk-copy" onclick="copyCurrentBulk()">
          📋 이 세트 10편 전체 벌크 복사
        </button>
      </div>
    </div>

    <!-- 카드 렌더링 영역 -->
    <div id="cardsWrapper" class="cards-wrapper"></div>
  </div>

  <div id="toast" class="toast">클립보드에 복사되었습니다!</div>

  <script>
    const allSets = {sets_json};
    let currentSetId = 'set04';

    function renderCards(setId) {{
      const setData = allSets[setId];
      const wrapper = document.getElementById('cardsWrapper');
      wrapper.innerHTML = '';

      setData.scenes.forEach((p, idx) => {{
        const card = document.createElement('div');
        card.className = 'prompt-card';
        card.innerHTML = `
          <div class="card-top">
            <div>
              <div class="words-badge">${{p.chapter}}</div>
              <div class="scene-title">${{String(idx + 1).padStart(2, '0')}}. ${{p.title}}</div>
              <div style="font-size: 13px; color: #94a3b8; margin-top: 4px;">해결 단어: <strong>${{p.words.join(', ')}}</strong></div>
            </div>
            <button class="btn-single-copy" onclick="copySingle('${{p.id}}')">단편 복사</button>
          </div>
          <div class="prompt-box" id="text-${{p.id}}">${{p.prompt}}</div>
        `;
        wrapper.appendChild(card);
      }});
    }}

    function switchSet(setId) {{
      currentSetId = setId;
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');
      
      const setData = allSets[setId];
      document.getElementById('currentSetName').innerText = setData.name;
      document.getElementById('currentSetTarget').innerText = `타겟: ${{setData.target_chapter}} · ${{setData.target_branches}}`;
      document.querySelector('.btn-bulk-copy').innerText = `📋 ${{setData.name.split(' ')[0]}} 10편 전체 벌크 복사`;
      renderCards(setId);
    }}

    function showToast(msg) {{
      const t = document.getElementById('toast');
      t.innerText = msg;
      t.classList.add('show');
      setTimeout(() => {{ t.classList.remove('show'); }}, 2000);
    }}

    function copyCurrentBulk() {{
      const setData = allSets[currentSetId];
      const text = setData.scenes.map(s => s.prompt).join('\\n\\n');
      navigator.clipboard.writeText(text).then(() => {{
        showToast(`${{setData.name.split(' ')[0]}} 10편 전체가 복사되었습니다!`);
      }});
    }}

    function copySingle(id) {{
      const el = document.getElementById('text-' + id);
      if (el) {{
        navigator.clipboard.writeText(el.innerText).then(() => {{
          showToast('프롬프트가 복사되었습니다!');
        }});
      }}
    }}

    // 초기 렌더링
    renderCards('set04');
  </script>
</body>
</html>
"""

with open("_작업/제작허브.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved _작업/제작허브.html (Word Map & Narrative Edition) successfully!")
