def row_number(t,e):
    for i in range(len(t)):
        if e in t[i]:
            return i
    return 0

def flatten(t):
    li = []
    for r in t:
        for c in r:
            if c != 0:
                li.append(c)
    return li

def inversions(x):
    s = 0
    i = 0
    while True:
        j = i+1
        while True:
            if x[i] > x[j]: s += 1
            j += 1
            if j == len(x):break
        i += 1
        if i == len(x)-1:break

    return s
def solvable(t):
    row = len(t)
    inv = inversions(flatten(t))
    row_0 = row_number(t,0)

    if row % 2 != 0 and inv % 2 == 0: return True
    if row % 2 == 0:
        if inv % 2 != 0 and row_0 % 2 == 0: return True
        if inv % 2 == 0 and row_0 % 2 != 0: return True
    return False

# print(row_number([[0,8,7],[6,5,4],[3,2,1]], 0))
# print(flatten([[0,8,7],[6,5,4],[3,2,1]]))
# print(inversions([8,7,6,5,4,3,2,1]))
# print(solvable([[0,8,7],[6,5,4],[3,2,1]]))

exec(input())

