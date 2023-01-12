def sqrt_n_times(x, n):
    for i in range(n):
        x = x**(1/2)
    return x
def cube_root(y):
    _pow = (1/4)
    __pow = 1
    for i in range(5):
        __pow *= 1 + 1/(2**(2**(i+1)))
    return y ** (_pow * __pow)

def main():
    q = float(input())
    print(cube_root(q))
exec(input()) # DON'T remove this line
