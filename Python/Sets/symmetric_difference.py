if __name__ == "__main__":
    m = int(input())
    set_a = set(map(int, input().strip().split()))
    n = int(input())
    set_b = set(map(int, input().strip().split()))
    set_c = set_a.union(set_b)
    s_diff = set_c.difference(set_a.intersection(set_b))
    for x in sorted(s_diff):
        print(x)
