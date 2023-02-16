li = list(map(float,input().split()))
if len(li) == 1:
    print(li)
else:
    ans = []
    for i in range(len(li) - 1):
        ans.append(li[i])
        ans.append((li[i] + li[i+1])/2)
        ans.append(li[i+1])
    print(ans)
