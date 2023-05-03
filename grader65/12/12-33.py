class piggybank:
    order = [1,2,5,10]
    def __init__(self) -> None:
        self.bank = {1:0,2:0,5:0,10:0}
        pass
    def add1(self,n): self.bank[1] += n
    def add2(self,n): self.bank[2] += n
    def add5(self,n): self.bank[5] += n
    def add10(self,n): self.bank[10] += n

    def __int__(self):
        s = 0
        for k,v in self.bank.items():
            s += v*k
        return s
    def __lt__(self, rhs):
        return int(self) < int(rhs)
    def __str__(self):
        return '{' + "1:{}, 2:{}, 5:{}, 10:{}".format(self.bank[1],self.bank[2], self.bank[5], self.bank[10]) + "}"



cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)

