def day_of_year(d,m,y):
    m30 = [4,6,9,11]
    _d = 0
    for _m in range(1,13):
        if _m == m:
            _d += d
            continue
        else:
            if _m in m30:
                _d += 30
            elif _m not in m30:
                if _m == 2:
                    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
                        _d += 28
                    else:
                        _d += 29
                else:
                    _d += 31


    return(_d)

exec(input())
    
