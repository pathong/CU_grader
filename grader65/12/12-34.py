class piggybank:
    def __init__(self) -> None:
        self.coin = dict()

    def add(self,v,n):
        if sum(list(self.coin.values())) + n > 100 :return False

        v = float(v)
        if v not in self.coin.keys():
            self.coin[v] = 0
        self.coin[v] += n
        return True
    
    def __float__(self):
        s = 0
        for k,v in self.coin.items():
            s += k*v
        return float(s)
    def __int__(self):
        return int(float(self))

    def __str__(self):
        li = []
        order = sorted(self.coin.keys())

        for o in order:
            li.append("{}:{}".format(o,self.coin[o]))
        return "{" + ', '.join(li) + "}"


cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)

