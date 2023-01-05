w = input().split(" ")

f = w[0]
l = w[-1]

v = 'aeiou'
def ind(s:str)->int:
    for i in range(len(s)):
        if s[i] in v:
            return i
    return -1
w[0] = f[:ind(f)] + l[ind(l):]
w[-1] = l[:ind(l)] + f[ind(l):]


print(' '.join(w))
