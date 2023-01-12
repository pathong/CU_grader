import math
a = float(input())
b = float(input())
c = float(input())

s = math.sqrt(math.pow(b,2) - 4*a*c) 
a2 = a * 2

an1 = round((-b - s)/a2, 3)
an2 = round((-b + s)/a2, 3)

print("{0} {1}".format(an1, an2))



