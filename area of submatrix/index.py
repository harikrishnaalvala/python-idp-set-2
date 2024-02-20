m,n=map(int, input().split())
mat=[]
for i in range(m):
    my=list(map(int,input().split()))
    mat.append(my)
k=int (input())
res=[]
a=m-k
b=n-k
for i in range(m):
    for j in range(n):
        if ((i<k) or (j<k)):
            continue
        elif (i>=a or j>=b):
            continue
        else:
            res.append(mat[i][j])
if res==[]:
    print(0)
else:
    p=1 
    for i in res:
        p*=i
    print(p)
