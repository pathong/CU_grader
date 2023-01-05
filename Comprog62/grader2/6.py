def Mult_Const(p:dict,k:int)->dict:
    for x in p:
        p[x] *= k
    return p


def Mult_Mono(_p1:dict ,_p2:dict)->dict:
    ans = dict()
    for a in _p1:
        for b in _p2:
            if a+b not in ans.keys():
                ans[a+b] = 0
            ans[a+b] += _p1[a] * _p2[b]
    return ans



def Add_Poly(_p1:dict, _p2:dict)->dict:
    for a in _p1:
        if a not in _p2.keys():
            _p2[a] = 0
        _p2[a] += _p1[a]
    return _p2


def Mult_Poly(_p1:dict, _p2:dict)->dict:
    ## IT'S FUCKING THE SAME DUDE
    ans = dict()
    for a in _p1:
        for b in _p2:
            if a+b not in ans.keys():
                ans[a+b] = 0
            ans[a+b] += _p1[a] * _p2[b]
    return ans

            
k1 = 7
k2 = -5
p1 = {3: 5} 
p2 = {5: 3, 3: -1, 0: 5} 
p3 = {3: 1, 2: 2, 1: 5, 0: -5} 
p4 = {7: 2, 5: -7} 
p5 = {2: 7, 0: 9}

print(Mult_Mono(p2, p1))
print(Mult_Mono (p3, p1))
print(Mult_Const(p2, k1))
print(Mult_Const(p1, k2))
print(Add_Poly(p2, p3))
print(Add_Poly(p3, p1))
print(Mult_Poly(p4, p4))
print(Mult_Poly(p4, p5))




