class Complex:
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b
    def __str__(self) -> str:
        front = ""
        back = ""
        if self.a != 0:
            if self.a < 0:
                front += '-'
            front += str(abs(self.a))


        if self.b !=0:
            if self.b < 0:
                back += '-'
            elif self.a != 0 and b>0:
                back += '+'
            if abs(self.b) != 1:
                back += str(abs(self.b))
            back += 'i'

        if self.b == 0 and self.a == 0: front = '0'
        return front + back 




    def __add__(self, rhs):
        return Complex(self.a + rhs.a, self.b + rhs.b)
    def __mul__(self,rhs):
        return Complex(self.a * rhs.a - self.b*rhs.b, self.a*rhs.b + self.b*rhs.a)
    def __truediv__(self,rhs):
        a = self.a
        b = self.b
        c = rhs.a
        d = rhs.b
        return Complex((a*c + b*d)/(c**2 + d**2), (-a*d + b*c)/(c**2 +  d**2))



t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)

        

