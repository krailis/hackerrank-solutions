import sys

def plus_minus (n, a):
    pos, neg, zer = 0, 0, 0
    for item in a:
        if item > 0:
            pos += 1
        elif item < 0:
            neg += 1
        else:
            zer += 1
    return [pos/n, neg/n, zer/n]

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
res = plus_minus(n, arr)
print("%.6f" % res[0])
print("%.6f" % res[1])
print("%.6f" % res[2])
