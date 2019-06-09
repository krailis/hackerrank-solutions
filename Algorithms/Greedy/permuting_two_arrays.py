#!/bin/python3

def twoArrays(k, A, B):
    len_arr = len(A)
    s_a, s_b = sum(A), sum(B)
    if ((s_a + s_b) / len_arr < k):
        return 'NO'
    if ((s_a / len_arr < k) and (s_b / len_arr > 2*k)):
        return 'NO'
    if ((s_a / len_arr > 2*k) and (s_b / len_arr < k)):
        return 'NO'
    return 'YES'

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        _, k = list(map(int, input().strip().split()))
        A = list(map(int, input().rstrip().split()))
        B = list(map(int, input().rstrip().split()))
        result = twoArrays(k, A, B)
        print(result)
