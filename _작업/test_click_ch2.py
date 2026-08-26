# -*- coding: utf-8 -*-
import subprocess, time

out_img = "_작업/learning_ch2_unlocked.png"
# 챕터 2 열람 테스트
subprocess.run([
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "--headless",
    "--disable-gpu",
    "--window-size=390,844",
    f"--screenshot={out_img}",
    "http://localhost:8088/#learn"
], capture_output=True)

print("캡처 완료:", out_img)

