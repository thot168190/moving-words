# -*- coding: utf-8 -*-
import os, glob

prompt_files = glob.glob("_작업/*.txt") + glob.glob("_작업/*.json") + glob.glob("_작업/프롬프트/*.txt")
for pf in prompt_files:
    try:
        content = open(pf, "r", encoding="utf-8").read()
        if "Cinematic" in content or "watercolor" in content or "001_" in content:
            print(f"매칭 파일 발견: {pf} ({len(content.splitlines())}줄)")
    except:
        pass

