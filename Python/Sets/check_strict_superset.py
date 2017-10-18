A = set(input().strip().split())
n = int(input())
ans = True
for _ in range(n):
    B = set(input().strip().split())
    if (not(A.issuperset(B) and len(A) > len(B))):
        ans = False
        break
print(ans)
