import math
n = int(input())
p1 = math.sqrt(2*math.pi)
p2 = pow(n,n+.5)

b = p1*p2* math.pow(math.e, (-n+(1/(12*n+1))))
t = p1*p2* math.pow(math.e, (-n+(1/(12*n))))

print("{0} {1}".format(b,t))

