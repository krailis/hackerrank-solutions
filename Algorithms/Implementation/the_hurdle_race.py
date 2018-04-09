#!/bin/python3

import sys

def hurdleRace(k, height):
    # Complete this function
    distinct_heights = set(height)
    max_height = max(distinct_heights)
    if max_height <= k:
        return 0
    else:
        return max_height - k

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = list(map(int, input().strip().split(' ')))
    result = hurdleRace(k, height)
    print(result)

