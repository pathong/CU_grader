n = int(input())
d = dict()
for _ in range(n):
    e = input().split()
    d[e[0]] = e[1]

m = int(input())
for _ in range(m):
    o = input()
    for k,v in d.items():
        if k == o: print(v)
        elif v == o: print(k)

