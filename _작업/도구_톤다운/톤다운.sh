#!/bin/bash
# 보는 단어장 — 장면 영상 일괄 톤다운 (로부장, 2026-08-01 / 검증: ffmpeg eq 필터)
# 사용법: 이 파일이 있는 폴더에 mp4들을 넣고 실행 → 톤다운완성/ 에 결과 생성
# 강도 조절: SAT(채도) 0.75=많이 연하게 ~ 0.85=살짝 / GAMMA 1.03=아주 살짝 밝게
SAT=0.80
GAMMA=1.03
cd "$(dirname "$0")"
mkdir -p 톤다운완성
count=0
for f in *.mp4; do
  [ -e "$f" ] || continue
  ffmpeg -i "$f" -vf "eq=saturation=${SAT}:gamma=${GAMMA}" -c:v libx264 -crf 18 -preset medium -movflags +faststart -an -y "톤다운완성/$f" -loglevel error
  count=$((count+1)); echo "✓ $f"
done
echo "완료: ${count}개 → 톤다운완성/"
