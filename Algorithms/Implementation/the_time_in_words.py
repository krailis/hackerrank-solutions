#!/bin/python3

time_dict = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
    9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'quarter',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one',
    22: 'twenty two', 23: 'twenty three', 24: 'twenty four', 25: 'twenty five', 26: 'twenty six',
    27: 'twenty seven', 28: 'twenty eight', 29: 'twenty nine', 30: 'half'
}

def timeInWords(h, m):
    # Complete this function
    if m == 0:
        return time_dict[h] + " o' clock"
    if m == 15 or m == 30:
        return time_dict[m] + ' past ' + time_dict[h]
    if 2 <= m <= 29:
        return time_dict[m] + ' minutes past ' + time_dict[h]
    if m == 1:
        return 'one minute past ' + time_dict[h]
    if m == 45:
        if h != 12:
            return time_dict[60 - m] + ' to ' + time_dict[h + 1]
        else:
            return time_dict[60 - m] + ' to one'
    if 31 <= m <= 58:
        if h != 12:
            return time_dict[60 - m] + ' minutes to ' + time_dict[h + 1]
        else:
            return time_dict[60 - m] + ' minutes to one'
    if m == 59:
        if h != 12:
            return 'one minute to ' + time_dict[h + 1]
        else:
            return 'one minute to one'


if __name__ == "__main__":
    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)
    print(result)

