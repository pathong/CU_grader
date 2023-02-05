import math
def GetX():
    return (l+r)/2
a = float(input())
L = 0
U = a


l = L
r = U
x = GetX()


while abs(a - (x**2)) > (10**(-10)) * max(a, x**2):
    if x**2 > a:
        l = L
        r = x
    if x**2 < a:
        l = x
        r = U

    x = GetX()
    print(x)


print(x)




