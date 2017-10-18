import sys

def solve(grades):
    rounded_grades = []
    for x in grades:
        if (x < 38 or x % 5 == 1 or x % 5 == 2 or x % 5 == 0):
            rounded_grades.append(x)
        else:
            rounded_grades.append(x + 5 - (x % 5))
    return rounded_grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))



