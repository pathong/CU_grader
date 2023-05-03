n = int(input())
sw = set()
sl = set()
for _ in range(n):
    w,l = input().split()
    sw.add(w)
    sl.add(l)

print(sorted(list(sw-sl)))
    

