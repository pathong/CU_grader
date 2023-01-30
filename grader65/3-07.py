n = int(input())

if n < 1000:
    print(n)
elif n < 1000000:
    if n >= 10000 or n % 1000 == 0:
        print(str(round(n/1000)) + "K")
    else:
        print(str(round(n/1000, 1)) + "K")
elif n < 1000000000:
    if n >= 10000000 or n % 1000000 == 0:
        print(str(round(n/1000000)) + "M")
    else:
        print(str(round(n/1000000, 1)) + "M")
elif n >= 1000000000:
    if n >= 10000000000 or n %1000000000 == 0:
        print(str(round(n/1000000000)) + "B")
    else:
        print(str(round(n/1000000000,1)) + "B")

