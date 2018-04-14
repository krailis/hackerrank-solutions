#!/bin/python3

from itertools import combinations

def divisibleSumPairs(n, k, ar):
    # Complete this function
    pairs = 0
    for x, y in combinations(ar, 2):
        if (x + y) % k == 0:
            pairs += 1
    return pairs

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)

