def is_mobile_number(n:str)->bool:

    li = ['06','08','09']

    if len(n) == 10 and n[:2] in li:
        return True
    else:
        return False


exec(input())
