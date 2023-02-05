m = int(input())
sc = [0,0]
win = ""
def Compare(a,b):
    # -1 = tie, 0 = a win 1 = b win
    if a == b: return -1
    elif a == "R":
        if b == "P": return 1
        elif b == "S": return 0
    elif a == "P":
        if b == "S": return 1
        elif b == "R": return 0
    elif a =="S":
        if b == "P": return 0
        elif b == "R": return 1
    return -1
for i in range(3*m):
    x = input().strip().split()
    re = Compare(x[0],x[1])
    if re != -1: sc[re] += 1

    if sc[0] >= m or sc[1] >= m:
        win = "1" if sc[0] > sc[1] else "2"
        break

print(" ".join(list(map(str,sc))))
if win != "":
    print("Player {} wins".format(win))
else:
    print("Tie")








