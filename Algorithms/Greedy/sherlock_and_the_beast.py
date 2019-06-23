#!/bin/python3

# Complete the decentNumber function below.
def decentNumber(n):
    if n < 3:
        return -1
    elif n == 5:
        return 33333
    elif n % 3 == 0:
        return int('5' * n)
    else:
        number = '3' * 5
        while n >= 3:
            n -= 5
            if n % 3 == 0:
                number = ('5' * n) + number
                return int(number)
            number += '3' * 5
    return -1

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = decentNumber(n)
        print(result)

