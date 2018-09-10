import sys
import math

def primesList (lower):
	# Implemented the Sieve of Eratosthenes
	a = [True for i in range(0, 104730)]
	for i in range(2, int(math.sqrt(104729)) + 1):
		if (a[i]):
			j = i * i
			while (j <= 104729):
				a[j] = False
				j += i
	return [i + lower for i, x in enumerate(a[lower:]) if x]

t = int(input().strip())
pl = primesList(1)
for a0 in range(t):
    n = int(input().strip())
    print(pl[n])
