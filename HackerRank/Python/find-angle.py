from math import acos, sqrt, degrees
ab, bc = int(input()), int(input())
ac = sqrt(ab**2 + bc**2)
print(round(degrees(acos(bc/ac))), chr(176), sep='')