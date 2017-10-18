n, k = map(int, input().strip().split(' '))
l_t, t_c, l_s = [], 0, 0
for i in range(n):
    l, t = map(int, input().strip().split(' '))
    if t == 1:
        t_c += 1
    l_s += l
    l_t.append((l, t))
l_t, t_c = sorted(l_t), t_c - k
if (t_c <= 0 or k == 100):
    print(l_s)
else:
    for item in l_t:
        if (item[-1] == 1):
            l_s -= (item[0] + item[0])
            t_c -= 1
            if t_c == 0:
                break
    print(l_s)
