n = int(input())
dat = dict()
for _ in range(n):
    inp = input().split()
    dat[inp[0]] = set(inp[1].split(","))
while True:
    inp = input()
    if inp == "q": break
    inp = inp.split()
    print(sorted(list(dat[inp[0]] & dat[inp[1]])))

