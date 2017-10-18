t = int(input().strip())
for k in range(t):
    grid = []
    n = int(input().strip())
    for i in range(n):
        row = input().strip()
        grid.append(sorted(row))
    done = False
    for j in range(n):
        for i in range(n-1):
            if grid[i][j] > grid[i+1][j]:
                done = True
                break
        if (done):
            break
    if (done):
        print('NO')
    else:
        print('YES')
