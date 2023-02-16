n = int(input())

re = []

for i in range(n):
    li = [float(e) for e in input().split()]
    dis = (li[0] **2 + li[1] ** 2 ) ** .5
    re.append([dis,i+1, li])

re.sort()
ans = re[2]
print("#{}: ({}, {})".format(ans[1],ans[2][0], ans[2][1]))


