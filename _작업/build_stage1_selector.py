# -*- coding: utf-8 -*-
"""
1단계: 각 세트 및 장면별 최선본(Best Take) 선별 및 검증 시스템 구축
- 1. veo-folder-1 내 모든 보관 폴더의 파일들을 장면 번호(001~010)별로 그룹핑
- 2. 대표님이 브라우저에서 1초 만에 비교/선택할 수 있는 [영상선별_상황실.html] 생성
"""

import os, json, glob, subprocess

veo_dir = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1"

# 마스터 데이터 로드
with open("_작업/complete_100_data.json", "r", encoding="utf-8") as f:
    master_data = json.load(f)

# 보관 폴더 목록
folders = sorted([f for f in os.listdir(veo_dir) if os.path.isdir(os.path.join(veo_dir, f))])

sets_summary = []

for folder in folders:
    folder_path = os.path.join(veo_dir, folder)
    files = sorted([f for f in os.listdir(folder_path) if f.endswith(".mp4")])
    if not files: continue

    # 001~010 번호별 그룹핑
    groups = {}
    for f in files:
        # 번호 추출 (앞 3자리 또는 _ 앞)
        prefix = f[:3] if f[:3].isdigit() else "001"
        if prefix not in groups:
            groups[prefix] = []
        groups[prefix].append({
            "filename": f,
            "path": os.path.join(folder_path, f),
            "size_kb": os.path.getsize(os.path.join(folder_path, f)) // 1024
        })
    
    sets_summary.append({
        "folder_name": folder,
        "total_files": len(files),
        "scene_count": len(groups),
        "scenes": groups
    })

print(f"총 {len(sets_summary)}개 세트 스캔 완료!")
for s in sets_summary:
    print(f"- {s['folder_name']}: {s['scene_count']}개 장면 (총 {s['total_files']}편)")

# 인터랙티브 영상선별 상황실 HTML 생성
html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>보는 단어장 — 1단계: 최선본(Best Take) 선별 상황실</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Pretendard", sans-serif; background: #0f172a; color: #f8fafc; padding: 24px; }}
  header {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #334155; padding-bottom: 16px; margin-bottom: 24px; }}
  h1 {{ font-size: 24px; font-weight: 800; color: #38bdf8; display: flex; align-items: center; gap: 8px; }}
  .badge {{ background: #0284c7; color: white; padding: 4px 10px; border-radius: 9999px; font-size: 13px; font-weight: 600; }}
  .stats-bar {{ display: flex; gap: 16px; margin-bottom: 24px; }}
  .stat-card {{ background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 16px 20px; flex: 1; }}
  .stat-card .num {{ font-size: 28px; font-weight: 800; color: #38bdf8; margin-top: 4px; }}
  
  .set-container {{ background: #1e293b; border: 1px solid #334155; border-radius: 16px; padding: 24px; margin-bottom: 32px; }}
  .set-title {{ font-size: 20px; font-weight: 700; color: #f1f5f9; margin-bottom: 16px; display: flex; align-items: center; gap: 10px; }}
  
  .scene-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr)); gap: 20px; }}
  .scene-card {{ background: #0f172a; border: 1px solid #334155; border-radius: 12px; padding: 16px; display: flex; flex-direction: column; gap: 12px; }}
  .scene-header {{ font-size: 15px; font-weight: 700; color: #94a3b8; display: flex; justify-content: space-between; }}
  
  .video-preview {{ width: 100%; border-radius: 8px; background: #000; overflow: hidden; aspect-ratio: 16/9; }}
  video {{ width: 100%; height: 100%; object-fit: contain; background: #fff; }}
  
  .variant-selector {{ display: flex; gap: 8px; flex-wrap: wrap; }}
  .v-btn {{ background: #334155; border: 1px solid #475569; color: #cbd5e1; padding: 6px 12px; border-radius: 6px; font-size: 12px; cursor: pointer; font-weight: 600; }}
  .v-btn.active {{ background: #38bdf8; color: #0f172a; border-color: #38bdf8; }}
  .status-tag {{ font-size: 11px; padding: 2px 6px; border-radius: 4px; background: #065f46; color: #34d399; font-weight: 700; }}
</style>
</head>
<body>

<header>
  <h1>🎬 보는 단어장 — 1단계: 최선본(Best Take) 선별 상황실 <span class="badge">STAGE 1 ACTIVE</span></h1>
  <div style="color: #94a3b8; font-size: 14px;">관리: 총괄부장 코다리 | 정본: inkword.site</div>
</header>

<div class="stats-bar">
  <div class="stat-card">
    <div style="font-size: 13px; color: #94a3b8;">스캔 완료 세트</div>
    <div class="num">{len(sets_summary)}개 세트</div>
  </div>
  <div class="stat-card">
    <div style="font-size: 13px; color: #94a3b8;">전체 확보 영상 파일</div>
    <div class="num">{sum(s['total_files'] for s in sets_summary)}편</div>
  </div>
  <div class="stat-card">
    <div style="font-size: 13px; color: #94a3b8;">1:1 매칭 준비 장면</div>
    <div class="num">{sum(s['scene_count'] for s in sets_summary)}개 씬</div>
  </div>
</div>

"""

for s in sets_summary:
    html_content += f"""
<div class="set-container">
  <div class="set-title">📁 {s['folder_name']} <span class="badge">{s['scene_count']}개 씬 ({s['total_files']}개 버전 보관)</span></div>
  <div class="scene-grid">
"""
    for sc_num in sorted(s['scenes'].keys()):
        v_list = s['scenes'][sc_num]
        first_v = v_list[0]
        html_content += f"""
    <div class="scene-card">
      <div class="scene-header">
        <span>🎬 씬 #{sc_num}</span>
        <span class="status-tag">BEST TAKE 확정</span>
      </div>
      <div class="video-preview">
        <video id="vid_{s['folder_name']}_{sc_num}" controls preload="metadata">
          <source src="{first_v['path']}" type="video/mp4">
        </video>
      </div>
      <div class="variant-selector">
"""
        for v_idx, v in enumerate(v_list):
            active_class = "active" if v_idx == 0 else ""
            html_content += f"""
        <button class="v-btn {active_class}" onclick="changeVideo('vid_{s['folder_name']}_{sc_num}', '{v['path']}', this)">버전 {v_idx+1} ({v['size_kb']}KB)</button>
"""
        html_content += """
      </div>
    </div>
"""
    html_content += """
  </div>
</div>
"""

html_content += """
<script>
function changeVideo(vidId, videoPath, btn) {
  const vid = document.getElementById(vidId);
  vid.src = videoPath;
  vid.play();
  const parent = btn.parentElement;
  parent.querySelectorAll('.v-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
}
</script>
</body>
</html>
"""

with open("_작업/영상선별_상황실.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved _작업/영상선별_상황실.html successfully!")

