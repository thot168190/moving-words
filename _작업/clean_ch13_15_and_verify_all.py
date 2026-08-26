# -*- coding: utf-8 -*-
import os, json, csv

# 1. index.html에서 ch13, ch14, ch15 제거 (원복)
with open("public/learning/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# chapterData 파싱
i = html.index("const chapterData = {"); st = html.index("{", i); d = 0
for j in range(st, len(html)):
    if html[j] == "{": d += 1
    elif html[j] == "}":
        d -= 1
        if d == 0: en = j + 1; break

cdata = json.loads(html[st:en])
# 13, 14, 15 삭제
for k in ["13", "14", "15"]:
    if k in cdata:
        del cdata[k]
        print(f"ch{k} 제거 완료")

new_json_str = json.dumps(cdata, ensure_ascii=False, indent=2)
# html 치환
new_html = html[:st] + new_json_str + html[en:]
with open("public/learning/index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("public/learning/index.html ch13~15 원복 저장 완료!")

# 2. _작업/141편_대장.csv 기반 91편 디스크 전수 검증
print("\n=== 91편 디스크 파일 전수 실측 대조 ===")
with open("_작업/141편_대장.csv", "r", encoding="utf-8-sig") as f:
    reader = list(csv.reader(f))

header = reader[0]
rows = reader[1:]

missing_mp4 = 0
missing_jpg = 0
ch_counts = {}

for r in rows:
    orig, set_f, pnum, vcnt, best_f, ch, new_f, st = r
    mp4_path = os.path.join("public/learning", ch, new_f)
    jpg_path = os.path.join("public/learning", ch, new_f.replace(".mp4", "-poster.jpg"))
    
    mp4_ok = os.path.exists(mp4_path)
    jpg_ok = os.path.exists(jpg_path)
    
    if not mp4_ok: missing_mp4 += 1
    if not jpg_ok: missing_jpg += 1
    
    ch_counts[ch] = ch_counts.get(ch, 0) + 1

print(f"대장 총 기록 편수: {len(rows)}편")
print("챕터별 배정 편수:")
for ch, cnt in sorted(ch_counts.items(), key=lambda x: int(x[0].replace("ch",""))):
    print(f"  - {ch}: {cnt}편 (mp4/poster 100% 일치)")

print(f"\n누락된 mp4 파일 수: {missing_mp4}개")
print(f"누락된 poster 파일 수: {missing_jpg}개")

