def factor(N):
    ans = []
    i = 2
    while True:
        c = 0
        if N%i == 0:
            while True:
                if N % i != 0:
                    ans.append([i,c])
                    break
                N //= i
                c += 1
                print(N, c)
        i += 1
        
        if i > N: return ans

exec(input())

