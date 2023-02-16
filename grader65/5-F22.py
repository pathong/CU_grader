def index_of(grades, ID):
    for i in range(len(grades)):
        if grades[i][0] == ID:
            return i
    return -1
def upgrade(grades, uids):
    g =['F','D','D+','C','C+','B','B+','A']
    re = []
    for grade in grades:
        for _id in uids:
            if grade[0] == _id and grade[1] != "A":
                grade[1] = g[g.index(grade[1]) + 1]
        re.append([grade[0], grade])
    re.sort()
    grades.clear()
    for r in re:
        grades.append(r[1])
                
# DON'T remove the following three lines
exec(input())
exec(input())
exec(input())
