m= int(input())
p1=0
p2=0
win = ""
for _ in range(3*m):

    a,b = input().split()
    
    if a == "R":
        if b == "P":
            p2 +=1
        if b == "S":
            p1 += 1
    if a == "P":
        if b == "S":
            p2 +=1
        if b == "R":
            p1 += 1
    if a == "S":
        if b == "R":
            p2 +=1
        if b == "P":
            p1 += 1
    if p1 == m:
        win ='1' 
        break
    elif p2 == m:
        win = "2"
        break
    
print("{} {}".format(p1,p2))
if win != "":
    print("Player {} wins".format(win))
else:
    print("Tie")
