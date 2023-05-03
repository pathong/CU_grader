#{CE:{Bat:[name,name...], Fut:[name}, }

data = dict()
d = dict()
sport_order = []
while True:
    inp = input().split()
    if len(inp) <= 1:
        break
    data[inp[0]] = int(inp[1])
    sport_order.append(inp[0])
sport_order.sort()

while True:
    inp = input().split()
    if len(inp) <= 1:
        break
    n = inp[0]
    fa = inp[1]
    s = set(inp[2].split(','))
    
    if fa not in d.keys():
        d[fa] = dict()
    for _s in s:
        if _s not in d[fa]:
            d[fa][_s] = set()
        d[fa][_s].add(n)

# print(d)
sport_fa = dict()
# {sport: {fa : 3}}
for sport in sport_order:
    num = 0
    s_fa_li = []
    for fas in d.keys():
        s_fa_li.append(fas)
        if sport in d[fas].keys():
            num = len(d[fas][sport])
        real = num//data[sport]
        not_real = num%data[sport]
        if sport not in sport_fa.keys():
            sport_fa[sport] = dict()

        sport_fa[sport][fas] = (real,not_real)
        num = 0

    s_fa_li.sort()
    if sport in sport_fa.keys():   
        tail = ""
        for fa in s_fa_li:
            if sport_fa[sport][fa][0] > 0:
                tail += fa
                
                tail += str(sport_fa[sport][fa]).replace(' ','')
        ans = "{}:{}".format(sport, tail)
        print(ans)
    else:
        print('{}:'.format(sport))
