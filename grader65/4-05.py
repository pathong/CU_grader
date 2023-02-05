n = input()
w = input()

ln = len(n)

c = 0
i = 0
while True:
    if w[i:i+ln] == n:
        c += 1
    if i+ln >= len(w):
        break;
    i += 1
print(c)
