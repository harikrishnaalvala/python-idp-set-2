n=int (input())
k=n
j=n-1
mat1=[]
mat2=[]
for i in range(n):
    m=list(map(int, input().split()))
    mat1.append(m[:k])
    mat2.append(m[j:]) 
    k-=1 
    j-=1 
sum1=0 
for i in mat1:
    sum1+=sum(i)
print(sum1)
sum2=0
for i in mat2:
    sum2+=sum(i)
print(sum2)

    
