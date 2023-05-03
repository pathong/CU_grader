def first_fit(L:list,e:int):
    if len(L) == 0:L.append([e]); return
    for pocket in L:
        if sum(pocket) + e <= 100:
            pocket.append(e)
            return
    L.append([e])
    
def best_fit(L:list,e:int):
    if len(L) == 0:L.append([e]); return
    best_sum = 100 
    best = -1
    for i in range(len(L)):
        pocket = L[i]
        if 100 - (sum(pocket) + e) < best_sum and sum(pocket) + e <= 100:
            best = i
            best_sum = 100 - (sum(pocket)+e)

    if best != -1:
        L[best].append(e)
    else:
        L.append([e])

def partition_FF(D):
    li = []
    for d in D:
        first_fit(li,d)
    return li

def partition_BF(D):
    li = []
    for d in D:
        best_fit(li,d)
    return li

exec(input().strip())
# L=[[50],[90]];first_fit(L,10);print(L)
# L=[[50],[90]];best_fit(L,10);print(L)
# print(partition_FF([50,90,10,80,50,20]))
# print(partition_BF([50,90,10,80,50,20]))

