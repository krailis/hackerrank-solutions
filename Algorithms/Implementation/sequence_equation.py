#!/bin/python3

import sys

def permutationEquation(p):
    # Complete this function
    index_list = []
    for x in range(1, len(p) + 1):
        x_index = p.index(x) + 1
        y_index = p.index(x_index) + 1
        index_list.append(y_index)
    return index_list


if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    result = permutationEquation(p)
    print ("\n".join(map(str, result)))



