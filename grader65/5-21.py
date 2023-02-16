ids = []
grade = []
uids = []
g = 'FDCBA'
while True:
    n = input()
    if n == "q": break
    l = n.split()
    ids.append(l[0])
    grade.append(l[1])

uids = input().split()


for i in range(len(ids)):
    for u in uids:
        if ids[i] == u:
            #check grade
            if "+" in grade[i]:
                grade[i] = g[g.index(grade[i][0]) + 1]
            else:
                if grade[i] == "F":
                    grade[i] = g[g.index(grade[i][0]) + 1]
                elif grade[i] != "A":
                    grade[i] = grade[i] + "+"
                    
    print(ids[i], grade[i])


