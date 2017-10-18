import re

t = int(input())
for _ in range(t):
    s = input().strip()
    if bool(re.match(r"[456][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$", s)) and not bool(re.search(r"(0000|1111|2222|3333|4444|5555|6666|7777|8888|9999)", s.replace("-", ""))):
        print("Valid")
    else:
        print("Invalid")
