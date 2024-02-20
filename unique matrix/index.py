def row_check(mat,n): 
    for i in range(n):
        k=list(range(1,n+1))
        for j in range(n):
            if mat[i][j] in k:
                k.remove(mat[i][j])
            else:
                return False 

    return True 
def col_check(mat,n):
    matrix=[[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n): 
            matrix[j][i]=mat[i][j]
    for i in range(n):
            k=list(range(1,n+1))
            for j in range(n):
                if mat[i][j] in k:
                    k.remove(mat[i][j])

                else:
                    return False 
    return True
n=int(input())
mat=[]
for i in range(n):
    m=list(map(int,input().split()))
    mat.append(m)
a=row_check(mat,n)
b=col_check(mat,n)
if a and b:
    print("True")
else:
    print("False")
    
    
    
    
    
    
    
    
    
    
