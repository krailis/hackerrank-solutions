_ = input()
set_a = set(map(int, input().strip().split()))
t = int(input())
for _ in range(t):
    op = input().strip().split()[0]
    s = set(map(int, input().strip().split()))
    exec("set_a." + op + "(s)")
print(sum(set_a))
