def convex_polygon_area(p):
    a = 0
    b = 0
    for i in range(len(p)):
        if i + 1 < len(p):
            a += p[i][0] * p[i+1][1]
            b += p[i][1] * p[i+1][0]
        elif i+1 == len(p):
            a += p[i][0] * p[0][1]
            b += p[i][1] * p[0][0]

    return .5* abs(a-b)


# print(convex_polygon_area([[0,0], [0,3], [4,0]]))
# print(convex_polygon_area([[0,0], [4,0], [0,3]]))


def is_heterogram(s):
    s = s.lower()
    for _s in s:
        if not _s.isalpha():continue
        if s.count(_s) > 1: return False
    return True

# print(is_heterogram("The big dwarf only jumps."))
# print(is_heterogram("Java"))


def replace_ignorecase(s,a,b):
    nw = ""
    i = 0
    la = len(a)
    while True:
        check = s[i:i+la]
        if check.lower() != a.lower():
            nw += s[i]
            i+=1
        else:
            nw += b
            i+=la
        if i >= len(s): 
            return nw

def top3(votes):
    score = [0,0,0]
    name = ['z','z','z']
    
    for k,v in votes.items():
        for i in range(3):
            if v > score[i]:
                score.insert(i,v)
                name.insert(i,k)
                break
            elif v == score[i]:
                if k < name[i]:
                    score.insert(i,v)
                    name.insert(i,k)
                    break
        score = score[:3]
        name = name[:3]
    return name


for k in range(2):
    exec(input().strip())



