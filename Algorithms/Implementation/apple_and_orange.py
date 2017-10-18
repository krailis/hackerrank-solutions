import sys

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
count_apples = 0
count_oranges = 0
for x in apple:
    pos = a + x
    if (pos >= s and pos <= t):
        count_apples += 1
for x in orange:
    pos = b + x
    if (pos >= s and pos <= t):
        count_oranges += 1
print(count_apples)
print(count_oranges)


