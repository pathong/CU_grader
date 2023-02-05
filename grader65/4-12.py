n = int(input())
a = []
b = []
z,o = 0,1
for _ in range(n):
    inp = list(map(int,input().split()))
    a.append(inp[z])
    b.append(inp[o])
    z,o = o,z

t = input()

_min = 0
_max = 0
if t == "Zig-Zag":
    _min = min(a)
    _max = max(b)
elif t == "Zag-Zig":
    _min = min(b)
    _max = max(a)
print("{} {}".format(str(_min),str(_max)))


