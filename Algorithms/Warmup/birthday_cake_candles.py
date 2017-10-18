import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    height = max(ar)
    return ar.count(height)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)

