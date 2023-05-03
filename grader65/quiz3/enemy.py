ally = {}
enemy = {}
while True:
    inp = input().split()
    if len(inp) <= 1:
        break
    mode = inp[0]
    li = inp[1:]

    if mode == 'Ally':
        for l in li:
            ally[l] = set(li)
    if mode == 'Enemy':
        for ei in range(len(li)):
            curr = ""
            e = ""
            if ei == 0:
                curr = li[ei]
                e = li[1]
            elif ei == 1:
                curr = li[ei]
                e = li[0]
            if curr not in enemy.keys():
                enemy[curr] = set()
            enemy[curr].add(e)
            if e in ally.keys(): enemy[curr].add(ally[e])

            

    

