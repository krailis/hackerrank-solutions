#!/bin/python3

import sys

def findDigits(n):
    # Complete this function
    digits_list = list(map(int, list(str(n))))
    digits, divisors = set(digits_list), 0
    digits.discard(0)
    for d in digits:
        if n % int(d) == 0:
            divisors += digits_list.count(d)
    return divisors
    

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = findDigits(n)
        print(result)

