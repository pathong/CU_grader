def peaks(li):
    ans = []
    for i in range(1,len(li)-1):
        if li[i] > li[i-1] and li[i] > li[i+1]:
            ans.append(i)

    return ans
exec(input())
