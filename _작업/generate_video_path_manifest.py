# -*- coding: utf-8 -*-
import os, json

veo_dir = "/Users/mihyunlee/Desktop/현재작업다운로드/veo-folder-1"

folders = sorted([f for f in os.listdir(veo_dir) if os.path.isdir(os.path.join(veo_dir, f))])

report = "# 📦 [보는 단어장] 수확 완료 전체 영상 절대 경로 및 매니페스트\n\n"
report += f"> **루트 절대 경로:** `{veo_dir}`\n"
report += f"> **총 보관 폴더:** {len(folders)}개 세트\n\n"
report += "---\n\n"

total_files = 0
for folder in folders:
    folder_path = os.path.join(veo_dir, folder)
    files = sorted([f for f in os.listdir(folder_path) if f.endswith(".mp4")])
    total_files += len(files)
    
    report += f"## 📁 {folder} (총 {len(files)}편)\n"
    report += f"- **폴더 경로:** `{folder_path}`\n\n"
    report += "| 번호 | 파일명 | 파일 크기 | 절대 경로 |\n"
    report += "| :---: | :--- | :---: | :--- |\n"
    
    for idx, f in enumerate(files):
        fpath = os.path.join(folder_path, f)
        fsize = os.path.getsize(fpath) // 1024
        report += f"| {str(idx+1).zfill(2)} | `{f}` | {fsize} KB | `{fpath}` |\n"
    
    report += "\n---\n\n"

report += f"### 🏆 전체 보관 영상 파일 총계: {total_files}편\n"

out_path = "_작업/01_지시서/수확완료_전체영상_절대경로_목록.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(report)

print(f"Manifest generated: {out_path} (총 {total_files}편)")

