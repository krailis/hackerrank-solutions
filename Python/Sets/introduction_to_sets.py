def average(array):
    # your code goes here
    a_set = set(array)
    return sum(a_set)/len(a_set)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
