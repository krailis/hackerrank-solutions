import numpy

# Input Matrices
n, m = map(int, input().strip().split())
l = []
for _ in range(n):
    l.append(list(map(int, input().strip().split())))
a = numpy.array(l, dtype = numpy.int)
l = []
for _ in range(n):
    l.append(list(map(int, input().strip().split())))
b = numpy.array(l, dtype = numpy.int)
# Operations
print(a + b, a - b, a * b, a // b, a % b, a**b, sep='\n')
