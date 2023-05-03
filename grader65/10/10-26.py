d = dict()
n = int(input())
orders = []
for _ in  range(n):
    inp = input().split(':')
    d[inp[0]] = inp[1].split(', ')
    orders.append(inp[0])
o = input()
ans = [] 
des = d[o]
# print(d)
for k in orders:
    if k == o: continue
    for v in d[k]:
        for de in des:
            de = de.strip()
            if de[0] in v.strip() and k not in ans: ans.append(k)




if len(ans) <= 0: print('Not Found')
else:
    for a in ans:
        print(a)

