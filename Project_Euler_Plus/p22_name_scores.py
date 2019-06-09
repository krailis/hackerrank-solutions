n = int(input().strip())
names = list(range(n))
for i in range(n):
    next_name = input().strip()
    names[i] = next_name
names = sorted(names)
scores = [0 for i in range(n)]
for i in range(n):
    temp_name = names[i]
    for j in range(len(temp_name)):
        scores[i] += ord(temp_name[j]) - 64
    scores[i] *= (i + 1)
q = int(input().strip())
for i in range(q):
    query = input().strip()
    print(scores[names.index(query)])
