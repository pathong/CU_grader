li = []
while True:
    n = input()
    if n == "q":
        break;
    li.append(float(n))
le = len(li)
if le == 0:
    print("No Data")
else:
    print(round(sum(li)/le,2))

