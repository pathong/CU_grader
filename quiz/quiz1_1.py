x = list(map(int, input().split()))
k = int(input())
s = 0

t = x[0]
li = []
for i in range(len(x)):
    if x[i] == t:
        li.append(x[i])
    else:
        if len(li) < k:
            s += sum(li)
        t = x[i]
        li = [x[i]]
if len(li) < k:
    s += sum(li)
print(s)
        
    


    