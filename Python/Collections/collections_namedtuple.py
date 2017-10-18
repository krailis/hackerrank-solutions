N, marks_index, s = int(input()), input().strip().split().index("MARKS"), 0
for _ in range(N):
    s += int(input().strip().split()[marks_index])
print(s/N)
