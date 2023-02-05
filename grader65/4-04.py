a='([)]'
b='[(])'

n = input()
an = ""
for i in range(len(n)):
    _n = n[i]
    if _n not in a:
        an+=_n
    else:
        an += b[a.index(_n)]

print(an)
