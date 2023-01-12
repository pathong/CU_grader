import math
t1 = math.pi
t2 = math.factorial(10) / math.pow(8,8)
t3 = math.log(9.7, math.e)
t4 = (7/math.sqrt(71)) - math.sin(math.radians(40)) 
b1 = math.pow(1.2, math.pow(2.3, 1/3))

print(round((t1 - t2 + math.pow(t3,t4))/b1,6))
