import sys
from math import floor

def sockMerchant(n, ar):
    # Complete this function
    colors = set(ar)
    pairs = 0
    for c_i in colors:
        pairs += floor(ar.count(c_i) / 2)
    return int(pairs)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
