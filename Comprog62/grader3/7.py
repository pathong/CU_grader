n = int(input())
mat = []
re = []
_n = n
while _n>0:
    mat.append(input().split(" "))
    _n-=1

for i in range(n):
    l = []
    for j in range(n):
        if mat[i][j] == "1":
            l.append("9")
        elif mat[i][j] == "0":
            _sum = 0
            for x in range(i-1, i+2):
                if x < 0: continue
                if x >= n: continue
                for y in range(j-1, j+2):
                    if y < 0: continue
                    if y >= n: continue
                    if x == i and y == j:continue
                    if mat[x][y] == "1":
                        _sum+=1
            l.append(str(_sum))
    re.append(l)


for li in re:
    print(" ".join(li))


