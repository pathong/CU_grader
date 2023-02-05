ans = input()
inp = input()

if len(ans) != len(inp):
    print("Incomplete answer")
else:
    s = 0
    for i in range(len(ans)):
        if ans[i] == inp[i]:
            s +=1

    print(s)
 

