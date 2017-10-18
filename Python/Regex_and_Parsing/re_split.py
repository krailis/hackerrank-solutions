import re

s = input()
l = re.split("[,\.]", s)
l = [x for x in l if len(x) >= 1]
for x in l:
    print(x)
