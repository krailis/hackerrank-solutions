import sys
from collections import Counter

if __name__ == "__main__":
    s = input().strip()
    c = sorted(Counter(s).most_common())
    c = sorted(c, key=lambda el: el[0])
    c = sorted(c, key=lambda el: el[1], reverse=True)
    print(c[0][0], c[0][1])
    print(c[1][0], c[1][1])
    print(c[2][0], c[2][1])
