def distance1(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**.5
def distance2(p1,p2):
    return distance1(p1[0],p1[1],p2[0],p2[1])
def distance3(c1,c2):
    dis = distance1(c1[0],c1[1],c2[0],c2[1])
    
    return dis, dis <= c1[2] + c2[2]
def perimeter(points):
    s = 0
    for i in range(len(points)-1):
        s += distance2(points[i],points[i+1]) 
    s += distance2(points[0],points[-1])
    return s

# print(distance1(0, 0, 3, 4))
# print(distance2([0,0], [3,4]))
# a,b = distance3([0,0,1], [5,0,2]);print(a, b)
# print(perimeter([[0,0], [0,2], [2,2], [2,0]]))


exec(input())
