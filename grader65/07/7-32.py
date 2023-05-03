s = input()

def leng(s)->bool:
    return len(s) < 8
def Cap(s)->bool:
    cap = False
    uncap = False
    num = False
    spe = False
    n = '1234567890'
    s = '"!@#$%^&*()-+?_=,<>//'''
    for _s in s:
        if _s.isupper(): cap = True
        elif _s.islower(): uncap = True
        elif _s in n: num = True
        elif _s in s: spe = True
    return cap and uncap and num and spe


if leng(s):
    print("Less than 8 characters")
elif Cap(s):
    print()
elif 

