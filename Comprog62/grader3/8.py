N = int(input())
_n = N 
party= dict()
votes = dict()
while _n > 0:
    _ = input()
    party[_] = list()
    _n-=1

p = int(input())
_p = p
while _p > 0:
    _name,_pa = input().strip().split(" ")
    party[_pa].append(_name)
    _p-=1

nv= int(input())
_nv = nv
while _nv > 0:
    _name,_v = input().strip().split(" ")
    votes[_name] = _v
    _nv-=1

for name, li in party.items():
    compare_vote = {"Y":0,"X":0,"N":0}
    for people,vote in votes.items():
        if people in li:
            if vote in list(compare_vote.keys()):
                compare_vote[vote] += 1

    sortValue = sorted(compare_vote.values(), reverse=True)
    print(name)
    ans = ""
    if sortValue[0] == sortValue[1]:
        ans = "Inconclusive"
    else:
        m = ""
        cob = []
        for c,v in compare_vote.items():
            if sortValue[0] == v:
                m = c
        for people,vote in votes.items():
            if people in li:
                if vote != m:
                    cob.append(people)

        ans = ",".join(cob) if len(cob) > 0 else "No Cobra"
    print(ans)







