def maxMin(k, arr):
    # Write your code here
    arr.sort()
    unfairnesses = []
    for i in range(len(arr) - k + 1):
        unfairnesses.append(arr[i+k-1] - arr[i])
    return min(unfairnesses)

if __name__ == '__main__':
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)
    result = maxMin(k, arr)
    print(result)
