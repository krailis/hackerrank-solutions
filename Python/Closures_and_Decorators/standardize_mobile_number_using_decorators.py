def wrapper(f):
    def fun(l):
        # complete the function
        new_l = []
        for number in l:
            if len(number) == 13:
                new_l.append(number[0:3] + ' ' + number[3:8] + ' ' + number[8:13])
            elif len(number) == 12:
                new_l.append('+' + number[0:2] + ' ' + number[2:7] + ' ' + number[7:12])
            elif len(number) == 11:
                new_l.append("+91" + ' ' + number[1:6] + ' ' + number[6:11])
            elif len(number) == 10:
                new_l.append("+91" + ' ' + number[0:5] + ' ' + number[5:10])
        f(new_l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

