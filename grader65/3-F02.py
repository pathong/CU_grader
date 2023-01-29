def choose(student1:list,student2:list):
    g = "FDCBA"
    def a_4(p:list):
        for i in range(len(p)):
            if isinstance(p[i], str) and p[i] in g:
                p[i] = g.index(p[i])
        return p

    a = a_4(student1)
    b = a_4(student2)

    def CheckPass(p:list)->bool:
        if p[2] >= g.index("A") and p[3] >= g.index("C") and p[4] >= g.index("C"):
            return True
        return False
         

    pa = CheckPass(a)
    pb = CheckPass(b)

    li  = []

    if not pa and not pb:
        pass
    elif pa and not pb:
        li.append(a[0])
    elif not pa and pb:
        li.append(b[0])
    else:
        if a[1] == b[1]:
            if a[3] == b[3]:
                if a[4] == b[4]:
                    li.append(a[0])
                    li.append(b[0])
                else:
                    li.append(a[0]) if int(a[4]) > int(b[4]) else li.append(b[0])
            else:
               li.append(a[0]) if int(a[3]) > int(b[3]) else li.append(b[0])
        else:
            li.append(a[0]) if float(a[1]) > float(b[1]) else li.append(b[0])


    return li



exec(input())
