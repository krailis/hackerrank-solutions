#!/bin/python3

import sys

def beautifulDays(i, j, k):
    # Complete this function
    beautiful_days = 0
    for d in range(i, j + 1):
        rev = list(str(d))
        rev.reverse()
        if abs(d - int("".join(rev))) % k == 0:
            beautiful_days += 1
    return beautiful_days

if __name__ == "__main__":
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print(result)

