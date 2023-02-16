a = float(input())
_a = a
l = 0
u = 0
while True:
    _a  = _a//10
    u +=1
    if _a == 0: break
x = (l+u)/2
while abs(a-(10**x))>(10**(-10)*max(a,10**x)):
    if 10**x > a:u = x
    else: l = x
    x = (l+u)/2
x = round(x,6)

print(x)
    
