def check(m):
    count=0
    for w in m:
        if (count==2) or (count==-2):
            return "YES"
        if w=="L":
            k=1
        if w=="R":
            k=-1
        count+=k 
    if (count==2) or (count==-2):
        return "YES"
    else:
       return "NO" 
n=int(input())
for i in range(n):
    m=input()
    result=check(m)
    print(result)
