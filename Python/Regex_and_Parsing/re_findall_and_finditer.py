import re

s = input()
m = re.findall(r'(?=([^AEIOUaeiou\s+-][AEIOUaeiou]{2,}[^AEIOUaeiou\s+-]))', s)
if not m:
    print(-1)
else:
    for x in m:
        print(x[1:len(x)-1])
