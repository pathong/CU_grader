import math
sum_p = 0
sum_s = 0
sum_sc = 0
for _ in range(9):
    x = list(map(int, input().strip().split()))
    p,s,c = x[0],x[1],x[2]
    sc = 0
    if c == 1:
        sc = min(s, p+2)
    if c == 0:
        sc = 0
    sum_p += p
    sum_s += s
    sum_sc += sc


tt = math.floor(.8*(1.5*sum_sc - sum_p))
score = sum_s - tt

    
print(sum_s)
print(tt)
print(score)


