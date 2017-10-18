cube = lambda x: pow(x, 3)

def fibonacci(n):
    if (n == 0):
        return []
    if (n == 1):
        return [0]
    if (n == 2):
        return [0, 1]
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
