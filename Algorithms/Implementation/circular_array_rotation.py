#!/bin/python3

def circularArrayRotation(a, m):
    # Complete this function
    responses = []
    for m_i in m:
        responses.append(a[m_i])
    return responses

if __name__ == "__main__":
    n, k, q = input().strip().split(' ')
    n, k, q = [int(n), int(k), int(q)]
    a = list(map(int, input().strip().split(' ')))
    
    # Rotate k times
    k = k % n
    temp_list = a[-k:]
    temp_list.extend(a[:n - k + 1])
    a = temp_list
    
    m = []
    m_i = 0
    for m_i in range(q):
       m_t = int(input().strip())
       m.append(m_t)
    result = circularArrayRotation(a, m)
    print ("\n".join(map(str, result)))



