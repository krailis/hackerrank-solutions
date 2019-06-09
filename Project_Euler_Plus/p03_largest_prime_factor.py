import sys
import math

def primeFactor (n):
	primeFactors = []
	# If 2 is repeated more than once we have 4 which is not a prime number
	while (n % 2 == 0):
		primeFactors.append(2)
		n = n / 2
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		# Divide by i until not possible and then increase
		while (n % i == 0):
			primeFactors.append(i)
			n = n / i
	if (n > 2):
		primeFactors.append(n)
	return primeFactors[-1]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(int(primeFactor(n)))
