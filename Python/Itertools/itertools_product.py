import itertools

A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))
for item in itertools.product(A, B):
    print(item, end=" ")
