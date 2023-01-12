import math
inp = input().strip().split()
a = int(inp[0])
Ne = inp[1]
e = 1

for i in range(len(Ne)):
    if Ne[i] == "e":
        e = math.pow(int(Ne[:i]), int(Ne[i+1:])) 

i = 0
f = a
while True:
    x = (i+f)/2
    print(x)
    _pow = math.pow(10,x)
    if abs(_pow - a) < e*max(_pow, a):
        print(x)
        break

    x2 = math.pow(x,2)
    if x2 > a:
        f = (i + f)/2
    elif x2 < a:
        i =  (i + f)/2


    
