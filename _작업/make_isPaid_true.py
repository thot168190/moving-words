# -*- coding: utf-8 -*-
with open("public/learning/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# isPaid 기본값 변경
html = html.replace("let isPaid = false;", "let isPaid = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' || localStorage.getItem('inkword_paid') === 'true' || true);")

with open("public/learning/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("isPaid = true (완전 해금) 적용 완료!")

