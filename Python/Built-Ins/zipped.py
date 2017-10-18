N, X = map(int, input().strip().split())
marks = []
for _ in range(X):
    marks.append(list(map(float, input().strip().split())))
all_subjects = zip(*marks)
for subs in all_subjects:
    print(sum(subs)/X)
