import math
def distance(x1,y1,x2,y2): 
    return math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
d = distance(1,1,4,5)
print(d)
