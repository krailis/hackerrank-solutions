#!/bin/python3

import sys

def solve(n, s, d, m):
    # Complete this function
    if m == 1:
        return s.count(d)
    
    number_of_options = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:(i + m)]) == d:
            number_of_options += 1
    return number_of_options

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)

