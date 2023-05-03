def knows(R,x,y): return True if y in R[x] else False

def is_celeb(R,x):
    knows()
    for k,v in R.items():
        if k == x: continue
        if x not in v: return False
    return True

def find_celeb(R):
    for k in R.keys():
        if is_celeb(R,k): return k
    return None

def read_relations():
    R = dict()
    while True:
        d = input().split()
        if len(d) == 1: break
        if d[0] not in R.keys(): R[d[0]] = set()
        if d[1] not in R.keys(): R[d[1]] = set()
        R[d[0]].add(d[1])

    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None: print('Not Found')
    else:print(c)


exec(input().strip())
