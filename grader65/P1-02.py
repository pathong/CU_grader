x = list(map(int, input().split()))
n = x[0]
k = x[1]

if n%2 != 0:
    sum_a,sum_b,sum_c,m = 0,0,0,0
    while m < k:
        z = list(map(int, input().split()))
        a,b,c = z[0], z[1], z[2]
        if a==b:
            if a == c:
                if a+b > k:
                    sum_a += 1
                    sum_b += 2
                    sum_c -= 3
                else:
                    sum_a -= 3
                    sum_b -= 2
                    sum_c += 1
            else:
                sum_a+=2
                sum_b-=3
                
        m += 1
    
    print(sum_a, sum_b, sum_c)
else:
    y = list(map(int, input().split()))
    s = y[0]
    t = y[1]
    x=s
    y=t
    if s>t: x = s-t
    elif s < t: y = 2*(t-s)

    if x + y > k:
        x,y = y,x
        x = y+s**2
    print(x,y)

