#!/bin/python3

import sys

def angryProfessor(k, a):
    # Complete this function
    early = 0
    for t in a:
        if t <= 0:
            early += 1
        if early >= k:
            break
    return 'NO' if early >= k else 'YES'

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        a = list(map(int, input().strip().split(' ')))
        result = angryProfessor(k, a)
        print(result)

