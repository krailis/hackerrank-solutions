import re

n = int(input())
s = ""
for _ in range(n):
    s += input() + "\n"
m = re.findall(r'.[#]([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})', s)
for hex_code in m:
    print("#" + hex_code)
