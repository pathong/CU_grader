#22.01 22.39 22.56
file=input()
n=int(input())
def rotate(line):
    p=line.find('\n')
    while p!=-1:
        line=line[:p]+'.'+line[p+1:]
        p=line.find('\n')
    return line.split('.')
line1=''
for i in range(1,n//10+1):
    line='-'*9+str(i)
    line1+=line
line1=line1+'-'*(n%10)
print(line1)
jing=open(file,'r')
line=jing.read()
line=rotate(line)
c1=0
c2=1
bar2='.'.join(line[c1:c2]).strip('.')
c2+=1
while c2<=len(line):
    bar1='.'.join(line[c1:c2]).strip('.')
    if len(bar1)>len(line1) and len(bar2)!=0:
        print(bar2)
        c1=c2-1
    bar2='.'.join(line[c1:c2]).strip('.')
    c2+=1
print(bar2)
jing.close()

