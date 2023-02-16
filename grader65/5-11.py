l = ["0",'1','2','3','4','5','6','7','8','9']
n = input()
for _n in n:
    if _n in l:
        l.pop(l.index(_n))
print(",".join(l)) if len(l) > 0 else print("None")

