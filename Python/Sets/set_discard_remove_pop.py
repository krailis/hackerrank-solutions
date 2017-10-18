n = int(input())
s = set(map(int, input().split())) 

number_of_ops = int(input())
for _ in range(number_of_ops):
    query = input().strip().split()
    if (len(query) == 2):
        op, element = query[0], int(query[1])
        if (op == "discard"):
            s.discard(element)
        elif (op == "remove"):
            if (not(len(s) == 0 or not element in s)):
                s.remove(element)
    else:
        if (not (len(s) == 0)):
            s.pop()
print(sum(s))
