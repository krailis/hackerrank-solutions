import itertools

data = input()
groups = []
uniquekeys = []
for k, g in itertools.groupby(data):
    groups.append(list(g))
    uniquekeys.append(k)
    print((len(groups[-1]), int(k)), end=" ")
