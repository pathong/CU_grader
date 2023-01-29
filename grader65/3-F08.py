def day_of_year(d,m,y):
    d30 = [4,6,9,11]
    _d = 0
    _d += d
    for _m in range(1,m):
        if _m in d30:
            _d += 30
        else:
            if _m == 2:
                y -= 543
                if y % 4 == 0:
                    if y % 100 == 0:
                        if y % 400 == 0:
                            _d += 29
                        else:
                            _d += 28
                    else:
                        _d += 29
                else:
                    _d += 28
            else:
                _d += 31
    return _d


exec(input())
