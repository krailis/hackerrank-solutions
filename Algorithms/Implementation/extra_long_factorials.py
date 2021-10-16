import sys

def extraLongFactorials(n):
    # Complete this function
    if n == 1 or n == 2:
        return n
    return n * extraLongFactorials(n - 1)
    

if __name__ == "__main__":
    n = int(input().strip())
    print(extraLongFactorials(n))

