o = input()
if o == "RLE2str":
    s = input()
    li = s.strip().split()
    ans =""
    for i in range(0, len(li), 2):
        if int(li[i+1] != 0) : ans += li[i] * int(li[i+1]) 
    print(ans)
elif o == "str2RLE":
    s = input()
    li = []
    li.append(s[0])
    c = 1 
    for i in s[1:]:
        if i == li[-1]: c+=1
        else: 
            li.append(str(c))
            c =1
            li.append(i)
    li.append(str(c))
    ans = " ".join(li)
    print(ans)
else: print("Error")
