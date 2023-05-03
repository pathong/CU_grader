track = dict()
bidder_order = set() 
n = int(input())
for _ in range(n):
    inp = input().strip().split()
    if inp[0] == 'B':
        n=inp[1];b=inp[2];p=int(inp[3])
        if b not in track.keys():
            track[b] = []

        index = 0
        #(price, bidder)
        isFound = False
        for i in range(len(track[b])):
            _b = track[b][i]
            if _b[0] < p:
                # track[b].insert(i,(p,n))
                index = i 
                isFound = True
                break
            if _b[0] == p:
                # track[b].insert(i+1,(p,n))
                index = i+1
                isFound = True
                break
        if not isFound:
            index = len(track[b])
        
        isCheckFound = False
        for i in range(len(track[b])):
            _b = track[b][i]
            if _b[1] == n:
                if p > _b[0]:
                    track[b].pop(i)

        track[b].insert(index, (p,n))
        bidder_order.add(n)


    elif inp[0] == 'W':
        n = inp[1]; b = inp[2]
        for i in range(len(track[b])):
            if n == track[b][i][1]:
                track[b].pop(i)
                break

bidder_order = sorted(list(set(bidder_order)))


## visualize
ans = dict()

## {bidder : [sum, list()]}
b = sorted(track.keys())

for _b in b:
    k = _b
    v = track[_b]
    if len(track[_b]) == 0:continue

    first = v[0][1]
    if first not in ans.keys():
        ans[first] = [0,[]]
    ans[first][0] += v[0][0]
    ans[first][1].append(k)


for bidder in bidder_order:
    if bidder not in ans.keys():
        print('{}: ${}'.format(bidder, '0'))
    else:
        print('{}: ${} -> {}'.format(bidder, ans[bidder][0], " ".join(ans[bidder][1])))


