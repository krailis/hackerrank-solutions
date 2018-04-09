#!/bin/python3

import sys

def countingValleys(n, s):
    # Complete this function
    valleys, altitude, altitude_list, i = 0, 1, [], 0
    for step in s:
        altitude += 1 if step == 'U' else -1
        altitude_list.append(altitude)
    while i < n:
        if altitude_list[i] < 1:
            valleys += 1
            i += 1
            while altitude_list[i] != 1:
                i += 1
        else:
            i += 1
    return valleys
    

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)

