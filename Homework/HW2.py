def riemann_left(f,a:float,b:float, n:int):
    delX = (b-a)/n
    s = 0
    for i in range(n):
        s += f(a+i*delX)
    return s * delX
def riemann_right(f,a:float,b:float,n:int):
    delX = (b-a)/n
    s = 0
    for i in range(n):
        s += f(a + (i+1)*delX) 
    return s * delX
def riemann_mid(f,a:float,b:float,n:int):
    delX = (b-a)/n
    s = 0
    for i in range(n):
        s += f(a + (2*i+1)*delX/2) 
    return s * delX
def riemann_trap(f,a:float,b:float,n:int):
    delX = (b-a)/n
    s = 0
    s += f(a)
    s += f(b)
    for i in range(1,n):
        s += 2 * f(a + i*delX)
    return .5*delX*s
def estimate(riemann_sum_function, f, a:float, b:float, precision):
    n = 1
    while True:
        x = riemann_sum_function(f,a,b,n)
        y = riemann_sum_function(f,a,b,n+1)
        if round(x,precision) == round(y,precision):
            return [round(x,precision),n]
        n += 1
        


import math

def f1(x):
    return 0.5*(x**2)
def test_riemann_left_1():
    print('---riemann_left of math.sin---')
    x = riemann_left(math.sin, 0, 0.5*math.pi, 10)
    print(x, round(x, 10))
    x = riemann_left(math.sin, 0, 0.5*math.pi, 100)
    print(x, round(x, 10))
    x = riemann_left(math.sin, 0, 2*math.pi, 10)
    print(x, round(x, 10))
    x = riemann_left(math.sin, 0, 2*math.pi, 100)
    print(x, round(x, 10))

def test_riemann_left_2():
    print('---riemann_left of f1---')
    x = riemann_left(f1, 0, 4, 50)
    print(x, round(x, 10))
    x = riemann_left(f1, 0, 4, 500)
    print(x, round(x, 10))
    x = riemann_left(f1, 3, 10, 50)
    print(x, round(x, 10))
    x = riemann_left(f1, 3, 10, 500)
    print(x, round(x, 10))
#-----------------------------------------------------
def test_riemann_right_1():
    print('---riemann_right of math.sin---')
    x = riemann_right(math.sin, 0, 0.5*math.pi, 10)
    print(x, round(x, 10))
    x = riemann_right(math.sin, 0, 0.5*math.pi, 100)
    print(x, round(x, 10))
    x = riemann_right(math.sin, 0, 2*math.pi, 10)
    print(x, round(x, 10))
    x = riemann_right(math.sin, 0, 2*math.pi, 100)
    print(x, round(x, 10))

def test_riemann_right_2():
    print('---riemann_right of f1---')
    x = riemann_right(f1, 0, 4, 50)
    print(x, round(x, 10))
    x = riemann_right(f1, 0, 4, 500)
    print(x, round(x, 10))
    x = riemann_right(f1, 3, 10, 50)
    print(x, round(x, 10))
    x = riemann_right(f1, 3, 10, 500)
    print(x, round(x, 10))
#-----------------------------------------------------
def test_riemann_mid_1():
    print('---riemann_mid of math.sin---')
    x = riemann_mid(math.sin, 0, 0.5*math.pi, 10)
    print(x, round(x, 10))
    x = riemann_mid(math.sin, 0, 0.5*math.pi, 100)
    print(x, round(x, 10))
    x = riemann_mid(math.sin, 0, 2*math.pi, 10)
    print(x, round(x, 10))
    x = riemann_mid(math.sin, 0, 2*math.pi, 100)
    print(x, round(x, 10))

def test_riemann_mid_2():
    print('---riemann_mid of f1---')
    x = riemann_mid(f1, 0, 4, 50)
    print(x, round(x, 10))
    x = riemann_mid(f1, 0, 4, 500)
    print(x, round(x, 10))
    x = riemann_mid(f1, 3, 10, 50)
    print(x, round(x, 10))
    x = riemann_mid(f1, 3, 10, 500)
    print(x, round(x, 10))
#-----------------------------------------------------
def test_riemann_trap_1():
    print('---riemann_trap of math.sin---')
    x = riemann_trap(math.sin, 0, 0.5*math.pi, 10)
    print(x, round(x, 10))
    x = riemann_trap(math.sin, 0, 0.5*math.pi, 100)
    print(x, round(x, 10))
    x = riemann_trap(math.sin, 0, 2*math.pi, 10)
    print(x, round(x, 10))
    x = riemann_trap(math.sin, 0, 2*math.pi, 100)
    print(x, round(x, 10))

def test_riemann_trap_2():
    print('---riemann_trap of f1---')
    x = riemann_trap(f1, 0, 4, 50)
    print(x, round(x, 10))
    x = riemann_trap(f1, 0, 4, 500)
    print(x, round(x, 10))
    x = riemann_trap(f1, 3, 10, 50)
    print(x, round(x, 10))
    x = riemann_trap(f1, 3, 10, 500)
    print(x, round(x, 10))
#-----------------------------------------------------
def test_estimate_1():
    print('### test estimate of math.sin ###')
    print('---riemann_left---')
    for precision in [1, 3, 5, 7]:
        print(estimate(riemann_left, math.sin, 0, 0.5*math.pi, precision))
    print('---riemann_right---')
    for precision in [1, 3, 5, 7]:
        print(estimate(riemann_right, math.sin, 0, 0.5*math.pi, precision))
    print('---riemann_mid---')
    for precision in [1, 3, 5, 7]:
        print(estimate(riemann_mid, math.sin, 0, 0.5*math.pi, precision))
    print('---riemann_trap---')
    for precision in [1, 3, 5, 7]:
        print(estimate(riemann_trap, math.sin, 0, 0.5*math.pi, precision))
#-----------------------------------------------------
def test_estimate_2():
    print('### test estimate of f1 ###')
    print('---riemann_left---')
    for precision in [2, 4, 6]:
        print(estimate(riemann_left, f1, 2, 5, precision))
    print('---riemann_right---')
    for precision in [2, 4, 6]:
        print(estimate(riemann_right, f1, 2, 5, precision))
    print('---riemann_mid---')
    for precision in [2, 4, 6]:
        print(estimate(riemann_mid, f1, 2, 5, precision))
    print('---riemann_trap---')
    for precision in [2, 4, 6]:
        print(estimate(riemann_trap, f1, 2, 5, precision))
test_riemann_left_1()
test_riemann_left_2()
test_riemann_right_1()
test_riemann_right_2()
test_riemann_mid_1()
test_riemann_mid_2()
test_riemann_trap_1()
test_riemann_trap_2()
test_estimate_1()
test_estimate_2()
