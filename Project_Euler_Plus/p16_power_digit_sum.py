def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    print(sum_digits(2 << (n-1)))
