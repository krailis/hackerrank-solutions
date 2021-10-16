# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    arr.sort()
    nsticks = [len(arr)]
    while arr != []:
        shortest = arr[0]
        arr = list(filter((shortest).__ne__, arr))
        arr = list(map(lambda x: x - shortest, arr))
        nsticks.append(len(arr))
    return nsticks[:-1]

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = cutTheSticks(arr)
    print(result)
