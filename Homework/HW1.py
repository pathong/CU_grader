# x,y,w,h ; start at top-left cornor #cringe
# 0,1,2,3
def center(r):
    w_2 = r[2]/2
    h_2 = r[3]/2
    return [r[0] + w_2, r[1]- h_2]

def distance(r1,r2):
    c1 = center(r1)
    c2 = center(r2)
    return ( ((c1[0] - c2[0])**2) + ((c1[1] - c2[1])**2) )**.5

def intersection(r1,r2):
    R1 = r1[0] + r1[2]
    L1 = r1[0] 

    R2 = r2[0] + r2[2]
    L2 = r2[0] 

    min_R = min(R1,R2)
    max_L = max(L1,L2)

    dX = max(0,min_R - max_L)

    T1 = r1[1]
    B1 = r1[1] - r1[3]

    T2 = r2[1]
    B2 = r2[1] - r2[3]

    min_T = min(T1,T2)
    max_B = max(B1,B2)

    dY = max(0,min_T - max_B)


    return dX * dY

def union(r1,r2):
    a1 = r1[3] * r1[2]
    a2 = r2[3] * r2[2]
    return a1 + a2 - intersection(r1,r2)


def iou(r1,r2):
    return intersection(r1,r2) / union(r1,r2)
    
r1=[1.0, 4.0, 1.5, 2.0]
r2=[2.0, 5.0, 2.5, 2.0]
r3=[4.0, 5.5, 1.5, 3.5]
r4=[6.0, 4.5, 1.5, 2.0]
r5=[5.75, 7.0, 2.0, 5.0]
print(center(r1))
print(center(r2))
print(round(distance(r1,r2),2))
print(round(distance(r3,r4),2))
print(intersection(r1,r2)) 
print(intersection(r2,r3))
print(intersection(r4,r5))
print(intersection(r1,r5)) # กรณีโบนัส
print(union(r1,r2))
print(union(r2,r3))
print(union(r4,r5))
print(round(iou(r1,r2),2))
print(round(iou(r2,r3),2))
print(round(iou(r4,r5),2))
