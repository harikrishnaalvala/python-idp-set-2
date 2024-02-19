def check_wins(n,m):
    b=m.count("M")
    c=m.count("A")
    if b>c:
        return 60*n 
    elif c>b:
        return 40*n 
    else:
        return 55*n
a=int(input())
for i in range(a):
    n=int(input())
    m=list(input())
    result=check_wins(n,m)
    print(result)
