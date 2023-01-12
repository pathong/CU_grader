f = input()
fi = open(f,"r")


c = 0
s = 0
for li in fi.readlines():
    sp = li.split(" ")
    s += int(sp[c%2])

    c += 1


print(s/c)

