#!/bin/bash
# 움직이는그림사전 · 안전 푸시
#   bash _작업/푸시.sh "커밋 메시지"
# 검증에 걸리면 멈춘다. 억지로 넘기지 말 것.

set -e
cd "$(dirname "$0")/.."

echo "════════ 1. 빌드 금지 확인 ════════"
echo "  npm run build 는 절대 돌리지 않습니다 (심사 중 · 번들 해시 변경 금지)"

echo
echo "════════ 2. dist 동기화 ════════"
cp public/learning/index.html dist/learning/index.html
echo "  public → dist 복사 완료"

echo
echo "════════ 3. 전체 검증 ════════"
if ! python3 _작업/검증_전체.py; then
  echo
  echo "  ★★ 검증에 걸렸습니다. 푸시하지 마십시오. ★★"
  echo "  위 목록을 고친 뒤 다시 실행하십시오."
  exit 1
fi

echo
echo "════════ 4. 나갈 파일 ════════"
git add -A
git status --short | head -40
N=$(git status --porcelain | wc -l | tr -d ' ')
echo "  총 $N 개"

echo
echo "════════ 5. 커밋 ════════"
MSG="${1:-fix(learning): 단어·좌표 정리 및 소챕터 탭 복구}"
git commit -m "$MSG" -m "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
echo "  커밋 완료: $MSG"

echo
echo "════════ 6. 푸시 ════════"
B=$(git rev-parse --abbrev-ref HEAD)
echo "  현재 가지: $B"
read -p "  정말 푸시합니까? (yes 입력) " OK
[ "$OK" = "yes" ] || { echo "  중단했습니다. 커밋은 남아 있습니다."; exit 0; }
git push origin "$B"
echo
echo "  ✅ 푸시 완료"
echo "  사이트를 열어 챕터1·2·3 이 정상인지 눈으로 확인하십시오."
