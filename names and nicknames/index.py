def check_same_name(l):
    for name in l:
        if (l.count(name)>1):
            return "Yes"
    return "No"
def takes_names(n):
    l=[]
    for i in range(n):
        a,b=input().split()
        l.append(a+b)
    return l
t=int(input())
for i in range(t):
    n=int(input())
    l=takes_names(n)
    result=check_same_name(l)
    print(result)
