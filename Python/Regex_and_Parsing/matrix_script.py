import sys
import re

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
matrix = []
matrix_i = 0
for matrix_i in range(n):
    matrix_t = str(input())
    matrix.append(matrix_t)
columns = []
for i in range(m):
    columns.append([x[i] for x in matrix])
string = ""
for col in columns:
    string += "".join(col)
findall = re.findall(r'[a-zA-Z0-9][!@#$%&\s]+[a-zA-Z0-9]', string)
findall.reverse()
count = len(findall)
for m in findall:
    string = re.sub(r'[a-zA-Z0-9][!@#$%&\s]+[a-zA-Z0-9]', m[0] + " " + m[-1], string, count=count)
    count -= 1
print(string)
