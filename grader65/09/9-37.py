n = int(input())
d = dict()
for _ in range(n):
    s, n = input().split()
    d[s] = int(n)

scores= []
stu = dict()
m = int(input())
for _ in range(m):
    inp = input().strip().split()
    scores.append(float(inp[1]))
    stu[inp[1]] = [inp[0], inp[2:]]

ans_d = dict()
scores.sort(reverse=True)
# print(scores)
# print(stu.keys())
for sc in scores:
    for s in stu.keys(): 
        if sc == float(s):
            orders = stu[s][1]
            _id = stu[s][0]
            for order in orders:
                if d[order] > 0:
                    d[order] -= 1
                    ans_d[_id] = order
                    break


ids = sorted(ans_d.keys())
for i in ids:
    print(i, ans_d[i])

