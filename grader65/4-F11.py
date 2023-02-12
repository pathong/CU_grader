def RLE(t:str):
    if(len(t) == 0) : return []
    curr = t[0]
    li = []
    c =0
    for i in range(len(t)):
        s = t[i]
        if s == curr:
            c += 1
        if s != curr:
            li.append([curr,c])
            curr = s
            c = 1
        if i == len(t)-1:
            li.append([curr,c])
            curr = s
            c = 1
    return li
exec(input())
