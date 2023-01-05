# https://drive.google.com/drive/u/0/folders/1JzOI_paAp2kBHpP4zIDlRFUUNN-XwRR6

while True:
    w = input()
    s = w.split(".")

    if "." not in w:
        s.append("00")
    else:
        if len(s[0]) == 0:
            s[0] += "0"
        while len(s[1]) < 2:
            s[1] += "0"


    a = s[1]
    if len(a) > 2:
        if int(a[2]) >=5:
            a = int(a[:2]) + 1
            if a >= 100:
                a = str(a - 100)
                if len(a) < 2:
                    a += "0"
                s[0] = str(int(s[0]) + 1)
        else:
            a = a[:2]

        s[1] = str(a)


    b = s[0]
    c = 1
    t = 1
    while c < len(b):
        if c == 3*t+t-1:
            t +=1;
            b = b[:-c] + "," + b[-c:]

        c+=1
    s[0] = b




    print(".".join(s))
