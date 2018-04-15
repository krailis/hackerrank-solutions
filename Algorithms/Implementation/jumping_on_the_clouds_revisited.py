#!/bin/python3


def jumpingOnClouds(c, k):
    # Complete this function
    has_revisited, n, i, e = False, len(c), 0, 100
    while not has_revisited:
        next_pos = (i + k) % n
        i = next_pos
        if next_pos == 0:
            has_revisited = True
        e -= 1 if c[next_pos] == 0 else 3
    return e

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    c = list(map(int, input().strip().split(' ')))
    result = jumpingOnClouds(c, k)
    print(result)

