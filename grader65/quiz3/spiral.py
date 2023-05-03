def spiral_square(n):
    a=[list((0,)*n) for a in range(n)]
    row1=colum1=n-1
    row2=colum2=0
    s=n*n
    l=1
    p=(n+1)//2-1
    while a[p][p]!=1:
        
        if l%4==1:
            for i in range(colum1,colum2-1,-1):
                a[row1][i]=s
                s-=1
            row1-=1
            l+=1
        if l%4==2:
            for i in range(row1,row2-1,-1):
                a[i][colum2]=s
                s-=1
            colum2+=1
            l+=1
        if l%4==3:
            for i in range(colum2,colum1+1):
                a[row2][i]=s
                s-=1
            row2+=1
            l+=1
        if l%4==0:
            for i in range(row2,row1+1):
                a[i][colum1]=s
                s-=1
            colum1-=1
            l+=1
    return a
def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))

exec(input().strip())