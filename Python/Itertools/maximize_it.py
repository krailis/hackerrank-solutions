import itertools

K, M = map(int, input().strip().split())
lists = []
for _ in range(K):
    lists.append(list(map(int, input().strip().split()))[1:])
max_val = 0
for item in itertools.product(*lists):
    S = sum(map(lambda x: x**2, item)) % M
    if (S > max_val):
        max_val = S
print(max_val)
