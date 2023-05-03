n = int(input())
li = []
for _ in range(n):
    li.append(set(map(int, input().split())))
if len(li) != 0:
    un = li[0]
    inter = li[0]

    for l in li:
        un = un | l
        inter = inter & l
    print(len(un))
    print(len(inter))
else:
    print(0)
    print(0)

    

