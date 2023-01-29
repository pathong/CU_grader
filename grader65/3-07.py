n = int(input())

if n < 1000:
    print(n)
elif n < 1000000:
    print(str(round(n/1000, 1)))

elif n > 1000000000:
