# -*- coding: utf-8 -*-
import subprocess, time

out_img = "_작업/ch3_11_preview.png"
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--window-size=1200,900",
    f"--screenshot={out_img}",
    "http://localhost:8088/learning/index.html?ch=3&v=3"
], capture_output=True)

print("캡처 완료:", out_img)

