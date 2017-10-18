import sys

n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
# your code goes here
c = sorted(calories, reverse=True)
miles = c[0]
miles = miles + (c[1] << 1)
for i in range(2, n):
    miles = miles + c[i]*(2 << (i-1))
print(miles)

