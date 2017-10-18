from collections import deque

dq = deque()
N = int(input())
for _ in range(N):
    op = input().strip().split()
    opcode, operand = op[0], op[-1]
    if (opcode == "pop" or opcode == "popleft"):
        exec("dq." + opcode + "()")
    else:
        exec("dq." + opcode + "(" + operand + ")")
for x in dq:
    print(x, end=" ")
