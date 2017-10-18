import numpy

A = numpy.array(list(map(float, input().strip().split())))
print(numpy.floor(A), numpy.ceil(A), numpy.rint(A), sep = '\n')
