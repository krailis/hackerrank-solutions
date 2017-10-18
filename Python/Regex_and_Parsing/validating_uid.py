import re

t = int(input())
for _ in range(t):
    s = input()
    letters = re.findall(r'[a-zA-Z]', s)
    numbers = re.findall(r'\d', s)
    llen, nlen, lset_let, lset_num, slen = len(letters), len(numbers), len(set(letters)), len(set(numbers)), len(s)
    if (lset_let == llen >= 2 and lset_num == nlen >= 3 and len(s) == 10 and llen + nlen == 10):
        print("Valid")
    else:
        print("Invalid")
