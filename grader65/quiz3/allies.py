ally_li = []
enermy_li = []
enemy_dict = dict()
while True:
    inp = input().split()
    if len(inp) <= 1: break

    mode = inp[0] 
    li = inp[1:]
    if mode == 'Ally':
        ally_li.append(li)
    elif mode == 'Enemy':
        enermy_li.append(li)
        for l in li:
            found = False
            for a in ally_li:
                if l in a:
                    found = True
            if not found:
                ally_li.append([l])

def findEnemy(nation):
    enemys = set()
    for enemy_group in enermy_li:
        if nation in enemy_group:
            for e in enemy_group:
                if nation != e:
                    enemys.add(e)
                    ## get own Enemy
                    # find enemy's ally
                    for a in ally_li:
                        if e in a:
                            enemys.update(set(a))  


for ally_group in ally_li:
    for nation in ally_group:
        if nation not in enemy_dict.keys():
            enemy_dict[nation] = {} 







