n = 5

for i in range(0,2*n-1,2):
    t = 2*n-i-2
    print(' '*int(t/2),'*'*(i+1),' '*int(t/2),end='')
    print()
print()
for i in range(2*n-1,-1,-2):
    t = 2*n-1-i
    print(' '*int(t/2),'*'*(i),' '*int(t/2),end='')
    print()
print()
for i in range(1,n+1):
    print('*'*i)
for i in range(n-1,0,-1):
    print('*'*i)
print()
for i in range(n):
    if i%2==0:
        for j in range(i+1):
            print('0' if j%2!=0 else '1',end='')
    else:
        for j in range(i+1):
            print('1' if j%2!=0 else '0',end='')
    print()

print()
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end='')
    print(' '*(2*n - 2*i -2),end='')
    for j in range(i,0,-1):
        print(j,end='')
    print()
print()
c=1
for i in range(n):
    for j in range(i+1):
        print(c,end=' ')
        c+=1
    print()

print()
for i in range(n-1,-1,-1):
    for j in range(i+1):
        print(chr(65+j),end='')
    print()
print()
for i in range(n):
    print(chr(65+i)*(i+1))
print()


for j in range(1,2*n + 1,2):
    space = ' '*int((2*n-j)/2)
    lh = ''.join([chr(65+t) for t in range(int(j/2)+1)])
    rh = ''.join([chr(65+t-1) for t in range(int(j/2),0,-1)])
    print(space,lh,rh,space,sep='')

for i in range(1,n+1):
    data = ''.join([chr(65+n-j) for j in range(i,0,-1)])
    print(data)

n = 5

for i in range(n,0,-1):
    print('*'*i,' '*(2*n-2*i),'*'*i,sep='')

for i in range(1,n+1):
    print('*'*i,' '*(2*n-2*i),'*'*i,sep='')


for i in range(1,n+1):
    print('*'*i,' '*(2*n-2*i),'*'*i,sep='')

for i in range(n-1,0,-1):
    print('*'*i,' '*(2*n-2*i),'*'*i,sep='')


n = 4

for i in range(n):
    if i in [0,n-1]:
        print('*'*n)
    else:
        print('*',' '*(n-2),'*',sep='')


# TODO: ref
n = 4
for i in range(2*n-1):
    for j in range(2*n-1):
        # trick: distance from the edges of the matrix for the converted matrix
        print(n - min(i,j,2*n-2-i,2*n-2-j),end='')
    print()

