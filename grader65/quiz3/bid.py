#19.27 20.41 20.55
def check(x,product):
    if x[0] not in 'W B'.split() or len(x) <3:
        return False
    if x[0]=='W':
        if x[2] not in product:
            return False
        elif x[1] not  in product[x[2]]['user']:
            return False
    return True
user={}
product={}
for i in range(int(input())):
    x=input().split()
    if check(x,product):
        if x[0]=='B':
            if x[1] not in user:
                user[x[1]]={'total_bid':0,'product':set()}
            if x[2] in product:
                if x[1] not in product[x[2]]['user']:
                    product[x[2]]['user'].append(x[1])
                    product[x[2]]['bid'].append(int(x[3]))
                else:
                    indx_pos=product[x[2]]['user'].index(x[1])
                    product[x[2]]['user'].pop(indx_pos)
                    product[x[2]]['user'].append(x[1])
                    product[x[2]]['bid'].pop(indx_pos)
                    product[x[2]]['bid'].append(int(x[3]))
            else:
                 product[x[2]]={'user':[x[1]],'bid':[int(x[3])]}
        else:
            indx_pos=product[x[2]]['user'].index(x[1])
            product[x[2]]['user'].pop(indx_pos)
            product[x[2]]['bid'].pop(indx_pos)

for p,d in product.items():
    if len(d['bid'])!=0:
        top_bid=max(d['bid'])
        indx_pos=product[p]['bid'].index(top_bid)
        user[product[p]['user'][indx_pos]]['total_bid'] += top_bid
        user[product[p]['user'][indx_pos]]['product'].add(p)

user_key=sorted([i for i in user])
for i in user_key:
    line=i+': $'
    if user[i]['total_bid']==0:
        print(line+str(0))
    else:
        print(line+str(user[i]['total_bid']),'->',' '.join(sorted(user[i]['product']))  )
    

