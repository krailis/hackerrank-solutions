if __name__ == '__main__':
    N = int(input())
l = []
for i in range(N):
    op = input().strip().split(' ')
    if (len(op) == 3):
        l.insert(int(op[1]), int(op[2]))
    elif (len(op) == 2):
        if (op[0] == "remove"):
            l.remove(int(op[-1]))
        elif (op[0] == "append"):
            l.append(int(op[-1]))
    elif (len(op) == 1):
        if (op[0] == "print"):
            print(l)
        elif (op[0] == "sort"):
            l = sorted(l)
        elif (op[0] == "reverse"):
            l.reverse()
        else:
            l.pop()
