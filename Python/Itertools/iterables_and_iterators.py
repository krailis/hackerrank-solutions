import itertools
import math

N = int(input())
l = input().strip().split()
K = int(input())

a_indices = set()
for i in range(len(l)):
    if (l[i] == 'a'):
        a_indices.add(i)

a_in_combos = 0
all_combos = 0
for item in itertools.combinations(range(0, len(l)), K):
    for i in item:
        if (l[i] == 'a'):
            a_in_combos += 1
            break
    all_combos += 1
print(a_in_combos/all_combos)
