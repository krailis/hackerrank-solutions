import numpy

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().strip().split())))
a = numpy.array(l)
l = []
for _ in range(n):
    l.append(list(map(int, input().strip().split())))
b = numpy.array(l)
print(numpy.dot(a, b))
