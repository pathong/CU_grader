li = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
n = input().split("/")
print("{0} {1}, {2}".format(li[int(n[1])-1], n[0], n[2]))

