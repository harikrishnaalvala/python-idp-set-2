s,t=map(int,input().split())
count=0
for i in range(s+1):
    for j in range(s+1):
        for k in range(s+1):
            sum=i+k+j
            p=i*k*j
            if sum<=s and p<=t:
                count+=1
print(count)
