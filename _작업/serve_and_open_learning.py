# -*- coding: utf-8 -*-
import subprocess, time, os, webbrowser

# 1. 간단한 로컬 웹서버 백그라운드 구동 (동영상/포스터 CORS 및 범위 요청 지원을 위해)
# 포트 8080 또는 3000 사용
import http.server, socketserver, threading

PORT = 8088
DIRECTORY = "public"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

# 백그라운드 스레드로 서버 시작
t = threading.Thread(target=start_server, daemon=True)
t.start()

# 2. 브라우저에서 ch2가 바로 열리도록 URL 오픈
url = f"http://localhost:{PORT}/learning/index.html#ch2"
print(f"Opening {url} ...")
subprocess.run(["open", url])

# 파일 자체도 open
subprocess.run(["open", "public/learning/index.html"])

time.sleep(2)
print("브라우저 실물 오픈 완료!")
