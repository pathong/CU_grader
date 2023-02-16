n = int(input())
li = []
for _ in range(n):
    li.append(input())
li += input().split()
while True:
    a = input()
    if a == "-1":
        break
    li.append(a)

ans = []
n = 1
for i in range(len(li)):
    n *= -1
    if n == 1:
        ans.insert(0,li[i])
    elif n == -1:
        ans.append(li[i])


print(list(map(int,ans)))
