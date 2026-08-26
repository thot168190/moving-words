# -*- coding: utf-8 -*-
import subprocess, time

out_img = "_작업/clean_canvas_test.png"
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--window-size=1200,800",
    f"--screenshot={out_img}",
    "http://localhost:8088/#learn"
], capture_output=True)

print("클린 캔버스 캡처 완료:", out_img)

