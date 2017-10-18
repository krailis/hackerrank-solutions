import numpy

A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))
Α, Β = numpy.array(A), numpy.array(B)
print(numpy.inner(A, B), numpy.outer(A, B), sep='\n')
