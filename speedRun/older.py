m = "January,February,March,April,May,June,July,August,September,October,November,December"
li = m.split(",")

a = input().split()
a[2] = a[2][:-1]
b = input().split()
b[2] = b[2][:-1]

if int(a[3]) < int(b[3]):
    print(a[0])
elif int(a[3]) > int(b[3]):
    print(b[0])
else:
    if int(a[2]) < int(b[2]):
        print(a[0])
    elif int(a[2]) > int(b[2]):
        print(b[0])
    else:
        if li.index(a[1]) < li.index(b[1]):
            print(a[0])
        elif li.index(a[1]) > li.index(b[1]):
            print(b[0])
        else:
            print("{} {}".format(a[0],b[0]))



