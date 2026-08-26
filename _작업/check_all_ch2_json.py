# -*- coding: utf-8 -*-
import subprocess, os

for i in range(14, 34):
    n_str = str(i).zfill(2)
    p = f"_작업/새편/ch2_{n_str}.json"
    res = subprocess.run(["python3", "_작업/scene_tool.py", "check", p], capture_output=True, text=True)
    out = (res.stdout + res.stderr).strip()
    if out:
        print(f"[{n_str}] {out}")
    else:
        print(f"[{n_str}] ✅ 통과")

