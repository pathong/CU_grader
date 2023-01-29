import math
bd, bm, by, d,m,y= [int(e) for e in input().split()]

def GetDateFromMoth(_m:int, _y:int)->int:
    d30 = [4,6,9,11]
    _d = 0
    if _m in d30:
        _d += 30
    else:
        if _m == 2:
            if (_y -543) % 4 == 0:
                _d += 29
            else:
                _d += 28
        else:
            _d += 31
    return _d
# im blue im da be dee da ba die 
_d = 0
_d += GetDateFromMoth(bm,by) - bd 
for _m in range(bm+1,13):
    _d += GetDateFromMoth(_m,by)

# im black
diffY = y-by-1
_d  += diffY * 365

# im red

for _m in range(1,m):
    _d += GetDateFromMoth(_m,y)

_d += d


t = 2*math.pi*_d
print("{} {:.2f} {:.2f} {:.2f}".format(_d, math.sin(t/23),math.sin(t/28),math.sin(t/33) ))


