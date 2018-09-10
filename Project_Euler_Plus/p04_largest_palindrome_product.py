import sys

def isPalindrome (list_a):
	l = int(len(list_a)/2)
	# Compare elements of the list symmetrically. If any two symmetric elements
	# differ then the list is not palindrome
	for i in range(0, l):
		if (list_a[i] != list_a[-1-i]):
			return False
	return True

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    palin = []
    m_max = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            mult = i*j
            if (mult >= n):
                continue
            if (palin != []):
                if (mult < m_max):
                    break
            if (isPalindrome(list(str(mult)))):
                if (m_max < mult):
                    m_max = mult
                palin.append(mult)
    print(max(palin))        
