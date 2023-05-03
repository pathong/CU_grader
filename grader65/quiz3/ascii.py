def Transpose(m):
    mt = []
    for i in range(len(m[0])):
        _mt = []
        for j in range(len(m)):
            _mt.append(m[j][i])

        mt.append(_mt)
    return mt
path = input()
modes = ['LSTRIP','RSTRIP','STRIP','STRIP_ALL']
mode = input()
if mode in modes:
    f = open(path)
    m = []
    for l in f:
        l = l.strip()
        _m = []
        for s in l:
            _m.append(s)
        if len(_m) != 0:
            m.append(_m)
    mt = Transpose(m)
    # for _mt in mt:
        # print(''.join(_mt))


    l = 0
    r = len(mt[0])
    a = [] 

    for i in range(len(mt)):
        if mt[i].count('.') != len(mt[i]):
            l = i
            break
    for i in range(len(mt)):
        if mt[i].count('.') == len(mt[i]):
            a.append(i)
    for i in range(len(mt)-1,-1,-1):
        if mt[i].count('.') != len(mt[i]):
            r = i
            break

            
    if mode == 'LSTRIP':
        mt = mt[l:]
    if mode == 'RSTRIP':
        mt = mt[:r+1]
    if mode == 'STRIP':
        mt = mt[l:r+1]
    if mode == 'STRIP_ALL':
        a.reverse()
        for _a in a:
            print(_a)
            mt.pop(_a)

    # for _mt in mt:
        # print(''.join(_mt))

    m = Transpose(mt) 
    for _m in m:
        print(''.join(_m))
else:
    print('Invalid command')

            







