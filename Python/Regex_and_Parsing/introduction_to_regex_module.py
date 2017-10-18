import re

t = int(input())
for _ in range(t):
    s = input()
    print(bool(re.match(r"[+-]?[0-9]{0,}\.[0-9]+$", s)))
