score = 'XRYGWBPK'
summary = [0,0]
while True:
    n = input()
    player = int(n[0]) -1
    for s in n[1:]:summary[player] += score.find(s)
    if n[1] == "K": break
print(" ".join(list(map(str,summary))))
if summary[0] != summary[1]:print("Player {} wins".format(summary.index(max(summary)) + 1))
else: print("Tie")


