import re

t = int(input())
for _ in range(t):
    s = input().strip().split(" ")
    m = re.match(r'[a-z][\w\.-]+@[a-z]+\.[a-z]{1,3}$', s[1][1:len(s[1])-1])
    if bool(m):
        print(s[0], s[1])
