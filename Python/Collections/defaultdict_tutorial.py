from collections import defaultdict

n, m = map(int, input().strip().split())
A = defaultdict(list)
for i in range(1, n + 1):
    char = input()
    A[char].append(i)
for _ in range(m):
    char = input()
    if char in A.keys():
        for x in A[char]:
            print(x, end=" ")
        print()
    else:
        print(-1)
