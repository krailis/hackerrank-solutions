from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    cubes = deque(map(int, input().strip().split()))
    pile = [cubes.pop() if cubes[-1] > cubes[0] else cubes.popleft()]
    while (len(cubes) > 0):
        if (cubes[0] > pile[-1] or cubes[-1] > pile[-1]):
            break
        else:
            pile.append(cubes.pop() if cubes[-1] > cubes[0] else cubes.popleft())
    if (len(cubes) == 0):
        print("Yes")
    else:
        print("No")
