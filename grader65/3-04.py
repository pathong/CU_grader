n = input()
li = ['06','08','09']

if len(n) == 10 and n[:2] in li:
    print("Mobile number")
else:
    print("Not a mobile number")


