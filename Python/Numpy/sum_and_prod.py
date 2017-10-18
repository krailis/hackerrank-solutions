import numpy

n, m = map(int, input().strip().split())
l = []
for _ in range(n):
    l.append(list(map(int, input().strip().split())))
a = numpy.array(l)
s = numpy.sum(a, axis = 0)
print(numpy.prod(s, axis = None))
