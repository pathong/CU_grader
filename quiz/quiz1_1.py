x = list(map(int, input().split()))
k = int(input())


s=0
su = []
li = [x[0]]
for i in range(1,len(x)):
    print(x[i])
    if x[i] == li[0]:
        li.append(x[i])
    elif x[i] != li[0]:
        su.append(li)
        li = []
        li.append(x[i])
        if i == len(x)-1 : su.append(li)

for l in su:
    if len(l) < k:
        s+=sum(l)

print(su)
print(s)
    


    
