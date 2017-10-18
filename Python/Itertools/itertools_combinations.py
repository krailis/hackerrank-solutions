import itertools

inp = input().strip().split()
string = sorted(inp[0])
for i in range(1, int(inp[1]) + 1):
    for item in itertools.combinations(string, i):
        print("".join(item))
