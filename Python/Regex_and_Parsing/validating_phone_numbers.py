import re

t = int(input())
for _ in range(t):
    s = input()
    m = re.match(r'[789][0-9]{9}$', s)
    if bool(m):
        print('YES')
    else:
        print('NO')
