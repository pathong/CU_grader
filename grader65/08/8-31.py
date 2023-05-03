from re import I


def total(pocket):
    tot = 0
    for k,v in pocket.items():
        tot += int(k) * int(v)
    return tot
def take(pocket,money_in):
    for k,v in money_in.items():
        if k not in pocket.keys():
            pocket[k] = 0
        pocket[k] += v
    return pocket

def pay(pocket,amt):
    pocket_copy = pocket.copy()
    track = dict()
    key = list(pocket.keys())
    key.sort(reverse=True)
    for k in key:
        k = int(k)
        a = amt//k
        allowed_amount = min(a,pocket_copy[k])
        amt -= k*allowed_amount


        pocket_copy[k] -= allowed_amount


    for k in key:
        diff = int(pocket[k])- int(pocket_copy[k])
        if diff > 0:
            track[k] = diff

    if amt > 0:
        return {}
    else:
        for k,v in pocket_copy.items():
            pocket[k] = v
        return track

    

exec(input())
    



# p={10:5, 1:7};print(pay(p, 18));print(p)
# p={10:5, 1:7};print(pay(p, 100));print(p)
# p={10:5, 1:7};print(pay(p, 57));print(p)






