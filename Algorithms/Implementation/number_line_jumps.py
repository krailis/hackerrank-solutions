import sys
from math import floor

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    if x1 == x2:
        return 'YES'
    elif (x1 > x2 and v1 >= v2) or (x1 < x2 and v1 <= v2):
        return 'NO'
    # Equalize the Arithmetic Progressions
    # and solve for n
    n = abs((x1 - x2 - v1 + v2) / (v1 - v2))
    if n == floor(n):
        return 'YES'
    else:
        return 'NO'
    

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)

