import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    b_actual = (sum(ar) - ar[k])/2
    if (b == b_actual):
        return "Bon Appetit"
    else:
        return int(b - b_actual)
    

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)

