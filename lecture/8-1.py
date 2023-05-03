n = int(input())
pizza_time = {'PZ871': 265.25, 'PZ953':246.50, 'Z1983':256.50, 'Z2853':272.50, 'LC673':309.25}
customer = dict()
for _ in range(n):
    inp = input().split(",")
    cus = inp[0]
    inp.pop(0)
    for i in range(0,len(inp),2):
        if cus not in customer.keys():
            customer[cus] = 0
        customer[cus] += pizza_time[inp[i]] * int(inp[i+1])

k = list(customer.keys()).copy()
k.sort()
for _k in k:
    print('{} -> {}'.format(_k, customer[_k]))


