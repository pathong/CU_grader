d = dict()
start = ""
while True:
    e = input().split()
    if len(e) <= 1:
        start = e[0]
        break
    if e[0] not in d.keys():
        d[e[0]] = set() 
    if e[1] not in d.keys():
        d[e[1]] = set() 
    d[e[0]].add(e[1])
    d[e[1]].add(e[0])


ans = set()
ans.add(start)

if start in d.keys():
    firstlayer = d[start]
    secondlayer = set() 
    for l in firstlayer:
        if l in d.keys():
            secondlayer.update(d[l])

    firstlayer.update(secondlayer)
    ans = sorted(list(firstlayer))

for a in ans:
    print(a)






