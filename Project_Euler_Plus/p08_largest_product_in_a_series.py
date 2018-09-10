import sys

def max_product(n, k):
    max_p = 0
    for i in range(0, len(n)-k):
        p = 1
        for j in range(i, i + k):
            p *= n[j]
        if max_p < p:
            max_p = p
    return max_p

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = list(input().strip())
    num = [int(x) for x in num]
    print(max_product(num, k))

