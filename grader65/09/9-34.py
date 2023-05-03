def pattern1(nrow, ncol):
    li = []
    curr = 0
    for i in range(nrow):
        _li = []
        for j in range(ncol):
            curr+=1
            _li.append(curr)
        li.append(_li)
    return li

def pattern2(r,c):
    li = []
    curr = 0
    for i in range(r): li.append([])

    for i in range(c):
        for j in range(r):
            curr +=1
            li[j].append(curr)
    return li


def pattern3(n):
    li = []
    curr = 0
    for i in range(n):
        l = []
        for j in range(n):
            if j >= i:
                curr += 1
                l.append(curr)
            else:
                l.append(0)
        li.append(l)
    return li

def pattern4(n):
    li = []
    b_skip = 0 
    start = 1
    for i in range(n):
        l = []
        num0 = i
        skip =i+2 
        curr = start 
        for j in range(n):
            if j < num0: 
                l.append(0)
                continue
            l.append(curr)
            curr += skip
            skip += 1
        li.append(l)
        b_skip +=1
        start += b_skip 
    return li


def pattern5(n):
    li = []
    start = 1
    for i in range(n):
        l = []
        skip = n 
        curr = start
        for j in range(n):
            if j < i: 
                l.append(0)
                continue
            l.append(curr)
            curr += skip - (j-i)
        start +=1
        li.append(l)
    return li


def pattern6(n):
    li = []
    for i in range(n):
        l = []
        for j in range(n):
            if j < i:l.append(0)
        li.append(l)

    curr = 1

    for i in range(n):
        if i%2==0:
            for j in range(0,n-i):
                li[j].append(curr)
                curr+=1
        if i%2 != 0:
            for j in range(n-i-1,-1,-1):
                li[j].append(curr)
                curr+=1
    return li



# def visualize(li):
    # for l in li:
        # print(l)

# visualize(pattern6(5))


# print(pattern1(3,4))
# print(pattern2(3,4))
# print(pattern3(4))
# print(pattern4(4))
# print(pattern5(4))
# print(pattern6(4))

exec(input().strip())
