m = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
a = input().strip().split()
a[2] = a[2][:-1]
b = input().strip().split()
b[2] = b[2][:-1]

ans = []
if int(a[3]) < int(b[3]):
    ans.append(a[0])
elif int(a[3]) > int(b[3]):
    ans.append(b[0])
else:
    if m.index(a[1]) < m.index(b[1]):
        ans.append(a[0])
    elif m.index(a[1]) > m.index(b[1]): 
        ans.append(b[0])
    else:
        if int(a[2]) < int(b[2]):
            ans.append(a[0])
        elif int(a[2]) > int(b[2]):
            ans.append(b[0])
        else:
            ans.append(a[0])
            ans.append(b[0])

print(" ".join(ans))



