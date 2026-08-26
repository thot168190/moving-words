# -*- coding: utf-8 -*-
"""
정본 제작 통합 마스터 허브 빌더:
- 일회용 파일 난립 100% 제거
- [1차 수확 완료 10편] / [2차 생성 10편] / [3차 신규 대기 10편] 탭으로 단일 허브 파일 (_작업/제작허브_통합.html) 일원화!
- 헬리콥터 황금 문법(Helicopter Golden Rule) 100% 적용
"""

import json, html, subprocess

# 1. 2차 10편 데이터
from build_next_10_prompts import NEXT_10_PROMPTS
set2_data = []
for p in NEXT_10_PROMPTS:
    set2_data.append({
        "id": p["id"],
        "chapter": p["chapter"],
        "title": p["title"],
        "words": p["words"],
        "prompt": " ".join(p["prompt"].split())
    })

# 2. 3차 10편 데이터 (헬리콥터 황금 문법 적용)
from build_set3_prompts import SET3_PROMPTS
set3_data = []
for p in SET3_PROMPTS:
    set3_data.append({
        "id": p["id"],
        "chapter": p["chapter"],
        "title": p["title"],
        "words": p["words"],
        "prompt": " ".join(p["prompt"].split())
    })

# 3. 텍스트 파일 단일화 (현재 Flow 투입용)
with open("_작업/google_flow_bulk_next10.txt", "w", encoding="utf-8") as f:
    for p in set3_data:
        f.write(p["prompt"] + "\n\n")

print("Saved _작업/google_flow_bulk_next10.txt successfully.")

# 4. 통합 HTML 생성
set2_json = json.dumps([p["prompt"] for p in set2_data])
set3_json = json.dumps([p["prompt"] for p in set3_data])

html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>보는 단어장 — 정본 통합 제작 상황실</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Pretendard:wght@400;600;700;900&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, sans-serif;
      background: #070a13;
      color: #f1f5f9;
      padding: 30px 20px 100px;
      line-height: 1.6;
    }}
    .container {{
      max-width: 1050px;
      margin: 0 auto;
    }}
    
    /* 상단 통합 컨트롤 패널 */
    .master-panel {{
      background: linear-gradient(135deg, #131d31, #0a1120);
      border-radius: 24px;
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 30px 36px;
      margin-bottom: 28px;
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.6);
    }}
    .panel-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 20px;
    }}
    .badge-gold {{
      background: linear-gradient(135deg, #d97706, #b45309);
      color: #ffffff;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 0.02em;
    }}
    h1 {{
      font-size: 26px;
      font-weight: 900;
      color: #ffffff;
      margin-bottom: 4px;
    }}
    .panel-sub {{
      font-size: 14px;
      color: #94a3b8;
    }}
    
    /* 탭 내비게이션 */
    .tabs-bar {{
      display: flex;
      gap: 10px;
      margin-top: 20px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 14px;
    }}
    .tab-btn {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #94a3b8;
      padding: 10px 22px;
      border-radius: 12px;
      font-size: 14.5px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .tab-btn:hover {{
      background: rgba(255, 255, 255, 0.1);
      color: #f1f5f9;
    }}
    .tab-btn.active {{
      background: #0284c7;
      border-color: #38bdf8;
      color: #ffffff;
      font-weight: 900;
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.4);
    }}
    
    /* 일괄 복사 바 */
    .action-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(56, 189, 248, 0.2);
      border-radius: 16px;
      padding: 16px 24px;
      margin-top: 18px;
    }}
    .action-info {{
      font-size: 14px;
      color: #e2e8f0;
    }}
    .action-info strong {{
      color: #38bdf8;
    }}
    .btn-bulk-copy {{
      background: linear-gradient(135deg, #0284c7, #2563eb);
      color: #ffffff;
      border: none;
      padding: 12px 24px;
      border-radius: 12px;
      font-size: 15px;
      font-weight: 800;
      cursor: pointer;
      transition: all 0.2s ease;
      box-shadow: 0 4px 15px rgba(37, 99, 235, 0.35);
    }}
    .btn-bulk-copy:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(37, 99, 235, 0.5);
    }}
    
    /* 프롬프트 카드 */
    .prompt-card {{
      background: #0f172a;
      border: 1px solid rgba(255, 255, 255, 0.07);
      border-radius: 18px;
      padding: 22px 26px;
      margin-bottom: 18px;
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
      background: #070c16;
      border: 1px solid rgba(255, 255, 255, 0.05);
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
      font-weight: 800;
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
    <div class="master-panel">
      <div class="panel-header">
        <div>
          <span class="badge-gold">★ 헬리콥터 황금 문법 표준 적용</span>
          <h1 style="margin-top: 8px;">보는 단어장 정본 통합 제작 상황실</h1>
          <p class="panel-sub">하나의 통합 상황실에서 10편씩 차수별로 즉시 복사 및 관리합니다.</p>
        </div>
      </div>
      
      <!-- 탭 바 -->
      <div class="tabs-bar">
        <button class="tab-btn active" onclick="switchTab('set3')">🚀 3차 대기 (다음 10편)</button>
        <button class="tab-btn" onclick="switchTab('set2')">✓ 2차 제작 (헬리콥터 세트 10편)</button>
      </div>

      <!-- 액션 바 -->
      <div class="action-bar">
        <div class="action-info" id="tabStatusInfo">
          현재 선택: <strong id="currentTabName">3차 신규 10편 (다음 투입용)</strong> · 정확히 10편 벌크 인식
        </div>
        <button class="btn-bulk-copy" onclick="copyCurrentBulk()">
          📋 이 탭의 10편 전체 벌크 복사
        </button>
      </div>
    </div>

    <!-- 3차 신규 10편 탭 (기본 활성) -->
    <div id="tab-set3" class="tab-content active">
"""

for i, p in enumerate(set3_data, 1):
    html_content += f"""
      <div class="prompt-card">
        <div class="card-top">
          <div>
            <div class="words-badge">{p["chapter"]}</div>
            <div class="scene-title">{i:02d}. {p["title"]}</div>
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
    html_content += f"""
      <div class="prompt-card">
        <div class="card-top">
          <div>
            <div class="words-badge">{p["chapter"]}</div>
            <div class="scene-title">{i:02d}. {p["title"]}</div>
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
      
      if (tabId === 'set3') {{
        document.querySelector('.tabs-bar button:nth-child(1)').classList.add('active');
        document.getElementById('tab-set3').classList.add('active');
        document.getElementById('currentTabName').innerText = '3차 신규 10편 (다음 투입용)';
      }} else {{
        document.querySelector('.tabs-bar button:nth-child(2)').classList.add('active');
        document.getElementById('tab-set2').classList.add('active');
        document.getElementById('currentTabName').innerText = '2차 제작 (헬리콥터 세트 10편)';
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
        showToast((currentTab === 'set3' ? '3차 10편' : '2차 10편') + ' 프롬프트가 복사되었습니다! (Flow에서 정확히 10편 인식)');
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

# 단일 정본 통합 파일로 저장
with open("_작업/제작허브.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved _작업/제작허브.html successfully.")
