import operator

students = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    students.append([name, score])
students = sorted(students, key = operator.itemgetter(1, 0))
grades = sorted(set([y for x, y in students]))
second = [x for x, y in students if y == grades[1]]
for name in second:
    print(name)
