import math
n = input().split(",")
n[1] = "0" + n[1]


f = n[0]
a = n[1] + n[2]
na = n[1]
t = int(a) - int(na)
b = "9"* len(n[2]) + "0" * (len(na)-1)
b = 10 ** (len(a)-1) - 10 ** (len(na)-1)

t += int(f) * int(b)

gcd = math.gcd(t,b)

t //= gcd
b //= gcd
print("{0} / {1}".format(t,b))







