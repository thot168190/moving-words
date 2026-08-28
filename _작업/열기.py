# -*- coding: utf-8 -*-
import subprocess, time, os, webbrowser, http.server, socketserver, threading

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = 8088

# Check if port 8088 is already active
def is_port_open(port):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

if not is_port_open(PORT):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=os.path.join(ROOT, "public"), **kwargs)
            
    def start_server():
        socketserver.TCPServer.allow_reuse_address = True
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            httpd.serve_forever()
            
    t = threading.Thread(target=start_server, daemon=True)
    t.start()
    time.sleep(1)

# 1. Open the Visual Spot Inspector
inspector_path = os.path.join(ROOT, "_작업/신규주입_실물감리관.html")
print(f"Opening Inspector: {inspector_path}")
subprocess.run(["open", inspector_path])

# 2. Open the real Learning App at Chapter 1
learning_url = f"http://localhost:{PORT}/learning/index.html#ch1"
print(f"Opening Real App: {learning_url}")
subprocess.run(["open", learning_url])

print("✅ 브라우저 오픈 완료!")
