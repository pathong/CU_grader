class Ota():
    def __init__(self,_n) -> None:
        self.name = _n
        self.votes = dict()
    def vote(self, who, vote):
        if who not in self.votes.keys():
            self.votes[who] = 0
        self.votes[who] += vote
    def GetKami(self):
        maxV = max(self.votes.values())
        li = []
        for b,v in self.votes.items():
            if v == maxV:
                li.append(b)
        li.sort()
        kami = li[0]

        for b in bnk_li:
            if b.name == kami:
                b.kami_count += 1

class Bnk():
    def __init__(self,_n) -> None:
        self.name = _n
        self.ota_set = set()
        self.kami_count =0
        self.votes = 0
    def GetVoted(self, who, vote):
        self.votes += vote
        self.ota_set.add(who)


ota_li = []
bnk_li = []

mode = ''
while True:
    inp = input().split()
    if len(inp) <= 1:
        mode = inp[0]
        break
    ota_n = inp[0]; bnk_n = inp[1]; v = int(inp[2])

    ## ota list
    isOtaInList = False 
    for o in ota_li:
        if o.name == ota_n:
            ## already have
            isOtaInList = True
            o.vote(bnk_n, v)
    if not isOtaInList:
        curr_ota = Ota(ota_n)
        curr_ota.vote(bnk_n,v)
        ota_li.append(curr_ota)

    ## bnk list
    isBnkInList = False
    for b in bnk_li:
        if b.name == bnk_n:
            isBnkInList = True
            b.GetVoted(ota_n, v)
    if not isBnkInList:
        curr_bnk = Bnk(bnk_n)
        curr_bnk.GetVoted(ota_n,v)
        bnk_li.append(curr_bnk)


## Calculate for kami
for o in ota_li:
    o.GetKami()

            

def mode1():
    ts_li = []
    for b in bnk_li:
        ts_li.append([-b.votes, b.name])
    ts_li.sort()
    ans = []
    for t in ts_li[:3]:
        ans.append(t[1])
    return ", ".join(ans)



def mode2():
    ts_li = []
    for b in bnk_li:
        ts_li.append([-len(b.ota_set), b.name])
    ts_li.sort()
    ans = []
    for t in ts_li[:3]:
        ans.append(t[1])
    return ", ".join(ans)


def mode3():
    ts_li = []
    for b in bnk_li:
        ts_li.append([-b.kami_count, b.name])
    ts_li.sort()
    ans = []
    for t in ts_li[:3]:
        ans.append(t[1])
    return ", ".join(ans)


if mode == '1':
    print(mode1())
if mode == '2':
    print(mode2())
if mode == '3':
    print(mode3())
