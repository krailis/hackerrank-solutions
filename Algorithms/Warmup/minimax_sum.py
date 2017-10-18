import sys

def mini_max (arr):
    m_min = 10000000000
    m_max = 0
    s_sum = sum(arr)
    for i in range(5):
        t_sum = s_sum - arr[i]
        if (t_sum > m_max):
            m_max = t_sum
        if (t_sum < m_min):
            m_min = t_sum
    print(m_min, m_max)

arr = list(map(int, input().strip().split(' ')))
mini_max(arr)

