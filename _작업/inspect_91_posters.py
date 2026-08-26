# -*- coding: utf-8 -*-
import io, csv, os, glob

# 91편 목록 가져오기
with open("_작업/141편_대장.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"대장 총 {len(rows)}건")

# 91편에 대해 새파일명, 원본대표파일, 세트 등 정보 정리
clean_91 = []
for r in rows:
    mp4 = r["새파일명"]
    poster = mp4.replace(".mp4", "-poster.jpg")
    ch = r["배정챕터"]
    full_poster = os.path.join("public/learning", ch, poster)
    clean_91.append({
        "mp4": mp4,
        "ch": ch,
        "poster_path": full_poster,
        "orig_file": r["원본대표파일"],
        "set_name": r["세트"],
        "prompt_no": r["프롬프트번호"]
    })

print(f"91편 파일 수집 완료: {len(clean_91)}개")

