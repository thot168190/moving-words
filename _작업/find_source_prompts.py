# -*- coding: utf-8 -*-
import os, glob

files = glob.glob("_작업/*.txt") + glob.glob("_작업/프롬프트/*.txt") + glob.glob("_작업/01_지시서/*.md")
for f in files:
    print(f)

