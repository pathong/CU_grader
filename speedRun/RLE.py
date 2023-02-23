o = input()
if o == "str2RLE" or o == "RLE2str":
    w = input()
    if o == "str2RLE":
        li = []
        t = w[0]
        c = 1
        for _w in w[1:]:
            if t == _w:
                c+=1
            elif t != _w:
                
                li.append(t)
                li.append(str(c))

                c = 1
                t = _w

        li.append(t)
        li.append(str(c))


        print(" ".join(li))

    elif o == "RLE2str":
        li = w.split()
        s = ""
        for i in range(0,len(li),2):
            s += li[i] * int(li[i+1])
        print(s)
else:
    print("Error")

