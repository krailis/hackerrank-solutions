import sys

squares = [i*i for i in range(0, 10001)]
numbers = [i for i in range(0, 10001)]
for i in range(1, 10001):
    squares[i] += squares[i-1]
    numbers[i] += numbers[i-1]
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print((numbers[n])**2 - squares[n])
