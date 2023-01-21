s = input()
a = int(s[3] + s[10] + s[17] + s[24] + s[31])
b = int(s[7] + s[12] + s[17] + s[22] + s[27])
c = a+b+10000
t = int(str(c)[-2])
tt = int(str(c)[-3])
ttt = int(str(c)[-4])
tttt = str(c)[-4:-1]

li = 'ABCDEFGHIJ'
c = li[(t + tt + ttt) % 10]

print(tttt+c)
