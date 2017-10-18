def merge_the_tools(string, k):
    # your code goes here
    words = [string[i:i+k] for i in range(0, len(string), k)]
    for item in words:
        unique = []
        for letter in item:
            if not letter in unique:
                unique.append(letter)
        print("".join(unique))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
