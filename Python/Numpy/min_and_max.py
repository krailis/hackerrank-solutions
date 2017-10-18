import numpy

n, _ = map(int, input().strip().split())
l = list()
for _ in range(n):
    l.append(list(map(int, input().strip().split())))
a = numpy.array(l)
print(numpy.max(numpy.min(a, axis = 1)))
