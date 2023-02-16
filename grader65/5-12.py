n = int(input())
rn = ["Robert","William","James","John",'Margaret','Edward','Sarah','Andrew','Anthony','Deborah']
nn = ['Dick','Bill','Jim','Jack','Peggy','Ed','Sally','Andy','Tony','Debbie']
for _ in range(n):
    na = input()
    if na in rn:
        print(nn[rn.index(na)])
    elif na in nn:
        print(rn[nn.index(na)])
    else:
        print("Not found")



