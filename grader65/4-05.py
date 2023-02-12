n = input()
w = input()
c = 0
s = '"(),.\''
li = w.strip().split()
for l in li:
    if n in l:
        while l[0] in s or l[-1] in s:
            if l[0] in s:
                l = l[1:]
            if l[-1] in s:
                l = l[:-1]
        if l == n:
            c +=1

print(c)



