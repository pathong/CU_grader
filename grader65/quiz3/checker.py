position  = input().strip()
row = '';col = ''
if len(position) <= 3:
    row = position[0].strip()
    col = position[1:].strip()

if len(position) > 3:
    inp = position.split(',')
    for _inp in inp:
        if 'col' in _inp:
            col = _inp.split('=')[1].strip()
        elif 'row' in _inp:
            row = _inp.split('=')[1].strip()


rows = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
valid_col = True; valid_row = True
if len(col) == 0: valid_col = False

if valid_col:
    for c in col:
        if not c.isnumeric():
            valid_col = False
            break
if valid_col:
    if int(col) > 52 or int(col) < 1: valid_col = False

if len(row) == 0: valid_row = False
if valid_row:
    if len(row) > 1: valid_row = False
    if row not in rows:valid_row = False


if not valid_col and valid_row:
    print("Invalid column")
elif not valid_row and valid_col:
    print("Invalid row")
elif not valid_col and not valid_row:
    print("Invalid row and column")
else:
    r = rows.find(row)
    if r%2 == int(col)%2 :
        print('Black')
    else:
        print('White')







# r = rows.find(row)
# if r%2 == int(col)%2:
    # print('Black')
# else:
    # print('White')

s = "{}:{}  -> {}".format('a','b','c')

li = ['1','2','3']
print("a".join(li))
:
