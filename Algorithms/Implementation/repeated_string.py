#!/bin/python3

import sys

def repeatedString(s, n):
    # Complete this function
    if s == 'a':
        return n
    if n % len(s) == 0:
        return int((n / len(s)) * s.count('a'))
    else:
        div = n // len(s)
        remain = n - div * len(s)
        return int((n // len(s)) * s.count('a') + s[0:remain].count('a'))

if __name__ == "__main__":
    s = input().strip()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)

