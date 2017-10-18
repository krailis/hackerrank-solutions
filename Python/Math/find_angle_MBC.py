import math

AB, BC = int(input()), int(input())
if (AB == BC):
    print("45" + '\u00b0')
else:
    print(str(round(math.degrees(math.atan2(AB,BC)))) + '\u00b0')

