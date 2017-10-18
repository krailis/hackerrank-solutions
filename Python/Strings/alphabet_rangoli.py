import string

def print_rangoli(size):
    # your code goes here
    if size == 1:
        print("a")
        return
    lower = list(string.ascii_lowercase)
    letters = (size << 1) - 1
    width = (letters << 1) - 1
    rangoli_left, rangoli_right = lower[size-1], lower[size-1]
    print(lower[size-1].center(width, "-"))
    for i in range(size-2, -1, -1):
        print((rangoli_left + "-" + lower[i] + "-" + rangoli_right).center(width, "-"))
        rangoli_left += "-" + lower[i]
        rangoli_right = lower[i] + "-" + rangoli_right
    rangoli_left, rangoli_right = rangoli_left[:-4], rangoli_right[4:]
    for i in range(1, size-1):
        print((rangoli_left + "-" + lower[i] + "-" + rangoli_right).center(width, "-"))
        rangoli_left, rangoli_right = rangoli_left[:-2], rangoli_right[2:]
    print(lower[size-1].center(width, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
