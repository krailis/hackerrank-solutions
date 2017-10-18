N = int(input())
input_list = list(map(int, input().strip().split()))
if (all([x > 0 for x in input_list])):
    if (any([(str(x)[0]==str(x)[-1]) for x in input_list])):
        print(True)
    else:
        print(False)
else:
    print(False)
