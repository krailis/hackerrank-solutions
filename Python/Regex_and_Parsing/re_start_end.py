import re

s = input()
k = input()
r = re.finditer(r'(?=(' + k + '))' , s)
count = 0
for m in r:
    print((m.start(), m.start()+len(k)-1))
    count += 1
if count == 0:
    print((-1, -1))
