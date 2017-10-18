import itertools

inp = list(input().strip().split())
string, k = sorted(inp[0]), int(inp[1])
for item in itertools.combinations_with_replacement(string, k):
    print("".join(item))
