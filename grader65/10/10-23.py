n = int(input())
d = dict()
for _ in range(n):
    inp = input().strip().split(',')
    if inp[2] not in d.keys(): d[inp[2]] = 0

    t = inp[3].split(":")
    d[inp[2]] += int(t[0])*60 + int(t[1])

time = sorted(list(d.values()),reverse=True)
for t in time[:3]:
    for k,v in d.items():
        if t == v:
            print('{} --> {}:{}'.format(k,v//60,v%60 if len(str(v%60)) >= 2 else "0" + str(v%60)))







