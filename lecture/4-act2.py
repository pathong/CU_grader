n = input()
s = 0
t = 0
for i in range(len(n)):
    a = 0
    if n[i] == "+" or n[i] == "-" and i != 0 :
        a = int(n[t:i])
        t = i
    if i == len(n)-1:
        a = int(n[t:])
    s += a

print(s)
