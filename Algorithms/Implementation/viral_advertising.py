#!/bin/python3

from math import floor

def viralAdvertising(n):
    # Complete this function
    if n == 1:
        return 2
    total_likes, day, recipients = 2, 2, 6
    while day <= n:
        likes = floor(recipients / 2)
        total_likes += likes
        recipients = likes * 3
        day += 1
    return total_likes
    
if __name__ == "__main__":
    n = int(input().strip())
    result = viralAdvertising(n)
    print(result)

