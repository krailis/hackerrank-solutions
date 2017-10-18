if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    array = list(map(int, input().strip().split()))
    set_a = set(map(int, input().strip().split()))
    set_b = set(map(int, input().strip().split()))
    happiness = 0
    for x in array:
        if x in set_a:
            happiness += 1
        elif x in set_b:
            happiness -= 1
    print(happiness)
