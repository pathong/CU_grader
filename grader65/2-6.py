a = input()
a = list(map(float, a[1:-1].split(", ")))
b = input()
b = list(map(float, b[1:-1].split(", ")))
an = []
for i in range(len(a)):
    an.append(a[i] + b[i])
print("{0} + {1} = {2}".format(a,b,an))

