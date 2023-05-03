
n = int(input())
yellow = dict()
yellow_r = dict()
for _ in range(n):
    inp = input().strip().split()
    name = " ".join(inp[:2])
    number = inp[2]
    yellow[name] = number
    yellow_r[number] = name


m = int(input())
for _ in range(m):
    search = input()
    if search in yellow.keys():
        print('{} --> {}'.format(search, yellow[search]))
    elif search in yellow_r.keys():
        print('{} --> {}'.format(search, yellow_r[search]))
    else:
        print('{} --> Not found'.format(search))

    



