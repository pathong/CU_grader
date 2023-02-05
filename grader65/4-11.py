n = input()
li = []
c = 0
t = n[0] 
li.append(t)
for _n in n:
    if _n == t:
        c +=1
    else:
        li.append(str(c))
        li.append(_n)
        t = _n
        c = 1 
li.append(str(c))

    

print(" ".join(li))
