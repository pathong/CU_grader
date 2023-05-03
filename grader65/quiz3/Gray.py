l = ['0','1']
n = int(input())
k = int(input())
for _ in range(n-1):
    lr = l.copy()
    lr.reverse()
    for i in range(len(l)):
        l[i] = '0' + l[i]
        lr[i] = '1' + lr[i]
    l = l+lr
    
s = ''
expect = n+1
for _k in range(1,k+1):
    s += str(_k)+'-'*(expect-len(str(_k)))
print(s[:-1])

start = 0
stop = k
while True:
    print(','.join(l[start:stop]))
    if stop>len(l):break
    start = stop
    stop += k 






