g = "FDCBA"
n = input().split()
s = 0
for _ in n: s += g.index(_)
print(round(s/len(n),2))

