import sys

def diff (n, a):
    sum_primary = 0
    sum_secondary = 0
    for i in range(n):
        sum_primary += a[i][i]
    for i in range(n):
        sum_secondary += a[i][-i - 1]
    return abs(sum_primary - sum_secondary)
        
n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
print(diff(n, a))
