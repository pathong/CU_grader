import math
x = input().split()
a,b,c,d = int(x[0]), int(x[1]), int(x[2]), int(x[3])

if a == 1:
    c,d = d,c
    if b==1:
        c += d
    elif b == 2:
        c -= d
    elif b != 3:
        c += c**d
    else:
        c /=d

    a = (d + ((c/b)**3 + d)**.5)/(2+b*d)
elif a ==2:
    if b>1: c+=d
    if b>2: c/=d
    if b>3: c+= c**d
    else: a = math.log(c, 10)
else:
    while a>d:
        a -= 2
        if a < b:
            break
        else:
            c += a

print(a,b,c,d)
