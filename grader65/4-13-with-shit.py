z,o = 0,1
min_a = 999999
min_b = 999999
max_a = -99999
max_b = -99999
t = ""
while True:
    inp = input()
    if inp != "Zig-Zag" and inp != "Zag-Zig":
        inp = list(map(int, inp.split()))
    else:
        t = inp
        break
    a = inp[z]
    b = inp[o]
    min_a = min(min_a, a)
    max_a = max(max_a, a)
    min_b = min(min_b, b)
    max_b = max(max_b, b)
    z,o = o,z


a1 = min_a if t == "Zig-Zag" else min_b
a2 = max_b if t == "Zig-Zag" else max_a

print("{} {}".format(str(a1), str(a2)))

