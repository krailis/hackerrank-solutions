import sys
import math

def primesList (lower, upper):
	# Implemented the Sieve of Eratosthenes
	a = [True for i in range(0, upper + 1)]
	for i in range(2, int(math.sqrt(upper)) + 1):
		if (a[i]):
			j = i * i
			while (j <= upper):
				a[j] = False
				j += i
	return [i + lower for i, x in enumerate(a[lower:]) if x]
    
def binarySearch(data, val):
    highIndex = len(data)-1
    lowIndex = 0
    while highIndex > lowIndex:
            index = int((highIndex + lowIndex) / 2)
            sub = data[index]
            if data[lowIndex] == val:
                    return [lowIndex, lowIndex]
            elif sub == val:
                    return [index, index]
            elif data[highIndex] == val:
                    return [highIndex, highIndex]
            elif sub > val:
                    if highIndex == index:
                            return sorted([highIndex, lowIndex])
                    highIndex = index
            else:
                    if lowIndex == index:
                            return sorted([highIndex, lowIndex])
                    lowIndex = index
    return sorted([highIndex, lowIndex])    
    
pl = primesList(2, 1000000)
psum = [2 for x in range(0, len(pl))]
for i in range(1, len(pl)):
    psum[i] = psum[i-1] + pl[i]
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    f = binarySearch(pl, n)
    print(psum[f[0]])
    
    
