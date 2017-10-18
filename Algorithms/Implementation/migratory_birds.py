import sys

def migratoryBirds(n, ar):
    # Complete this function
    types_count = [ar.count(i) for i in range(1, 6)]
    common = max(types_count)
    for i in range(5):
        if (types_count[i] == common):
            return i + 1
            break

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)

