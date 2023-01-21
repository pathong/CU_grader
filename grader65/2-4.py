a = input()
b = int(input())

d = b-len(a)
if d > 0:
    a = "0"*d + a

print(a)
