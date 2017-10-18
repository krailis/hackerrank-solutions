import itertools

inp = input().strip().split()
for item in sorted(itertools.permutations(inp[0], int(inp[1]))):
    print("".join(item))
