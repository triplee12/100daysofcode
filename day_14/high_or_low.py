#!/usr/bin/python3
"""high_or_low module"""


logo = '''high or low'''
print(logo)

high = {"me":200000, "ebuka":500000, "emmanuel":1000000}
low = {"you":100000, "emeka":400000, "colins":500000}
asked_h = {}
asked_l = {}

for h in high:
    if h not in asked_h:
        asked_h[h] =  high[h]
        print(f"Compare A: {h}")
        break
    break

vs_logo = '''Vs'''
print(vs_logo)

for l in low:
    if l not in asked_l:
        asked_l[l] = low[l]
        print(f"Against B: {l}")
        break
    break

player = input("Who has more followers? Type 'A' or 'B': ").upper()
