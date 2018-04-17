#!/bin/python3

import sys

def maximumToys(prices, k):
    # Complete this function
    prices, p_sum, toys = sorted(prices), 0, 0
    if prices[0] > k:
        return 0
    elif prices[0] == k:
        return 1
    for p in prices:
        if p_sum + p > k:
            return toys
        else:
            toys += 1
            p_sum += p
    return toys
        

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = list(map(int, input().strip().split(' ')))
    result = maximumToys(prices, k)
    print(result)

