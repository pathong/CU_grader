n = int(input())
li = []
li.append(n)
while n != 1:
    if n % 2 == 0: n //= 2
    else: n = 3*n +1
    li.append(n)

print("->".join(list(map(str,li)))) if len(li) <= 15 else print("->".join(list(map(str,li[-15:]))))
