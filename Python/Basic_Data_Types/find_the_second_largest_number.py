if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
first_max = max(arr)
second_max = -100
for i in range(n):
    if (second_max < arr[i] < first_max):
        second_max = arr[i]
print(second_max)

