def split_and_join(line):
    # write your code here
    split_line = line.split(" ")
    return "-".join(split_line)

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result
