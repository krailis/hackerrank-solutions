import numpy

n, m, p = map(int, input().strip().split())
l = []
for _ in range(n):
    l.append(list(map(int, input().strip().split())))
arr_1 = numpy.array(l)
l1 = []
for _ in range(m):
    l1.append(list(map(int, input().strip().split())))
arr_2 = numpy.array(l1)
print(numpy.concatenate((arr_1, arr_2), axis=0))
