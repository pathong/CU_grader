n_rows = int(input())
n_col = int(input())
li = [('sg',3), ('gg',4)]

matrix = []
curr = 1
for i in range(n_rows):
    
    mat =[]
    for j in range(n_col):
        mat.append(str(curr))
        curr += 1
    matrix.append(mat)

for name,ass in li:
    for i in range(n_rows):
        for j in range(n_col):
            if matrix[i][j] == str(ass):
                matrix[i][j] = name
            elif matrix[i][j] != str(ass) and not matrix[i][j].isalpha():
                matrix[i][j] = '--'
print(matrix)
for e in matrix:
    print('| '+' | '.join(e)+ ' |')




