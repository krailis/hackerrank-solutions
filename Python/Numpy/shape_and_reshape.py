import numpy

l = list(map(int, input().strip().split()))
arr = numpy.array(l)
print(numpy.reshape(arr, (3,3)))
