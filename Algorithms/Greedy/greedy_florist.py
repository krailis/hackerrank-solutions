#!/bin/python3

def getMinimumCost(k, c):
    minimumCost, flowersPurchased = 0, 1
    c.sort()
    while (len(c) >= k):
        minimumCost += sum([x * flowersPurchased for x in c[len(c) - k:]])
        c = c[:len(c) - k]
        flowersPurchased += 1
    minimumCost += sum([x * flowersPurchased for x in c])
    return minimumCost

if __name__ == '__main__':
    n, k = list(map(int, input().strip().split()))
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c)
    print(minimumCost)
