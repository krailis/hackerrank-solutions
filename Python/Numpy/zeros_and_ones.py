import numpy

l = list(map(int, input().strip().split()))
print(numpy.zeros(tuple(l), dtype = numpy.int))
print(numpy.ones(tuple(l), dtype = numpy.int))
