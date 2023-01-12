st = input()
le = len(st)
pin = ""
if le == 128:
    l1 = [3,101,24,32]
    l2 = [56, 89,92,12]
    w = ""
    v = ""
    for i in l1:
        for j in range(le):
            if i == j:
                w += st[i]
    for i in l1:
        for j in range(le):
            if i == j:
                v += st[i]

    w = int(w)
    v = int(v)

    pin = str((w+v)/2)

elif le == 64:
    l = [8, 22, 49, 34]
    w = ""
    for i in l:
        for j in range(le):
            if i == j:
                w += st[i]
    pin = w
print(pin)
