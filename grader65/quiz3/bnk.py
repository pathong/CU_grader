class ota():
    # votes = list() 
    votes = dict()
    name = ""
    kami = ""

    def __init__(self,_name:str, _bnk:str, vote:int) -> None:
        self.name = _name
        if _bnk not in self.votes.keys():
            self.votes[_bnk] = 0
        self.votes[_bnk] += vote

        AddBnkToList(_bnk,_ota,vote)
    def GetKami(self):
        kami_nor = []
        max_vote = max(self.votes.values())
        for b,v in self.votes.items():
            if v == max_vote:
                kami_nor.append(b)
        kami_nor.sort()
        self.kami = kami_nor[0]

class bnk():
    name = ""
    vote = 0
    ota_set = set()
    kamiCount = 0
    def __init__(self,_name:str) -> None:
        self.name = _name
    def AddVote(self, increment:int, who:str):
        self.vote += increment
        self.ota_set.add(who)
    def GetHowManyKami(self):
        for o in ota_list:
            if o.kami == self.name:
                self.kamiCount += 1
        return self.kamiCount


        
def AddBnkToList(bnk_name, ota_name, initial_vote):
    for b in bnk_list:
        if b.name == bnk_name:
            b.AddVote(vote, ota_name)
            return
    ## not in list
    curr_bnk = bnk(bnk_name)
    curr_bnk.AddVote(initial_vote,ota_name)
    bnk_list.append(curr_bnk)
    


def IsOtaExist(name):
    for o in ota_list:
        if o.name == name:
            return True
    return False

def mode1():
    ts_list = []
    for b in bnk_list:
        ts_list.append([-b.vote, b.name])
    ts_list.sort()
    print(ts_list)
    ans = []
    for t in ts_list[:3]:
        ans.append(t[1])
    return ans

def mode2():
    ts_list = []
    for b in bnk_list:
        ts_list.append([-len(b.ota_set), b.name])
    ts_list.sort()
    print(ts_list)
    ans = []
    ans = []
    for t in ts_list[:3]:
        ans.append(t[1])
    return ans


def mode3():
    ts_list = []
    for b in bnk_list:
        ts_list.append([-b.GetHowManyKami(), b.name])
    ts_list.sort()
    print(ts_list)
    ans = []
    ans = []
    for t in ts_list[:3]:
        ans.append(t[1])
    return ans

ota_list = []
bnk_list = []
mode = ""

while True:
    e = input().split()
    if len(e) <= 1:
        mode = e[0]
        break

    _ota = e[0]; _bnk = e[1]; vote = int(e[2])


    if not IsOtaExist(_ota):
        ota_list.append(ota(_ota, _bnk, vote))

# print(ota_list)
# print(bnk_list)

if mode == '1':
    print(", ".join(mode1()))

if mode == '2':
    print(", ".join(mode2()))

if mode == '3':
    print(", ".join(mode3()))




    








