import re

n = int(input())
for _ in range(n):
    s = input()
    sub_and, prev = re.sub(r"\s&&\s", " and ", s), ""
    while (prev != sub_and):
        prev = sub_and
        sub_and = re.sub(r"\s&&\s", " and ", sub_and)
    sub_or, prev = re.sub(r"\s\|\|\s", " or ", sub_and), ""
    while (prev != sub_or):
        prev = sub_or
        sub_or = re.sub(r"\s\|\|\s", " or ", sub_or)
    print(sub_or)
