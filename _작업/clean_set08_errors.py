# -*- coding: utf-8 -*-
with open("_작업/replace_set08_to_weather_transport.py", "r", encoding="utf-8") as f:
    code = f.read()

code = code.replace("spade hands", "indicator pointers")
code = code.replace("hands", "pointers")
code = code.replace("Roman numerals", "geometric hour markers")
code = code.replace("bike frame", "bike chassis")
code = code.replace("diamond frame tubes", "diamond chassis tubes")

with open("_작업/replace_set08_to_weather_transport.py", "w", encoding="utf-8") as f:
    f.write(code)

