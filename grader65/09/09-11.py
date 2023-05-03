n = int(input())
for _ in range(n):
    w = input()
    c = 0
    for i in range(len(w)):
        if w[i] != '.':
            w = w[i-round(c/2):]
            break
        c+=1
    print(w)
