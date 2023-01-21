s = input()
a = int(s[3] + s[10] + s[17] + s[24] + s[31])
b = int(s[7] + s[12] + s[17] + s[22] + s[27])
c = a+b+10000

t = str(c)[-4:-1]
s = 0
for i in t:
    s += int(i)

li = 'ABCDEFGHIJ'
l = li[s % 10]

print(t+l)
