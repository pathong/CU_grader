d = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
c = ["Red", "Yellow", "Pink", "Green", "Orange", "Blue", "Purple"]
for i in range(4):
    n = input()
    found =False 
    for j in range(len(d)):
        if d[j] == n:
            print(c[j])
            found = True
    if not found:
        print("Invalid day")
