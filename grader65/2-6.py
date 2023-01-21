a = input()
a = list(map(float, a[1:-1].split(", ")))
b = input()
b = list(map(float, b[1:-1].split(", ")))

def li_str(li:list)->str:
    return "[" + ", ".join(list(map(str,li))) + "]"

an = []
for i in range(len(a)):
    an.append(a[i] + b[i])

print("{0} + {1} = {2}".format(li_str(a),li_str(b),li_str(an)))

