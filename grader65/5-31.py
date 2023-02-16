w = input().split()
o = input()

for _o in o:
    h = round(len(w)/2)
    h1 = w[:h]
    h2 = w[h:]
    if "C" in _o:
        w = h2 + h1
    elif "S" in _o:
        l = []
        for i in range(round(h)):
            l.append(h1[i])
            l.append(h2[i])
        w = l


print(" ".join(w))


             



