import sys

def minimumAbsoluteDifference(n, arr):
    # Complete this function
    a = sorted(arr)
    m_min = 1000000000
    for i in range(n-1):
        diff = abs(a[i+1]-a[i])
        if m_min > diff:
            m_min = diff
    return m_min

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print(result)

