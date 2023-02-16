t = [float(i) for i in input().split()]
S = []
for j in range(0,len(t)) :
        S.append(t[j])
        if j + 1 < len(t) :
            S.append((t[j]+t[j+1])/2)
print(S)
