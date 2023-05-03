s = input().strip()
o = input().strip()
s = s.upper()


valid = True
for _s in s:
    if _s not in "AGCT":
        valid = False
        break

if valid:
    if o == "R":
        a = ""
        for _s in s:
            if _s == "A": a+="T"
            elif _s == "C": a+="G"
            elif _s == "G": a+="C"
            elif _s == "T": a+="A"
        print(a[::-1])
    elif o == "F":

        ca = s.count("A")
        cc = s.count("C")
        cg = s.count("G")
        ct = s.count("T")

        print("A={}, T={}, G={}, C={}".format(ca,ct,cg,cc))
        

    elif o == "D":
        m = input().strip()
        c = 0
        for i in range(len(s) -1):
            if s[i:i+2] == m:
                c += 1
        print(c)
else:
    print("Invalid DNA")

