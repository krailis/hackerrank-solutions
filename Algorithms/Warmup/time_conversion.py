import sys

def timeConversion(s):
    # Complete this function
    s = s.split(':')
    pm_am = s[-1][-2:]
    s[-1] = s[-1][:2]
    if (pm_am == 'AM'):
        if (s[0] == '12'):
            s[0] = '00'
    elif (pm_am == 'PM'):
        if (s[0] != '12'):
            s[0] = str(int(s[0]) + 12)
    return ':'.join(s)

s = input().strip()
result = timeConversion(s)
print(result)

