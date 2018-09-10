import sys

def fibonacci(n):
    fib_list = [0, 1]
    for i in range(2, n):
        l = fib_list[i-1] + fib_list[i-2]
        if l >= n:
            break
        else:
            fib_list.append(l)
    return [x for x in fib_list if x % 2 == 0]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum(fibonacci(n)))
