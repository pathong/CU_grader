courses_path = input()
teacher_path = input()
database_path = input()

cd = dict()
td = dict()

c = open(courses_path,'r')
for _c in c:
    _c = _c.strip().split(',')
    cd[_c[0]] = _c[1].strip()

t = open(teacher_path,'r')
for _t in t:
    _t= _t.strip().split(',')
    td[_t[0]] = _t[1].strip()

d = open(database_path,'r')
for _d in d:
    __d = _d.strip().split(',')
    if __d[0] not in cd.keys() or __d[1] not in td.keys():
        print('record error')
        continue
    print('{},{}'.format(cd[__d[0]], td[__d[1]]))


