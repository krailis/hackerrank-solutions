# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    number_of_jumps, position = 0, 0
    while position < len(c) - 1:
        if position + 2 == len(c):
            number_of_jumps += 1
            return number_of_jumps
        if c[position + 2] == 1:
            position += 1
            number_of_jumps += 1
        elif c[position + 2] == 0 or c[position + 1] == 1:
            position += 2
            number_of_jumps += 1
    return number_of_jumps

if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)

