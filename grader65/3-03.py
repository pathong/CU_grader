n = [float(e) for e in input().split()]
_min = 999
a = 0
_max = 0
b = 0
for i in range(len(n)):
    if n[i] <= _min:
        _min = n[i]
        a = i
    if n[i] >= _max:
        _max = n[i]
        b = i



c = 0
for i in range(len(n)):
    if i != a and i != b:
        c += n[i]

print(round(c/2,2))


        
    
