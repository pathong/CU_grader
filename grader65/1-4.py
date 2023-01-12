import math
w = float(input())
h = float(input())

print(math.sqrt(w*h)/60)
print(.024265 * math.pow(w, 0.5378) * math.pow(h,0.3964))
print(.0333 * math.pow(w,.6157 - .0188 * math.log(w,10)) * math.pow(h,.3))
