class Group:
    def __init__(self,ally:set):
        self.ally = ally 
        self.enemy = set()
        pass
    def UpdatEnemy(self,enemys:set):
        self.enemy.update(enemys)
    def isEnemy(self,n1,n2):
        if n1 in self.ally and n2 in self.enemy or n1 in self.enemy and n2 in self.ally: return True
        return False

def findEnemy(nation):
    enemys = set()
    for enemy_group in enemy_li:
        if nation in enemy_group:
            for e in enemy_group:
                if nation != e:
                    enemys.add(e)
                    ## get own Enemy
                    # find enemy's ally
                    for a in g_li:
                        if e in a.ally:
                            enemys.update(set(a.ally))  



g_li = []
enemy_li = []

tables= []
while True:
    inp = input().split()
    if len(inp) <= 1: break

    mode = inp[0] 
    li = inp[1:]
    if mode == 'Ally':
        cur_group = Group(set(li))
        g_li.append(cur_group)

    elif mode == 'Enemy':
        enemy_li.append(li)
        for l in li:
            for g in g_li:
                if l not in g.ally:
                    g_li.append(Group(set(l)))

    elif mode == 'Table':
        tables.append(li)

for g in g_li:
    for nation in g.ally:
        enemys = findEnemy(nation)
        g.UpdatEnemy(enemys)




avaliable = True
for table in tables:
    for i in range(len(table)-1):
        nation = table[i]
        _next = table[i+1]
        ## check enemy
        for g in g_li:
            if g.isEnemy(nation,_next):
                avaliable = False
                break

        if not avaliable:
            break
    if not avaliable:
        break






