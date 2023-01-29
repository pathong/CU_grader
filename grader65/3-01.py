li = ['01','02','51','53','55','58']

for i in range(20,41):
    li.append(str(i))



n = input()
if n in li:
    print("OK")
else:
    print("Error")
