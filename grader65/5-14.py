li = list(map(int,input().split()))
c = 0
for i in range(1,len(li)-1):
    if li[i] > li[i-1] and li[i] > li[i+1]:
        c+=1

print(c)

