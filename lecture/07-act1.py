# print(" ".join(list(map(lambda n: n[0].upper() + n[1:].lower(), input().replace(" ", "").split(",")))))


s = input()
s = s.replace(" ","")
s = s.split(",")
for i in range(len(s)):
    f = s[i][0].upper()
    r = s[i][1:].lower()
    s[i] = f + r
s = " ".join(s)
print(s)
    



