def missing_digits(n):

    l = ["0",'1','2','3','4','5','6','7','8','9']
    for _n in n:
        if _n in l:
            l.pop(l.index(_n))
    return list(map(int, l))


exec(input())
