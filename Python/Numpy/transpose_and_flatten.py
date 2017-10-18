import numpy

n, m = map(int, input().strip().split())
l = []
for _ in range(n):
    l.append(list(map(int,input().strip().split())))
arr = numpy.array(l)
print(numpy.transpose(arr))
print(arr.flatten())
