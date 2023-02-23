def make_int_list(x): return list(map(int, x.split()))
def is_odd(e): return e%2!=0
def odd_list(alist): return list(filter( lambda x: x%2 !=0, alist))
def sum_square(alist): return sum(list(map(lambda x : x*x,alist)))
exec(input())
