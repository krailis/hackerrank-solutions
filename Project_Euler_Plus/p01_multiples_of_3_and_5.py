import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if (n <= 3):
        print(0)
    elif (n > 3 and n <= 5):
        print(3)
    else:
        n3 = int((n-1)/3)
        n5 = int((n-1)/5)
        n15 = int((n-1)/15)
        n3sq = n3*n3
        n5sq = n5*n5
        n15sq = n15*n15
        n3s = (n3sq << 1) + n3sq
        n5s = (n5sq << 2) + n5sq
        n15s = (n15sq << 4) - n15sq
        s3 = (n3s + 3*n3) >> 1
        s5 = (n5s + 5*n5) >> 1
        s15 = (n15s + 15*n15) >> 1
        print(s3 + s5 - s15)
            
