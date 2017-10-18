import numpy

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(float, input().strip().split())))
a = numpy.array(l)
print(numpy.linalg.det(a))
