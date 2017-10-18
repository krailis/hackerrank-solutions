t = int(input())
for _ in range(t):
    try:
        a, b = map(int, input().strip().split())
        print(a // b)
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)
