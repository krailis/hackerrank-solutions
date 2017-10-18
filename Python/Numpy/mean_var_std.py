import numpy

n, _ = map(int, input().strip().split())
l = []
for _ in range(n):
    l.append(list(map(float, input().strip().split())))
a = numpy.array(l)
print(numpy.mean(a, axis=1), numpy.var(a, axis=0), numpy.std(a, axis=None), sep='\n')
