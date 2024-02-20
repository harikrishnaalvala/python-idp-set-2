w=list(map(int,input().split())) 
L=list(map(abs,w)) 
L.sort(reverse=True) 
s=[]
for i in range(len(L)-1):
    for j in range(i+1,len(L)): 
        num=L[i]-L[j]
        s.append(num) 
print(min(s)) 
