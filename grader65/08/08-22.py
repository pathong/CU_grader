N = int(input())
stock = dict()

for _ in range(N):
    inp = input().strip().split()
    stock[inp[0]] = int(inp[1])

M = int(input())
sellList = dict()
for _ in range(M):
    inp = input().strip().split()
    if inp[0] in stock.keys():
        ## create keys
        if inp[0] not in sellList.keys():
            sellList[inp[0]] = 0
        ## increase value
        sellList[inp[0]] += stock[inp[0]] * int(inp[1]) # price * amount


if len(sellList.keys()) == 0:
    print("No ice cream sales")
else:
    print("Total ice cream sales: {}".format(float(sum(list(sellList.values())))))
    maxSell = max(list(sellList.values()))
    maxSell_li = []
    for k,v in sellList.items():
        if v == maxSell:
            maxSell_li.append(k)
    maxSell_li.sort()
    print("Top sales: {}".format(', '.join(maxSell_li)))
