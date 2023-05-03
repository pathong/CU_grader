def convolute(m,k):
    _sum = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            _sum += m[i][j] * k[i][j]
    return _sum

exec(input())
# print(convolute([[1,2],[3,4]],[[1,1],[1,1]]))
# print(convolute([[1,2,3],[4,5,6],[7,8,9]],[[-1,-2,-1],[0,0,0],[1,2,1]]))
# print(convolute([[1,2],[3,4]],[[0,0],[0,0]]))
# print(convolute([[1,2],[1,2]],[[-1,-1],[1,1]]))


