n = int(input())
d = dict()
for _ in range(n):
    team, nation = input().split()
    d[team] = nation
while True:
    inp = input().split()
    if len(inp) <= 1:
        break
    ## list team
    unknown = False 
    nations = set()
    for t in inp:
        if t not in d.keys():
            unknown = True
            break
        nations.add(d[t])
    if unknown:
        print('Not OK')
        continue
    
    if len(nations) == len(inp):
        print('OK')
    else:
        print('Not OK')

