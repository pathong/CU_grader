n,m,_k = [int(e) for e in input().strip().split()]
b_k = dict()
a_li_k = dict()
for _ in range(n):
    b,k = input().split()
    b_k[b] = k

for _ in range(m):
    inp = input().split()
    a = inp[0]
    bs = inp[1:]
    ks = set() 
    for _b in bs:
        ks.add(b_k[_b])
    a_li_k[a] = ks


for _ in range(_k):
    inp = input().split()
    f = a_li_k[inp[0]]
    for _inp in inp:
        f = f&a_li_k[_inp]
    sf = sorted(list(f))
    if len(sf) > 0:
        print(' '.join(sf))
    else:
        print('None')





