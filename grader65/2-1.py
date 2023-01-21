n = input()

def N(i)->int:
    return int(n[i])
k = 0
for i in range(12):
      k += (13-i)*N(i)
n12 = (11 - (k % 11)) %10

print(n[0], n[1:5], n[5:10], n[10:12], n12)
