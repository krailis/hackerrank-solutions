import collections

X = int(input())
shoe_sizes = list(map(int, input().strip().split()))
shoe_count = collections.Counter(shoe_sizes)
N = int(input())
amount = 0
for _ in range(N):
    size, money = map(int, input().strip().split())
    if (shoe_count[size] >= 1):
        amount += money
        shoe_count[size] -= 1;
print(amount)
