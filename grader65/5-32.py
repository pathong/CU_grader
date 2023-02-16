n = int(input()) 
q = list() 
lastCall = list()
sometime = 0
finishedOrder = 0
qi = 301
for k in range(n):
    c = input().split()
    if c[0] == 'reset':
        qi = int(c[1]) 
    elif c[0] == 'new':
        q.append([qi, int(c[1])])
        qi += 1
        print("ticket {}".format(q[-1][0]))
    elif c[0] == 'next':
        lastCall = q[0]
        print("call {}".format(lastCall[0]))

        q.pop(0)
    elif c[0] == 'order':
        sometime += int(c[1]) - lastCall[1] 
        finishedOrder += 1

        print("qtime {} {}".format(lastCall[0], int(c[1]) - lastCall[1]))

    elif c[0] == 'avg_qtime':
        avg =  round(sometime/finishedOrder, 4)
        print("avg_qtime {}".format(avg))
