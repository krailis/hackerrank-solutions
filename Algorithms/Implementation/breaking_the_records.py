import sys

def getRecord(s):
    min_points, max_points = s[0], s[0]
    min_count, max_count = 0, 0
    for points in s:
        if (min_points > points):
            min_points = points
            min_count += 1
        if (max_points < points):
            max_points = points
            max_count += 1
    return [max_count, min_count]

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))

