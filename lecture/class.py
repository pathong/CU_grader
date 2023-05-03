class A:
    s = set()
    def ap(self,a):
        self.s.add(a)
        print(self.s)

a = A()
b = A()
a.ap('f')
b.ap('b')



