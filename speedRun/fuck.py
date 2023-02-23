w = input().strip()
op = "+-"
s = 0
e = w[0]
for i in range(1,len(w)):
    if w[i] not in op:
        e += w[i]
    elif w[i] in op:
        s += int(e)
        
        e = w[i]
    
s += int(e)

print(s)
        
        
        
        