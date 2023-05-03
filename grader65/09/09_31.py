def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a

def is_coprime(a,b,c):
    return gcd(gcd(gcd(a,b),gcd(b,c)),gcd(a,c)) == 1

def primitive_Pythagorean_triples(max_len):
    ts_list = []
    for a in range(3, max_len):
        for b in range(a+1, max_len+1):
            if gcd(a,b) == 1:
                c = (a**2 + b**2)**.5
                if c == round(c) and c <= max_len:
                    ts_list.append( [c,a,[int(a),int(b),int(c)]])
    ts_list.sort()
    ans = []
    for li in ts_list:
        ans.append(li[2])
    return ans


exec(input().strip())
# print(is_coprime(2,3,6),is_coprime(2,4,8))
# print(primitive_Pythagorean_triples(10))
# print(primitive_Pythagorean_triples(1000))
