# RotateString
o = input()
n = int(input())
matrix = []
invalid = False 
for i in range(n):
    inp = input().strip()
    li_inp = []
    for _ in inp:
        li_inp.append(_)
    matrix.append(li_inp)

l = len(matrix[0])
for li in matrix:
    if len(li) != l:
        invalid = True
        break


ans = []
if invalid == False:
    if o == "90":
        for j in range(len(matrix[0])):
            li = []
            for i in range(n-1,-1,-1):
                li.append(matrix[i][j])
            ans.append(li)
    elif o == "180":
        for i in range(n-1,-1,-1):
            li = []
            for j in range(len(matrix[0])-1, -1, -1):
                li.append(matrix[i][j])
            ans.append(li)
    elif o == "flip":
        for i in range(n):
            li = []
            for j in range(len(matrix[0])-1, -1, -1):
                li.append(matrix[i][j])
            ans.append(li)
    for i in range(len(ans)):
        print("".join(ans[i]))
else:
    print("Invalid size")


