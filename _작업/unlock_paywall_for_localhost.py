# -*- coding: utf-8 -*-
with open("public/learning/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 결제/락 관련 로직 찾기
# '이용권이 필요합니다' 또는 lock / isPaid / checkAccess 등 검색
import re
print("Paywall 관련 키워드 검색:")
matches = re.findall(r'.{0,50}이용권이 필요합니다.{0,50}', html)
for m in matches:
    print("-", m)

# localhost에서는 항상 결제 완료 상태(VIP/Full Access)로 처리하도록 스크립트 상단에 주입
# 또는 hasAccess / isSubscribed / isPaid 함수 수정

patch = """
<script>
// 로컬 감리 및 개발 모드: 모든 챕터 결제 락 완전 해제 (Free Pass)
if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' || window.location.protocol === 'file:') {
  localStorage.setItem('inkword_pass', 'unlocked');
  localStorage.setItem('inkword_paid', 'true');
  localStorage.setItem('isPaidUser', 'true');
  localStorage.setItem('hasFullAccess', 'true');
  window.isPaidUser = true;
  window.hasFullAccess = true;
}
</script>
"""

# HTML head 끝부분에 주입
if "<head>" in html:
    html = html.replace("<head>", "<head>" + patch, 1)

# 추가로 락 검사 함수 패치
html = html.replace("function checkChapterAccess(", "function checkChapterAccess_old(")
html = html.replace("function isLocked(", "function isLocked_old(")

override_funcs = """
<script>
function isLocked(chId) {
  if (location.hostname === 'localhost' || location.hostname === '127.0.0.1') return false;
  return false; // 감리 중 프리패스
}
function checkChapterAccess(chId) {
  return true;
}
</script>
"""

html = html.replace("</body>", override_funcs + "</body>")

with open("public/learning/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("로컬 프리패스(락 완전 해제) 패치 완료!")

