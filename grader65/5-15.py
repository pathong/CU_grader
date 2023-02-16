li = list(map(int,input().split()))
li.sort()
ans = []
c = 0
t = li[0]
for l in li:
    if l != t: 
        c+=1
        t = l


    if l not in ans and len(ans) < 10:
        ans.append(l)

print(c+1)
print(ans)


