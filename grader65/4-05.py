n = input()
w = input()
c = 0
s = '"(),.\''
li = w.strip().split()
for l in li:
    for _l in l:
        if _l in s:
            i = l.index(_l)
            l = l[:i] + " " + l[i+1:]
    a = l.split()
    for _a in a:
        if _a == n:
            c+=1
print(c)



