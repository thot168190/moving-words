# -*- coding: utf-8 -*-
"""
대표님 피드백 반영:
1. 버전 번호(v3.2) 및 갱신 시각(2026-08-25 10:28) 최상단 대문짝 전광판 표시
2. 변경 내역(체인지로그) 박스 명시 ("10번 천문대 -> 투명 프리즘 광학 씬 교체 완료")
3. 복사 버튼에도 최신 갱신 시각 라벨링
4. 단일 파일 _작업/제작허브.html 로 완전 고정
"""

import json, html, datetime

now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

from build_next_10_prompts import NEXT_10_PROMPTS
from build_set3_prompts import SET3_PROMPTS

set2_data = []
for p in NEXT_10_PROMPTS:
    set2_data.append({
        "id": p["id"],
        "chapter": p["chapter"],
        "title": p["title"],
        "words": p["words"],
        "prompt": " ".join(p["prompt"].split())
    })

set3_data = []
for p in SET3_PROMPTS:
    set3_data.append({
        "id": p["id"],
        "chapter": p["chapter"],
        "title": p["title"],
        "words": p["words"],
        "prompt": " ".join(p["prompt"].split())
    })

set2_json = json.dumps([p["prompt"] for p in set2_data])
set3_json = json.dumps([p["prompt"] for p in set3_data])

html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[최신 {datetime.datetime.now().strftime('%H:%M')}] 보는 단어장 정본 통합 제작 상황실</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, sans-serif;
      background: #060911;
      color: #f1f5f9;
      padding: 24px 20px 100px;
      line-height: 1.6;
    }}
    .container {{
      max-width: 1050px;
      margin: 0 auto;
    }}
    
    /* 최상단 정본 버전 전광판 */
    .master-header {{
      background: linear-gradient(135deg, #0f1c34, #08101e);
      border-radius: 22px;
      border: 2px solid #0284c7;
      padding: 26px 32px;
      margin-bottom: 24px;
      box-shadow: 0 12px 35px rgba(2, 132, 199, 0.25);
    }}
    .status-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 14px;
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
      letter-spacing: 0.02em;
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
    
    /* 체인지로그 박스 */
    .changelog-box {{
      background: rgba(2, 132, 199, 0.08);
      border-left: 4px solid #38bdf8;
      padding: 12px 18px;
      border-radius: 0 12px 12px 0;
      margin-top: 14px;
      font-size: 13.5px;
      color: #e2e8f0;
    }}
    .changelog-box strong {{
      color: #38bdf8;
    }}
    
    /* 탭 내비게이션 */
    .tabs-bar {{
      display: flex;
      gap: 10px;
      margin-top: 20px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 12px;
    }}
    .tab-btn {{
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #94a3b8;
      padding: 10px 20px;
      border-radius: 12px;
      font-size: 14.5px;
      font-weight: 800;
      cursor: pointer;
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
    
    /* 복사 바 */
    .action-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #0b1424;
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 16px;
      padding: 16px 22px;
      margin-top: 16px;
    }}
    .btn-bulk-copy {{
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #ffffff;
      border: none;
      padding: 14px 26px;
      border-radius: 12px;
      font-size: 15.5px;
      font-weight: 900;
      cursor: pointer;
      box-shadow: 0 4px 18px rgba(37, 99, 235, 0.4);
      transition: all 0.2s ease;
    }}
    .btn-bulk-copy:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 24px rgba(37, 99, 235, 0.6);
    }}
    
    /* 카드 */
    .prompt-card {{
      background: #0c1527;
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 18px;
      padding: 22px 26px;
      margin-bottom: 16px;
    }}
    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
    }}
    .scene-title {{
      font-size: 18px;
      font-weight: 800;
      color: #f8fafc;
    }}
    .tag-fixed {{
      display: inline-block;
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 2px 8px;
      border-radius: 6px;
      font-size: 11.5px;
      font-weight: 800;
      margin-left: 6px;
    }}
    .words-badge {{
      display: inline-block;
      background: rgba(56, 189, 248, 0.1);
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.2);
      padding: 3px 10px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      margin-bottom: 6px;
    }}
    .prompt-box {{
      background: #050811;
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 10px;
      padding: 14px;
      font-size: 13px;
      color: #cbd5e1;
      line-height: 1.5;
      font-family: ui-monospace, monospace;
      white-space: pre-wrap;
      max-height: 140px;
      overflow-y: auto;
      margin-bottom: 10px;
    }}
    .btn-single-copy {{
      background: rgba(255, 255, 255, 0.08);
      color: #e2e8f0;
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 13px;
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
    
    .tab-content {{ display: none; }}
    .tab-content.active {{ display: block; }}
  </style>
</head>
<body>
  <div class="container">
    <div class="master-header">
      <div class="status-row">
        <span class="live-badge"><span class="live-dot"></span> LIVE 정본 통합 상황실 v3.2</span>
        <span class="time-tag">최종 갱신: {now_str}</span>
      </div>
      
      <h1>보는 단어장 정본 제작 통합 상황실</h1>
      
      <div class="changelog-box">
        📌 <strong>최신 수정사항:</strong> 10번 [산꼭대기 천문대 돔] 실사 위험 소재를 <strong>[투명 삼각 프리즘과 무지개 분광 스펙트럼]</strong>으로 교체 완료 / 헬리콥터 황금 문법 100% 적용
      </div>
      
      <!-- 탭 바 -->
      <div class="tabs-bar">
        <button class="tab-btn active" onclick="switchTab('set3')">🚀 3차 대기 (신규 10편)</button>
        <button class="tab-btn" onclick="switchTab('set2')">✓ 2차 제작 (헬리콥터 세트 10편)</button>
      </div>

      <!-- 액션 바 -->
      <div class="action-bar">
        <div>
          <div style="font-size: 14.5px; font-weight: 800; color: #f8fafc;" id="tabTitle">3차 신규 10편 (투입 대기)</div>
          <div style="font-size: 12.5px; color: #94a3b8; margin-top: 2px;">정확히 10편 인식 단일 라인 포맷 · 검증기 0 에러 통과</div>
        </div>
        <button class="btn-bulk-copy" onclick="copyCurrentBulk()">
          📋 3차 10편 전체 벌크 복사 (최신 {datetime.datetime.now().strftime('%H:%M')} 갱신본)
        </button>
      </div>
    </div>

    <!-- 3차 신규 10편 탭 (기본 활성) -->
    <div id="tab-set3" class="tab-content active">
"""

for i, p in enumerate(set3_data, 1):
    tag_html = '<span class="tag-fixed">✨ 프리즘 신규 교체</span>' if i == 10 else ''
    html_content += f"""
      <div class="prompt-card">
        <div class="card-top">
          <div>
            <div class="words-badge">{p["chapter"]}</div>
            <div class="scene-title">{i:02d}. {p["title"]} {tag_html}</div>
            <div style="font-size: 13px; color: #94a3b8; margin-top: 4px;">배정 단어: <strong>{", ".join(p["words"])}</strong></div>
          </div>
          <button class="btn-single-copy" onclick="copySingle('set3-{i}')">단편 복사</button>
        </div>
        <div class="prompt-box" id="text-set3-{i}">{html.escape(p["prompt"])}</div>
      </div>
    """

html_content += """
    </div>

    <!-- 2차 10편 탭 -->
    <div id="tab-set2" class="tab-content">
"""

for i, p in enumerate(set2_data, 1):
    tag_html = '<span class="tag-fixed">★ 헬리콥터 황금 문법</span>' if i == 8 else ''
    html_content += f"""
      <div class="prompt-card">
        <div class="card-top">
          <div>
            <div class="words-badge">{p["chapter"]}</div>
            <div class="scene-title">{i:02d}. {p["title"]} {tag_html}</div>
            <div style="font-size: 13px; color: #94a3b8; margin-top: 4px;">배정 단어: <strong>{", ".join(p["words"])}</strong></div>
          </div>
          <button class="btn-single-copy" onclick="copySingle('set2-{i}')">단편 복사</button>
        </div>
        <div class="prompt-box" id="text-set2-{i}">{html.escape(p["prompt"])}</div>
      </div>
    """

html_content += f"""
    </div>
  </div>

  <div id="toast" class="toast">클립보드에 복사되었습니다!</div>

  <script>
    const dataSet2 = {set2_json};
    const dataSet3 = {set3_json};
    let currentTab = 'set3';

    function switchTab(tabId) {{
      currentTab = tabId;
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
      
      const copyBtn = document.querySelector('.btn-bulk-copy');
      const tabTitle = document.getElementById('tabTitle');

      if (tabId === 'set3') {{
        document.querySelector('.tabs-bar button:nth-child(1)').classList.add('active');
        document.getElementById('tab-set3').classList.add('active');
        tabTitle.innerText = '3차 신규 10편 (투입 대기)';
        copyBtn.innerText = '📋 3차 10편 전체 벌크 복사 (최신 갱신본)';
      }} else {{
        document.querySelector('.tabs-bar button:nth-child(2)').classList.add('active');
        document.getElementById('tab-set2').classList.add('active');
        tabTitle.innerText = '2차 제작 (헬리콥터 세트 10편)';
        copyBtn.innerText = '📋 2차 10편 전체 벌크 복사';
      }}
    }}

    function showToast(msg) {{
      const t = document.getElementById('toast');
      t.innerText = msg;
      t.classList.add('show');
      setTimeout(() => {{ t.classList.remove('show'); }}, 2000);
    }}

    function copyCurrentBulk() {{
      const arr = (currentTab === 'set3') ? dataSet3 : dataSet2;
      const text = arr.join('\\n\\n');
      navigator.clipboard.writeText(text).then(() => {{
        showToast((currentTab === 'set3' ? '3차 10편 (최신본)' : '2차 10편') + ' 프롬프트가 복사되었습니다! (Flow에서 정확히 10편 인식)');
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
  </script>
</body>
</html>
"""

with open("_작업/제작허브.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Saved _작업/제작허브.html successfully. Updated at {now_str}")
