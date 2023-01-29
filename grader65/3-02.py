
g = "FDCBA"


def a_4(p:list):
    for i in range(len(p)):
        if p[i] in g:
            p[i] = g.index(p[i])
    return p

a = a_4(input().split())
b = a_4(input().split())

def CheckPass(p:list)->bool:
    if p[2] >= g.index("A") and p[3] >= g.index("C") and p[4] >= g.index("C"):
        return True
    return False
     

pa = CheckPass(a)
pb = CheckPass(b)


if not pa and not pb:
    print("None")
elif pa and not pb:
    print(a[0])
elif not pa and pb:
    print(b[0])
else:
    win = ""
    if a[1] == b[1]:
        if a[3] == b[3]:
            if a[4] == b[4]:
                print("Both")
            else:
                win = a[0] if int(a[4]) > int(b[4]) else b[0]
        else:
            win = a[0] if int(a[3]) > int(b[3]) else b[0]
    else:
        win = a[0] if float(a[1]) > float(b[1]) else b[0]

    print(win)





