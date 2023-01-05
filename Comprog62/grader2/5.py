import math
def Permutation(p:str):
    t = math.factorial(len(p))
    b = 1

    ac = []
    for _p in p:
        if _p in ac : continue

        c = 0
        for f in p:
            if f == _p:
                c+=1
        ac.append(_p)
        b *= math.factorial(c)

    return int(t/b)
    


def Bids(p1:dict, p2:dict):
    check = []
    r1 = 0
    r2 = 0
    for n in p1:
        if n not in p2.keys():
            r1 += p1[n]
        else:
            if p1[n] > p2[n] : r1 += p1[n]
            elif p1[n] < p2[n] : r2 += p2[n]
        check.append(n)
        
    for n in p2:
        if n in check: continue
        r2 += p2[n]

    return [r1,r2]


def AdvFind(s:str, p:str):
    ans = []
    for i in range(len(p)-len(s)+1):
        if p[i:i+len(s)] == s:
            ans.append(i)
    return ans if len(ans)>0 else -1

print(Permutation("GETAEVERYONE"))
print(Permutation("SUSUTUKKHON"))
print(Bids({"Vest" : 40, "Watch" : 500}, {"Vest" : 50}))
print(Bids({"A" : 1, "B" : 7}, {"B" : 7, "A" : 2, "C" : 5}))
print(AdvFind("sp", "spSPspSpspSP"))
print(AdvFind("A", "All_A_Susu_NA"))
print(Permutation("AAAAAA"))
print(Bids({"A":1, "B":2, "C":5}, {"B":2, "A":1, "C":5}))
print(Bids({"Mask" : 50, "Watch" : 1}, {}))
print(AdvFind("F", "All_A_Susu_NA"))
