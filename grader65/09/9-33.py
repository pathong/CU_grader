def add_poly(p1,p2):
    ans = []
    for i in p1:
        isFound = False
        for j in p2:
            if i[1] == j[1]:
                isFound = True
                s = i[0] + j[0]
                degree = i[1]
                ans.append([degree, (s,degree)])
                break
        if not isFound:
            ans.append([i[1], i])
    for j in p2:
        isFound = False
        for a in ans:
            if j[1] == a[1][1]:
                isFound = True
        if not isFound:
            ans.append([j[1], j])

    ## finish raw
    ans.sort(reverse=True)
    actual = []
    for a in ans:
        if a[1][0] != 0:
            actual.append(a[1])
    return actual 

def mult_poly(p1,p2):
    if len(p1) == 0 or len(p2) ==0: return []
    not_sum = []
    for i in p1:
        new_poly = []
        for j in p2:
            new_poly.append((i[0]*j[0], i[1]+j[1]))
        not_sum.append(new_poly)

    ans = not_sum[0]
    for ns in not_sum[1:]:
        ans = add_poly(ans, ns)
    return ans

for i in range(3):
    exec(input().strip())

