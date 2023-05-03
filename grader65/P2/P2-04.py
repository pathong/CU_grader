def CheckYear(y):
    return True if y >= 2558 else False
def CheckMonth(m):
    return True if m in range(1,13) else False
def CheckDate(d,m,y):
    m30 = [4,6,9,11]
    dnm = 31
    if m in m30:
        dnm = 30
    else:
        if m == 2:
            dnm = 28 if y%400 == 0 or y%4 !=0 else 29
    return True if d > 0 and d <= dnm else False

def CheckType(ty):
    Type = ['E','Q','N','F'] 
    return True if ty in Type else False

def newDate(t,d,m,y):
    di = {'E':1, 'Q':3, 'N':7, 'F':14}


correctOrder = []
while True:
    order = input().strip()
    if order == "END" : break
    orders = order.split()

    # 0 1 2 3 4
    # id t d m y
    if not CheckYear(int(orders[4])):
        print("Error: {} --> Invalid {}".format(order,'year'))
    elif not CheckMonth(int(orders[3])):
        print("Error: {} --> Invalid {}".format(order,'month'))
    elif not CheckDate(int(orders[2]), int(orders[3]), int(orders[4])):
        print("Error: {} --> Invalid {}".format(order,'date'))
    elif not CheckType(orders[1]):
        print("Error: {} --> Invalid {}".format(order,'delivery type'))
    else:
        correctOrder.append([orders[2], orders[3], orders[4], orders[0], orders])
correctOrder.sort()
print(correctOrder)




