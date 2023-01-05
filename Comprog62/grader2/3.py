n = int(input())
ds = []
c = 0
while n > 0:
    ds.append(int(input()))
    n-=1
for i in range(len(ds)):
    l = i-1
    r = 0 if i == len(ds)-1 else i+1

    if ds[i] > ds[l] and ds[i] > ds[r]:
        c+=1
        print(i+1)

if c == 0: print('No hole')

