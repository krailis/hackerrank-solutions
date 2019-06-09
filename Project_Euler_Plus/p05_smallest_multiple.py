import sys

def lcm(a,b): 
    gcd, tmp = a,b 
    while tmp != 0: 
        gcd,tmp = tmp, gcd % tmp
    return a*(b/gcd)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if (n == 1 or n == 2):
        print(n)
    else:
        smallest = 2
        for i in range (3, n + 1):
            smallest = lcm(smallest, i)
        print(int(smallest))
