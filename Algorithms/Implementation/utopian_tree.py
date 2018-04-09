#!/bin/python3

from math import ceil, floor

def utopianTree(n):
    # Complete this function
    if n == 0 or n == 1:
        return n + 1
    height = 1
    while n > 0:
        height *= 2
        if n - 1 == 0:
            break
        height += 1
        n -= 2
    return height
        

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = utopianTree(n)
        print(result)

