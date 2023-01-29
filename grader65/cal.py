n = 0
b = 1
for i in range(10000): 
    b = 0
    for j in range(i+1):
        b += 1/(j+1)

    n += 1/b
    print(n)
    
        
        
    
