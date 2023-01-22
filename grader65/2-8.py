import math
n = input().split(",")
n[1] = "0" + n[1]


front = n[0]
_all = n[1] + n[2]
not_all = n[1]
top = int(_all) - int(not_all)
buttom = 10 ** (len(_all)-1) - 10 ** (len(not_all)-1)

top += int(front) * int(buttom)

gcd = math.gcd(top,buttom)

top //= gcd
buttom //= gcd
print("{0} / {1}".format(top,buttom))







