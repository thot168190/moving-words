# -*- coding: utf-8 -*-
import os, glob

files = glob.glob("_작업/*단어*.csv") + glob.glob("_작업/*뜻*.csv") + glob.glob("_작업/*.json") + glob.glob("_작업/*1200*")
for f in files:
    print(f)

