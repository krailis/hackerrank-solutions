def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r

def factorial():
    factorial = list(range(0, 1001))
    factorial[0] = 1
    for i in range(2, 1001):
        factorial[i] = factorial[i-1]*i
    return factorial

fact = factorial()
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum_digits(fact[n]))
