class Party():
    def __init__(self, _partyName) -> None:
        self.partyName = _partyName
        self.persons = dict()
        self.compareVotes ={"Y":0, "X":0, "N":0} 
        self.cob = []
    def AddPerson(self, _name):
        self.persons[_name] = "-"
    def AssignVote(self, _name, _vote):
        for n in self.persons.keys():
            if n == _name:
                self.persons[n] = _vote
                self.compareVotes[_vote] +=1
    def GetMaxVote(self): 
        sortedValues = sorted(self.compareVotes.values(), reverse=True)
        if sortedValues[0] == sortedValues[1]:
            return "Inconclusive"
        else:
            for c,v in self.compareVotes.items():
                if v == sortedValues[0]:
                    return c
    def GetAns(self):
        m = self.GetMaxVote()
        if m == "Inconclusive":
            return m
        else:
            for p,v in self.persons.items():
                if v == "-": continue
                if v != m:
                    self.cob.append(p)
            return ", ".join(self.cob) if len(self.cob) > 0 else "No Cobra"

partys = []

n = int(input())
while n > 0:
    _ = input()
    partys.append(Party(_))
    n-=1

p = int(input())
while p>0:
    _name, _party = input().strip().split(" ")
    for pa in partys:
        if pa.partyName == _party:
            pa.AddPerson(_name)
    p -= 1

nv = int(input())
while nv>0:
    _name,_vote = input().strip().split(" ")
    for party in partys:
        party.AssignVote(_name,_vote)
    nv -= 1 

for party in partys:
    print(party.partyName)
    print(party.GetAns())
    






