d = dict()
order = []
while True:
    inp = input()
    if inp == 'q':break
    inp = inp.split(',')
    if inp[1] not in d.keys():
        d[inp[1]] = []
        order.append(inp[1])

    d[inp[1]].append(inp[0])


for o in order:
    print('{}: {}'.format(o, ', '.join(d[o])))

