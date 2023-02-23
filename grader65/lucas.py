blue = " "
red = " "
Z = 0
while True:
    a = input()

    if a == "Zig-Zag": break

    x,y = a.split()

    Z+=1
red = [int(e) for e in red.split()]
blue =[int(e) for e in blue.split()]
if a == "Zig-Zag":
    print(min(red),max(blue))
elif a == "Zag-Zig":
    print(min(blue),max(red))
