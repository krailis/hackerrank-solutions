import numpy

l = list(map(float,input().strip().split()))
x = int(input())
print(numpy.polyval(l, x))
