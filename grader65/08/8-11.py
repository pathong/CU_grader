def reverse(d:dict):
    nd = dict()
    for key,value in d.items():
        nd[value] = key
    return nd

def keys(d,v):
    li = []
    for key,value in d.items():
        if value == v:
            li.append(key)
    return li



exec(input())


        

