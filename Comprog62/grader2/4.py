fn = input()
n = int(input())
# fn = 'dataGrader1.txt'
f = open(fn, "r")
_all = []

for l in f:
    line = l.split()
    if line[1] == "W":
        continue
    for s in range(5,len(line)):
        if line[s] == "-":
            line[s] = "0"

    _id = int(line[0])
    sc_li = list(map(int, line[2:]))
    sc = max(sc_li[0], sc_li[3]) + max(sc_li[1], sc_li[4]) + max(sc_li[2], sc_li[5]) + sc_li[6]+ sc_li[7]+ sc_li[8]


    _all.append([-sc, _id])

_all.sort()


if(n>len(_all)): n=len(_all)

c = 0
while c < n:
    print("{0} --> {1}".format(-_all[c][0], _all[c][1]))
    c+=1




