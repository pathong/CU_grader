def read_next(f):
    while True:
        t = f.readline()
        if len(t) == 0:
            break
        x = t.strip().split()
        if len(x) == 2:
            return x[0], x[1]
    return "", ""


inp = input().split()
path1 = inp[0]
path2 = inp[1]

f1 = open(path1,'r')


while True:
    data = read_next(f1)
    if data[0] == "": break
    print(data)
    






