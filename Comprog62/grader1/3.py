n = int(input())

li = []
for i in range(n):
    li.append(int(input()))




def Check( li:list) -> int:
    d1 = li[1]-li[0] 
    d2 = li[2]-li[1]
    d3 = li[3]-li[2]
    D = li[3]-li[0]

    if(d1 == d2): 
        if(d2==d3):
            return 0
        else:
            return 4
    elif(d1 != d2):
        if(d2 == d3):
            return 1
        else:
            if(d1 != D):
                return 2
            else:
                return 3
    return 0
            

s = 0;
e = 3;
while e <= len(li):
    index = Check(li[s:e+1])
    if(index != 0):
        print(index+s)
        break;
    s +=1;
    e +=1;









