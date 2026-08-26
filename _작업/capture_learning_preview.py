# -*- coding: utf-8 -*-
import subprocess, time

# Chrome으로 390px 캡처 시도 (헤드리스)
out_img = "_작업/learning_preview_390.png"
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--window-size=390,844",
    f"--screenshot={out_img}",
    "http://localhost:8088/learning/index.html"
], capture_output=True)

print("캡처 완료:", out_img)

